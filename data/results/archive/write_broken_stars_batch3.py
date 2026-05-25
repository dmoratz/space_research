import json, csv, os

chapters_data = [
    {
        "chapter": "The First Emperors Games",
        "q1": "Other / Unsure",
        "q1_justification": "A comedic story about Qin Shihuang, China's First Emperor, as an avid computer gamer. Various philosophical schools present games (Civilization, The Sims, Plants vs Zombies, etc.). Set entirely on Earth in an absurd version of ancient China. No space content.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. Story is set in ancient China with anachronistic video games.",
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
        "q9_justification": "A comedic satire mapping Classical Chinese philosophy onto modern video games. The First Emperor tries Civilization (Legalists), The Sims (Confucians), Plants vs Zombies (Mohists), and others, rejecting each. Each game satirizes a school of thought. Ends with Xu Fu running a vaporware scam.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Coming of the Light",
        "q1": "Other / Unsure",
        "q1_justification": "A story about a marketing professional in contemporary Beijing who devises a scheme to have a Buddhist monk consecrate a mobile app (Buddhagram). The story spirals into questions about whether the universe is a program. Set on Earth with no space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. Story is set in contemporary Beijing's tech industry.",
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
        "q9_justification": "A satirical drama about Zhou Chongbo, a marketing strategist who devises a scheme to consecrate a mobile app. When miraculous events follow, his life unravels. He hides in a Buddhist temple, where the abbot reveals that the cosmic microwave background may be the source code of the universe and the digital watermark algorithm may have altered reality. The story explores themes of simulation theory, marketing ethics, and Buddhist philosophy.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "The Brain Box",
        "q1": "Other / Unsure",
        "q1_justification": "A story about a brain pattern recorder implanted in a woman who dies in a plane crash. Her partner has the brain box's data imprinted on his own brain to experience her last five minutes. No space content.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. Story takes place on Earth: a lab and a crashing plane.",
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
        "q9_justification": "A deeply emotional drama about Fang Rui who has his dead partner Zhao Lin's brain box data imprinted on his brain. Her final five minutes reveal her struggle with self-reflection forced by the brain box, her doubts about love, and ultimately her decision to accept his proposal. He lies about what he learned to preserve a comforting narrative.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "A History of Future Illnesses",
        "q1": "Other / Unsure",
        "q1_justification": "A series of speculative essays about future diseases affecting humanity across centuries. While 'The New Moon' section involves a large asteroid becoming Earth's second moon, the focus is on its effects on human biology and society on Earth, not space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. All effects of the New Moon are experienced on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted. All societies are Earth-based.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted. The 'Speaking in Tongues' section involves Earth-based language manipulation.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment experienced by characters.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Other / Unsure",
        "q9_justification": "A series of speculative non-narrative essays cataloging future diseases: iPad Syndrome, Disease-Imitation Aesthetics, Controlled Personality Shattering, Twin Elegies, The New Moon, Neoteny, Ritual Dependency, Chaotic Chronosense, and Speaking in Tongues. The format is encyclopedic rather than narrative, making genre classification difficult.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Essay - A Brief Introduction to Chinese SF and Fandom",
        "q1": "Other / Unsure",
        "q1_justification": "Nonfiction essay by Regina Kanyu Wang about the history of Chinese science fiction and fandom. No narrative content depicting space.",
        "q2": "Other / Unsure",
        "q2_justification": "Nonfiction essay about literary history. No space habitation depicted.",
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
        "q9": "Other / Unsure",
        "q9_justification": "Nonfiction essay about Chinese SF literary history; not a narrative with classifiable genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain activity depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain analogy provided.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Essay - A New Continent for China Scholars",
        "q1": "Other / Unsure",
        "q1_justification": "Nonfiction essay by Mingwei Song about the emergence of Chinese science fiction studies as an academic field. No narrative content depicting space.",
        "q2": "Other / Unsure",
        "q2_justification": "Nonfiction academic essay. No space habitation depicted.",
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
        "q9": "Other / Unsure",
        "q9_justification": "Nonfiction academic essay about the development of Chinese SF studies; not a narrative with classifiable genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain activity depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain analogy provided.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Essay - Science Fiction Embarrassing No More",
        "q1": "Other / Unsure",
        "q1_justification": "Nonfiction essay by Fei Dao about the rise of Chinese science fiction from obscurity to mainstream recognition. No narrative content depicting space.",
        "q2": "Other / Unsure",
        "q2_justification": "Nonfiction essay about literary culture. No space habitation depicted.",
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
        "q9": "Other / Unsure",
        "q9_justification": "Nonfiction essay about the changing cultural status of sci-fi in China; not a narrative with classifiable genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain activity depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain analogy provided.",
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

print('Done with batch 3.')
