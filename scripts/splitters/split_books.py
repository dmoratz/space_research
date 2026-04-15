"""
split_books.py
--------------
Scans country folders for unsplit book .txt files (files sitting directly
in a country folder, not inside a book subdirectory), detects chapter
boundaries, and splits them into individual chapter files inside a new
folder named after the book.

Handles a wide range of chapter heading formats:
  - "Chapter 1", "CHAPTER 1", "Chapter One"
  - "Part I", "PART I: Title", "Part 1 The Psychohistorians"
  - "Act I:", "Act VII: January 2018"
  - "Prologue", "Epilogue", "Interlude"
  - "BOOK ONE", "BOOK TWO"
  - Bare numbers on their own line: "1", "2", "14"
  - Numbered titles: "1: THE THIEF AND THE PRISONER'S DILEMMA"
  - Indented numbered titles: "    1 THE ARRIVAL"

Front matter (everything before the first detected chapter) is saved
as front_matter.txt.

Usage:
    # Dry run — show what would be split, don't write anything:
    python scripts/split_books.py --dry-run

    # Split all countries:
    python scripts/split_books.py

    # Split one country:
    python scripts/split_books.py --country US
"""

import argparse
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BOOKS_DIR = PROJECT_ROOT / "data" / "books"

# Minimum number of characters between chapter headings to count as a real
# chapter.  Prevents false positives from TOC lines or stray numbers.
MIN_CHAPTER_LENGTH = 500

# Minimum number of chapters a book must split into for us to accept the
# result.  If we find fewer, we leave the book unsplit.
MIN_CHAPTERS = 2


# ---------------------------------------------------------------------------
# Chapter heading patterns (ordered from most specific to least)
# ---------------------------------------------------------------------------

# Each pattern is a tuple: (compiled regex, label function)
# The regex is matched against stripped lines.
# The label function takes the match object and returns a clean label.

def _label_chapter(m):
    """'Chapter 1' / 'CHAPTER 01' / 'Chapter One' → 'Chapter N'"""
    num = m.group("num").strip().lstrip("0") or "0"
    return f"Chapter {num}"

def _label_part(m):
    return f"Part {m.group('num').strip()}"

def _label_book(m):
    return f"Book {m.group('num').strip()}"

def _label_act(m):
    return f"Act {m.group('num').strip()}"

def _label_named(m):
    return m.group(0).strip()

def _label_numbered_title(m):
    num = m.group("num").strip()
    title = m.group("title").strip() if m.group("title") else ""
    if title:
        return f"Chapter {num} - {title}"
    return f"Chapter {num}"

def _label_ordinal(m):
    """e.g., 'THE FIRST LETTER' → 'The First Letter'"""
    return m.group(0).strip().title()


def _label_date_chapter(m):
    """e.g., 'January 1999:  ROCKET SUMMER' → 'January 1999 - Rocket Summer'"""
    month = m.group("month").title()
    year = m.group("year")
    title = m.group("title").strip().title() if m.group("title") else ""
    if title:
        return f"{month} {year} - {title}"
    return f"{month} {year}"


def _label_chapitre(m):
    """French chapter: 'CHAPITRE PREMIER' → 'Chapitre Premier'"""
    return m.group(0).strip().title()


def _label_roman_part(m):
    """'I - PRIMEVAL NIGHT' → 'Part I'"""
    return f"Part {m.group('num').strip()}"


def _label_bare_roman(m):
    """Bare Roman numeral on its own line: 'XIV' → 'Chapter XIV'"""
    return f"Chapter {m.group('num').strip()}"


def _label_bare_word_number(m):
    """Bare number word on its own line: 'SEVEN' → 'Chapter SEVEN'"""
    return f"Chapter {m.group('num').strip()}"


def _label_bare_number(m):
    return f"Chapter {m.group('num').strip()}"


