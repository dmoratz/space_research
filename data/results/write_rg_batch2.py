import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter VI",
        "q1": "No contestation",
        "q1_justification": "The chapter focuses on media management, press conferences, and PR activities before the launch. No strategic conflict occurs; the tension is between Yukari's desire for honesty and the program's need for favorable coverage.",
        "q2": "Other / Unsure",
        "q2_justification": "All action is Earth-based: press conferences, the barracks, the Taliho village, and the training facility.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The upcoming mission is a single LEO orbit. Launch is twenty days away.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter focuses on Earth-based media frenzy and family dynamics.",
        "q5": "Same languages as Earth",
        "q5_justification": "Japanese and English are used at press conferences. Matsuri speaks pidgin with the Taliho. Standard Earth languages throughout.",
        "q6": "Other / Unsure",
        "q6_justification": "Space environment is not depicted directly. Press questions reference dangers of spaceflight but no space conditions are shown.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. Launch preparations continue on the ground.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Director Nasuda describes the mission as Japan's first independent manned spaceflight, wrapped in the guise of the OECF. National prestige drives the program.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter satirizes media culture: invasive reporters ask about menstruation and boyfriends, a guerrilla reporter ambushes the girls in pajamas, Yukari fabricates her backstory, and she destroys a telephone in rage at her mother's media appearances.",
        "q10": "Entirely civilian",
        "q10_justification": "All characters are civilians: reporters, SSA staff, the astronaut trainees, and Yukari's family.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced. The chapter is entirely Earth-based.",
    },
    {
        "chapter": "Chapter VII",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter covers two scrubbed launches and a successful third attempt, with Yukari threatening to fire escape rockets if delayed again. The conflict is between Yukari and mission control over launch decisions, not between external adversaries.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Yukari reaches orbit in Tampopo, a single-person capsule designed for a brief four-orbit mission. No permanent space presence exists.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "Tampopo achieves orbit at 210 km altitude, traveling at 7.7 km/s. The mission plan is four orbits over six hours.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Yukari behaves exactly as she does on Earth: bantering with mission control, making observations about islands, and comparing the experience to a simulator. No distinct space culture exists.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication between Yukari and Solomon mission control is in Japanese. Standard radio procedures are used.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Launch subjects Yukari to up to 9G of acceleration. The capsule is barely large enough for one person. She ends up in a wrong, highly inclined orbit threatening her survival.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Yukari is the only person launched into space. She is described as the youngest astronaut in history, flying solo.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The Japanese-funded SSA operates the launch. Tracking relies on ground stations including Christmas Island. The mission represents Japan's first manned spaceflight.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Two launch scrubs build tension. Yukari threatens to fire escape rockets. After launch, the spacecraft enters a wrong orbit heading south toward New Zealand, with mission control unable to track her. The Taliho curse is implied as the cause.",
        "q10": "Entirely civilian",
        "q10_justification": "The SSA is a civilian organization. Yukari is a civilian astronaut. Mission control staff are civilian engineers and scientists.",
        "q11": "Like the air / airpower",
        "q11_justification": "Launch procedures closely mirror aviation: detailed checklists, countdown procedures, radio communications with mission control, telemetry monitoring, and abort decisions following standard flight protocols.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Yukari endures up to 9G during launch, three times shuttle levels. The capsule is barely larger than a phone booth. The wrong orbit places her in immediate danger with no easy way home.",
    },
    {
        "chapter": "Chapter VIII",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Space debris damages Tampopo's heat shield and oxidation tank. Yukari must perform an unplanned EVA, then execute an emergency orbital rendezvous with the Russian space station Mir. International negotiations between Russia and the SSA add diplomatic tension.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Mir is a long-duration station with two cosmonauts who have been aboard for six months. Tampopo is a temporary capsule. Both represent outpost-level presence.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All activity occurs in LEO at approximately 194-210 km altitude. Yukari's orbit passes over South America, Africa, Europe, and Asia.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Yukari interacts with the cosmonauts using normal Earth social conventions. International diplomacy mirrors Earth politics. No distinct space culture has developed.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Yukari and the Russian cosmonauts communicate in English as a shared lingua franca. Russian is used between cosmonauts. Japanese is used with Solomon mission control.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Debris impact cripples Tampopo. EVA is performed in a skinsuit not designed for spacewalks, with only 20 minutes of safe darkness. Heat shield tiles are missing, making reentry fatal. Oxygen is limited.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Yukari in Tampopo and two cosmonauts (Oleg and Nikolai) on Mir are in space. The entire crisis is managed with just three people in orbit.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The Russian space station Mir and Japanese SSA program represent their respective nations in orbit. Docking permission requires diplomatic negotiation between TsUP and the SSA. The cosmonauts override their government to accept Yukari.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Debris impact damages the heat shield, making reentry impossible. Yukari performs a dangerous EVA in inadequate equipment, then races to rendezvous with Mir before life support runs out. The chapter is dominated by survival tension.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Yukari is a civilian. The cosmonauts are former military (Oleg flew Sukhoi fighters) but serve in the civilian space program. Mir is a civilian research station.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The orbital rendezvous echoes naval operations: approaching another vessel, throwing tethers to moor the craft, transferring between ships through an airlock, and coordinating rescue across vast distances.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The skinsuit offers minimal protection during EVA. Debris impact can destroy a spacecraft in an instant. The vacuum is immediately lethal. Heat shield damage makes reentry impossible. Every system operates at the margins of survival.",
    },
    {
        "chapter": "Chapter IX",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "An explosion separates the Kristall-2 module from Mir with Yukari inside. The cosmonauts evacuate in the Soyuz. Matsuri launches in a third capsule for a desperate rescue. Yukari and Matsuri attempt manual reentry in a stripped-down capsule under extreme G-forces.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Mir is a deteriorating space station with a broken airlock, jury-rigged wiring, and decades of accumulated junk. The capsules Tampopo and Coconut are temporary craft. All space presence is fragile and temporary.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All activity is in LEO. Reentry targets the Arafura Sea. The entire space mission, including the rescue, occurs within Earth orbit.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The Morita family video conference from space replicates Earth family dynamics: bickering, teasing, and discussing everyday concerns. The broadcast reaches a worldwide TV audience. No distinct space culture exists.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "English serves as the lingua franca between Yukari and the cosmonauts. Russian is used between Nikolai and Oleg. Japanese is used in the family video conference and with Solomon mission control.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Mir is deteriorating with dangerous jury-rigged wiring. An explosion jettisons a module. Yukari drifts in space with limited oxygen. Reentry in a stripped capsule generates up to 10G, nearly crushing Matsuri beneath Yukari's weight.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Yukari and two cosmonauts are in orbit, later joined by Matsuri in the rescue capsule. The total human population in space is four people.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Russian TsUP and Japanese SSA coordinate the crisis response. International media broadcast the events worldwide. The SSA's success shakes the global space industry and doubles Japanese government funding.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is dominated by survival crises: the Mir explosion, Yukari stranded in space with dwindling oxygen, Matsuri's emergency launch and rescue, manual reentry without instruments, and 10G forces threatening to crush Matsuri.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Yukari and Matsuri are civilians. The cosmonauts are former military aviators serving in the civilian Russian space program. US Space Command provides tracking support.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The rescue operations echo naval metaphors: Mir is described as a sinking ship, Matsuri rescues Yukari by pulling alongside in a small craft, and the capsule splashes down in the ocean where they sit on the hull waiting for helicopter rescue.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Yukari nearly suffocates from oxygen depletion. Reentry subjects both girls to 10G in a capsule stripped of all instruments. Matsuri is crushed beneath Yukari's weight. The capsule must thread a precise reentry angle using only a wristwatch and manual switches.",
    },
]

country = 'Japan'
book_title = "rocket girls"
csv_path = "data/results/Japan_rocket_girls.csv"
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
