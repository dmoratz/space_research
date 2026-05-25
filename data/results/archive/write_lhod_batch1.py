import json, csv, os

chapters_data = [
    {
        "chapter": "front_matter",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The introduction establishes political tension between Karhide and Orgoreyn, but conflict is diplomatic rather than military or violent.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly Ai is a single envoy visiting Gethen; there is no permanent Ekumenical settlement, only his temporary diplomatic presence.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The front matter establishes Gethen as an extremely remote world, reachable only by NAFAL ships traveling near lightspeed across interstellar distances.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Gethenian society is fundamentally alien: ambisexual biology, kemmer cycle, and entirely non-Earth cultural norms are introduced.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Gethenians speak their own languages (Karhidish, Orgota) completely unrelated to any Earth language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Gethen is described as a planet in perpetual ice age, with extreme cold dominating all aspects of life.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only one person, Genly Ai, has come from off-world. Space travel to Gethen is extraordinarily rare.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Ekumen comprises 83 habitable worlds, while Gethen itself has multiple nations (Karhide, Orgoreyn). These are distinct political entities.",
        "q9": "Political / diplomatic",
        "q9_justification": "The front matter frames the story as a diplomatic mission: an envoy sent to convince a world to join an interstellar alliance.",
        "q10": "Entirely civilian",
        "q10_justification": "The Ekumen's mission is purely diplomatic and civilian. No military presence is described.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Ekumen is expanding its alliance to include new worlds, echoing frontier expansion into unknown territories.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Gethen's ice-age climate poses constant challenges to Genly Ai's human physiology; the environment is markedly different from Earth.",
    },
    {
        "chapter": "Chapter 1 - A Parade in Erhenrang",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The Karhide-Orgoreyn border dispute over the Sinoth Valley is mentioned, and political factions compete, but there is no open space conflict.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly Ai is a lone envoy with a starship waiting in orbit. His presence is temporary and diplomatic.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The nearest Ekumenical world Ollul is 17 light-years away. NAFAL ships travel near lightspeed, making the journey feel effectively one-way.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Gethenian society with its ambisexual biology, shifgrethor social codes, and kemmer cycle is fundamentally alien to Earth norms.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Genly speaks Karhidish, a completely alien language he has learned. The ansible is mentioned as communicating across interstellar distances.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The cold climate is pervasive but Erhenrang functions as a city; survival requires adaptation but is managed by the inhabitants.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly Ai is the sole representative from off-world. He is the First Mobile, the only alien on the entire planet.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Ekumen of 83 Known Worlds is described alongside Karhide and Orgoreyn as separate political entities.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on Genly's diplomatic mission, his audience with King Argaven, and political maneuvering around Estraven's fall.",
        "q10": "Entirely civilian",
        "q10_justification": "All interactions are diplomatic and civilian. No military forces or operations are involved.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Ekumen's outreach to Gethen resembles frontier expansion, extending civilization's reach to a new, remote world.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Genly wears a coat when temperatures are in the 30s F, while Gethenians do not. The climate constantly challenges his Earth-adapted body.",
    },
    {
        "chapter": "Chapter 2 - The Place Inside the Blizzard",
        "q1": "Other / Unsure",
        "q1_justification": "This is a Karhidish myth about two brothers; it does not address space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "The myth takes place entirely on Gethen and does not discuss space territory or habitation.",
        "q3": "Other / Unsure",
        "q3_justification": "No interstellar journey or space travel is referenced in this mythological tale.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The myth depicts Gethenian kemmer and vow-keeping customs, revealing a fundamentally alien social and sexual order.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The myth is told in Karhidish, a language entirely distinct from any Earth language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The myth centers on exile to the Ice, depicting a world where blizzards and glaciers are omnipresent mortal threats.",
        "q7": "Other / Unsure",
        "q7_justification": "The myth does not reference space habitation or off-world presence.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structures related to space are mentioned in this mythological tale.",
        "q9": "Drama",
        "q9_justification": "The myth is a tragic tale of brotherly love, exile, death, and an encounter with a spirit on the Ice.",
        "q10": "Entirely civilian",
        "q10_justification": "The myth involves civilians and domestic life; no military elements are present.",
        "q11": "Other / Unsure",
        "q11_justification": "The myth does not provide analogies to space as a domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The myth depicts the Ice and blizzards as deadly forces, reinforcing Gethen's extremely harsh physical environment.",
    },
    {
        "chapter": "Chapter 3 - The Mad King",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Political intrigue leads to Estraven's exile. The border dispute simmers but no open conflict erupts.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly demonstrates the ansible to the king, but his presence remains that of a temporary envoy with no permanent infrastructure.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The ansible enables instant communication but physical distances remain vast; Genly's home is effectively unreachable.",
        "q4": "Radically different / alien social order",
        "q4_justification": "King Argaven's court operates on shifgrethor, fear, and alien political customs entirely unlike Earth governance.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Court proceedings occur in Karhidish. The ansible demonstrates cross-stellar communication but in alien tongues.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The cold is ever-present in Erhenrang, requiring significant adaptation, though the city functions.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is the sole off-worlder. The king is incredulous about the Ekumen and other worlds.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Ekumen of Known Worlds and the separate nations of Gethen represent multiple distinct polities.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter revolves around Genly's failed audience with the unstable king, and Estraven's sudden political exile.",
        "q10": "Entirely civilian",
        "q10_justification": "All encounters are political and civilian; no military apparatus is involved.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Ekumen's attempt to bring Gethen into its fold resembles diplomatic expansion into a frontier territory.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Genly remains physically out of place on this cold world; the environment challenges his Earth-adapted physiology.",
    },
    {
        "chapter": "Chapter 4 - The Nineteenth Day",
        "q1": "Other / Unsure",
        "q1_justification": "This is a Karhidish tale about a Foretelling; it does not address space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "The tale takes place entirely on Gethen with no reference to space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No interstellar travel is referenced in this traditional tale.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Foretelling tradition reveals a unique Gethenian cultural practice with no Earth parallel.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The tale is told in Karhidish, an entirely alien language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The tale's setting reflects Gethen's harsh winter environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation or off-world presence is mentioned.",
        "q8": "Other / Unsure",
        "q8_justification": "The tale does not address political structures related to space.",
        "q9": "Drama",
        "q9_justification": "The tale of the Foretelling is a dramatic narrative exploring fate, knowledge, and consequence.",
        "q10": "Entirely civilian",
        "q10_justification": "The tale involves only civilians and religious practitioners.",
        "q11": "Other / Unsure",
        "q11_justification": "The tale does not provide analogies for space as a domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The tale reinforces the harsh, cold environment of Gethen that differs greatly from Earth.",
    },
    {
        "chapter": "Chapter 5 - The Domestication of Hunch",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Genly observes Gethenian society from a position of diplomatic interest; no open conflict occurs.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly travels as a lone envoy visiting Handdara Fastnesses; no permanent off-world settlement exists.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Genly's profound isolation on Gethen underscores the extreme distance from Ekumenical worlds.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Handdara religion, Foretelling practice, and Gethenian social organization are fundamentally unlike anything on Earth.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Genly operates in Karhidish, an entirely distinct language from Earth tongues.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The winter environment is harsh but the Fastness functions; survival requires significant adaptation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is the only off-worlder on the entire planet.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Ekumen and Gethenian nations represent distinct political entities across space.",
        "q9": "Political / diplomatic",
        "q9_justification": "Genly's observations serve his diplomatic mission of understanding Gethenian society for the Ekumen.",
        "q10": "Entirely civilian",
        "q10_justification": "All activities are civilian: religious observation, travel, and cultural study.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Genly's solo exploration of an alien culture mirrors frontier-era explorers studying new territories.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Gethen's environment and society constantly challenge Genly's Earth-adapted body and assumptions.",
    },
    {
        "chapter": "Chapter 6 - One Way into Orgoreyn",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Karhide-Orgoreyn border dispute is central; Estraven is exiled and crosses into rival territory amid ongoing political rivalry.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Estraven enters Orgoreyn as a refugee; Genly's mission remains a temporary diplomatic visit.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Estraven reflects on Genly's alien origin from impossibly distant worlds, reinforcing the extreme separation.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Orgoreyn's commensality system, bureaucracy, and the contrast with Karhide reveal an alien political culture.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Estraven navigates between Karhidish and Orgota, both alien languages distinct from Earth tongues.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The border crossing in winter conditions highlights the harsh environment, though survivable with proper preparation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly remains the only alien on the planet; his mission is referenced as unprecedented.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Karhide, Orgoreyn, and the Ekumen are presented as separate political entities with distinct governance.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter follows Estraven's political exile and his attempts to influence Orgota Commensals regarding the Ekumen.",
        "q10": "Entirely civilian",
        "q10_justification": "All activities are civilian and political; no military forces are involved.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The narrative of crossing borders into rival territory echoes frontier-era political maneuvering.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The harsh winter conditions during border crossing emphasize Gethen's fundamentally different environment.",
    },
]

country = 'US'
book_title = "The Left Hand of Darkness"
csv_path = "data/results/US_The_Left_Hand_of_Darkness.csv"
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
