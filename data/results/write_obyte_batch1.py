import json, csv, os

chapters_data = [
    {
        "chapter": "front_matter",
        "q1": "Other / Unsure",
        "q1_justification": "The front matter contains only the title page, table of contents, and author biography. No narrative content or space portrayal.",
        "q2": "Other / Unsure",
        "q2_justification": "No narrative content. The front matter is purely bibliographic.",
        "q3": "Other / Unsure",
        "q3_justification": "No narrative content depicting any journey.",
        "q4": "Other / Unsure",
        "q4_justification": "No narrative content depicting any society.",
        "q5": "Other / Unsure",
        "q5_justification": "No narrative content depicting language dynamics.",
        "q6": "Other / Unsure",
        "q6_justification": "No narrative content depicting any environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No narrative content depicting space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No narrative content depicting political order.",
        "q9": "Other / Unsure",
        "q9_justification": "The front matter is bibliographic material, not a narrative chapter with a genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative content depicting any domain.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative content depicting any domain characterization.",
        "q12": "Other / Unsure",
        "q12_justification": "No narrative content depicting any environment.",
    },
    {
        "chapter": "Chapter 1",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is set entirely in Malianov's Leningrad apartment. No space or contestation over space is depicted. Malianov works on astrophysics at his desk.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory or habitation is portrayed. The chapter follows Malianov dealing with phone calls, a grocery delivery, and a visitor in his apartment.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. Malianov never leaves his apartment building.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is contemporary Soviet Leningrad with everyday domestic life.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics are present. All dialogue is in Russian in a Leningrad apartment.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is a hot summer apartment in Leningrad.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed. The chapter is entirely terrestrial.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter builds suspense through mysterious disruptions: relentless wrong-number phone calls, an unexplained grocery delivery, Weingarten's strange interest in Malianov's work, and the ominous arrival of Lidochka. An undercurrent of dread pervades.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. Malianov works on theoretical astrophysics at his kitchen table.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is a Leningrad apartment.",
    },
    {
        "chapter": "Chapter 2",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is set in Malianov's apartment. No space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed. The chapter follows drinking and socializing with Lidochka and Snegovoi.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is a Soviet apartment with domestic socializing.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics are present. All dialogue is in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Snegovoi arrives armed with a large pistol, interrogates Malianov about his work, asks about the unknown Gubar, and announces he is leaving. The scene is saturated with paranoia and menace beneath a veneer of social pleasantry.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. Snegovoi is revealed as a military colonel but the context is entirely terrestrial.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 3",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. The chapter involves a police investigation into Snegovoi's death in Malianov's apartment building.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed. The chapter is a police interrogation in an apartment.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is Soviet Leningrad with a CID investigator.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Snegovoi is found dead of a gunshot wound. Investigator Zykov conducts a surreal interrogation, accuses Malianov of murder, drinks his cognac, and behaves in bizarre fashion. Lidochka has vanished without a trace. The atmosphere is nightmarish.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter is a criminal investigation.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 4",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. Malianov visits Vecherovsky upstairs to discuss the strange events.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is Vecherovsky's elegant apartment.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Drama",
        "q9_justification": "Malianov seeks counsel from the brilliant mathematician Vecherovsky after the traumatic events. The chapter centers on their intellectual friendship and Malianov's emotional distress over Snegovoi's death and the disruption of his work.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter depicts civilian scientists discussing work and personal troubles.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 5",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. The chapter reveals that a mysterious force is suppressing scientific research, but this occurs entirely on Earth with no space setting.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed. The red-haired visitor claims to represent an extraterrestrial civilization but appears in Weingarten's apartment on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. The alien visitor simply appears and vanishes inside an Earth apartment.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays Soviet scientists in a Leningrad kitchen.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. The alien speaks Russian. All dialogue is in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is a kitchen.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Weingarten reveals that a vanishing red-haired alien demanded he stop his research and named Malianov, Gubar, and Snegovoi as other targets. The scientists realize they are all being persecuted by an unknown force. Fear and paranoia escalate.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. All characters are civilian scientists on Earth.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
]

country = 'Russia'
book_title = 'One Billion Years to the End of the World (Definitely Maybe)'
csv_path = 'data/results/Russia_One_Billion_Years_to_the_End_of_the_World_(Definitely_Maybe).csv'
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
