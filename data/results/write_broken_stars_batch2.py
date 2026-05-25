import json, csv, os

chapters_data = [
    {
        "chapter": "Under a Dangling Sky",
        "q1": "Other / Unsure",
        "q1_justification": "Set in Rainville under a crystal dome sky. A dolphin named Giana rides a giant fountain through the crystal sky and discovers another planet nearby. The space content is minimal and fantastical rather than depicting contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "The story hints at another planet beyond the crystal sky, but no space habitation is depicted. Characters live under a dome on their own world.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted by human characters. Giana the dolphin breaks through the crystal sky but this is more fantastical than a space journey.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted. The society lives under a dome in Rainville.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment experienced by characters in a meaningful way.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Adventure / exploration",
        "q9_justification": "A fantasy/sci-fi hybrid about a narrator collecting underwater sounds and a dolphin named Giana who dreams of reaching the stars. She rides a giant fountain through a crystal sky and discovers another planet. The shattering of the crystal sky is an act of exploration and discovery.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain activity depicted in civilian or military terms.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain analogy applicable.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment experienced by characters."
    },
    {
        "chapter": "The New Year Train",
        "q1": "Other / Unsure",
        "q1_justification": "Told as a TV interview transcript about an entrepreneur who creates a train using miniature black holes to bend space-time for faster travel during Spring Festival. The story is Earth-set and comedic; no space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. The train bends space-time but remains on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey. The train manipulates space-time but travels between Chinese cities.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Comedy / satire",
        "q9_justification": "A comic story told as a TV interview about a train using miniature black holes for faster Spring Festival travel. The train vanishes with 1500 passengers but returns safely, with passengers enjoying the extended journey. Humorous tone throughout.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "The Robot Who Liked to Tell Tall Tales",
        "q1": "Other / Unsure",
        "q1_justification": "A Calvinoesque fable about a robot soldier sent to become the greatest storyteller. The robot drifts through space for millions of years, but there is no contestation or strategic struggle over space.",
        "q2": "Other / Unsure",
        "q2_justification": "The robot drifts through space but there is no habitation or territorial holding. Space is a void through which the robot travels.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The robot drifts through space for millions of years, passing black holes and star systems, in an effectively one-way, generational-scale journey.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted. The robot is alone in space.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language barriers depicted. The robot communicates with Death and other characters through normal speech.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Space is depicted as a vast emptiness through which the robot drifts for millions of years, passing black holes and dead star systems. Only a robot could survive such conditions.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The robot is essentially alone in space. No other inhabitants are encountered during its millions-year drift.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Adventure / exploration",
        "q9_justification": "A fable about a robot soldier on a quest to become the greatest storyteller. It encounters a painter, writer, and wine connoisseur who each evade Death, drifts through space for millions of years, and fulfills quests before returning home.",
        "q10": "Other / Unsure",
        "q10_justification": "The robot's space journey is neither civilian nor military in nature; it is a fantastical quest narrative.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is used as a mythical/fable setting rather than as an analogy for any real-world domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The robot drifts through black holes, dead star systems, and vast emptiness for millions of years. The environment is fundamentally unlike Earth."
    },
    {
        "chapter": "The Restaurant at the End of the Universe Laba Porridge",
        "q1": "No contestation",
        "q1_justification": "The restaurant exists peacefully at the end of the universe. Multiple alien species visit without conflict. No contestation over space is depicted.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Multiple alien civilizations exist across the universe: three-body people of Alpha Centauri, Titanians, Suoyas. The universe is populated with diverse settled civilizations.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The restaurant is at the end of the universe. Travel involves singularity-based transport across vast cosmic distances. Characters from Alpha Centauri and Titan visit.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Multiple alien species with entirely different social structures: three-body people from Alpha Centauri, Titanians who are uploaded consciousnesses, Suoyas. Each has its own radically different culture.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Multiple alien species communicate at the restaurant despite coming from vastly different civilizations, suggesting translation technology mediates communication.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The restaurant environment is comfortable and hospitable, serving food to diverse alien species. The setting is designed for leisure and dining.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Space habitation is completely normalized. Multiple species travel the universe freely, visit restaurants at the edge of the cosmos, and live across many worlds.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple alien civilizations exist as distinct entities: Alpha Centauri's three-body people, Titanians, Suoyas, and others, each apparently governing themselves.",
        "q9": "Drama",
        "q9_justification": "A story-within-a-story set at a restaurant at the end of the universe, centered on writer Ah Chen who traded his capacity for love to the Agency of Mysteries for literary abilities. The emotional core is about love, sacrifice, and human connection.",
        "q10": "Entirely civilian",
        "q10_justification": "All space activity depicted is civilian: running a restaurant, dining, traveling for leisure. No military presence.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is depicted as a vast multicultural marketplace/social space, not easily analogized to a single real-world domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The restaurant exists at the end of the universe, with singularity-based transport and environments suited to multiple alien physiologies. The physical environment is very different from Earth."
    },
    {
        "chapter": "What Has Passed Shall in Kinder Light Appear",
        "q1": "Other / Unsure",
        "q1_justification": "An alternate history where time flows backward through Chinese history. The protagonist lives from modern prosperity through the Cultural Revolution, civil war, and WWII. Set entirely on Earth with only a brief mention of a satellite launch and the American moon landing. No space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. The story is entirely Earth-based alternate history.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted. All travel is terrestrial.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted. The story portrays Earth-based Chinese society across decades.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Drama",
        "q9_justification": "An epic alternate history drama spanning decades, centered on the love story between Xie Baosheng and Qiqi. Time flows backward through Chinese history: from modern prosperity through Tiananmen, the Cultural Revolution, civil war with Nationalists, and WWII. Deeply emotional and philosophical.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted. Military activity is entirely terrestrial.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "The Snow of Jinyang",
        "q1": "Other / Unsure",
        "q1_justification": "Set in 10th century China during a siege. Features anachronistic technology (internet, fire-oil carriages) created by mysterious Prince Lu who claims to be from 1000 years in the future. A time-travel/alternate history story set entirely on Earth.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. All action takes place within the besieged city of Jinyang in 10th century China.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted. Prince Lu traveled through time, not space.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted. The society is medieval Chinese.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Adventure / exploration",
        "q9_justification": "A time-travel adventure set during a 10th century siege. Scribe Zhu Dagun is sent to persuade or assassinate Prince Lu, a mysterious figure from the future who has introduced anachronistic technology (internet, steam carriages, chemistry) to defend the city. Rich with humor and historical detail.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted. Military activity is entirely terrestrial/medieval.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Reflection",
        "q1": "Other / Unsure",
        "q1_justification": "A story about a man named Ed Lin who discovers he has a split personality: his other self is a clairvoyant girl who experiences time in reverse. Set entirely on Earth with no space content.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. Story takes place in apartments and offices on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Drama",
        "q9_justification": "A psychological drama about Ed Lin, who discovers his clairvoyant alter ego is a split personality who experiences time in reverse. The story explores identity, memory, and the trauma of his parents' death in a car accident he foresaw but couldn't prevent.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
]

country = 'China'
book_title = 'Broken Stars'
csv_path = 'data/results/China_Broken_Stars.csv'
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

print('Done with batch 2.')
