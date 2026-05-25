import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter I",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The SSA faces cancellation from the Department of Economic Planning after LS-7's sixth consecutive failure. The pressure is institutional (budget deadline) rather than strategic or military conflict.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is entirely Earth-based, set on the island of Maltide in the Solomons. No orbital or space territory is depicted.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The SSA's goal is a single manned orbit of Earth using the LS-5 rocket. All planned missions are low Earth orbit.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays life on a remote island base and a tribal village.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Japanese (Yukari, Nasuda), English, and Solomon Islands pidgin. Matsuri uses pidgin terms like 'wantok.' Standard Earth languages throughout.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is entirely the tropical island of Maltide.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. The program has not yet achieved manned spaceflight.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The SSA is funded by the Japanese government through the OECF. The Department of Economic Planning threatens to cut funding, demonstrating state control over the space program.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter's tone is broadly comedic: a teenage girl is recruited as an astronaut because she weighs 37 kg, the previous astronaut fled rather than diet, and the director describes spaceflight as a job a monkey could do.",
        "q10": "Entirely civilian",
        "q10_justification": "The SSA is a civilian space program. All characters are civilian scientists, engineers, or the teenage recruit Yukari.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. All action takes place on the ground.",
        "q12": "Other / Unsure",
        "q12_justification": "The setting is entirely Earth-based. No space environment is experienced.",
    },
    {
        "chapter": "Chapter II",
        "q1": "No contestation",
        "q1_justification": "The chapter covers Yukari's training: centrifuge, classroom instruction, and survival training. There is no strategic conflict or competition, only the personal challenge of enduring grueling preparation.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is entirely Earth-based. All scenes take place in training facilities and a firing range on Maltide.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "Training prepares Yukari for a single LEO mission. Kinoshita teaches orbital mechanics from Feynman's lectures.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter focuses on Earth-based astronaut training.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in Japanese. Kinoshita's physics instruction uses standard Earth academic language.",
        "q6": "Other / Unsure",
        "q6_justification": "Space is not directly depicted. The centrifuge simulates G-forces up to 9G, but this occurs on the ground.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. The chapter is entirely about ground-based training.",
        "q8": "Other / Unsure",
        "q8_justification": "Space governance is not discussed in this chapter.",
        "q9": "Comedy / satire",
        "q9_justification": "The training scenes are played for dark comedy: Satsuki giggles while pushing Yukari to 9G blackout, Kurosu fires live machine gun rounds at her during obstacle courses, and Yukari demands her own machine gun to shoot back.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The SSA is civilian, but security chief Kurosu conducts military-style survival training with live firearms including a Colt .45 and Ingram MAC-11, and fires an M-60 machine gun at Yukari during obstacle courses.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. Training occurs entirely on the ground.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced. Centrifuge training simulates G-forces but on Earth.",
    },
    {
        "chapter": "Chapter III",
        "q1": "No contestation",
        "q1_justification": "Yukari's jungle survival exercise leads to meeting Matsuri and discovering her father as the Taliho chief. No conflict or strategic struggle occurs.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is entirely Earth-based, set in the jungle and the Taliho village.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The space program's LEO goal is referenced. The father's deal with Yukari hinges on her completing the astronaut job.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter contrasts modern Japanese culture with the Taliho tribal lifestyle.",
        "q5": "Same languages as Earth",
        "q5_justification": "Japanese, English, and pidgin are spoken. Matsuri is bilingual (Japanese/English). The father speaks fluent Japanese as former Japanese citizen and tribal languages.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space.",
        "q8": "Other / Unsure",
        "q8_justification": "Space governance is not discussed. The chapter focuses on family dynamics and tribal life.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter is broadly comedic: Yukari's father has dozens of wives and can't remember all their names, Yukari threatens him at gunpoint, Matsuri is recruited as backup astronaut because she happens to match Yukari's size, and Nasuda secretly coordinates with the chief via mobile phone.",
        "q10": "Entirely civilian",
        "q10_justification": "All characters are civilians. The Taliho village and SSA base are entirely civilian settings.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "The setting is entirely Earth-based.",
    },
    {
        "chapter": "Chapter IV",
        "q1": "No contestation",
        "q1_justification": "The chapter centers on Yukari's comedic weight-gain scheme to switch positions with Matsuri, and the booster test explosion. No strategic conflict between parties.",
        "q2": "Other / Unsure",
        "q2_justification": "All action is Earth-based. The capsule simulator mimics orbit but is ground-based training equipment.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The simulator depicts a 180 km altitude orbit. The training program aims for a single LEO mission.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter focuses on training routines and sneaking extra food.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Japanese. The Tianjin Restaurant staff speak Chinese-accented English and pidgin.",
        "q6": "Other / Unsure",
        "q6_justification": "The booster test explosion demonstrates the danger of rocket technology, but no space environment is directly depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. Training and preparation continue on the ground.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The Department of Economic Planning deadline looms. The program's survival depends on Japanese government funding decisions.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter is dominated by comedy: Yukari's midnight food smuggling scheme via canoe, Matsuri's magic fish-catching songs, both girls gaining weight despite strict monitoring, and Kinoshita catching them on the beach.",
        "q10": "Entirely civilian",
        "q10_justification": "All characters are civilian. The training, food smuggling, and social outings are entirely civilian activities.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed directly. The simulator replicates space but is ground-based.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced. The simulator session is brief and Earth-based.",
    },
    {
        "chapter": "Chapter V",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Yukari clashes with the engineering team over Motoko's new tankless fuel, staging a hunger strike. The conflict is internal to the program rather than between external parties.",
        "q2": "Other / Unsure",
        "q2_justification": "All action is Earth-based: the VAB, engineering meetings, and the protest outside the building.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The capsule being built is for a single LEO orbit. Discussions focus on the rocket barely reaching orbital velocity.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter focuses on engineering decisions and personal conflicts.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Japanese. Yukari's mother speaks Japanese during her brief visit.",
        "q6": "Other / Unsure",
        "q6_justification": "Space environment is discussed indirectly through capsule safety concerns but not directly depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The chapter discusses the global space industry implications of Motoko's revolutionary fuel. Yukari's mother suggests mass-producing rockets as a business model.",
        "q9": "Comedy / satire",
        "q9_justification": "Yukari's hunger strike and protest sign ('Redesigns Kill!'), her mother's pragmatic mass-production solution, and the absurdity of a teenager overruling rocket scientists create a satirical tone.",
        "q10": "Entirely civilian",
        "q10_justification": "All characters are civilian engineers, scientists, and the astronaut trainees. Yukari's mother is a civilian architect.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. The chapter is about ground-based engineering decisions.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is discussed through capsule design but not experienced.",
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

print('Done batch 1.')
