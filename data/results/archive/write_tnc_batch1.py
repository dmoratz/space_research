import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 1",
        "q1": "No contestation",
        "q1_justification": "The chapter is a peaceful introduction set entirely on Earth. Sohya visits Tae at the underwater Dragon Palace theme park. Sennosuke Toenji proposes the moon base project. There is no conflict or contestation in space.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely on Earth, at an undersea theme park and in meetings. No space territory is depicted or discussed in terms of habitability.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. The setting is entirely terrestrial. The moon base is proposed but no travel takes place.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays near-future Earth corporate culture and theme park entertainment.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters speak Japanese. Standard Earth languages are used throughout with no space-specific language.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is an undersea theme park and offices on Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. The moon base is only a proposal at this stage.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order exists yet. The chapter focuses on corporate decision-making on Earth.",
        "q9": "Drama",
        "q9_justification": "The chapter is character-driven drama: Sohya meets the enigmatic 13-year-old Tae, learns about her loneliness and her grandfather's ambitions, and receives a momentous business proposal to build on the moon.",
        "q10": "Entirely civilian",
        "q10_justification": "The setting is entirely civilian: a theme park, corporate offices, and business meetings. No military presence exists.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. All action takes place on Earth.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced. The chapter is set entirely on Earth.",
    },
    {
        "chapter": "Chapter 2",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Tension exists at Kunlun Base with Cui's psychological breakdown and a meteor strike emergency, but there is no strategic conflict or open rivalry in space. The visit is cooperative.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Kunlun Base is a tiny Chinese station with only 3 crew, barely maintained and deteriorating. It functions as a temporary outpost, not a permanent settlement.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The trip to the Moon via Chang'e spacecraft is depicted as relatively routine near-Earth travel, taking a few days each way.",
        "q4": "Other / Unsure",
        "q4_justification": "Kunlun is barely functional with only 3 crew. No real space society exists; it is a minimal research outpost.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Chinese and Japanese. Standard Earth languages are used throughout with no space-specific language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Kunlun's infrastructure is deteriorating: leaking pipes, broken systems, inadequate life support. A meteor strike causes an emergency. The lunar environment demands constant technological maintenance.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only about 40 astronauts total are in space worldwide, and only 3 crew reside at Kunlun. Space habitation is exceptionally rare.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Kunlun is a Chinese national base. The visit is arranged through diplomatic channels between Japanese corporations and the Chinese space program. National frameworks govern space activity.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows Sohya and Tae's first trip to the Moon, experiencing lunar conditions, visiting Kunlun, and exploring the feasibility of the moon base project. Discovery drives the narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "All personnel are civilian: astronauts from national space agencies and corporate visitors. No military presence exists at Kunlun or in the mission.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Kunlun feels like a remote frontier outpost barely hanging on, with deteriorating infrastructure and minimal crew, reminiscent of an early colonial settlement.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Low gravity, bulky space suits (Krechet M), life support failures, meteor strikes, and the harshness of the lunar surface constantly challenge the characters.",
    },
    {
        "chapter": "Chapter 3",
        "q1": "No contestation",
        "q1_justification": "The chapter is entirely peaceful, focused on engineering presentations, TROPHY engine tests, and planning the construction phases. No conflict occurs in space.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely on Earth at Tanegashima Island. No space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. All action takes place on Earth during planning and testing phases.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays Earth-based corporate and engineering culture.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters speak Japanese. Standard Earth languages are used throughout.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is entirely terrestrial.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space in this chapter. The moon base remains in the planning stage.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is depicted. The chapter focuses on corporate partnerships on Earth.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on the drama of revealing the TROPHY engine, Gotoba's construction plan, and Tae's surprise announcement that the base is a wedding palace. The naming of 'Sixth Continent' provides the emotional climax.",
        "q10": "Entirely civilian",
        "q10_justification": "The setting is entirely civilian: rocket company facilities, engineering demonstrations, and corporate meetings. No military presence.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. All activity is on Earth.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced. The chapter is set entirely on Earth.",
    },
    {
        "chapter": "Chapter 4",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "NASA announces a competing moon base (Liberty Island), creating rivalry. But the competition is commercial and legal, not military. The Serpent probe mission and site selection proceed without conflict.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Serpent probe visits the lunar south pole on an unmanned mission. No permanent human presence exists on the Moon yet. Activities are robotic exploration and site selection.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All missions are Earth-to-Moon, near-Earth operations. The Serpent probe and Eve I launches are short-distance lunar missions.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists. The chapter depicts unmanned robotic missions and Earth-based planning. No humans live in space.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters speak standard Earth languages. No space-specific language exists.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The lunar south pole where Serpent explores is permanently shadowed and extremely cold. The discovery of water ice with mysterious golden metallic threads (ENG) highlights the alien harshness of the environment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "No humans travel to space in this chapter. All lunar activity is unmanned. The space presence is limited to robotic probes.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "NASA competes with the Japanese private consortium. National space agencies and corporate interests drive space activity. The competition is framed by national and commercial rivalry.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is driven by exploration and discovery: the Serpent probe discovers water ice and the mysterious ENG fibers in Eden Crater. Engineering achievements with TROPHY and multidozers propel the narrative forward.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: corporate engineering, scientific probes, and commercial space development. No military presence.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter depicts site selection and exploration of new territory, with competing claims (NASA vs. Sixth Continent), echoing frontier expansion dynamics.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The robotic operations on the Moon manage the environmental differences through technology. The extreme cold and vacuum are challenging but handled by unmanned systems.",
    },
    {
        "chapter": "Chapter 5",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The US sues Japan at the ICJ over the Moon Treaty. NASA announces the competing Liberty Island base. However, cooperation also occurs: NASA's Frontier assists with solar arrays, and TROPHY technology is shared. The rivalry is legal and commercial, not military.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Apple 3 makes Japan's first manned spaceflight to orbit. NASA's shuttle assists. These are temporary missions, not permanent settlements. Construction is beginning but no one lives on the Moon yet.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "Apple 3's maiden orbital flight and NASA shuttle operations are all near-Earth. The Moon operations are robotic. All travel is within the Earth-Moon system.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists. The chapter depicts early manned spaceflight and robotic construction. No permanent human presence in space.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Japanese and English. ICJ proceedings use standard languages. No space-specific language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Space operations require extensive technology: TROPHY engines, multidozers, contaminated solar panels needing cleanup. The lunar environment is demanding.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Ryuichi's Apple 3 flight makes him the first Japanese person in a private spacecraft. Very few people are in space.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The US-Japan ICJ dispute over the Moon Treaty directly extends Earth nation-state politics into space. NASA competes with the Japanese consortium while national legal frameworks govern space activities.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on the ICJ legal battle over the Moon Treaty, diplomatic maneuvering between the US and Japan, Tae's courtroom strategy with the SETI module, and Ringstone's testimony. Legal and political struggle drives the narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: corporate space development, legal proceedings, scientific research. No military presence in space.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Legal disputes over territory, competing claims, and the struggle for access to lunar resources mirror frontier colonial expansion dynamics.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Orbital flight and robotic lunar operations present manageable environmental challenges handled by technology. The contaminated solar panels illustrate ongoing but manageable difficulties.",
    },
]

country = 'Japan'
book_title = "The Next Continent"
csv_path = "data/results/Japan_The_Next_Continent.csv"
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
