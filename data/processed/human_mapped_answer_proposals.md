# Proposed Mapped-Answer Corrections (Human-Coded Files)

Generated: 2026-05-25 by the Phase 1 validation probe for Task 2
(`intercoder_reliability.Rmd`). Review and approve / amend, then I'll bake the
accepted version into `scripts/source.R` as `human_mapped_answer_corrections`
and the per-book exclusion lists into `human_coded_coverage_overrides`.

---

## A. Mechanical corrections (apply uniformly across all files)

These are unambiguous fixes for whitespace / shorthand. Recommended: accept all.

| From | To | Question | Files | N |
|---|---|---|---|---|
| `Moderate contestation (ongoing rivalry/disputes);` | `Moderate contestation (ongoing rivalry/disputes)` | Q1 | Three-Body | 1 |
| `Visiting / Temporary presence only (stations, missions, outposts);` | `Visiting / Temporary presence only (stations, missions, outposts)` | Q2 | Three-Body | 4 |
| `Moderately different (regular adaptation needed);` | `Moderately different (regular adaptation needed)` | Q12 (if moved) | Off on a Comet | 6 |
| `Civilian` | `Entirely civilian` | Q10 | Off on a Comet | 7 |

---

## B. Per-cell `→ NaN` (treat as if the human left it blank)

Freeform paragraphs that aren't a mapped answer. NaN → "Other / Unsure" via the
agreed coercion rule.

| Book | Chapter | Q | Recorded value (truncated) |
|---|---|---|---|
| Off on a Comet | 9 | Q2 | "Maybe? The 2 main characters somewhat tongue in cheek refer to themselves as the leader and population…" |
| Off on a Comet | (TBD) | Q10 | "Potentially somewhat military as the two main characters are members of the military…" |
| Off on a Comet | 1 | "General notes" row (proposed: drop, not load as Q12) | Long content-warning paragraph |

---

## C. Structural issues (need your call)

### C.1 Off on a Comet — "General notes" row

The file's 12th criteria row is labeled `"General notes"`, not a real Q12.
Proposed: drop this row from the loader; Off-on-a-Comet contributes zero Q12 data.

### C.2 Off on a Comet — Q4 answers look like Q12 wording

