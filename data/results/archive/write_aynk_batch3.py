import json, csv, os

chapters_data = [
    {
        "chapter": "Part 4 Chapter 1",
        "q1": "Total war / constant conflict",
        "q1_justification": "Loop 159. Keiji and Rita fight together against waves of Mimics on Kotoiushi Island. Rita explains the time loop mechanics and they execute the three-step plan to destroy the server, but the loop resets again.",
        "q2": "Other / Unsure",
        "q2_justification": "Earth battlefield. No space territory depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey. Combat on Earth.",
        "q4": "Other / Unsure",
        "q4_justification": "Earth society at war. No space setting.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Keiji (Japanese) and Rita (American) communicate over comms during battle. Rita explains complex time loop mechanics to Keiji in English.",
        "q6": "Other / Unsure",
        "q6_justification": "Earth battlefield. No space environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance.",
        "q9": "Military / war",
        "q9_justification": "Intense combat as Keiji and Rita coordinate attacks against Mimics, executing the antenna-backup-server destruction sequence during a massive battle.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are soldiers in active combat against Mimics.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "Earth setting.",
    },
    {
        "chapter": "Part 4 Chapter 2",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Loop 160. Keiji and Rita bond deeply on the eve of battle. They train together, eat lunch, and spend the night together, knowing the next day brings war.",
        "q2": "Other / Unsure",
        "q2_justification": "Earth military base. No space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey.",
        "q4": "Other / Unsure",
        "q4_justification": "Earth society. No space setting.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Keiji (Japanese) and Rita (American) communicate throughout the day. Their shared experience transcends the language barrier.",
        "q6": "Other / Unsure",
        "q6_justification": "Earth military base. No space environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance.",
        "q9": "Drama",
        "q9_justification": "Deeply emotional chapter as Keiji and Rita connect. He knows her from 158 battles but she is meeting him for the first time. They share lunch, an umeboshi eating contest, and an intimate night together.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are military personnel on a military base.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain.",
        "q12": "Other / Unsure",
        "q12_justification": "Earth setting.",
    },
    {
        "chapter": "Part 4 Chapter 3",
        "q1": "Total war / constant conflict",
        "q1_justification": "Surprise Mimic attack directly on Flower Line Base. The Mimics adapted their strategy because Keiji nearly broke the loop. Javelins hit the Sky Lounge. The base itself becomes a battlefield.",
        "q2": "Other / Unsure",
        "q2_justification": "Earth military base under attack. No space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey.",
        "q4": "Other / Unsure",
        "q4_justification": "Earth society. No space setting.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Keiji and Rita communicate. Shasta arrives and Rita gives her orders in English.",
        "q6": "Other / Unsure",
        "q6_justification": "Earth military base. No space environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance.",
        "q9": "Military / war",
        "q9_justification": "Surprise enemy attack on the base forces immediate combat readiness. Mimics have adapted their tactics, escalating the war to a new level of danger.",
        "q10": "Mostly military",
        "q10_justification": "Rita and Keiji are military. Shasta is a civilian engineer who arrives from a party in costume.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain.",
        "q12": "Other / Unsure",
        "q12_justification": "Earth setting.",
    },
    {
        "chapter": "Part 4 Chapter 4",
        "q1": "Total war / constant conflict",
        "q1_justification": "Rita and Keiji fight through the devastated base, rallying fragmented troops. They find Nijou dead, save journalist Murdoch, and link up Japanese and U.S. forces after hours of combat.",
        "q2": "Other / Unsure",
        "q2_justification": "Earth military base. No space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey.",
        "q4": "Other / Unsure",
        "q4_justification": "Earth society. No space setting.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Japanese and U.S. troops coordinate during the battle. Keiji and Rita communicate across the language divide.",
        "q6": "Other / Unsure",
        "q6_justification": "Earth battlefield. No space environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance.",
        "q9": "Military / war",
        "q9_justification": "Sustained combat across the destroyed base. Rita and Keiji lead troops, discover casualties, and fight to reunite Japanese and American forces.",
        "q10": "Mostly military",
        "q10_justification": "Mostly military personnel in combat, but journalist Murdoch is a civilian casualty they rescue.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain.",
        "q12": "Other / Unsure",
        "q12_justification": "Earth setting.",
    },
    {
        "chapter": "Part 4 Chapter 5",
        "q1": "Total war / constant conflict",
        "q1_justification": "Rita reveals that one of them must die to break the loop — their brains have become antennas for Mimic tachyon signals. She attacks Keiji in a deadly duel across the entire base with battle axes.",
        "q2": "Other / Unsure",
        "q2_justification": "Earth military base. No space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey.",
        "q4": "Other / Unsure",
        "q4_justification": "Earth society. No space setting.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Rita explains the loop mechanics to Keiji in English over comms. U.S. squad leader communicates with Rita using call signs.",
        "q6": "Other / Unsure",
        "q6_justification": "Earth military base. No space environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance.",
        "q9": "Military / war",
        "q9_justification": "A climactic duel between two elite warriors in mechanized Jackets, fighting across the destroyed base with tungsten carbide battle axes. The fight determines who survives to end the time loop.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "Both combatants are elite soldiers in powered armor. U.S. Special Forces support Rita. The duel occurs amid ongoing battle.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain.",
        "q12": "Other / Unsure",
        "q12_justification": "Earth setting.",
    },
    {
        "chapter": "Part 4 Chapter 6",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Aftermath of the battle. Keiji is court-martialed then cleared, receives the Order of the Valkyrie. Yonabaru punches him. Three thousand casualties including Rachel. The war continues with Keiji as Rita's replacement.",
        "q2": "Other / Unsure",
        "q2_justification": "Earth military base. No space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey.",
        "q4": "Other / Unsure",
        "q4_justification": "Earth society. No space setting.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Keiji interacts with both Japanese soldiers (Yonabaru, Ferrell) and American personnel (Shasta). Communication spans both language groups.",
        "q6": "Other / Unsure",
        "q6_justification": "Earth military base. No space environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance.",
        "q9": "Drama",
        "q9_justification": "Emotional aftermath as Keiji grieves Rita, faces hostility from former friends, visits the Sky Lounge where they spent their last night, and drinks the last cup of coffee she ever made.",
        "q10": "Mostly military",
        "q10_justification": "Mostly military personnel (Keiji, Ferrell, Yonabaru), but Shasta is a civilian engineer. The chapter deals with post-battle military proceedings.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain.",
        "q12": "Other / Unsure",
        "q12_justification": "Earth setting.",
    },
]

country = 'Japan'
book_title = "All You Need is Kill"
csv_path = "data/results/Japan_All_You_Need_is_Kill.csv"
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

print('Done batch 3.')
