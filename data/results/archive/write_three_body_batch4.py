import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 33",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The sophon chapter: Trisolaris unfolds protons into 2D to create superintelligent computers (sophons) that will infiltrate Earth's particle accelerators and lock down human science. A proton unfolded into 3D attacks Trisolaris's own capital. Intense strategic struggle.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The particle accelerator and sophon construction take place in synchronous orbit around Trisolaris. These are temporary orbital installations, not permanent habitation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The sophons travel at near-lightspeed from Trisolaris to Earth (4 light-years). The fleet takes 450 years. The distance is extreme and generational.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Trisolaran society depicted in detail: authoritarian princeps-consul system, suppression of emotions, execution for incompetence, destruction of microcosmic civilizations treated as routine. Radically alien.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Sophons enable real-time quantum-entangled communication between Trisolaris and Earth, and can display messages directly on human retinas. Communication technology makes language barriers irrelevant.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Trisolaris endures Chaotic Eras during the chapter. The sophon construction requires wrapping the planet in darkness, causing extreme cold. The three-sun system remains lethally unstable.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Space activity is limited to orbital construction of the particle accelerator and sophon etching. Only specialized spaceships and crews work in orbit. Space presence is rare.",
        "q8": "Single unified authority",
        "q8_justification": "Trisolaris operates under a princeps who orders the consuls, controls military and science budgets, and unilaterally decides on Project Sophon. Single authoritarian authority.",
        "q9": "Military / war",
        "q9_justification": "Project Sophon is a weapon of war: protons transformed into superintelligent computers to infiltrate and sabotage Earth's scientific progress. The chapter details the engineering of this strategic weapon, including failed attempts that attack Trisolaris itself.",
        "q10": "Mostly military",
        "q10_justification": "All space activity serves the military objective of conquering Earth: building the particle accelerator, creating sophons, and deploying them as strategic weapons.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The sophons operate as an abstract, networked intelligence infiltrating physical space at the subatomic level, analogous to cyberspace warfare. They multitask across accelerators like networked agents.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The chapter depicts protons unfolded into lower dimensions: a 1D string 1500 light-hours long, 3D geometric solids with intelligence, a 2D membrane wrapping around a planet. Physics is fundamentally unlike Earth experience."
    },
    {
        "chapter": "Chapter 34",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Wang and Ding despair after learning about the sophons, believing human science is permanently locked. Da Shi takes them to see locusts as an analogy: bugs have never been truly defeated. The strategic struggle with Trisolaris frames the entire chapter.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. The chapter takes place in Beijing and rural Hebei.",
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
        "q9_justification": "A powerful emotional turning point: after despairing that humanity is doomed, Da Shi takes the two scientists to see locust swarms. His analogy - bugs have never been defeated despite all of humanity's efforts - restores their fighting spirit.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 35",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The final chapter operates on two levels: Ye Wenjie visits Red Coast ruins and dies; a prologue to the sequel shows Evans communicating with Trisolaris through sophons. Trisolaris cannot understand human deception because their thoughts are transparent. Ye gives Luo Ji the axioms of cosmic sociology. The strategic struggle continues.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. The chapter takes place on Earth.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Trisolaran fleet is en route, 450 years from Earth. Communication via sophons is instantaneous but the physical distance remains extreme.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Trisolaran revelation that 'think' and 'say' are synonyms shows a fundamentally different biological and social order: Trisolarans broadcast thoughts as electromagnetic radiation, making deception impossible. This radical difference is strategically significant.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Evans communicates with Trisolaris through sophons that display text on his retinas. The sophons translate between languages seamlessly.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment experienced by characters.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Drama",
        "q9_justification": "A multilayered finale: Ye Wenjie visits the ruins of Red Coast Base and dies watching the sunset, whispering about humanity's sunset. Meanwhile, Evans's dialogue with Trisolaris reveals a fundamental cognitive difference. Ye passes the axioms of cosmic sociology to Luo Ji at Yang Dong's grave.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain activity depicted directly.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
]

country = 'China'
book_title = 'Human Split_Three Body Problem'
csv_path = 'data/results/China_Human_Split_Three_Body_Problem.csv'
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

print('Done with batch 4.')
