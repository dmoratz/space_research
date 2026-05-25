import json, csv, os

chapters_data = [
    {
        "chapter": "Part 4 Act I",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Nine UNSDF battleships launch to intercept the Builders. The Phalanx leads as the contact ship. The Builders continue on a direct course for Mercury ignoring all communication. A three-wave attack plan is ready if contact fails. The strategic struggle is intense.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The UNSDF fleet operates temporarily in the inner solar system. The Mercury Base Station continues operations. No permanent settlements exist.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The fleet travels within the inner solar system toward Mercury. The journey takes months but remains within near-Earth space.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists. The fleet crews are military personnel on a mission.",
        "q5": "Same languages as Earth",
        "q5_justification": "The crew speaks English. Broadcasts from Earth come in many languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The fleet operates near Mercury with ring material contamination risks. The ships require corrosion-retarding coatings. Solar radiation is intense.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Nine battleships with crews of ~60 each, plus the five-person Phalanx. Hundreds of military specialists are in space.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands the entire fleet from Strategic Air Command headquarters.",
        "q9": "Military / war",
        "q9_justification": "The chapter details the launch of nine battleships, the battle plan with three attack waves, and preparations for humanity's first interstellar war. Military operations dominate.",
        "q10": "Mostly military",
        "q10_justification": "The fleet is military. Aki commands the Phalanx as a military commander. The mission structure is entirely military.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The fleet with its battleships, armadas, and naval command hierarchy operates like a naval task force. Ships are designated UNSS (United Nations Space Ship).",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Zero gravity, cocoon-based living, ring material contamination, solar radiation near Mercury, and the challenge of intercepting an object at 90 km/s all demonstrate how different space is.",
    },
    {
        "chapter": "Part 4 Act II",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Phalanx approaches the Builders' ship. The alien vessel is revealed as a rotating Torus. The crew debates whether the Builders have physical bodies or uploaded consciousness. The strategic challenge of rendezvous at extreme velocity intensifies.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The fleet operates temporarily in the inner solar system. The Builders' ship is a transient presence.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "The Phalanx has been traveling for months. The crew is meaningfully separated from Earth with communication delays.",
        "q4": "Other / Unsure",
        "q4_justification": "No human space society exists. The Builders' society is unknown but their Torus suggests biological life with artificial gravity.",
        "q5": "Same languages as Earth",
        "q5_justification": "The crew speaks English. The Builders have not responded to any communication.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Operating near Mercury with the Builders' ship requires extensive resources and constant vigilance.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "The fleet with hundreds of crew represents a small specialist population in space.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands the fleet.",
        "q9": "Adventure / exploration",
        "q9_justification": "The first visual contact with the alien Torus and speculation about its inhabitants drives the narrative as exploration and discovery.",
        "q10": "Mostly military",
        "q10_justification": "The fleet operates under military command. The Phalanx's contact mission is framed within the military operation.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Naval nomenclature and command structure continue throughout the fleet operations.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Matching velocity with an object at 90+ km/s, the rotating Torus, and communication delays challenge human technology.",
    },
    {
        "chapter": "Part 4 Act III",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Builders destroy the probe hound and the Remora with their attack beam. Every approach is met with lethal force. The Phalanx must decide whether to proceed despite the Builders' hostility.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The Builders destroy anything that approaches within 14,000 km. No territory near them can be held.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "The Phalanx has been traveling for months. Communication with Earth has significant delays.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Builders destroy all approaching objects without communication. Their behavior suggests a radically different social order that does not recognize other intelligences.",
        "q5": "Other / Unsure",
        "q5_justification": "The Builders refuse all communication. No common language or communication medium has been established.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Builders' attack beam destroys the probe and Remora instantly. The environment near the alien vessel is lethal.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "The fleet crew represents a small specialist population.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands the fleet.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The destruction of the hound and Remora, the Builders' lethal hostility, and the crew's desperate decision-making create intense thriller and survival tension.",
        "q10": "Mostly military",
        "q10_justification": "The mission operates under military command. The Builders' attack beam creates a battlefield.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The Phalanx maneuvers like a naval vessel approaching a hostile ship.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Objects destroyed instantly by energy beams, velocities of 90 km/s, the rotating alien Torus, and the vacuum of deep space create a radically non-Earth-like environment.",
    },
    {
        "chapter": "Part 4 Act IV",
        "q1": "Total war / constant conflict",
        "q1_justification": "The First Armada launches missiles and spiderwebs at the Builders. The Builders' center separates from the Torus and destroys every weapon with its attack beam in rapid succession. Total warfare is underway.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The Builders dominate the space around their ship. No human forces can approach.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "The fleet is deep in the inner solar system, months from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Builders treat human weapons as obstacles to swat aside, showing no recognition of human intelligence or agency.",
        "q5": "Other / Unsure",
        "q5_justification": "No communication with the Builders has been established.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Builders' attack beam vaporizes all approaching objects. The space near their ship is lethal.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Fleet crews represent a small specialist population.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands the fleet from headquarters.",
        "q9": "Military / war",
        "q9_justification": "The chapter depicts the First Armada's attack and its complete failure. Military operations and strategy dominate.",
        "q10": "Mostly military",
        "q10_justification": "The entire chapter is military: missile launches, attack coordination, and tactical analysis.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The armada structure, missile salvos, and naval-style engagement create a naval domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Energy beams destroy missiles in milliseconds. Objects vaporize into superheated plasma. Velocities and distances are completely unlike Earth warfare.",
    },
    {
        "chapter": "Part 4 Act V",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Second Armada attacks with enhanced tactics. The Phalanx acts as a forward observer at 20,000 km. All missiles are destroyed. The crew debates the graser's likely failure. Total warfare continues.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The Builders destroy everything approaching their ship.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "The fleet is deep in the inner solar system with significant communication delays.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Builders continue to ignore human presence, treating missiles as obstacles.",
        "q5": "Other / Unsure",
        "q5_justification": "No communication has been established.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Builders' attack beam and nuclear explosions make the war zone lethal.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Fleet crews represent a small specialist population.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands the fleet.",
        "q9": "Military / war",
        "q9_justification": "The Second Armada's attack and its failure dominate the chapter. The Phalanx serves as a forward observer. Military tactics and their futility drive the narrative.",
        "q10": "Mostly military",
        "q10_justification": "The entire chapter is military operations: missile launches, observation, tactical coordination.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The fleet engagement, forward observer role, and armada structure are naval.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Space combat at extreme velocities with energy beams and nuclear weapons in vacuum is radically unlike Earth experience.",
    },
    {
        "chapter": "Part 4 Act VI",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Second Armada's final attack fails. Raul reveals that Natalia is communicating with the Builders. The crew votes unanimously to approach the Builders' ship using Natalia as a shield. The contact mission is revived at the brink of war.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The Builders destroy all approaching objects except the Phalanx (protected by Natalia's communication).",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "The crew is deep in the inner solar system, months from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Natalia communicates with the Builders in a way humans cannot understand, suggesting a radically different form of intelligence.",
        "q5": "Other / Unsure",
        "q5_justification": "Natalia and the Builders communicate in an incomprehensible non-linguistic mode. Humans cannot understand it.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The war zone is lethal. The graser is about to fire. The crew risks death to approach.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Fleet crews represent a small specialist population.",
        "q8": "Single unified authority",
        "q8_justification": "The UNSDF commands operations but the Phalanx crew makes autonomous decisions due to communication delays.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The desperate revelation of Natalia's communication with the Builders, the crew's unanimous vote to approach the lethal alien ship, and the ticking clock to the graser attack create intense thriller tension.",
        "q10": "Mostly military",
        "q10_justification": "Military operations frame the chapter. The Phalanx operates as a military vessel making a desperate tactical decision.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The fleet engagement and naval command structure continue.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Communication through non-linguistic AI, energy beams, and velocities of 90 km/s create a radically non-Earth-like domain.",
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

print('Done batch 4.')