The 6 Q4 cells use options that match Q12's option list, not Q4's. Proposed:
**drop the Q4 entries** for Off-on-a-Comet rather than guess at re-mapping.
Alternative: move them to Q12 (i.e., the human used Q12's options because Q12
wasn't a slot in their sheet).

### C.3 Off on a Comet — Q5, Q8, Q11 missing entirely

These criteria rows do not exist in the file. No proposal — just record as "not
covered" in the report so the per-question IRR for this book excludes them.

### C.4 Planet of the Apes — Q12 missing entirely

The file has only Q1-Q11. No proposal — exclude Q12 for this book from IRR, or
back-fill.

### C.5 Ender's Game — re-canonicalized 2026-05-25

Donald rewrote the `answer` column to canonical labels and added an embedded
shorthand reference block at the right side of the CSV (rows 1..12, columns
5..12).  Re-probe summary (180 rows, no NaN):

```
176 cells already match the canonical answer_options for their question
  4 cells still need a mechanical fix:
       Q3  'long-distance journey'  -> 'Long-distance journey (years, major separation from Earth)'   (x3, chapters 13/14/15)
       Q12 'Mostly Earth-like with minor adaptations' -> 'Almost Earth-like'   (x1, chapter 15: a Q4 label was pasted into Q12 by mistake; the Q12 shorthand parallel is "earth-like" -> "Almost Earth-like")
```

Proposed correction table additions (folded into §A above for source.R):

| From | To | Question | File | N |
|---|---|---|---|---|
| `long-distance journey` | `Long-distance journey (years, major separation from Earth)` | Q3 | Ender's Game | 3 |
| `Mostly Earth-like with minor adaptations` | `Almost Earth-like` | Q12 | Ender's Game | 1 |

Note: The Q12 fix is the only judgment-call one — the cell at ch=15 Q12 used
a Q4 (cultural) option in a Q12 (physical) slot.  Mapping it to the parallel
Q12 shorthand "earth-like" -> "Almost Earth-like" preserves the rater's
clear intent ("world they colonize is essentially exactly [Earth-like]" in
their justification text).  If you'd rather drop the cell to "Other /
Unsure", say so and I'll switch the rule.

---

## E. Shorthand label map (from Ender's Game reference block)

Donald embedded a shorthand-label lookup at the right side of
`enders_game.csv` (rows 1..12, columns 5..12).  The map below is what I
extracted, aligned to the canonical `answer_options` in `questions.json` and
then proposed for encoding into `source.R` as `answer_options_short` — a
nested named list keyed first on `question_number`, then on canonical
answer text.  Plots in `analysis.Rmd` (and IRR per-question facets) will
use the short labels.

Two small fix-ups needed before encoding:

  - **Q5 typo**: the file says `shared lingua france + local variation`;
    proposed shorthand: `shared lingua franca + local variation` (with
    correct spelling).  Suggest accepting the spelling fix.
  - **Q7 missing level**: the file lists only 4 levels before "Other /
    Unsure" (`rare`, `uncommon`, `moderatecommon`, `normal`) but the
    canonical Q7 has 5 levels.  Proposed shorthand mapping:
      * `Exceptionally rare (few astronauts/explorers)`            -> `rare`
      * `Uncommon (small specialist population)`                    -> `uncommon`
      * `Moderately common (noticeable settlements/populations)`    -> `moderately common`  (fix typo `moderatecommon` -> two words)
      * `Common (many people live/work there)`                      -> `common`  (not in file; interpolated)
      * `Normalized / widespread (space habitation is ordinary ...)`-> `widespread`  (was `normal` in file; "widespread" reads more naturally next to "common")
      * `Other / Unsure`                                            -> `Other / Unsure`

Full proposed `answer_options_short` (canonical -> short):

```
Q1 (contestation)
  No contestation                                          -> no contestation
  Low contestation (minor competition, ...)                -> low contestation
  Moderate contestation (ongoing rivalry/disputes)         -> moderate contestation
  High contestation (frequent conflict ...)                -> high contestation
  Total war / constant conflict                            -> total war
  Other / Unsure                                           -> Other / Unsure

Q2 (inhabitable)
  Cannot inhabit or hold territory                         -> cannot inhabit
  Visiting / Temporary presence only (...)                 -> visiting/temporary only
  Limited settlement (...)                                 -> limited settlement
  Habitable and governable (...)                           -> habitable and governable
  Extensive territorial occupation (...)                   -> extensive occupation
  Other / Unsure                                           -> Other / Unsure

Q3 (journey distance)
  Near-Earth / very short journey                          -> near-earth/very short
  Short interplanetary journey                             -> short journey
  Moderate journey (months/meaningful separation)          -> moderate journey
  Long-distance journey (years, ...)                       -> long-distance journey
  Extreme / effectively unreachable (...)                  -> extreme/unreachable
  Other / Unsure                                           -> Other / Unsure

Q4 (cultural difference)
  Basically Earth society in space                         -> earth in space
  Mostly Earth-like with minor adaptations                 -> earth-like
  Mixed / hybrid culture                                   -> hybrid culture
  Distinct space culture                                   -> distinct space culture
  Radically different / alien social order                 -> radically different culture
  Other / Unsure                                           -> Other / Unsure

Q5 (language)
  Same languages as Earth                                  -> earth language
  Mostly same, with dialect/slang differences              -> dialect differences
  Shared lingua franca plus local variation                -> shared lingua franca + local variation
  Distinct space language(s)                               -> distinct languages
  Translation-mediated communication (...)                 -> translation-mediated
  Other / Unsure                                           -> Other / Unsure

Q6 (geographic hostility)
  Benign / easily survivable                               -> benign
  Manageable but risky                                     -> risky
  Harsh and resource-intensive                             -> harsh
  Extremely hostile (constant survival pressure)           -> hostile
  Nearly uninhabitable / lethal without major intervention -> uninhabitable/lethal
  Other / Unsure                                           -> Other / Unsure

Q7 (common experience)
  Exceptionally rare (few astronauts/explorers)            -> rare
  Uncommon (small specialist population)                   -> uncommon
  Moderately common (noticeable settlements/populations)   -> moderately common
  Common (many people live/work there)                     -> common
  Normalized / widespread (...)                            -> widespread
  Other / Unsure                                           -> Other / Unsure

Q8 (different countries)
  No political order / ungoverned                          -> ungoverned
  Single unified authority                                 -> single authority
  Earth nation-states extend into space                    -> Earth nation-states extend into space
  Multiple distinct space polities                         -> distinct polities
  Highly fragmented political landscape (...)              -> high fragmentation
  Other / Unsure                                           -> Other / Unsure

Q9 (genre)
  Adventure / exploration                                  -> adventure
  Drama                                                    -> drama
  Political / diplomatic                                   -> political
  Military / war                                           -> military/war
  Thriller / Horror / Survival                             -> thriller/horror
  Comedy / satire                                          -> comedy
  Other / Unsure                                           -> Other / Unsure

Q10 (military or civilian domain)
  Entirely civilian                                        -> civilian
  Mostly civilian with some military presence              -> mostly civilian
  Mixed civilian-military domain                           -> mixed
  Mostly military                                          -> mostly military
  Entirely military / war-focused                          -> military
  Other / Unsure                                           -> Other / Unsure

Q11 (nearest neighbor)
  Totally unique domain                                    -> unique
  Like the ocean / naval                                   -> ocean/naval
  Like the air / airpower                                  -> air/airpower
  Like the frontier / colonial expansion                   -> frontier/colonial
  Like cyberspace / networked or abstract domain           -> cyberspace
  Other / Unsure                                           -> Other / Unsure

Q12 (physical differences)
  Almost Earth-like                                        -> earth-like
  Somewhat different (manageable environmental ...)        -> minor differences
  Moderately different (regular adaptation needed)         -> moderately different
  Very different (human bodies/technology ...)             -> very different
  Radically non-Earth-like (...)                           -> radically different environment
  Other / Unsure                                           -> Other / Unsure
```

---

## D. Chapter alignment (human integer chapter -> Claude chapter label)

Four of the five IRR books have a trivial 1:1 alignment between the human's
integer chapter ID and Claude's chapter label / chapter_position.  Only Off on
a Comet needs a per-book lookup because Claude's labels include the part
prefix.

| Book                  | Claude rows | Human chapters | Rule                                            |
|-----------------------|-------------|----------------|-------------------------------------------------|
| The Martian           | 26          | 1..26          | `human N -> Claude row N` (`Chapter N`)         |
| Three-Body Problem    | 35          | 1..35          | `human N -> Claude row N` (`Chapter N`)         |
| Planet of the Apes    | 38          | 1..38          | `human N -> Claude row N` (`Chapter N`)         |
| Ender's Game          | 15          | 1..15          | `human N -> Claude `Chapter N - <TITLE>``       |
| **Off on a Comet**    | 43          | 1..10 (only)   | `human N -> Claude `Book 1 - Chapter N`` for N in 1..10 |

The Off-on-a-Comet rule is the substantive judgment call: the human only coded
the first 10 narrative chapters and the natural interpretation is that those
are the first 10 chapters of the book, which Claude splits as
`Book 1 - Chapter 1`..`Book 1 - Chapter 10`.  Will be exposed in
`source_irr.R` as an overridable named-list constant.

