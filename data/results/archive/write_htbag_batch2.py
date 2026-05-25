import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter SIX",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. The chapter focuses on the night of the coup: Rumata guards the prince, reflects on the city, and is arrested by Sturmoviks after the prince is murdered.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata's role as temporary observer is explicit: his circlet transmits to Earth historians, his metalloplast shirt is hidden technology, and he takes Sporamin tablets from Earth supplies.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata's separation from Earth is profound. He reflects on what future Earth students will learn about this era, highlighting the vast temporal and spatial distance from his home world.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The alien society is described as 20,000 people who are slaves of faith, passion, and avarice. Rumata reflects that they are not yet human in the current sense, raw material for future evolution.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Rumata converses with the prince, the officer of the guard, and his servants in the local Arkanarian language, which is distinct from Earth languages.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment is benign. Rumata looks out over the city from the prince's hill, sees fires and streets. All dangers come from the political coup, not the environment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Rumata is the sole observer present during the coup. His circlet transmits events for the benefit of historians on distant Earth.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter references the kingdom's internal power struggle between the king, Don Reba, the Gray hordes, Waga's nocturnal army, and the Holy Order monks now appearing in the streets.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter builds to a violent climax: fires erupt across the city, the prince is murdered, Rumata fights fifteen Sturmoviks, is hit by a lance, and is overwhelmed and captured.",
        "q10": "Entirely civilian",
        "q10_justification": "The Earth mission remains civilian. Rumata's guard duty is his cover role. His metalloplast shirt and circlet are civilian research equipment, not weapons.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Rumata reflects on historical progress and the inevitability of social evolution, framing the alien planet as a frontier society that will eventually develop, echoing colonial-era progressive theories.",
        "q12": "Almost Earth-like",
        "q12_justification": "The city with its 20,000 inhabitants, streets, harbor, and medieval architecture is indistinguishable from a medieval Earth city. The physical environment is identical to Earth.",
    },
    {
        "chapter": "Chapter SEVEN",
        "q1": "No contestation",
        "q1_justification": "No space contestation occurs. The chapter centers on Rumata's interrogation by Don Reba, the removal of Zupik and Brother Aba, and the revelation of the Holy Order's takeover.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata's status as visitor is highlighted when Don Reba accuses him of being an impostor and speculates he comes from some faraway, powerful domain.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Don Reba speculates Rumata may be the devil, the Son of God, or from some faraway powerful domain. The vast, unknowable distance of Rumata's origin is emphasized.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Holy Order seizes power through a night of slaughter. Don Reba reveals himself as Bishop of the new theocratic regime, a political transformation utterly alien to Earth's society.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The interrogation occurs entirely in the local language. Rumata maintains his cover identity while speaking Arkanarian throughout.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment is not a threat. Rumata is held in rooms and corridors. All danger comes from political actors, not environmental conditions.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Rumata is the sole Earth observer captured by the regime. His mysterious nature puzzles Don Reba, who cannot categorize him.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Holy Order's cavalry now controls Arkanar, replacing the previous monarchy. Multiple polities are referenced: Irukan, Soan, the Empire, and the new Order regime.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is dominated by political maneuvering: Reba eliminates rivals Zupik and Aba during the interrogation, reveals the Order's coup, and Rumata negotiates his freedom and Budach's release.",
        "q10": "Entirely civilian",
        "q10_justification": "Rumata is a civilian researcher. His confrontation with Don Reba is diplomatic, not military. He uses intimidation and wit, not weapons.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Rumata walks through a conquered city seeing corpses and black-cloaked riders, paralleling colonial-era observers witnessing violent regime changes in frontier territories.",
        "q12": "Almost Earth-like",
        "q12_justification": "The city, palace, streets, and physical conditions remain indistinguishable from medieval Earth. The Holy Order's cavalry and architecture are all Earth-analogous.",
    },
    {
        "chapter": "Chapter EIGHT",
        "q1": "No contestation",
        "q1_justification": "No space contestation occurs. The chapter follows Rumata navigating the new Order regime to free Budach and Baron Pampa from the Tower of Joy.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata operates as a temporary agent, using iron bracelets and bureaucratic forms to navigate the new regime. His hidden Earth medicine (Sporamin) underscores his visitor status.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata's dialogue with Budach about God's role implies his vast distance from Earth. He speaks as one with godlike knowledge, hinting at his origin from a far superior and distant civilization.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Holy Order's bureaucracy assigns punishments by number, citizens queue for lashings or bracelets, and the Tower of Joy houses torture chambers with graduating students. The society is radically different from Earth.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All interactions occur in the local language: with the chancellery official, monks, Baron Pampa, and Doctor Budach. The alien planet's distinct language is used throughout.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment remains benign. Rumata navigates dump heaps, towers, and streets without environmental danger. All threats are human-made.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Rumata acts alone to rescue Budach and Pampa. His spy/bodyguard follows at a distance, but he is the sole Earth representative operating in the city.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Holy Order now governs Arkanar as a province. Other polities remain: Irukan, Soan, the Empire. Baron Pampa mentions Father Arima occupying his castle, showing fragmented authority.",
        "q9": "Drama",
        "q9_justification": "The chapter's emotional core is the philosophical dialogue between Rumata and Budach about evil, suffering, and what God could do to improve the world. Kyra watches with fear and hope.",
        "q10": "Entirely civilian",
        "q10_justification": "Rumata's rescue operations and philosophical discussions are civilian activities. He uses wit, bureaucratic manipulation, and physical prowess, not military force.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Rumata rescues local intellectuals from a repressive regime, paralleling colonial-era missionaries or agents extracting individuals from hostile frontier territories.",
        "q12": "Almost Earth-like",
        "q12_justification": "The Tower of Joy, chancellery, streets, and dump heaps closely mirror medieval Earth settings. The physical environment is indistinguishable from Earth.",
    },
    {
        "chapter": "Chapter NINE",
        "q1": "No contestation",
        "q1_justification": "No space contestation occurs. The chapter focuses on Arata the rebel's visit to Rumata, requesting advanced weapons and discussing revolution.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata's status as a visitor from Earth is explicit: Arata knows his true identity and demands thunderbolts from the gods who descended from heaven.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Arata references Rumata descending from heaven. Rumata once showed Arata Sol, Earth's sun, as a tiny star in the night sky, emphasizing the immense distance between worlds.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Arata's history of failed rebellions, slave revolts, and brutal suppressions illustrates a feudal society trapped in cycles of violence, radically unlike Earth's advanced civilization.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Arata and Rumata converse in the local language. Arata interprets Rumata's origins through local religious and mythological frameworks, showing the distinct linguistic-cultural gulf.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment is benign. Arata enters Rumata's study through a secret passage. No environmental hazards are present.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Arata is one of the very few locals who knows Rumata's true origin. The Earth observers' presence is so rare that Arata interprets it through religious mythology.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple political forces are discussed: the Holy Order, peasant rebellions, Waga Koleso's criminal network, the duke's warriors, and baronial estates.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is a political dialogue about revolution, intervention, and the ethics of providing advanced weapons to local rebels. Rumata refuses Arata's request for thunderbolts.",
        "q10": "Entirely civilian",
        "q10_justification": "The Earth observers' policy is explicitly non-military. Rumata refuses to provide weapons, maintaining the civilian nature of their mission. He gives only gold, not arms.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The dilemma of an advanced civilization deciding whether to arm indigenous rebels closely parallels colonial-era debates about intervention in frontier societies.",
        "q12": "Almost Earth-like",
        "q12_justification": "The physical setting of Rumata's study, the planet's environment, and Arata's world are all physically Earth-like. No alien environmental features are present.",
    },
    {
        "chapter": "Chapter TEN",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. The chapter focuses on the Earth agents' conference, Rumata's final night with Kyra, and her murder by crossbow.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The agents meet at the Drunkard's Lair outpost. Don Kondor arrives and departs by helicopter. Budach is transported unconscious. The entire Earth presence is a temporary mission.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata dreams of taking Kyra to Earth by spaceship and considers how she would adapt. The journey to Earth is presented as a major undertaking requiring careful planning.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The contrast is explicit: the agents speak Russian and discuss communist ideals while Kyra's brother swears loyalty to the Holy Order. Two radically different social orders coexist.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The Earth agents speak Russian among themselves at the conference, switching to the local language with natives. Rumata speaks Russian unconsciously to Kyra, who doesn't understand it.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment is benign. The helicopter flight, forest hut, and city house all present no environmental hazards. The threat is entirely human violence.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Twenty Earth agents attend an extraordinary conference, out of 250 total on the planet. Their presence remains exceptionally rare and covert.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The conference discusses the Holy Order's takeover and its implications for the entire kingdom. Earth operates as a separate, distant authority whose agents debate intervention policy.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter builds to a devastating climax: monks storm Rumata's house at night, Kyra is killed by crossbow bolts through the window. Rumata takes his swords and descends to fight.",
        "q10": "Entirely civilian",
        "q10_justification": "The Earth agents are civilian researchers debating policy. Even Don Kondor's suggestion to kill Don Reba is discussed as an extraordinary deviation from their civilian mandate.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The agents debate whether to blockade or intervene in the alien province, directly paralleling colonial-era decisions about frontier territories under hostile regimes.",
        "q12": "Almost Earth-like",
        "q12_justification": "The planet remains physically Earth-like: forests, birch trees, ferns, horses, medieval cities. The helicopter flight over familiar terrain underscores the planet's Earth-like nature.",
    },
]

country = 'Russia'
book_title = 'Hard to Be a God'
csv_path = 'data/results/Russia_Hard_to_Be_a_God.csv'
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