# Number words for "Chapter One" etc.
# IMPORTANT: compound words (twenty-one) must come BEFORE simple words (twenty)
# in the alternation so the regex tries the longer match first.
_NUM_WORDS = (
    "twenty-one|twenty-two|twenty-three|twenty-four|twenty-five|"
    "twenty-six|twenty-seven|twenty-eight|twenty-nine|"
    "thirty-one|thirty-two|thirty-three|thirty-four|thirty-five|"
    "thirty-six|thirty-seven|thirty-eight|thirty-nine|"
    "forty-one|forty-two|forty-three|forty-four|forty-five|"
    "forty-six|forty-seven|forty-eight|forty-nine|"
    "one|two|three|four|five|six|seven|eight|nine|ten|"
    "eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|"
    "eighteen|nineteen|twenty|thirty|forty|fifty"
)

# Ordinal words for "The First Letter" etc.
_ORDINAL_WORDS = (
    "first|second|third|fourth|fifth|sixth|seventh|eighth|ninth|tenth|"
    "eleventh|twelfth|thirteenth|fourteenth|fifteenth|sixteenth|"
    "seventeenth|eighteenth|nineteenth|twentieth|"
    "twenty-first|twenty-second|twenty-third|twenty-fourth|twenty-fifth|"
    "twenty-sixth|twenty-seventh|twenty-eighth|twenty-ninth|thirtieth"
)

# French number words
_FRENCH_NUM_WORDS = (
    "premier|première|deuxième|troisième|quatrième|cinquième|"
    "sixième|septième|huitième|neuvième|dixième|"
    "onzième|douzième|treizième|quatorzième|quinzième"
)

# Month names for date-based chapters
_MONTHS = (
    "january|february|march|april|may|june|july|august|"
    "september|october|november|december"
)

