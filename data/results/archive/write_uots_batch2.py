import json, csv, os

chapters_data = [
    {
        "chapter": "Part 2 Act I",
        "q1": "No contestation",
        "q1_justification": "The chapter is set on Earth. Aki visits the ETICC and discusses the Builders' incoming fleet with scientists. No space conflict occurs.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is depicted. Discussion centers on the approaching Builder fleet but all action is on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. The Builders' fleet is discussed but not directly depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak English at the ETICC.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is experienced.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance is depicted.",
        "q9": "Drama",
        "q9_justification": "The chapter focuses on Aki's personal struggle with guilt over destroying the Ring and the scientific discussion about the approaching Builders.",
        "q10": "Entirely civilian",
        "q10_justification": "The ETICC is a civilian research institution.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced.",
    },
    {
        "chapter": "Part 2 Act II",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The UNSS Chadwick operates near Mercury studying ring material. The graser defense system remains a potential threat. The Builders' fleet approaches but there is no open conflict.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The UNSS Chadwick orbits near Mercury on a research mission. The RMRF is a temporary research facility. No permanent settlement exists.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The Chadwick operates near Mercury, a short interplanetary journey from Earth.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists. The crew operates as a scientific research team.",
        "q5": "Same languages as Earth",
        "q5_justification": "The crew speaks English.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Proximity to Mercury and the sun creates extreme conditions. Ring material contamination is a constant threat. The crew must maintain electrostatic containment of samples.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the small Chadwick crew is in space near Mercury.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands all space operations.",
        "q9": "Adventure / exploration",
        "q9_justification": "Molly and Anastacia's discovery of the fifth nanobot type (the messenger cell) drives the chapter as scientific exploration and discovery.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Chadwick operates under UNSDF military command but the crew are primarily civilian scientists like Molly and Anastacia.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The Chadwick operates like a naval research vessel with Commander Kindersley in command.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Working near Mercury with ring material requires constant technological safeguards. Solar radiation and nanotechnology contamination constantly challenge the crew.",
    },
    {
        "chapter": "Part 2 Act III",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Molly and Anastacia discover the messenger cell aboard the RMRF. The graser defense remains a latent threat but no conflict occurs.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The RMRF is a temporary research facility near Mercury.",
        "q3": "Short interplanetary journey",
        "q3_justification": "Operations are near Mercury in the inner solar system.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists. The crew are researchers on a temporary mission.",
        "q5": "Same languages as Earth",
        "q5_justification": "The crew speaks English.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Working with ring material requires electrostatic containment. The environment near Mercury is extremely hostile.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the small research crew is in space.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands operations.",
        "q9": "Adventure / exploration",
        "q9_justification": "The discovery of the messenger cell is a breakthrough moment of scientific exploration.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Civilian scientists work under UNSDF military oversight.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The research vessel operates under naval-style command.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Handling alien nanotechnology in the hostile environment near Mercury constantly challenges human technology.",
    },
    {
        "chapter": "Part 2 Act IV",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Aki presents her Vert-Ring proposal to the UN Security Council and faces strong opposition. A shadowy group secretly discusses using the Ring technology for military purposes. The political rivalry over how to handle the Builders intensifies.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is depicted in this chapter. All action is on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak English at the UN and in private meetings.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is experienced in this chapter.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space in this chapter.",
        "q8": "Single unified authority",
        "q8_justification": "The UN and UNSDF govern the global response to the Builders.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on Aki's UN speech proposing the Vert-Ring, political opposition, and a secret cabal discussing military weaponization of the graser technology.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Aki's civilian scientific proposal conflicts with military interests. The secret group discusses weaponizing alien technology.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed in this chapter.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced.",
    },
]

country = 'Japan'
book_title = "Usurper of the Sun"
csv_path = "data/results/Japan_Usurper_of_the_Sun.csv"
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
