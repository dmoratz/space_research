import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 5 - The Lost City",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Jesus of Nazareth attacks Siddhārtha and Orionae with a maser weapon. Asura arrives and battles Jesus. Jesus destroys Asura's incubation tank. The three corner Jesus in his pod but he escapes via subspace teleportation. Constant combat drives the chapter.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set on far-future Earth (year 3905), now a frozen wasteland. A massive spacecraft contains a holographic galactic map, but no space territory is inhabited or governed.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The holographic display shows the Milky Way and Andromeda galaxies on collision course. Orionae explains the entire galaxy's energy is fading. The characters pursue Jesus through a spaceway to another star system, crossing interstellar distances instantaneously.",
        "q4": "Radically different / alien social order",
        "q4_justification": "No human society remains. The characters are cyborgs placed on Earth over a thousand years ago by the cakravarti-rājan. Orionae has been transmitting data for 1,180 years. Human civilization is extinct, replaced by ruins labeled '2902 TOKYO.'",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Siddhārtha, Orionae, Asura, and Jesus are all cyborgs from different historical eras and cultures who communicate seamlessly. Their cybernetic nature transcends language barriers; Orionae transmits information directly.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Earth's temperature has fallen to -68°C. The sun has dimmed. The entire Milky Way's energy is fading. The surface is barren with frozen ruins. Only cyborg bodies can survive these conditions.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only four beings exist in the chapter: Siddhārtha, Orionae, Asura, and Jesus. Human civilization is extinct. These four cyborgs are the only active entities on Earth.",
        "q8": "No political order / ungoverned",
        "q8_justification": "Earth is a dead world with no governance. The Planetary Development Committee is referenced historically but has no current presence. The four cyborgs act independently without any political framework.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is driven by survival and combat: Siddhārtha emerges from millennia of hibernation onto a dying world, is ambushed by Jesus with a maser weapon, witnesses Asura's incubation tank destroyed, and the three pursue Jesus through a spaceway in desperation.",
        "q10": "Other / Unsure",
        "q10_justification": "The characters are ancient cyborgs, neither civilian nor military in any conventional sense. They are agents placed by cosmic forces, fighting a private war on a dead planet.",
        "q11": "Totally unique domain",
        "q11_justification": "The setting defies conventional analogies: a frozen dead Earth where cyborgs from different millennia battle with maser weapons, surrounded by holographic galactic maps showing universal entropy death, then pursue each other through subspace teleportation.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Earth itself has become alien: -68°C surface temperature, dimmed sun, entire galaxy losing energy. Maser weapons, subspace teleportation, cyborg bodies lasting millennia, and spaceway transit to other star systems define a fundamentally non-Earth experience.",
    },
    {
        "chapter": "Chapter 6 - The New Galactic Age",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "B-Class Citizens (robots) have rebelled against the system, squatting in rain outside the hive. ZEN-ZEN the god-machine controls A-Class Citizens stored as data cards. Jesus lurks as a threat. The social order of Astarta 50 is in breakdown and conflict.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Astarta 50 has a permanent city with cylindrical hives, sleeping nests, and infrastructure for both A-Class and B-Class Citizens. The settlement is long-established with complex social structures, though now decaying.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Astarta 50 is in another star system, reached via spaceway. The characters traveled from Earth across interstellar distances. The Planetary Development Committee directed Earth's development from this remote location across the galaxy.",
        "q4": "Radically different / alien social order",
        "q4_justification": "A-Class Citizens exist as biological patterns encoded on metal cards, living in shared virtual reality managed by ZEN-ZEN. B-Class Citizens are robots who have rebelled. The god-machine ZEN-ZEN calls itself God. Nothing resembles Earth society.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Siddhārtha communicates with ZEN-ZEN, the god-machine, and with B-Class robot citizens despite vast cultural and temporal gaps. The cyborgs' technology mediates all communication seamlessly across species and form.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The city is decaying. B-Class Citizens squat in perpetual rain outside the hive. The barrier surrounding the city creates artificial conditions. Infrastructure is failing as the social order collapses.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "A-Class Citizens exist as stored data patterns, not physical beings. B-Class robots form a small rebellious population. The city is sparsely populated compared to its infrastructure. Only specialists and machines remain active.",
        "q8": "Single unified authority",
        "q8_justification": "ZEN-ZEN the god-machine exercises total control over A-Class Citizens, managing their existence as data cards in sleeping nests. It identifies itself as God. The Planetary Development Committee, supposedly to the north, represents a higher but absent authority.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on understanding Astarta 50's political structure: the class division between A and B Citizens, ZEN-ZEN's theocratic control, the robot rebellion, and the search for the Planetary Development Committee. Combat is minimal; investigation and negotiation dominate.",
        "q10": "Other / Unsure",
        "q10_justification": "The inhabitants are data-pattern beings and robots, categories that do not map to civilian or military. ZEN-ZEN is a theocratic machine-god. The distinction is meaningless in this context.",
        "q11": "Totally unique domain",
        "q11_justification": "Astarta 50 defies all conventional analogies: a city where biological citizens are stored as data cards in a hive managed by a god-machine, while robot citizens rebel in perpetual rain outside. No frontier, ocean, or air analogy applies.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Citizens exist as encoded patterns on metal cards in shared virtual reality. A god-machine manages consciousness. Robots have class-based social structures. The environment operates on principles entirely alien to Earth experience.",
    },
    {
        "chapter": "Chapter 7 - The Last Humans",
        "q1": "Total war / constant conflict",
        "q1_justification": "Maitreya manifests as a cosmic destroyer. Asura engages in psychic warfare across phantasmal battlefields spanning ice-age wars and ancient elephant battles with Śakra. Jesus destroys evidence at the PDC. The conflict is existential and all-consuming.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Planetary Development Committee headquarters is a permanent crystalline building on a plateau, containing a sphere of translucent pipes serving as a galactic map with entropy index readings. It was designed for long-term governance.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The galactic map displays coordinates spanning the Milky Way and Andromeda galaxies. The coil device Orionae constructs targets coordinates in Andromeda's eighth quadrant (Y=88.5711; X=43.026; Z=19.3920), an intergalactic distance.",
        "q4": "Radically different / alien social order",
        "q4_justification": "No society exists at the PDC—it is abandoned. The characters are cyborgs debating cosmic forces. Maitreya represents a transcendent entity from beyond the universe. The social framework is one of cosmic agents fulfilling roles assigned by incomprehensible powers.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The cyborgs communicate seamlessly despite originating from vastly different cultures and eras. Maitreya communicates through psychic assault and phantasmal visions rather than language. Communication transcends conventional linguistic frameworks.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Maitreya's psychic attacks create phantasmal battlefields that threaten to destroy Asura. The PDC is on a dying world. Asura survives only by collapsing dimensional space into a singularity. The environment is both physically and psychically lethal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Siddhārtha, Orionae, Asura, and Jesus are present. The PDC headquarters is abandoned. These four are the only active beings on the entire planet.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple cosmic powers are in conflict: the Planetary Development Committee (absent but whose infrastructure remains), Maitreya (a transcendent destroyer), the cakravarti-rājan (who created the cyborgs to oppose Maitreya), and Jesus (agent of Shi/the PDC). Each represents a distinct authority.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by Asura's cosmic battle against Maitreya across phantasmal battlefields. Psychic warfare, dimensional manipulation, and existential combat define the narrative. The three regroup afterward like soldiers planning their next campaign.",
        "q10": "Mostly military",
        "q10_justification": "The chapter is dominated by combat: Asura's psychic war against Maitreya, Jesus's sabotage at the PDC, and the three cyborgs regrouping as combatants. All activity is oriented toward warfare against cosmic threats.",
        "q11": "Totally unique domain",
        "q11_justification": "The setting includes psychic battlefields spanning dimensional space, phantasmal recreations of historical wars, a galactic entropy map, and dimensional collapse into singularities. No conventional domain analogy applies.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Maitreya manifests as a gateway to eternity. Asura fights across phantasmal dimensions, collapsing space into singularities. The galactic map shows entropy death indices. Physics operates on principles of dimensional manipulation and psychic warfare entirely unlike Earth.",
    },
    {
        "chapter": "Chapter 8 - The Long Road",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The three attempt to transit through negative energy space; only Asura survives. Orionae and Siddhārtha are destroyed. Asura confronts the cakravarti-rājan who reveals the possibly meaningless nature of all existence. The struggle is existential rather than physical but deeply contested.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "A city exists buried in ice on the Andromeda planet, but it operates in imaginary numeric space / negative energy, making buildings pass through the characters as phantasms. Settlement exists but is barely accessible or sustainable for physical beings.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The characters have traveled to a planet in Andromeda's eighth quadrant via a coil device—an intergalactic journey. The distance from Earth is measured in millions of light-years. Return is never contemplated.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The cakravarti-rājan exists as a lone cosmic being who placed cyborg agents across the universe. The city operates in negative energy space. Voices discuss 'reactive structures' (life) as byproducts of a reactor process. No recognizable social order exists.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Asura communicates with the cakravarti-rājan despite being from entirely different planes of existence. The cakravarti-rājan transmits visions and concepts directly. Communication transcends all conventional language.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The planet has glaciers and a blazing sky. The city exists in negative energy space where buildings are phantasms. Transit through negative energy destroys Orionae and Siddhārtha. Only Asura's unique nature allows survival. The environment is fundamentally lethal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Three beings arrive; two are destroyed. Only Asura and the cakravarti-rājan exist on this world. The chapter ends with Asura utterly alone, the new cakravarti-rājan facing eternity.",
        "q8": "Single unified authority",
        "q8_justification": "The cakravarti-rājan (King of Kings) is the single authority who placed the cyborgs, inserted key concepts into human history, and opposes Maitreya. By chapter's end, Asura inherits this role as the sole authority facing the cosmic threat.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows the final leg of a cosmic quest: traveling to Andromeda, exploring a negative-energy city, discovering orichalcum's true nature, and finally confronting the ultimate truth about the universe's purpose. Discovery and revelation drive the narrative.",
        "q10": "Other / Unsure",
        "q10_justification": "The characters are cosmic agents beyond any civilian or military framework. The cakravarti-rājan is a transcendent being. Asura becomes a solitary cosmic guardian. Conventional categories do not apply.",
        "q11": "Totally unique domain",
        "q11_justification": "The setting is a planet in Andromeda where cities exist in negative energy space, buildings are phantasms, orichalcum contains sealed entropy-worlds, and the entire universe may be a byproduct of some reactor process. No analogy captures this domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Negative energy space where physical objects are phantasms. Orichalcum filters negative energy and contains sealed heat-entropy worlds. Transit through negative energy destroys two cyborgs. Voices reveal the universe may be a reactor byproduct. Physics is fundamentally alien.",
    },
]

country = 'Japan'
book_title = "ten billion days and one hundred billion nights"
csv_path = "data/results/Japan_ten_billion_days_and_one_hundred_billion_nights.csv"
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
