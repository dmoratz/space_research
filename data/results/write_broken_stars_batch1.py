import json, csv, os

chapters_data = [
    {
        "chapter": "front_matter",
        "q1": "Other / Unsure",
        "q1_justification": "Front matter contains publisher info, table of contents, dedication, and contributor bios. No narrative content depicting space.",
        "q2": "Other / Unsure",
        "q2_justification": "No narrative content. Editorial and publishing information only.",
        "q3": "Other / Unsure",
        "q3_justification": "No narrative content depicting any journey or distance.",
        "q4": "Other / Unsure",
        "q4_justification": "No narrative content depicting any society.",
        "q5": "Other / Unsure",
        "q5_justification": "No narrative content depicting language or communication.",
        "q6": "Other / Unsure",
        "q6_justification": "No narrative content depicting any environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No narrative content depicting space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No narrative content depicting political order.",
        "q9": "Other / Unsure",
        "q9_justification": "Front matter with no narrative content; not classifiable by genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative content depicting civilian or military activity.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative content providing any domain analogy.",
        "q12": "Other / Unsure",
        "q12_justification": "No narrative content depicting any physical environment."
    },
    {
        "chapter": "Introduction",
        "q1": "Other / Unsure",
        "q1_justification": "Ken Liu's editorial introduction about curating the anthology of Chinese science fiction. Nonfiction, no narrative depicting space.",
        "q2": "Other / Unsure",
        "q2_justification": "Nonfiction essay about translation and curation. No space habitation depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No narrative depicting any space journey.",
        "q4": "Other / Unsure",
        "q4_justification": "No narrative depicting space society.",
        "q5": "Other / Unsure",
        "q5_justification": "No narrative depicting space communication.",
        "q6": "Other / Unsure",
        "q6_justification": "No narrative depicting space environmental conditions.",
        "q7": "Other / Unsure",
        "q7_justification": "No narrative depicting space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No narrative depicting space political order.",
        "q9": "Other / Unsure",
        "q9_justification": "Nonfiction editorial introduction; not a narrative with classifiable genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative depicting civilian or military space activity.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative providing a space domain analogy.",
        "q12": "Other / Unsure",
        "q12_justification": "No narrative depicting space physical conditions."
    },
    {
        "chapter": "Goodnight Melancholy",
        "q1": "Other / Unsure",
        "q1_justification": "Near-future Earth story about a woman dealing with depression using therapeutic robots Lindy and Nocko, interweaved with fictionalized accounts of Alan Turing. No space setting or contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space setting. Story takes place entirely on near-future Earth with iWall and iVatar technology.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted. All action is Earth-based.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted. Characters live in near-future Earth society.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted. Communication is normal Earth language.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Drama",
        "q9_justification": "A deeply emotional drama about a woman's struggle with depression, her relationship with therapeutic AI robots, and parallels drawn to Alan Turing's life and his conversations with a machine called Christopher.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Broken Stars",
        "q1": "Other / Unsure",
        "q1_justification": "Dark psychological story set in 1998 China about a teenage girl discovering her mentally ill mother has been secretly imprisoned by her father. Stars are metaphorical/astrological, not outer space.",
        "q2": "Other / Unsure",
        "q2_justification": "No space setting. Story takes place entirely in a Chinese city in 1998.",
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
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "A dark psychological thriller where teenager Tang Jiaming discovers her mother has been imprisoned behind one-way glass for over a decade. She kills her mother, imprisons her father, and plans revenge on her school tormenters.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Moonlight",
        "q1": "Other / Unsure",
        "q1_justification": "A man receives phone calls from future versions of himself, each presenting a different environmental catastrophe. Set entirely on Earth with time-travel communication, no space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space setting. Story involves Earth-based environmental catastrophes (flooding, siliconization, magnetic field destruction).",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted. Time-travel communication only.",
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
        "q9_justification": "A philosophical drama about a man who changes history three times in one night by receiving calls from future selves, each presenting a different catastrophic timeline, but ultimately changes nothing.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Submarines",
        "q1": "Other / Unsure",
        "q1_justification": "Allegorical story about peasant migrant workers who build crude submarines and live on the Yangtze River. No space setting or contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space setting. Story takes place on the Yangtze River in China.",
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
        "q9_justification": "An allegorical drama about migrant workers building crude submarines on the Yangtze River. Social commentary on the urban-rural divide in China, with children kept in underwater cages and submarines eventually burning in a mysterious fire.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Salinger and the Koreans",
        "q1": "Other / Unsure",
        "q1_justification": "Surreal/satirical story where a Cosmic Observer watches North Korea conquer the world using a Quantum Reambiguator. The Cosmic Observer is abstract, not a space-based character. No space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. The Cosmic Observer is an abstract narrative device.",
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
        "q9": "Comedy / satire",
        "q9_justification": "A darkly comic, absurdist political satire where North Korea conquers the world using a Quantum Reambiguator while a Cosmic Observer watches and Salinger loses his reclusive home.",
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

print('Done with batch 1.')
