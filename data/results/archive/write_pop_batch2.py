import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 6",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry occurs. The chapter is an exposition of the planet's geopolitical landscape through Guy's perspective as he returns to the capital.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains the sole space visitor. The chapter focuses on Guy navigating the city and encountering Rada's involvement with the underground.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced. The chapter is focused on planetary politics and Guy's personal struggles.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter reveals the full scope of the totalitarian mind-control society: twice-daily ecstasy broadcasts, persecution of degens, propaganda against mutants, and the existence of multiple hostile nations including Khonti and the Island Empire.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Maxim now speaks the alien language fluently but it remains entirely distinct from Earth languages. The chapter is narrated from Guy's perspective in the native tongue.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The urban environment shows post-nuclear decay: polluted air, militarized streets, propaganda broadcasts, and the constant threat of mind-control radiation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling on the planet.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter reveals multiple nations on Saraksh: the Creators' state, Khonti (divided into League and Union factions), the Island Empire conducting submarine warfare, Pandeya, and the Ondol Principality.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is an exposition of the planet's complex political landscape: multiple warring nations, the underground resistance, Guy's growing disillusionment with the Legion, and Rada's secret degen status.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Guy transitions between military duty and civilian life. The chapter shows both Legion operations and civilian underground resistance activities.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim navigates an alien political landscape as an outsider, while Guy serves in frontier military operations against hostile neighbors.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Mind-control radiation towers, post-nuclear contamination, hostile neighboring states, and pervasive surveillance make the environment fundamentally challenging.",
    },
    {
        "chapter": "Chapter 7",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. Maxim investigates the mind-control towers and witnesses a degen persecution raid.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a lone visitor, now actively investigating the planet's oppressive systems.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced in this chapter.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter depicts mass mind-control ecstasy episodes and violent persecution of degens who are immune to the towers' radiation. Citizens are turned into frenzied mobs.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication occurs in the alien language, which Maxim has learned. It remains wholly distinct from Earth languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The mind-control radiation creates twice-daily episodes of mass psychosis, and degens suffer excruciating pain. The environment is pervasively hostile.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim is the sole Earthling on the planet.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The broader political landscape with multiple nations remains established from the previous chapter.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Maxim witnesses a degen raid: security forces hunt down people immune to mind-control, civilians turn into a violent mob during an ecstasy episode, and Maxim discovers the towers' true purpose. The atmosphere is one of horror and revelation.",
        "q10": "Mostly military",
        "q10_justification": "The chapter centers on Legion operations, degen raids, and Maxim's military service. The mind-control system is enforced through military infrastructure.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim, an outsider immune to the planet's control systems, investigates the oppressive infrastructure like a frontier explorer uncovering colonial atrocities.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mind-control radiation physically affects all inhabitants, causing either ecstasy or agony. The towers represent technology fundamentally unlike anything on Earth.",
    },
    {
        "chapter": "Chapter 8",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter focuses on Maxim's moral crisis over the degen persecution he witnessed.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor, now morally conflicted about the society he has joined.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter deepens the picture of the totalitarian society: Guy defends the degen persecution as necessary, revealing how deeply the mind-control has shaped citizens' moral reasoning.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Maxim and Guy debate in the alien language. The language remains distinct from any Earth tongue.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The militarized society with mind-control infrastructure and active persecution of minorities makes survival harsh for anyone outside the system.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The political landscape with multiple nations remains as previously established.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on the moral debate between Maxim and Guy about the treatment of degens. Maxim is horrified; Guy, shaped by mind-control, sees the persecution as justified. Their friendship is tested by irreconcilable worldviews.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Maxim and Guy discuss the degen question in both military and civilian contexts, bridging their Legion duties and personal moral convictions.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim, an outsider with a fundamentally different ethical framework, confronts the moral norms of the alien society he has entered.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mind-control system that shapes citizens' moral reasoning represents a fundamentally alien technological challenge to human autonomy.",
    },
    {
        "chapter": "Chapter 9",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. Maxim makes contact with the underground resistance against the Creators.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor, now joining the underground resistance.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The underground reveals the full extent of the Creators' tyranny: mind-control towers, persecution of immune individuals, and a resistance movement fighting for mental freedom.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication is in the alien language. Maxim is now fluent but the language remains wholly distinct.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The underground operates in constant danger of discovery. Radiation from the towers causes degens excruciating pain.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim is the sole Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple nations and factions on Saraksh remain established.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Maxim is interrogated by the underground, subjected to radiation torture to test if he is a degen, and must prove his loyalty. The atmosphere is tense and dangerous, with the constant threat of betrayal and discovery.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The underground resistance is a civilian organization fighting against military infrastructure. Maxim bridges both worlds.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim joins an indigenous resistance movement against an oppressive regime, paralleling frontier narratives of outsiders allying with local rebels.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mind-control radiation physically tortures degens, and the underground must constantly evade technological surveillance.",
    },
    {
        "chapter": "Chapter 10",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter focuses on the underground planning an attack on a mind-control tower.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim participates as a sole visitor embedded in the resistance.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The underground's military planning against the Creators' mind-control infrastructure reveals a society organized around technological oppression and armed resistance.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in the alien language. Maxim is fluent.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The resistance must operate clandestinely, planning military operations against heavily defended mind-control towers.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim is the sole Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple nations on Saraksh remain established.",
        "q9": "Military / war",
        "q9_justification": "The chapter centers on military planning: the underground prepares an assault on a mind-control tower, assigns roles, discusses tactics, and Maxim volunteers for the most dangerous task.",
        "q10": "Mostly military",
        "q10_justification": "The chapter is dominated by military planning and preparation for the tower attack.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "An outsider joins a guerrilla resistance planning attacks against an oppressive regime's infrastructure, echoing colonial resistance narratives.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mind-control towers represent alien technology that must be physically destroyed to liberate the population.",
    },
    {
        "chapter": "Chapter 11",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter depicts the underground's attack on the mind-control tower.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim participates in the attack as a sole visitor embedded in the resistance.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The tower attack reveals the depths of the mind-control system: when the tower is briefly disabled, nearby citizens wake from their mental fog, then relapse when backup systems activate.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in the alien language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The tower attack results in multiple casualties: Ordi, Forester, and Green are killed. The military response is swift and lethal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim is the sole Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple nations on Saraksh remain established.",
        "q9": "Military / war",
        "q9_justification": "The chapter is a combat sequence: the underground attacks the tower, Maxim destroys it, but government forces counterattack. Ordi, Forester, and Green are killed. Maxim is captured. The chapter is dominated by violence and tactical action.",
        "q10": "Mostly military",
        "q10_justification": "The entire chapter is a military engagement between the underground and government forces.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "A guerrilla attack on colonial-style oppressive infrastructure, with heavy casualties among the resistance fighters.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mind-control tower and the military technology used to defend it represent fundamentally alien challenges.",
    },
]

country = 'Russia'
book_title = 'Prisoners of Power'
csv_path = 'data/results/Russia_Prisoners_of_Power.csv'
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