HEADING_PATTERNS = [
    # "Chapter 1", "CHAPTER 01", "Chapter 1: Title", "Chapter 1. Title",
    # "Chapter I", "CHAPTER XXII" (Roman numerals), "CHAPTER ONE - Spaceguard"
    (re.compile(
        r"^(?:chapter)\s+(?P<num>\d+|[IVXLCDM]+|" + _NUM_WORDS + r")"
        r"(?:\s*[.:\-–—]\s*.*)?$",
        re.IGNORECASE,
    ), _label_chapter),

    # "BOOK ONE", "BOOK I", "Book 1", "BOOK TWO"
    (re.compile(
        r"^book\s+(?P<num>\w+)(?:\s*[.:]\s*.*)?$",
        re.IGNORECASE,
    ), _label_book),

    # "Part I", "Part 1 The Psychohistorians", "PART II: Three Body",
    # "PART ONE: ROBINSON CRUSOE", "PART THREE: TERRORIST"
    (re.compile(
        r"^part\s+(?P<num>[IVXLCDM]+|\d+|" + _NUM_WORDS + r")\b.*$",
        re.IGNORECASE,
    ), _label_part),

    # "Act I:", "Act VII: January 2018"
    (re.compile(
        r"^act\s+(?P<num>[IVXLCDM]+|\d+)\b.*$",
        re.IGNORECASE,
    ), _label_act),

    # "Prologue", "Epilogue", "Interlude", "Introduction", "Afterword",
    # "THE PRIEST'S TALE: ..." (Hyperion)
    (re.compile(
        r"^(?:prologue|epilogue|interlude|introduction|afterword|"
        r"author'?s?\s+note|translator'?s?\s+note|"
        r"the\s+\w+'?s?\s+tale)(?:\s*[.:]\s*.*)?$",
        re.IGNORECASE,
    ), _label_named),

    # "I - PRIMEVAL NIGHT", "VI - THROUGH THE STARGATE" (Roman numeral Part headings)
    # Roman numeral + dash + ALL-CAPS title (e.g. 2001: A Space Odyssey)
    (re.compile(
        r"^(?P<num>[IVXLCDM]+)\s*[-–—]\s*(?P<title>[A-Z][A-Z\s\",;'!?\-()]{3,})$"
    ), _label_roman_part),

    # "1: THE THIEF AND THE PRISONER'S DILEMMA"  or  "    1 THE ARRIVAL"
    # (number followed by colon/period/space/dash then ALL-CAPS title, min 4 chars)
    # Number limited to 1-200 to avoid matching years (e.g., "2902 TOKYO")
    (re.compile(
        r"^\s*(?P<num>\d{1,3})\s*[:.\s\-–—]\s*(?P<title>[A-Z][A-Z\s\",;'!?\-()]{3,})$"
    ), _label_numbered_title),

    # "1. A Parade in Erhenrang" — number + period + Title Case title
    # (less strict than ALL-CAPS, but requires period and short line < 80 chars)
    (re.compile(
        r"^\s*(?P<num>\d{1,3})\.\s+(?P<title>[A-Z][A-Za-z\s\",;'!?\-()]{3,})$"
    ), _label_numbered_title),

    # "1  Spaceguard" — number + 2+ spaces + Mixed Case title (Rendezvous with Rama)
    # Requires double-space to distinguish from regular prose
    (re.compile(
        r"^\s*(?P<num>\d{1,3})\s{2,}(?P<title>[A-Z][A-Za-z\s\",;'!?\-()]{3,})$"
    ), _label_numbered_title),

    # "1 - The Road to Extinction", "31- Survival" — number + dash + Mixed Case title
    # (2001: A Space Odyssey style — dash separator distinguishes from prose)
    (re.compile(
        r"^\s*(?P<num>\d{1,3})\s*[-–—]\s*(?P<title>[A-Z][A-Za-z\s\",;'!?\-()]{3,})$"
    ), _label_numbered_title),

    # "CHAPITRE PREMIER", "CHAPITRE II", "CHAPITRE III" (French chapters)
    (re.compile(
        r"^chapitre\s+(?P<num>[IVXLCDM]+|\d+|" + _FRENCH_NUM_WORDS + r")"
        r"(?:\s*[.:]\s*.*)?$",
        re.IGNORECASE,
    ), _label_chapitre),

    # "THE FIRST LETTER", "THE SECOND LETTER" (ordinal named sections — Tainaron)
    # Limited to short headings (1-3 words after the ordinal) to avoid matching prose
    (re.compile(
        r"^THE\s+(?:" + _ORDINAL_WORDS + r")\s+(?:\w+\s*){1,3}$",
        re.IGNORECASE,
    ), _label_ordinal),

    # "January 1999:  ROCKET SUMMER" (date-based chapters — Martian Chronicles)
    (re.compile(
        r"^(?P<month>" + _MONTHS + r")\s+(?P<year>\d{4})\s*:\s*(?P<title>.+)$",
        re.IGNORECASE,
    ), _label_date_chapter),

    # Bare Roman numeral on its own line: "I", "XIV", "XXII"
    # (la zone du dehors style — aggressive, like bare numbers)
    (re.compile(
        r"^\s*(?P<num>[IVXLCDM]+)\s*$"
    ), _label_bare_roman),

    # Bare number word on its own line: "ONE", "TWO", "TEN"
    # (Hard to Be a God style — aggressive, like bare numbers)
    (re.compile(
        r"^\s*(?P<num>" + _NUM_WORDS + r")\s*$",
        re.IGNORECASE,
    ), _label_bare_word_number),

    # Bare number with period on its own line: "1.", " 2.", "14."
    # (Prisoners of Power style — slightly less aggressive than pure bare number)
    (re.compile(
        r"^\s*(?P<num>\d{1,3})\.\s*$"
    ), _label_bare_number),

    # Bare number on its own line: "1", " 2 ", "14"
    # (most aggressive — tried last)
    (re.compile(
        r"^\s*(?P<num>\d{1,3})\s*$"
    ), _label_bare_number),
]

# Indices of aggressive patterns (bare numbers / bare Roman numerals / bare word numbers)
# Used to filter them out when they aren't the primary pattern
BARE_ROMAN_PATTERN_IDX = len(HEADING_PATTERNS) - 4           # "XIV"
BARE_WORD_NUMBER_PATTERN_IDX = len(HEADING_PATTERNS) - 3     # "SEVEN"
BARE_NUMBER_PATTERN_IDX_PERIOD = len(HEADING_PATTERNS) - 2   # "1."
BARE_NUMBER_PATTERN_IDX = len(HEADING_PATTERNS) - 1           # "1"


# ---------------------------------------------------------------------------
# Detect chapter headings in a list of lines
# ---------------------------------------------------------------------------

