import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 6",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. The chapter continues the group discussion about mysterious forces suppressing research, set entirely in Malianov's kitchen.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed. Gubar's story involves the Union of the Nine, a terrestrial secret society, not space habitation.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays Soviet scientists debating in a kitchen.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue is in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Gubar reveals his nightmare: an invasion of former lovers, a woman delivering a mysterious child with warnings about the Union of the Nine. The scientists debate whether to report to authorities, realizing no one would believe them. Fear and helplessness dominate.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. All characters are civilian scientists on Earth.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 7",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. Vecherovsky leads a philosophical discussion about the nature of the force opposing the scientists.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is Malianov's apartment with gathered scientists.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Drama",
        "q9_justification": "Vecherovsky dominates with a philosophical argument: first pretending to support the supercivilization hypothesis, then proving it leads to a dead end. He reveals Glukhov has already been crushed by the pressure. The chapter is an intellectual and moral drama about individual choice under impossible pressure.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter is a philosophical discussion among civilian scientists.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 8",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted directly. Vecherovsky theorizes about the Homeostatic Universe opposing human progress, but this is philosophical speculation, not a depiction of space conflict.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed. The Homeostatic Universe theory is about cosmic laws, not habitable territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter is set in Malianov's apartment.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Drama",
        "q9_justification": "Vecherovsky presents the Homeostatic Universe theory, arguing the universe itself prevents civilizations from transcending entropy. Malianov is devastated by the hopelessness. Then Irina arrives unexpectedly, summoned by a mysterious telegram. The emotional intensity is profound.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter depicts civilian scientists and Malianov's wife.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 9",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. The chapter shows escalating pressure on Malianov: a tree explodes overnight in his courtyard, a fake passport appears, and Weingarten capitulates.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is Soviet Leningrad apartments.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "A massive tree has exploded into existence overnight in the courtyard. A stranger's passport replaces Irina's. Weingarten arrives in panic, delivering a terrified monologue about choosing survival over science. Gubar also capitulates. The pressure is relentless and terrifying.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 10",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. The chapter centers on Malianov's decision to capitulate and give his research to Vecherovsky.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is entirely domestic.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Drama",
        "q9_justification": "Irina finds Lidochka's bra and confronts Malianov. He breaks down and tells her everything. She supports him unconditionally. A telegram threatens Bobchik. Malianov packages his research to surrender. Glukhov, broken and philosophical, warns him on the stairs. The chapter is raw emotional drama about sacrifice and capitulation.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted.",
    },
    {
        "chapter": "Chapter 11",
        "q1": "Other / Unsure",
        "q1_justification": "No space contestation is depicted. The chapter is the finale where Malianov surrenders his work and Vecherovsky reveals he will continue the fight alone.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. Vecherovsky plans to go to the Pamirs, a terrestrial location.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter is set in Vecherovsky's soot-damaged apartment.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All dialogue in Russian.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. Vecherovsky's apartment shows signs of attack: soot, charred floor, chemical smell. But these are on Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Drama",
        "q9_justification": "Malianov delivers his research to Vecherovsky, who reveals he has been under pressure himself for two weeks. Vecherovsky plans to continue everyone's research alone. Malianov realizes he is crossing a line of no return. The chapter ends with profound resignation and quiet heroism.",
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

print('Done batch 2.')
