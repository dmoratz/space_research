import json, csv, os

chapters_data = [
    {
        "chapter": "Introduction",
        "q1": "Other / Unsure",
        "q1_justification": "The Introduction is Theodore Sturgeon's critical essay about the book, not a narrative chapter. No space contestation is depicted in any story sense.",
        "q2": "Other / Unsure",
        "q2_justification": "As a meta-commentary essay, no space territory or habitation is portrayed narratively. Sturgeon discusses D-ships and Mars abstractly.",
        "q3": "Other / Unsure",
        "q3_justification": "Sturgeon discusses time dilation and D-ships conceptually, noting that a year aboard a D-ship means a century on Earth, but no journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No social order is depicted directly. Sturgeon describes the book's themes of unanimity among humans and fellowship of sapience.",
        "q5": "Other / Unsure",
        "q5_justification": "No language dynamics are portrayed. Sturgeon notes characters with English, German, and Japanese names appear in the stories.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. Sturgeon mentions Mars surface and blue star atmospheres only as examples of the authors' storytelling skill.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation frequency is portrayed. Sturgeon references orbiting D-ships and scouts but as narrative summaries, not depictions.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order is depicted. Sturgeon notes the authors see unanimity among humans in the future world.",
        "q9": "Other / Unsure",
        "q9_justification": "The Introduction is a critical essay, not a narrative. It has no genre tone of its own beyond literary criticism.",
        "q10": "Other / Unsure",
        "q10_justification": "No civilian or military space activity is depicted. Sturgeon discusses the book's themes abstractly.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain framing is depicted. Sturgeon references interstellar and intergalactic travel conceptually.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is portrayed directly. Sturgeon mentions Mars and blue star planets only as examples of the authors' imagination.",
    },
    {
        "chapter": "Chapter 1 - Night on Mars",
        "q1": "No contestation",
        "q1_justification": "Earth colonists on Mars cooperate without any competing powers or conflict over space. The international team includes Russians, Canadians, and Japanese working together.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "Mars has bases, biostations, and small settlements, but the colony is small and vulnerable. The first child is about to be born on Mars, and crawlers are the main transport across dangerous desert.",
        "q3": "Short interplanetary journey",
        "q3_justification": "Mars is within the solar system. The doctors and Pathfinders operate from a nearby base, and ships from Earth arrive yearly. No interstellar distances are involved.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The colonists maintain Earth social norms: Russian doctors, a Canadian Pathfinder, Japanese researcher Hasegawa. Their behavior, language, and social dynamics are transplanted Earth culture.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Russian and English. Morgan speaks English, Opanasenko speaks Russian. No space-specific languages exist.",
        "q6": "Manageable but risky",
        "q6_justification": "Mars requires oxygen masks, fur clothing, and lead-soled boots, but survival is manageable. The flying leech poses real danger at night, and quicksand patches exist, but the colonists cope with equipment and Pathfinder escorts.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "The Mars colony has a base, biostations, and Pathfinder camps, representing a small specialist population of scientists, doctors, and explorers. Five years of colonization with modest numbers.",
        "q8": "Single unified authority",
        "q8_justification": "All Mars colonists operate under a single cooperative authority. Russians, Canadians, and Japanese work together without competing political entities.",
        "q9": "Adventure / exploration",
        "q9_justification": "Two doctors cross the Martian desert at night, fight off a flying leech with Pathfinder escorts, and race to deliver the first baby born on Mars. The tone is pure adventure.",
        "q10": "Entirely civilian",
        "q10_justification": "All characters are civilian: doctors Novago and Mandel, Pathfinders Opanasenko and Morgan (explorers/archaeologists), and the Slavin family at the biostation.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Mars is explicitly a frontier: first child being born, Pathfinders searching for traces of ancient Martian civilization, dangerous wildlife, small settlements pushing into wilderness.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Mars has reduced gravity (180-pound Novago weighs 90 pounds), thin atmosphere requiring oxygen masks, extreme cold, and alien wildlife, but colonists manage with appropriate technology.",
    },
    {
        "chapter": "Chapter 2 - Almost the Same",
        "q1": "No contestation",
        "q1_justification": "No conflict over space exists. The nationalization of United Rocket Construction is presented as international cooperation, not competition.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Space is accessed through ships and missions. The Moon is a launching pad, Mars has colonists, Venus has actinides extraction, but the chapter focuses on Earth-based training for space travel.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Panin describes a hypothetical journey to UV Ceti at 2.4 parsecs, taking decades subjectively while 150 years pass on Earth. The Khius-Lightning departs for Interstellar One at 1.5 light-months.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The Advanced School of Cosmonautics is a normal Earth institution with cadets, instructors, volleyball courts, and dining halls. Society extending into space remains fundamentally Earth-like.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian and English. Cadets include Vietnamese (Nguyen), Georgian (Gurgenidze), and others, all speaking the same languages as on Earth.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Space travel requires extreme physical conditioning: cadets train at 5-8 gravities weekly, the Khius-Lightning operates at 6G maximum, and Bykov survived 12G. The demands are enormous.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Spacemen are an elite specialist population trained at the Advanced School of Cosmonautics. Cadets undergo years of rigorous selection and conditioning.",
        "q8": "Single unified authority",
        "q8_justification": "International cooperation is explicit: United Rocket Construction is being nationalized for collective benefit. The Lightning launches from an international context.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on Sergei's personal crisis: forbidden from high-G training, struggling with his relationship with Katya, and his burning ambition for interstellar travel. The emotional stakes are deeply personal.",
        "q10": "Entirely civilian",
        "q10_justification": "The School of Cosmonautics is a civilian institution. All space activity described is scientific exploration and research, not military.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Venus is for actinides, Mars for colonization, and the stars represent the ultimate frontier. Panin's monologue frames interstellar travel as expansion into the unknown with colonial-era consequences.",
        "q12": "Other / Unsure",
        "q12_justification": "No actual space environment is depicted in this Earth-set chapter. Space is discussed in terms of training requirements and hypothetical journeys, not environmental conditions.",
    },
    {
        "chapter": "Chapter 3 - Old-timer",
        "q1": "No contestation",
        "q1_justification": "No competing powers contest space. The traffic controller manages orbital space cooperatively, and all stations respond to a unified command structure.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Earth orbit is densely populated with orbital hangars, fueling stations, the Orbiting Observatory's Big Reflector, near-Earth stations, and D-ship launching zones. Permanent infrastructure fills multiple orbital zones.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The Taimyr has been gone for over a century. Slavin emerges calling the onlookers 'great-great-grandchildren,' highlighting the profound temporal separation caused by their near-light-speed journey.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Orbital space is managed by traffic controllers, assistants, and emergency officers using familiar organizational structures. The society in orbit mirrors Earth institutions.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in Russian. Slavin requests touchdown permission in standard language. No space-specific languages exist.",
        "q6": "Manageable but risky",
        "q6_justification": "Orbital space is generally managed safely with traffic control and emergency robots, but the uncontrolled nuclear rocket poses catastrophic collision risk, grazing the Big Mirror and threatening stations.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Orbital space is dense with infrastructure: multiple zones, orbital hangars, fueling stations, D-ship launching areas, and an observatory. The controller's daughter works on a station. Many people operate in near-Earth space.",
        "q8": "Single unified authority",
        "q8_justification": "A single Main Control manages all orbital traffic. All flights, touchdowns, and stations respond to unified commands. No competing authorities exist.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a tense emergency: an uncontrolled ancient nuclear rocket careens through densely populated orbital space, grazing mirrors, threatening stations, while the controller desperately coordinates emergency robots.",
        "q10": "Entirely civilian",
        "q10_justification": "All personnel are civilian: traffic controllers, emergency officers, observatory staff. The emergency response is a civilian operation with no military involvement.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Orbital space is managed like a maritime zone: traffic control, designated zones, emergency response protocols, and the controller monitoring a screen tracking vessels evokes naval traffic management.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Near-Earth orbital space is managed with extensive infrastructure but remains fundamentally different from Earth's surface. The vacuum environment requires specialized stations, and collision risks are ever-present.",
    },
    {
        "chapter": "Chapter 4 - The Conspirators",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. The World Council unanimously approves the Venus terraforming project, and all space activity is cooperative.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "Venus is being prepared for colonization through Operation October's atmosphere precipitation project. The planet requires massive terraforming before habitation, indicating limited current settlement.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The boys plan to stow away on an interplanetary tanker bound for Pluto, and Venus is accessible by regular cargo flights. These are routine solar system journeys.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The Anyudin School is a standard Earth educational institution. The boys discuss space using Earth cultural frameworks: captains, engineers, navigators modeled on Earth roles.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian. The boys use Earth languages exclusively, and no space-specific languages are mentioned.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is directly depicted. Venus is discussed as requiring atmosphere regeneration, implying hostility, but no environmental details are shown in this Earth-set chapter.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Spacemen are described as a specialist profession. The boys learn that the most honored professionals are teachers and doctors, not spacemen, suggesting space workers are a small elite.",
        "q8": "Single unified authority",
        "q8_justification": "The World Council governs all space activity, examining and approving the Venus plan. No competing political entities exist.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter is warmly comic: four boys plan an absurd escape to Venus, their teacher cleverly manipulates them into staying, they punish bully Walter Saronian, and their grand Operation October collapses hilariously.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: a school, teachers, the World Council's civilian Venus project. No military presence or context exists.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Venus is explicitly a new frontier to be colonized and transformed. The boys dream of going there as pioneers, and the World Council's project echoes historical colonization efforts.",
        "q12": "Other / Unsure",
        "q12_justification": "The chapter is set entirely at the Anyudin School on Earth. No space environment is directly depicted or described in detail.",
    },
    {
        "chapter": "Chapter 5 - Chronicle",
        "q1": "No contestation",
        "q1_justification": "The Taimyr-Ermak expedition is an international cooperative effort under the USCR Academy of Sciences. No competing powers or conflict over space are mentioned.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The expedition departs from the international spaceport Pluto-2 on a deep-space research mission. The presence is purely exploratory and temporary.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The expedition launched in 2017 toward the constellation Lyra. The Ermak returned in 2020, but the Taimyr was lost after 344 subjective days at near-light velocities, implying years of real elapsed time.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The expedition is organized by Earth institutions (USCR Academy) with an international crew including Russians, Americans, and a German. Standard Earth organizational structures govern.",
        "q5": "Same languages as Earth",
        "q5_justification": "The bulletin is in standard Russian/English. The crew includes Russian, American, and German members. No space-specific languages appear.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The Taimyr was lost with all hands after a bright flash near the light barrier. Deep space at extreme velocities proved fatal, destroying the ship and killing the entire six-person crew.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only six crew members ventured into deep space on this pioneering expedition. The mission represents the absolute vanguard of human exploration.",
        "q8": "Single unified authority",
        "q8_justification": "The expedition operates under the USCR Academy of Sciences as part of an international program. A single authority governs space research.",
        "q9": "Drama",
        "q9_justification": "The terse news bulletin announcing the loss of the Taimyr with all hands is deeply dramatic in its understated, clinical language conveying tragedy.",
        "q10": "Entirely civilian",
        "q10_justification": "The expedition is a civilian scientific research mission organized by an academy of sciences. No military involvement is indicated.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The expedition pushes into deep space toward the constellation Lyra, attempting to approach the light barrier. This is frontier exploration at its most extreme and dangerous.",
        "q12": "Other / Unsure",
        "q12_justification": "The bulletin is a brief factual report with no description of the space environment. Only technical data about velocity and distance are provided.",
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

print('Done batch 1.')