def _normalize_spaced_letters(text: str) -> str:
    """
    Collapse spaced-out letters from OCR artifacts.
    'N I N E T E E N' → 'NINETEEN'
    'T W E N T Y - O N E' → 'TWENTY-ONE'
    """
    # Find sequences of 3+ single uppercase letters separated by single spaces
    def _collapse(m):
        return m.group(0).replace(' ', '')
    # Match: single uppercase letter, then 2+ more single uppercase letters
    # separated by spaces, not adjacent to other letters
    result = re.sub(
        r'(?<![A-Za-z])([A-Z])((?:\s[A-Z\-]){2,})(?![A-Za-z])',
        _collapse, text
    )
    # Also collapse excessive internal whitespace
    result = re.sub(r'\s{2,}', ' ', result)
    return result


def _is_in_toc(line_idx: int, lines: list[str], heading_count_so_far: int) -> bool:
    """
    Heuristic: if we're near the top of the file and the next few lines
    also look like headings, this is probably a table of contents.
    We detect TOC by checking if headings are densely packed (multiple
    heading-like lines within a small window).
    """
    if line_idx > 300:
        return False  # TOCs don't go this deep

    # Look ahead: how many of the next 10 non-blank lines also match a pattern?
    matches_ahead = 0
    checked = 0
    for future_line in lines[line_idx + 1:]:
        if not future_line.strip():
            continue
        checked += 1
        if checked > 10:
            break
        for pattern, _ in HEADING_PATTERNS:
            if pattern.match(future_line.strip()):
                matches_ahead += 1
                break

    # If more than 3 of the next 10 content lines are also headings,
    # and we're in the first 300 lines, this smells like a TOC
    return matches_ahead >= 3


def detect_chapters(lines: list[str]) -> list[dict]:
    """
    Scan lines and return a list of chapter break points.
    Each entry: {'line': int, 'label': str, 'pattern_idx': int}
    """
    # Identify pattern indices that need line-length filtering
    # (title-case and double-space numbered title patterns)
    _LINE_LENGTH_FILTER_PATS = set()
    for _idx, (_pat, _lab) in enumerate(HEADING_PATTERNS):
        # Match the title-case and double-space patterns by their regex pattern string
        ps = _pat.pattern
        if r"\d{1,3})\.\s+" in ps and "A-Za-z" in ps:
            _LINE_LENGTH_FILTER_PATS.add(_idx)
        if r"\d{1,3})\s{2,}" in ps:
            _LINE_LENGTH_FILTER_PATS.add(_idx)

    # First pass: find ALL lines that match any heading pattern
    candidates = []
    for i, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        # Skip very long lines — headings are typically short
        if len(stripped) > 120:
            continue
        # Normalize spaced-out letters from OCR (e.g., "N I N E T E E N")
        stripped = _normalize_spaced_letters(stripped)
        for pat_idx, (pattern, labeler) in enumerate(HEADING_PATTERNS):
            m = pattern.match(stripped)
            if m:
                # Extra filter for title-case numbered pattern: line must be short
                if pat_idx in _LINE_LENGTH_FILTER_PATS and len(stripped) > 80:
                    continue
                # Filter out time-related false positives for numbered titles
                # ("8 AM GMT", "3 PM", "10 PM GMT" etc.)
                if m.group("title") if "title" in m.groupdict() else None:
                    title_text = m.group("title").strip()
                    if re.match(r'^[AP]M(\s+[A-Z]{2,4})?$', title_text):
                        continue
                label = labeler(m)
                candidates.append({
                    "line": i,
                    "label": label,
                    "pattern_idx": pat_idx,
                    "raw": stripped,
                })
                break  # first matching pattern wins

    if not candidates:
        return []

    # Determine which pattern is the "primary" one — the one that appears
    # most often.  This helps us distinguish real chapters from TOC entries.
    from collections import Counter
    pattern_counts = Counter(c["pattern_idx"] for c in candidates)
    primary_pattern = pattern_counts.most_common(1)[0][0]

    # Second pass: filter candidates
    filtered = []
    for c in candidates:
        # Skip TOC entries (dense clusters of headings near the top)
        if _is_in_toc(c["line"], lines, len(filtered)):
            continue

        # For bare numbers / bare Roman numerals, only keep them if they
        # are the primary pattern.  Otherwise they're too noisy.
        bare_idxs = {BARE_NUMBER_PATTERN_IDX, BARE_NUMBER_PATTERN_IDX_PERIOD, BARE_ROMAN_PATTERN_IDX, BARE_WORD_NUMBER_PATTERN_IDX}
        if c["pattern_idx"] in bare_idxs and primary_pattern not in bare_idxs:
            continue

        filtered.append(c)

    if not filtered:
        return []

    # Third pass: remove chapters that are too short (< MIN_CHAPTER_LENGTH chars)
    # This catches leftover TOC lines or false positives
    validated = []
    for i, chap in enumerate(filtered):
        start = chap["line"]
        end = filtered[i + 1]["line"] if i + 1 < len(filtered) else len(lines)
        content = "\n".join(lines[start:end])
        if len(content) >= MIN_CHAPTER_LENGTH or i == len(filtered) - 1:
            validated.append(chap)

    # Fourth pass: remove TOC bleed-through — if an early entry is a duplicate
    # label of a later entry but much smaller, it's a TOC line
    deduped = []
    label_sizes = {}
    # First, compute sizes for all entries
    for i, chap in enumerate(validated):
        start = chap["line"]
        end = validated[i + 1]["line"] if i + 1 < len(validated) else len(lines)
        size = len("\n".join(lines[start:end]))
        label_sizes.setdefault(chap["label"], []).append((i, size))

    # Mark entries to skip: for duplicate labels, keep only the largest
    skip_indices = set()
    for label, entries in label_sizes.items():
        if len(entries) > 1:
            max_size = max(s for _, s in entries)
            for idx, size in entries:
                # Skip if this is a tiny duplicate (< 10% of the largest)
                if size < max_size * 0.1:
                    skip_indices.add(idx)

    deduped = [c for i, c in enumerate(validated) if i not in skip_indices]

    return deduped


