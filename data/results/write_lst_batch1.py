import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 1",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Miyo and Kan are attacked by a mononoke (ET creature) on Mount Shiki. Messenger O arrives from the future, destroys the creature with his sword Cutty, and warns that an army of ETs must be destroyed. The chapter establishes the central conflict: extermination-level war between humanity and alien self-replicating fighting machines.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely on Earth in 248 AD Japan (the Land of Wa). No space territory is depicted. The Messenger comes from the future, not from space.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. The Messenger traveled through time, not space. He arrived from 2,300 years in the future via temporal upstreaming across multiple timestreams.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays 3rd-century Japan: Queen Himiko rules Yamatai, with ministers, slaves, and chiefdoms. The Messenger is from the future, not a space culture.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak archaic Japanese. Cutty identifies it as archaic Japanese with vowel shift. The Messenger uses translation capability to communicate with Miyo. The Laws of the Messenger exist in every language worldwide.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is entirely the mountains and plains of 3rd-century Japan.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. The Messenger is a time traveler, not a space traveler. The chapter is set on Earth.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is depicted. Earth governance consists of the chiefdoms of Wa under Queen Himiko, with relations to Wei, Kushina, Roma, and Kentak.",
        "q9": "Military / war",
        "q9_justification": "The chapter establishes a war narrative: the Messenger arrives to prepare humanity for battle against the ETs. He tells Miyo to prepare for war, lift the ban on steel production, and mobilize forces. The mononoke attack is the inciting incident of a military campaign.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Miyo is a civilian ruler (shaman queen) thrust into military leadership. Kan is a civilian boy-servant. The Messenger is a military cyborg. The chapter blends civilian court life with the onset of military operations.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. The conflict takes place on Earth's surface across historical time periods.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced. The physical setting is terrestrial Japan.",
    },
    {
        "chapter": "Chapter 2",
        "q1": "Total war / constant conflict",
        "q1_justification": "Earth was annihilated by the ETs 62 years prior. Venus fell first, then Earth lost sunlight for 3 years, then the enemy landed in force. By year 10, humanity withdrew to Neptune. The entire chapter details an existential war for species survival across the solar system.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Triton has a permanent city with residences, roads, forests, a commercial district, and automated transport. It serves as humanity's principal stronghold. Mars and other bodies also had settlements. The city is designed for comfortable living despite being a military hub.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Humanity withdrew to Neptune's moon Triton after losing Earth. The Messengers are deployed on near-lightspeed vessels from a Lagrangian point between Jupiter and Saturn. The journey into the past is a one-way trip spanning timestreams.",
        "q4": "Distinct space culture",
        "q4_justification": "Triton has developed its own culture: AI-human relationships are normalized, Messengers (cyborg AIs) are socialized alongside humans, full data presence enables instant information sharing, and the population has adapted to war as a permanent condition. Average lifespan exceeds 140 years.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in standard Earth languages. Orville and Sayaka speak normally. Sayaka has a Russian name from Valles Marineris. No distinct space language has developed.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Triton is far from the Sun, requiring artificial luminosity sources. Antimatter production without solar energy took 40 years. The ET depend on solar energy, which is greatly attenuated at Neptune's distance, giving humanity a survival advantage.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Several hundred million humans survive, with Triton as the hub. Nearly 50,000 Messengers are on Triton alone. The city has civilians, military, corporations, nurseries, schools, and a commercial district. Space habitation is widespread among survivors.",
        "q8": "Single unified authority",
        "q8_justification": "The Triton Central Council governs Sol System. The Sol System Recovery Command directs the war effort. Sandrocottos AI is Supreme Commander. While free cities exist beyond Jupiter, Triton is the single hub of centralized authority.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on Orville's relationship with Sayaka: their meeting, courtship, philosophical debates about humanity, and heartbreaking parting. The war frames the story but the emotional core is their love and the impossibility of their future together.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Triton has both civilian life (restaurants, study circles, commercial districts) and military operations (Defense Force, Supply Section, deployment of Messengers). Sayaka works in military supply but is civilian. Orville is military but lives among civilians.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The fleet assembles at a Lagrangian point like a naval staging area. Ships are docked and deployed. The farewell scene resembles a naval departure with crowds watching from the gangway. The fleet drops into the well of time like ships setting sail.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Life on Triton requires artificial light sources suspended above the surface. Antimatter production without solar energy was a 40-year endeavor. The ET destroyed Earth's biosphere with a half-million-kilometer disk blocking sunlight. Space habitation demands constant technological intervention.",
    },
    {
        "chapter": "Chapter 3",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Kunu has been overrun by mononoke, sending refugees flooding into Yamatai. The Messenger stages a dramatic arrival to win political support. Battle lines are established. Cutty reports simultaneous crises worldwide: a Messenger destroyed in East Africa, stations urgently mobilized across the Middle East.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely on Earth in 248 AD Japan. No space territory is depicted. Cutty's surveillance network covers the planet from an unspecified location.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. All action is on the surface of Earth. The Messenger's temporal journey is referenced but not depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays the political dynamics of Yamatai: Miyo vs. Takahikone, Mimaso's timidity, Takahaya's loyalty.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak archaic Japanese. Miyo and the Messenger communicate via the magatama bead. Cutty translates and communicates in the local language.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is entirely terrestrial.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. All action occurs on Earth's surface.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance is depicted. The chapter focuses on Earth-based politics between Yamatai's rulers and allied chiefdoms.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by military preparations: staging the Messenger's arrival, marching with 5,000 warriors, combat with Emishi pathfinders, and learning that Kunu has fallen to the mononoke. Strategic planning drives every scene.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Miyo is a civilian ruler directing military operations. Takahaya commands soldiers. Peasants observe the ceremonies. The Emishi envoy delivers a plea for humanitarian aid amid the military crisis.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. All operations are on Earth's surface.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced. The setting is terrestrial Japan.",
    },
    {
        "chapter": "Chapter 4",
        "q1": "Total war / constant conflict",
        "q1_justification": "The ET launch 14,000 asteroids at Earth from the asteroid belt. Ten colonies mature on every continent. Cities and forests burn. Mars is attacked. A floating city of refugees faces imminent destruction. Messengers lose units as their creators' ancestors die. Humanity faces extinction in this timestream.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Mars has settlements under construction with materials from Earth and the Moon. The Moon has polar bases and commercial enterprises. Orbital and planetary infrastructure exists across the inner solar system. Humanity holds territory from Earth to Mars.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The Messengers travel between Earth, the Moon, Mars, and Venus. Orville shuttles between bases scattered throughout Sol System as far as Mars. Interplanetary communication and administration have been perfected. Distances are measured in hours of comm lag.",
        "q4": "Basically Earth society in space",
        "q4_justification": "22nd-century humanity extends Earth institutions into space: the United Nations, sovereign nations, corporations, commercial enterprises, and military bases. There is no distinct space culture; Moon bases have transport chiefs and commercial operations identical to Earth.",
        "q5": "Same languages as Earth",
        "q5_justification": "Orville speaks to Chan, a human officer from Shanghai, in standard language. Earth's languages are used throughout. The Messengers are fluent in all Earth languages. No space-specific language exists.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Venus is explored for hidden colonies in its thick atmosphere. The Moon requires commercial installations. Mars settlements depend on Earth supplies. The asteroid attack demonstrates the fragility of Earth. The floating city Penglai faces destruction from mass-produced airborne ET.",
        "q7": "Moderately common (noticeable settlements/populations)",
        "q7_justification": "Mars has settlements under construction. The Moon has multiple commercial bases. The floating marine city Penglai houses refugees. Off-world production plants and lunar mining operations employ people throughout the inner solar system.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "National governments control lunar bases and refuse to cooperate without domestic legislation. The UN passes resolutions but sovereign members resist. Great powers dominate negotiations. Corporations obstruct the Messengers. Earth's political divisions extend into space wholesale.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by war: the ET asteroid bombardment, nuclear counterstrikes, ground invasion of Earth, burning cities visible from orbit, and the desperate defense of refugee cities. Chan's plea for his pregnant wife underscores the human cost.",
        "q10": "Mostly military",
        "q10_justification": "The chapter revolves around military operations: asteroid defense, nuclear strikes, fleet deployments, and ground combat against ET. Chan is a military liaison. The Moon base is a military-adjacent commercial facility. Civilians appear mainly as refugees.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The fleet deploys nuclear weapons from ships retrofitted for human officers. The floating marine city Penglai echoes naval operations. Ships jammed with refugees dock while vessels bristling with antiaircraft guns head out to sea. The defense has distinctly naval characteristics.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Asteroids are weaponized against Earth. Venus has crushing atmosphere hiding ET colonies. The Moon's low gravity requires specialized operations. Nuclear strikes devastate Earth's surface. The biosphere is under catastrophic assault from multiple directions.",
    },
    {
        "chapter": "Chapter 5",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Continuous battle against the mononoke across western Japan. Soldiers learn to fight ETs with rams, crossbows, and fire. The Messenger leads the frontlines. Cutty deliberately lures weakened mononoke to Yamatai as 'immunization.' Miyo discovers the deception and is devastated.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely on Earth in 248 AD Japan. No space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. All action takes place on the surface of ancient Japan.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays the wartime society of Yamatai with its queen, ministers, and allied chiefdoms.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in archaic Japanese via the magatama bead. Cutty speaks through the bead in the local language.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is entirely terrestrial.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. All characters are on Earth's surface.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance exists. The chapter focuses on Earth political dynamics: Miyo vs. Takahikone, and the mobilization of allied chiefdoms.",
        "q9": "Military / war",
        "q9_justification": "The chapter is entirely about military operations: destroying solar panels, training soldiers with new weapons, battles at Mount Miminashi, the arrival of reinforcements from Kunu and Toma. Miyo leads troops as bait in an ambush. Takahaya commands the trap.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Miyo is a civilian queen commanding military forces. Peasants and villagers are caught in the fighting. Takahikone struggles between civil governance and military ambition. The chapter mixes civilian political intrigue with battlefield action.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced. The setting is entirely on Earth.",
    },
]

country = 'Japan'
book_title = "The Lord of the Sands of Time"
csv_path = "data/results/Japan_The_Lord_of_the_Sands_of_Time.csv"
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
