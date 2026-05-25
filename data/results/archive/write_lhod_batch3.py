import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 14 - The Escape",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Estraven infiltrates the prison farm and rescues Genly through stealth, not combat. The conflict is against the state, not in open warfare.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly remains a stranded temporary visitor; Estraven's rescue underscores the lack of any off-world support infrastructure.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Estraven had hoped Genly signaled the Ship before arrest, but with no ansible, off-world help is impossibly distant.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Estraven uses dothe (voluntary summoning of body's full strength from Handdara training), a uniquely Gethenian ability.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Estraven and Genly communicate in Karhidish; Estraven also uses Orgota with guards. Both are alien languages.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The escape occurs in deep winter with heavy snow; Genly is near death from starvation, drugging, and cold.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is the only off-worlder; his rescue is a personal act by one individual, not institutional support.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Karhide, Orgoreyn, and the Ekumen operate independently; Estraven uses contacts in both nations.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a tense escape narrative: infiltration, drugging, carrying an unconscious man through snow, evading guards.",
        "q10": "Entirely civilian",
        "q10_justification": "The prison guards are civilian, and the escape involves no military forces.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The daring rescue in hostile wilderness echoes frontier captivity and escape narratives.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Genly's non-Gethenian body has been poisoned by drugs meant for Gethenians; the winter cold nearly kills him.",
    },
    {
        "chapter": "Chapter 15 - To the Ice",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Genly and Estraven plan their route to avoid authorities; the conflict is evasion rather than open struggle.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly discusses the NAFAL ship in orbit but it remains distant; his presence on Gethen is still temporary.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The ship needs at least 8 days to reach Gethen on rocket drive; NAFAL drive cannot be used within a solar system.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Gethenian wilderness survival skills, shifgrethor social codes, and Estraven's stolen-food shame reflect alien values.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Genly and Estraven speak Karhidish together; they negotiate names and forms of address in alien social conventions.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The journey begins in deep winter through mountains, rain, and snow; diarrhea, cold, and exhaustion threaten Genly.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is the sole alien, entirely dependent on Estraven for survival in the wilderness.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "They must cross from Orgoreyn to Karhide, two distinct nations, while the Ekumen waits in orbit.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter begins an 800-mile wilderness trek across glaciers: a classic adventure/exploration narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "Two civilians undertake a survival journey; no military forces are involved.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The overland trek through unmapped glacial wilderness strongly evokes frontier exploration.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Rain, cold, altitude, and hostile terrain constantly challenge Genly's Earth-adapted body.",
    },
    {
        "chapter": "Chapter 16 - Between Drumner and Dremegole",
        "q1": "No contestation",
        "q1_justification": "The two travelers are alone on the glacier between erupting volcanoes; no political or military contestation occurs.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly remains a visitor to Gethen, now traversing its most inhospitable regions.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Genly reveals he was born 120 years ago on Earth due to relativistic time dilation, underscoring the extreme separation.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Estraven enters kemmer while on the ice; they discuss women and sexual difference, highlighting the alien biology.",
        "q5": "Distinct space language(s)",
        "q5_justification": "They speak Karhidish together; Estraven quotes poetry in his language. Orgota terms appear in the journal.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Active volcanic eruptions on the glacier, earthquakes, falling cinders, frostbite, and extreme conditions make the region nearly lethal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is the only off-worlder, now in one of the most remote places on the planet.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Discussion of Ekumenical worlds and Genly's time-jumping between planets implies multiple distinct space polities.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is a harrowing account of crossing a glacier between erupting volcanoes: pure adventure.",
        "q10": "Entirely civilian",
        "q10_justification": "Two civilian travelers navigate volcanic terrain; no military presence exists.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The trek across unmapped, lethal volcanic ice strongly evokes frontier exploration of unknown territory.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Erupting volcanoes on glaciers, earthquakes shaking the ice, falling cinders mixed with snow: fundamentally unlike Earth.",
    },
    {
        "chapter": "Chapter 17 - An Orgota Creation Myth",
        "q1": "Other / Unsure",
        "q1_justification": "This creation myth does not address space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "The myth describes the creation of the world from ice and sun, with no reference to space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No interstellar travel is referenced in this prehistoric myth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The myth depicts Gethenian kemmer and creation from ice, reflecting a fundamentally alien cultural worldview.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The myth is from a pre-Yomesh text found in a cave shrine, told in an ancient Gethenian language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The myth begins with nothing but ice and sun, depicting a world born from extreme cold.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed in this creation myth.",
        "q8": "Other / Unsure",
        "q8_justification": "The myth concerns mythological origins, not political structures.",
        "q9": "Other / Unsure",
        "q9_justification": "This is a creation myth, not a standard narrative genre.",
        "q10": "Entirely civilian",
        "q10_justification": "The myth involves mythological figures, not military forces.",
        "q11": "Other / Unsure",
        "q11_justification": "The myth provides no analogy for space as a domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The myth's world is born from ice and shaped by primal cold, reflecting Gethen's harsh environment.",
    },
    {
        "chapter": "Chapter 18 - On the Ice",
        "q1": "No contestation",
        "q1_justification": "The two travelers are alone on the Gobrin Ice; no conflict or contestation over territory occurs.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly remains a temporary visitor, now crossing the most desolate part of Gethen.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Genly teaches Estraven mindspeech, connecting two beings from worlds separated by vast interstellar distances.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Estraven's kemmer, the development of mindspeech between them, and the exploration of gender difference reveal a radically alien social context.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Mindspeech is taught across species; Estraven hears it in Karhidish. Multiple distinct communication systems coexist.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Temperatures drop below -60F, blizzards last days, and survival depends entirely on precise rationing and equipment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is the sole alien on the planet, isolated on the ice with one companion.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Discussion of the Ekumen's customs and Karhide's potential membership implies multiple space polities.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter chronicles the grueling daily routine of crossing the ice sheet: a quintessential exploration narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "Two civilians cross the ice; no military element is present.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The crossing of the Gobrin Ice echoes frontier exploration of unknown, lethal wilderness.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "White weather with no shadows, temperatures below -60F, breath freezing into snow crystals: fundamentally unlike Earth.",
    },
    {
        "chapter": "Chapter 19 - Homecoming",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Political maneuvering leads to Estraven's death at the border; governments fall but through political shifts, not warfare.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The starship finally lands with 11 crew, but this is a first-contact landing, not permanent settlement.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The nearest allied world is 17 years away; Earth is 50 years away by ship. The distances are effectively generational.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The arrival of the ship crew highlights the radical difference: Genly sees his own people as strange after adapting to Gethen.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The first Ekumenical greeting is delivered in Karhidish; multiple languages coexist across worlds.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The final ice crossing, border guards shooting Estraven, and extreme cold maintain constant survival pressure.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only 11 people arrive on the ship. Space habitation remains exceptionally rare; this is first contact.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Karhide joins the Ekumen; Orgoreyn's government falls and reforms. Multiple distinct polities negotiate.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter resolves the diplomatic mission: the ship lands, Karhide receives the Ekumen, and governments change.",
        "q10": "Entirely civilian",
        "q10_justification": "The ship carries civilians; the diplomatic reception is civilian. Border guards shoot Estraven but this is police action.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The first ship landing on Gethen, diplomatic reception, and Genly's visit to Estraven's ancestral home echo frontier first-contact narratives.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The ship lands on frozen marshland; the crew enters a world of ice. Genly has been physically transformed by his ordeal.",
    },
]

country = 'US'
book_title = "The Left Hand of Darkness"
csv_path = "data/results/US_The_Left_Hand_of_Darkness.csv"
questions = [{'number': i} for i in range(1, 13)]
fieldnames = ['country', 'book', 'chapter']
for q in questions:
    fieldnames.append('q' + str(q['number']))
for q in questions:
    fieldnames.append('q' + str(q['number']) + '_justification')

existing_chapters = set()
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_chapters.add(row['chapter'])

for ch_data in chapters_data:
    chapter = ch_data['chapter']
    if chapter in existing_chapters:
        print('Skipped (already exists): ' + chapter)
        continue
    row_dict = {'country': country, 'book': book_title, 'chapter': chapter}
    for q in questions:
        n = q['number']
        row_dict['q' + str(n)] = ch_data['q' + str(n)]
        row_dict['q' + str(n) + '_justification'] = ch_data['q' + str(n) + '_justification']
    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row_dict)
    print('Written: ' + chapter)

print('Done batch 3.')