# ---------------------------------------------------------------------------
# Detect chapter-number restarts and add Part prefixes
# ---------------------------------------------------------------------------

_NUMBERED_LABEL_RE = re.compile(
    r'^(?:Chapter|Act)\s+\S', re.IGNORECASE
)


def _add_part_prefixes(result_chapters: list[dict]) -> None:
    """
    Detect when numbered chapter labels restart (e.g., "Chapter 1" appears
    again) and add "Part N" prefixes to ALL labels in each section.

    Only numbered labels (Chapter N, Act N) trigger restart detection.
    Named sections (Prologue, Interlude, Epilogue) don't trigger restarts
    but still receive the Part prefix if restarts exist.

    Modifies result_chapters in place.  Does nothing if no restarts found.
    """
    # Find restart points by tracking seen numbered labels
    seen_numbered: set[str] = set()
    restart_indices: list[int] = [0]  # Part 1 always starts at 0

    for i, chap in enumerate(result_chapters):
        label = chap["label"]
        if _NUMBERED_LABEL_RE.match(label):
            if label in seen_numbered:
                restart_indices.append(i)
                seen_numbered.clear()  # reset for the new part
            seen_numbered.add(label)

    # If no restarts detected, leave labels as-is
    if len(restart_indices) <= 1:
        return

    # Assign Part N prefix to every chapter
    part_num = 0
    restart_set = set(restart_indices)
    for i, chap in enumerate(result_chapters):
        if i in restart_set:
            part_num += 1
        chap["label"] = f"Part {part_num} {chap['label']}"


# ---------------------------------------------------------------------------
# Split a single book
# ---------------------------------------------------------------------------

