import json, csv, os

chapters_data = [
    {
        "chapter": "THE DETECTIVE'S TALE- The Long Good-Bye",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Brawne Lamia faces assassination attempts, a gunfight in Concourse Mall, violent combat in Lusus Dregs' Hive, and kidnapping. The TechnoCore's three factions wage strategic struggle over AI evolution. Johnny the Keats cybrid is murdered.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Tau Ceti Center has 5 billion inhabitants. The Worldweb connects hundreds of worlds via farcasters. Lusus is a settled industrial hive world. The Old Earth analog exists somewhere in the Web. Colonies span known space.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Hyperion is described as far from the Web, months of travel away. Colony worlds require significant travel time. The pilgrimage itself represents major separation from the core Worldweb civilization.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Lusus has a distinct industrial hive culture with combat guilds and 1.3g gravity adaptations. Tau Ceti Center is cosmopolitan. The Old Earth analog preserves 19th-century culture. BB Surbringer's bounty-hunting culture and Dregs' Hive underworld represent distinct subcultures.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters communicate in standard English. The Keats cybrid speaks archaic literary English. No translation barriers exist between characters from different worlds. Legal proceedings, investigations, and casual conversation all occur in English.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Lusus has 1.3 standard gravities requiring physical adaptation, industrial hive conditions, and violent underworld areas like Dregs' Hive. Brawne faces lethal combat situations. The journey to Hyperion involves dangerous conditions and the Shrike threat.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Tau Ceti Center alone has 5 billion people. Lusus is a major industrial world. Billions live across the Worldweb. Farcaster commuting between worlds is routine. Space habitation is completely ordinary.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony governs the Worldweb. The TechnoCore operates as three rival factions (Stables, Volatiles, Ultimates) with autonomous governance. The Ousters exist independently. The Shrike Church and Templar Brotherhood are distinct entities.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a noir detective story: Brawne investigates an AI client's murder, faces assassination attempts, engages in violent combat in Lusus Hive, and uncovers a conspiracy involving the TechnoCore. The pacing and structure follow thriller conventions.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The narrative centers on civilian detective work, legal proceedings, and private investigation. FORCE is mentioned peripherally. Combat occurs but in civilian contexts: bounty hunters, underworld violence, and personal defense rather than military operations.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The TechnoCore exists as a networked AI civilization in the datumplane. Johnny hacks into the Core periphery. The datasphere and megasphere are key operational domains. Farcaster technology creates a networked space connecting worlds.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Lusus has 1.3 standard gravities requiring physical adaptation. Various Worldweb worlds have different environments. The Old Earth analog recreates Earth conditions artificially. Hyperion has alien ecology and different atmospheric conditions."
    }
]

country = 'US'
book_title = 'Hyperion_Cleaned'
csv_path = 'data/results/US_Hyperion_Cleaned.csv'
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
