import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 16 - Pilgrims and Wayfarers",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. Gorbovsky and Ivanov discuss space exploration cooperatively. The Voice of the Void is a mystery, not a source of conflict.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Gorbovsky describes visiting EN 101 and EN 2657 as temporary expeditions. No permanent settlements on those worlds are mentioned. The chapter is set at a lake on Earth.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Gorbovsky traveled to EN 101 and EN 2657, distant star systems. He became a radio source after his return, suggesting extreme conditions encountered far from Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Ivanov tags septipods as a biologist, Gorbovsky is a spaceship captain who fishes and philosophizes. Their culture, interests, and social interactions are entirely Earth-derived.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. No space-specific languages are mentioned even when discussing alien worlds and the Voice of the Void.",
        "q6": "Manageable but risky",
        "q6_justification": "Gorbovsky's body became a radio source emitting at wavelength 6.083 meters after his deep-space journey. Space travel has real physiological consequences, but they are manageable.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Gorbovsky represents a small specialist class of deep-space explorers. Ivanov is an Earth-based biologist. Space exploration involves a dedicated but limited community.",
        "q8": "Single unified authority",
        "q8_justification": "All space activity is coordinated cooperatively. The Voice of the Void is studied collectively. No competing political entities govern space.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on Gorbovsky's mysterious transformation into a radio source and philosophical discussions about alien intelligence, the Voice of the Void, and humanity's place in the cosmos.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: biological field research, fishing, philosophical discussion about astroarchaeology and alien signals. No military context exists.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Gorbovsky describes exploring distant star systems and searching for traces of alien civilizations, framing space as an archaeological frontier full of mysteries to uncover.",
        "q12": "Other / Unsure",
        "q12_justification": "The chapter is set at a lake on Earth. Space environments are referenced through Gorbovsky's stories but not directly depicted.",
    },
    {
        "chapter": "Chapter 17 - The Planet with All the Conveniences",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. Komov's Pathfinder team explores planet Leonida cooperatively. Gorbovsky confiscated weapons, emphasizing peaceful intent.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The team establishes a temporary base on Leonida with cyberbuilders. This is a Pathfinder mission, not a permanent settlement. Waseda was left as a temporary caretaker.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Leonida orbits EN 23, a distant star system. The crew arrived by D-ship across interstellar distances, representing major separation from Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The Pathfinder team maintains Earth culture: Komov leads as a standard expedition commander, Mboga serves as zoopsychologist, and their social dynamics mirror Earth institutions.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian and Japanese. Waseda and Komov speak standard Earth languages. No space-specific languages appear.",
        "q6": "Benign / easily survivable",
        "q6_justification": "Leonida has breathable air, real water, grass, rivers, and comfortable temperatures. It is described as a planet with all the conveniences, almost suspiciously Earth-like.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only a handful of Pathfinders are on Leonida: Komov, Mboga, Waseda, and a few others. They represent the vanguard exploring an entirely new world.",
        "q8": "Single unified authority",
        "q8_justification": "The Pathfinder team operates under unified Earth authority. Gorbovsky confiscated weapons as policy. The Commission on Preservation of Wildlife of Alien Planets governs conduct.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows Pathfinders exploring an alien planet: discovering gray limestone alien buildings, investigating mysterious conveniences, and encountering an Earth-like world that raises questions about its origins.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian scientific exploration. Gorbovsky explicitly confiscated weapons. Mboga is a zoopsychologist, Waseda an atmosphere physicist.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Pathfinders explore and establish a base on a new world, encountering alien ruins and setting up cyberbuilder construction. The framing echoes frontier exploration and settlement.",
        "q12": "Almost Earth-like",
        "q12_justification": "Leonida is remarkably Earth-like: breathable atmosphere, real water, grass, rivers, and comfortable conditions. The alien city's gray limestone buildings are the main difference.",
    },
    {
        "chapter": "Chapter 18 - Defeat",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is set entirely on Earth's Kuril Islands. No space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory or habitation is portrayed. The chapter follows Sidorov testing the embryomech Egg on a volcanic island.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. The chapter is entirely about testing a self-replicating machine on Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The advanced 22nd-century Earth society is shown: embryomechs designed for planetary exploration, automated technology, and the legacy of 20th-century wars still buried underground.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. No space-related language dynamics appear.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The chapter takes place on a volcanic island on Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not discussed in this Earth-set chapter about embryomech testing.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Drama",
        "q9_justification": "Sidorov watches his embryomech Egg attempt to build a factory, only for it to be destroyed when it encounters buried World War II ammunition. His years of work end in defeat.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter depicts civilian scientific testing of exploration technology.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed in this entirely terrestrial chapter.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is a volcanic island in the Kuril chain on Earth.",
    },
    {
        "chapter": "Chapter 19 - The Meeting",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. Pol reflects on past exploration missions cooperatively conducted. The ethical dilemma is personal, not geopolitical.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Pol's missions to alien planets were temporary expeditions. The Museum of Exozoology on Earth houses specimens from these visits. No permanent off-world settlements are described.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Pol explored planet Crookes in the EN 92 system (a red dwarf). Exhibits come from Pandora, Ruzhen, and Vladislava. These interstellar distances represent major separation from Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The Capetown Museum of Exozoology is a standard Earth institution. Pol is a retired Hunter now working as a museum guard. Earth society extends to space exploration but remains Earth-derived.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue and narration is in standard Earth languages. No space-specific languages are mentioned.",
        "q6": "Manageable but risky",
        "q6_justification": "Pol's memories of planet Crookes show real danger: he killed a creature that may have been an intelligent alien when its oxygen tank ignited in the hydrocarbon atmosphere. Space exploration carries serious risks.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Pol was a Hunter, a specialist explorer of alien worlds. The museum's exhibits represent decades of work by a small community of interstellar explorers.",
        "q8": "Single unified authority",
        "q8_justification": "All exploration is coordinated under unified Earth authority. The Museum of Exozoology and the discovery of a landing pad on Crookes are managed through centralized institutions.",
        "q9": "Drama",
        "q9_justification": "The chapter is haunted by Pol's guilt over possibly killing an intelligent alien on Crookes. He is tormented by the memory, especially after a landing pad was found there, suggesting the creature may have been a visiting spacefarer.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: museum work, biological specimen collection, and scientific exploration. Pol is a civilian Hunter, not military.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Pol explored alien frontier worlds as a Hunter, encountering unknown species and environments. The ethical dilemma of killing a possibly intelligent being parallels colonial-era encounters with indigenous peoples.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Planet Crookes has a hydrocarbon atmosphere where oxygen is explosive. Vladislava has eyeless monsters. These alien worlds differ significantly from Earth but are navigable with technology.",
    },
    {
        "chapter": "Chapter 20 - What You Will Be Like",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. Gorbovsky, Kondratev, and Slavin discuss space cooperatively over a fishing trip. The Contact Commission works peacefully with aliens on Tagora.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Gorbovsky references the Contact Commission for Tagora, implying sustained diplomatic presence on alien worlds. The breadth of space activity described suggests permanent infrastructure across many systems.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Tagora and other alien contact worlds are at interstellar distances. Gorbovsky's stories span many star systems, representing major separation from Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The three friends fish, cook soup, and discuss amusements and olfactiles. Their leisure culture is entirely Earth-derived even as they discuss interstellar contacts and time travel.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. Even discussion of alien contacts and the far future uses standard Earth languages.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter is set at an Earth river during a fishing trip. No space environment is directly depicted.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The Contact Commission for Tagora, widespread interstellar exploration, and the casual way space travel is discussed suggest that space habitation has become common in this era.",
        "q8": "Single unified authority",
        "q8_justification": "The Contact Commission operates under unified Earth authority. Gennady Komov leads the commission. No competing political entities govern space activity.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter is warmly comic: three friends argue over fish soup recipes, discuss absurd amusements, and Gorbovsky tells a fantastical story about meeting a time traveler from the far future named Petr Petrovich.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: fishing, cooking, philosophical discussion, and references to the civilian Contact Commission. No military context exists.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "References to the Contact Commission and alien civilizations frame space as a frontier where humanity establishes diplomatic and cultural relations with new peoples.",
        "q12": "Other / Unsure",
        "q12_justification": "The chapter is set at a river on Earth. Space environments are not directly depicted, though alien worlds are referenced in conversation.",
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

print('Done batch 4.')