def split_book(
    txt_path: Path,
    dry_run: bool = False,
) -> dict:
    """
    Split a book .txt into chapter files.

    Returns a dict with:
      'title': str
      'chapters': list of {'label': str, 'chars': int}
      'status': 'split' | 'no_chapters' | 'already_split'
      'front_matter_chars': int
    """
    title = txt_path.stem
    book_dir = txt_path.parent / title

    # Skip if already split
    if book_dir.exists() and any(book_dir.glob("*.txt")):
        return {
            "title": title,
            "chapters": [],
            "status": "already_split",
            "front_matter_chars": 0,
        }

    # Read the file
    for encoding in ("utf-8", "utf-8-sig", "latin-1"):
        try:
            text = txt_path.read_text(encoding=encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        text = txt_path.read_text(encoding="latin-1")

    lines = text.split("\n")

    # Detect chapter headings
    chapters = detect_chapters(lines)

    if len(chapters) < MIN_CHAPTERS:
        return {
            "title": title,
            "chapters": [],
            "status": "no_chapters",
            "front_matter_chars": 0,
        }

    # Build chapter content
    result_chapters = []
    front_matter_text = "\n".join(lines[:chapters[0]["line"]]).strip()

    for i, chap in enumerate(chapters):
        start = chap["line"]
        end = chapters[i + 1]["line"] if i + 1 < len(chapters) else len(lines)
        content = "\n".join(lines[start:end]).strip()
        result_chapters.append({
            "label": chap["label"],
            "content": content,
            "chars": len(content),
        })

    # Detect chapter-number restarts and add Part prefixes
    _add_part_prefixes(result_chapters)

    # Quality filter 1: reject splits that produce only a few massive chunks.
    # This catches books where we only found Prologue/Epilogue/Introduction
    # but no real chapter structure.
    MAX_AVG_CHAPTER_CHARS = 150_000  # 150K chars avg = not a real chapter split
    total_chapter_chars = sum(c["chars"] for c in result_chapters)
    avg_chapter_chars = total_chapter_chars / len(result_chapters)
    if avg_chapter_chars > MAX_AVG_CHAPTER_CHARS and len(result_chapters) < 3:
        return {
            "title": title,
            "chapters": [],
            "status": "no_chapters",
            "front_matter_chars": 0,
        }

    # Quality filter 2: reject splits with too many tiny chapters.
    # This catches bare-number false positives (e.g., page numbers from
    # PDF conversion producing 100+ "chapters" of ~2K chars each).
    MIN_MEDIAN_CHAPTER_CHARS = 3_000
    sorted_sizes = sorted(c["chars"] for c in result_chapters)
    median_chars = sorted_sizes[len(sorted_sizes) // 2]
    if median_chars < MIN_MEDIAN_CHAPTER_CHARS and len(result_chapters) > 20:
        return {
            "title": title,
            "chapters": [],
            "status": "no_chapters",
            "front_matter_chars": 0,
        }

    # Quality filter 3: reject lopsided splits where one chapter has >80% of
    # the total text.  This catches anthologies/collections where we find an
    # Introduction + one massive block + Epilogue but no real internal splits.
    max_chapter_chars = max(c["chars"] for c in result_chapters)
    if max_chapter_chars > total_chapter_chars * 0.8 and len(result_chapters) < 6:
        return {
            "title": title,
            "chapters": [],
            "status": "no_chapters",
            "front_matter_chars": 0,
        }

    # Quality filter 4: reject splits where all "chapters" share the same
    # label (e.g., three sections all labelled "PROLOGUE").
    unique_labels = {c["label"] for c in result_chapters}
    if len(unique_labels) == 1 and len(result_chapters) > 1:
        return {
            "title": title,
            "chapters": [],
            "status": "no_chapters",
            "front_matter_chars": 0,
        }

    # Quality filter 5: trim tiny trailing chapters that are likely backmatter
    # (e.g., "Also in this series" blurbs picked up as numbered titles).
    # If the last chapter is < 5K chars and < 10% of the median, drop it.
    if len(result_chapters) > 3:
        while len(result_chapters) > 3:
            last = result_chapters[-1]
            median_for_trim = sorted(c["chars"] for c in result_chapters)[len(result_chapters) // 2]
            if last["chars"] < 5_000 and last["chars"] < median_for_trim * 0.10:
                result_chapters.pop()
            else:
                break

    if dry_run:
        return {
            "title": title,
            "chapters": [{"label": c["label"], "chars": c["chars"]} for c in result_chapters],
            "status": "split",
            "front_matter_chars": len(front_matter_text),
        }

    # Write files
    book_dir.mkdir(parents=True, exist_ok=True)

    if front_matter_text:
        (book_dir / "front_matter.txt").write_text(front_matter_text, encoding="utf-8")

    used_filenames = {}  # track used filenames to avoid collisions
    for chap in result_chapters:
        # Sanitize label for filename
        safe_label = re.sub(r'[<>:"/\\|?*]', '-', chap["label"])
        # Deduplicate: if label already used, append a suffix
        if safe_label in used_filenames:
            used_filenames[safe_label] += 1
            safe_label = f"{safe_label} ({used_filenames[safe_label]})"
        else:
            used_filenames[safe_label] = 1
        filename = f"{safe_label}.txt"
        (book_dir / filename).write_text(chap["content"], encoding="utf-8")

    return {
        "title": title,
        "chapters": [{"label": c["label"], "chars": c["chars"]} for c in result_chapters],
        "status": "split",
        "front_matter_chars": len(front_matter_text),
    }


# ---------------------------------------------------------------------------
# Process a country folder
# ---------------------------------------------------------------------------

# Books handled by dedicated split scripts (not by this generic splitter)
EXCLUDE_BOOKS = {
    "Broken Stars",
    "Aelita",
    "Administrator by Taku Mayumura",
    "Orbital Cloud",
    "A View from the Stars",
    "The Wandering Earth",
    "Vagabonds",
    "ten billion days and one hundred billion nights",
    "Roadside Picnic",
    "The Three Body Problem_cleaned",
    "Quantum Thief",
    "Dune",
    # Too short to split — send to Gemini as-is
    "The Village Schoolteacher by Liu Cixin",
    "The Ouroboros Wave",
    "Day of the Oprichnik",
}


def find_unsplit_books(country_dir: Path) -> list[Path]:
    """Find .txt files sitting directly in the country folder (not in subdirs).
    Skips 'Human Split_' prefixed folders (used for comparison) and books
    in the EXCLUDE_BOOKS set (handled by dedicated scripts)."""
    return sorted(
        f for f in country_dir.iterdir()
        if f.is_file() and f.suffix.lower() == ".txt"
        and not f.name.startswith("Human Split_")
        and f.stem not in EXCLUDE_BOOKS
    )


def process_country(country_dir: Path, dry_run: bool = False) -> list[dict]:
    """Process all unsplit books in a country folder."""
    books = find_unsplit_books(country_dir)
    results = []

    for book_path in books:
        result = split_book(book_path, dry_run=dry_run)

        status_icon = {
            "split": "✓",
            "no_chapters": "?",
            "already_split": "→",
        }[result["status"]]

        print(f"  {status_icon} {result['title']}")

        if result["status"] == "split":
            for ch in result["chapters"]:
                print(f"      {ch['label']}  ({ch['chars']:,} chars)")
            if result["front_matter_chars"]:
                print(f"      [front matter: {result['front_matter_chars']:,} chars]")
        elif result["status"] == "no_chapters":
            print(f"      (no chapter delimiters found — left as-is)")
        else:
            print(f"      (already split into folder)")

        results.append(result)

    return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def list_countries() -> list[str]:
    if not BOOKS_DIR.exists():
        return []
    return sorted(
        d.name for d in BOOKS_DIR.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    )


def main():
    p = argparse.ArgumentParser(
        description="Split unsplit book .txt files into chapter files."
    )
    p.add_argument(
        "--country",
        help="Process only this country folder. If omitted, process all.",
    )
    p.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be split without writing any files.",
    )
    args = p.parse_args()

    if not BOOKS_DIR.exists():
        print(f"ERROR: books directory not found at {BOOKS_DIR}")
        sys.exit(1)

    countries = list_countries()
    if args.country:
        if args.country not in countries and args.country != "test":
            print(f"ERROR: '{args.country}' not found. Available: {', '.join(countries)}")
            sys.exit(1)
        targets = [args.country]
    else:
        # Skip 'test' folder
        targets = [c for c in countries if c != "test"]

    total_split = 0
    total_no_chapters = 0
    total_already = 0

    for country_name in targets:
        country_dir = BOOKS_DIR / country_name
        print(f"\n{'='*60}")
        print(f"  {country_name}")
        print(f"{'='*60}")

        results = process_country(country_dir, dry_run=args.dry_run)

        for r in results:
            if r["status"] == "split":
                total_split += 1
            elif r["status"] == "no_chapters":
                total_no_chapters += 1
            else:
                total_already += 1

    action = "Would split" if args.dry_run else "Split"
    print(f"\n{'='*60}")
    print(f"  {action}: {total_split} book(s)")
    if total_no_chapters:
        print(f"  No chapters found: {total_no_chapters} book(s) (left as-is)")
    if total_already:
        print(f"  Already split: {total_already} book(s)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
