import json, csv, os

chapters_data = [
    {
        "chapter": "PROLOGUE",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "An Ouster migration cluster of 4000+ units approaches Hyperion. FORCE:space deploys a full battle fleet. The Hegemony faces a major strategic decision about defending Hyperion vs. protecting the Worldweb.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Hegemony Worldweb connects hundreds of worlds via farcasters. Hyperion is a colonial world with millions of inhabitants. The Ousters control separate regions of space.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The treeship accumulates six years of Web time for the Hyperion voyage. Passengers spend months in cryogenic fugue. Time-debt creates meaningful temporal separation from origin worlds.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Earth cultural elements persist (Steinway piano, Rachmaninoff, Scotch whiskey, Catholic Church) alongside distinctly far-future elements like the Templar Brotherhood, Shrike Church, crew clones, and treeship culture.",
        "q5": "Same languages as Earth",
        "q5_justification": "All pilgrims communicate in standard English without translation issues. The poet quotes Yeats and Chaucer. No language barriers are mentioned between characters from different worlds.",
        "q6": "Manageable but risky",
        "q6_justification": "Space travel requires cryogenic fugue and carries time-debt. The Consul's unnamed world has an interdiction field and dangerous fauna. Travel is routine but not without risk.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Worldweb connects hundreds of worlds where billions live. Treeships carry thousands of passengers. Interstellar travel, while involving time-debt, is routine for humanity.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony governs the Worldweb. The Ousters are independent interstellar barbarians. The Templar Brotherhood operates autonomously with its treeships. The Shrike Church is another distinct entity.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter establishes a Canterbury Tales-style pilgrimage structure. Seven pilgrims journey to confront the mysterious Shrike, sharing stories along the way. The narrative is driven by exploration of the unknown.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "FORCE:space warships escort the civilian treeship. Colonel Kassad represents the military, while the other pilgrims are civilians (priest, poet, scholar, detective, diplomat). Both domains coexist.",
        "q11": "Like the ocean / naval",
        "q11_justification": "FORCE:space uses naval terminology: task forces, attack carriers, escort duties. The treeship resembles a great vessel. Warships have boom arms, command probes, and Hawking drives.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The Consul's unnamed world has alien megafauna and different atmosphere. Hyperion has a too-small sun and green-blue sky. Worlds vary but are generally habitable with manageable differences."
    },
    {
        "chapter": "THE PRIEST'S TALE- 'The Man Who Cried God'",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Ouster invasion approaches. The Shrike has killed 20,000+ people. Martial law is declared on Hyperion. Mobs destroy the Shrike Temple. An SDF army of 8,000 is lost confronting the Shrike.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Hyperion is a fully colonized world with cities, plantations, and millions of inhabitants. The broader Worldweb spans hundreds of settled worlds connected by farcasters and spinships.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Travel to Hyperion involves 20 months in cryogenic fugue and 8 years of time-debt. Father Hoyt loses decades to round-trip voyages. The time-debt creates profound separation from home.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Earth traditions persist (Catholic Church, classical music, Old Earth references) alongside distinctly colonial cultures: plantation society, Bikura tribe, Shrike cult, and unique Hyperion customs.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Standard English is spoken throughout, but with notable dialect variations: Bikura speak corrupted seedship English, plantation workers use a distinct argot, and Tuk speaks a thick colonial dialect.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Hyperion features deadly tesla tree flame forests that electrocute anything nearby, a 3000-meter deep Cleft, extreme terrain requiring specialized gear, and the lethal Shrike creature.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Hyperion alone has millions of inhabitants. The Worldweb has billions across hundreds of worlds. Spinship travel, while involving time-debt, is routine. Space habitation is fully ordinary.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony governs through Senate CEO and All Thing. Ousters threaten invasion. The Shrike Church and Templar Brotherhood are autonomous entities. Hyperion has its own Home Rule Council.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The Priest's Tale is a horror survival story: Father Dure trapped among the Bikura, the cruciform parasite infiltrating his body, the terrifying Shrike encounter, and Dure's seven years of agony on the tesla tree.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "FORCE Marines control the spaceport, the SDF operates under martial law, but the narrative centers on civilian experiences: religious pilgrimage, colonial life, and personal exploration.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Hyperion is depicted as a frontier colonial world: plantations, riverboats, indigenous peoples, wilderness exploration. Father Dure's journey inland mirrors classic frontier narratives.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Hyperion has a too-small sun, green-blue sky, alien flora and fauna, deadly tesla trees and flame forests, and a 26-hour day. Regular adaptation and specialized gear are needed for survival."
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

print('Done batch 1.')
