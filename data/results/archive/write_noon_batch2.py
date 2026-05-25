import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 6 - Two from the Taimyr",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. Kondratev recovers in hospital while Slavin explores the 22nd century. All space activity is cooperative.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The year is 2119 and D-ships now travel interstellar distances. Orbital infrastructure exists (the Big Mirror Slavin damaged). Space is routinely inhabited and governed.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Kondratev and Slavin have jumped a full century due to sigma-deritrinitation near the light barrier. Their separation from their original time is total and irreversible.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The 22nd-century society is advanced but recognizably Earth-derived: hospitals, pterocars, fashionable clothing, and familiar social interactions. Slavin adapts to modern customs.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. Slavin and Kondratev speak the same language as the 22nd-century inhabitants, with only minor pronunciation differences noted.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter is set entirely in a hospital on Earth. No space environment is directly depicted, though the Taimyr's crash and Kondratev's injuries testify to space dangers.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "D-ships are now routine vessels. Slavin mentions that all long-range ships work on the deritrinitation principle. Space travel has become a common aspect of civilization.",
        "q8": "Single unified authority",
        "q8_justification": "The unified Earth society is implied throughout. The Northwest Asian Economic Council and centralized medical system suggest a single governing authority.",
        "q9": "Drama",
        "q9_justification": "The chapter is an emotional reunion between injured Kondratev and his friend Slavin, centering on their struggle to adapt to a world a century beyond their own. The pain and isolation are deeply felt.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: hospital care, writing a book, exploring the new world. The Taimyr expedition was a civilian research mission.",
        "q11": "Other / Unsure",
        "q11_justification": "The chapter is set in a hospital. Space is referenced through the D-ship technology and the Taimyr's history, but no space domain is directly portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The chapter takes place entirely in a hospital room on Earth in the Ural Mountains.",
    },
    {
        "chapter": "Chapter 7 - The Moving Roads",
        "q1": "No contestation",
        "q1_justification": "No competition over space exists. Venus colonization is a cooperative international effort with volunteers from all backgrounds working together.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "Venus has an established but harsh colony. Moskvichev describes 20,000+ workers living underground, not seeing blue sky for months, waiting weeks for greenhouse grass. Settlement exists but is difficult to sustain.",
        "q3": "Short interplanetary journey",
        "q3_justification": "D-ships transport 600 people to Venus in about two days. Moskvichev says the day after tomorrow we will be there. Venus is a routine interplanetary destination.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The Venus volunteers are ordinary Earth citizens: a meteorologist, heavy-systems operator, World Council member. They bring Earth society's values and debates to Venus.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. The diverse characters (Moskvichev, Zavadskaya, Marina, Aleksandr) all speak the same Earth languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Venus is described as having radioactive deserts and black storms. Workers live underground, rarely see sky, and conditions are described as intolerably difficult. Kondratev remembers it as terrifying.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Venus has 20,000+ workers, a growing but still specialist population. Volunteers are eagerly sought, and D-ships ferry groups of hundreds. Space habitation is expanding but not yet common.",
        "q8": "Single unified authority",
        "q8_justification": "The World Council governs space activity. Zavadskaya is a World Council member going to Venus to assess conditions. No competing political entities exist.",
        "q9": "Drama",
        "q9_justification": "Kondratev wanders through the 22nd-century city feeling useless, explores the Yellow Factory, and meets passionate Venus volunteers. The emotional core is his search for purpose in an alien world.",
        "q10": "Entirely civilian",
        "q10_justification": "All Venus activity is civilian: volunteers, engineers, surgeons, meteorologists. The colonization project is organized by the World Council as a civilian enterprise.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Venus is explicitly a frontier. Volunteers rush to build cities on swamps, face ferocious storms, and a voice in the dark describes humanity's interplanetary expansion as the discharge of a giant electric potential.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Venus is described as having radioactive deserts, black storms, and conditions requiring underground living. Workers endure extreme hardship, and Kondratev imagines small Marina facing these conditions with horror.",
    },
    {
        "chapter": "Chapter 8 - Cornucopia",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is a domestic comedy set entirely on Earth. No space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory or habitation is portrayed. The chapter focuses on Evgeny and Sheila's home life and their struggle with a kitchen machine.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. Evgeny briefly references the Taimyr flight and being the first person born on Mars, but no journey occurs in this chapter.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The advanced 22nd-century Earth society is shown: cybernetic appliances, waste-disposal robots, Home Delivery systems, and suburban cottage living. This is the society that has expanded into space.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. Evgeny, Sheila, and neighbor Yurii speak standard Earth languages.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The entire chapter takes place in a suburban cottage on Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not discussed in this domestic comedy chapter.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown. The chapter depicts everyday domestic life.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter is pure comedy: Evgeny battles the UKM-207 kitchen machine, producing inedible goulash and losing a loaf of bread, while neighbor Yurii has similarly dismantled his washing machine.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian domestic life: reading, writing, cooking attempts, and conversations with neighbors about waste disposal technology.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. The chapter is set entirely in a domestic Earth setting.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is a suburban cottage with garden, apple trees, and bushes.",
    },
    {
        "chapter": "Chapter 9 - Homecoming",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. Gorbovsky describes cooperative space exploration, and the Venus project is a unified international effort.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "D-ships routinely travel to Venus and interstellar destinations. Gorbovsky mentions his ship Tariel going to EN 17 at 12 parsecs. Space is extensively inhabited with permanent infrastructure.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Gorbovsky describes going to EN 17, twelve parsecs out, on the frontier. The Taimyr's journey across a century of time is still fresh. Interstellar distances involve major separation.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Space explorers are ordinary Earth citizens: Gorbovsky loves couches and catches colds, Zvantsev is a practical oceanographer. Earth society extends unchanged into space.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. No space-specific languages are mentioned in conversations about interstellar exploration.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Kondratev's vivid flashback to Blue Sands describes oceans of fine blue dust, ferocious gales and typhoons, green flame whirlwinds, and Koenig being crushed and carried hundreds of miles into the desert.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "D-ships ferry Venus volunteers by the hundreds. Gorbovsky describes four problems that spacers work on, suggesting a large spacefaring population. Even proud D-principle researchers ferry volunteers.",
        "q8": "Single unified authority",
        "q8_justification": "A single unified Earth authority governs all space activity. Gorbovsky describes the Cosmonautical Museum, unified exploration programs, and the Venus project under central coordination.",
        "q9": "Drama",
        "q9_justification": "Kondratev is desperately lonely and searching for purpose. Gorbovsky and Zvantsev arrive to recruit him for the Oceanic Guard, giving him new meaning. The emotional arc is deeply personal.",
        "q10": "Entirely civilian",
        "q10_justification": "All space activity is civilian: scientific exploration, archaeological searches for alien traces, Venus colonization, and oceanographic work. No military context exists.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Gorbovsky describes searching for traces of alien civilizations on frontier planets, exploring Vladislava at 12 parsecs. The framing is of expansion into unknown territory.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Blue Sands is vividly described: oceans of fine blue dust with tides and typhoons, round-dances of green flame, blue dunes that shouted and howled, and dust clouds crawling like giant amoebas. Utterly alien.",
    },
    {
        "chapter": "Chapter 10 - Languor of the Spirit",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is set entirely on Earth at a cattle farm. No space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory or habitation is portrayed. The chapter focuses on Pol visiting Kostylin at a cattle farm.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted or referenced significantly. The chapter is entirely about personal life on Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The advanced Earth society is shown: automated cattle farms, cybernetic technology, and a society where personal fulfillment is the central concern rather than material needs.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian between Pol and Kostylin. No space-related language dynamics appear.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The chapter takes place at a cattle ranch on Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not discussed in this Earth-set chapter about personal relationships and unhappy love.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown. The chapter depicts personal drama at a cattle farm.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on Pol's unhappy love and his philosophical discussion with Kostylin about whether happy love is inherently boring. Kostylin announces his upcoming marriage.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter depicts cattle farming and personal conversations.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed in this entirely terrestrial chapter.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is a cattle farm on Earth with pastures, barns, and laboratory facilities.",
    },
]

country = 'Russia'
book_title = 'Noon: 22nd Century'
csv_path = 'data/results/Russia_Noon__22nd_Century.csv'
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

print('Done batch 2.')
