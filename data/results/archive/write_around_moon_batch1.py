import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 0",
        "q1": "No contestation",
        "q1_justification": "This preliminary chapter summarizes the backstory of the Gun Club's project to fire a projectile at the moon. There is no conflict or contestation over space itself; the endeavor is a cooperative scientific enterprise supported by public funding and international enthusiasm.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The chapter describes space as a transit zone through which the projectile travels. There is no inhabitation or territorial holding; the travelers are sealed inside a shell with the uncertain hope of reaching the lunar surface.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The journey from Earth to the Moon is described as taking about four days, covering roughly 216,000 miles. This is a relatively short interplanetary trip within the Earth-Moon system.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers are simply Earth people in a projectile; there is no distinct space culture. The chapter describes American and French society organizing the mission, with no cultural transformation occurring in space.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in the same Earth languages. The chapter references Americans and a Frenchman working together with no language barriers or new space languages.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter notes the travelers carried a year's supply of food, water for months, and an automatic air device, suggesting space is survivable but requires careful preparation. The outcome of their journey remains uncertain.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men have ever left Earth in this narrative. The chapter emphasizes this is an unprecedented scientific endeavor, the first time humans have entered interplanetary space.",
        "q8": "Other / Unsure",
        "q8_justification": "There is no political order in space. The mission is a private American venture by the Gun Club, but no governance or territorial claims in space are discussed in this chapter.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter frames the entire enterprise as a daring scientific exploration and adventure, describing the travelers as bold and the undertaking as extraordinary and unprecedented.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Gun Club is an association of artillerymen formed after the Civil War, giving a military background to the organizers. However, the mission itself is a civilian scientific endeavor, not a military operation.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter describes Michel Ardan wanting to conduct a 'scouting expedition' on the moon, framing the journey as frontier exploration of an unknown land, similar to colonial-era expeditions.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Space is depicted as a void requiring hermetic sealing, artificial air, and careful provisioning. The travelers face uncertainty about whether they can survive and return, highlighting the fundamental physical difference from Earth.",
    },
    {
        "chapter": "Chapter 1",
        "q1": "No contestation",
        "q1_justification": "There is no conflict over space in this chapter. The three travelers cooperate to prepare for launch, discussing bets and making final arrangements inside the projectile before departure.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers are sealed inside a metal shell at the bottom of a cannon, about to be launched. Space is simply a medium to traverse, not a place to inhabit or hold territory.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The journey is expected to take about 97 hours (roughly four days) to reach the moon. The travelers discuss having only minutes before launch and then days of travel ahead.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The three men behave exactly as they would on Earth, making bets, exchanging banter, and shaking hands. Michel Ardan compares the projectile to a train and the launch to a conductor blowing a whistle.",
        "q5": "Same languages as Earth",
        "q5_justification": "The travelers speak their normal Earth languages throughout. Michel Ardan speaks as a Frenchman and the Americans respond in kind, with no mention of any different communication system.",
        "q6": "Manageable but risky",
        "q6_justification": "Barbicane admits he is 'not quite sure' the water cushion will protect them from the impact. The travelers must lie on their sides to survive the launch, and 400,000 pounds of guncotton will propel them, showing real danger but manageable risk.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three humans plus two dogs are leaving Earth. The launch is watched by an extraordinary crowd of spectators, emphasizing how unprecedented and rare this space travel is.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order in space is discussed. The chapter focuses entirely on the moments before launch inside the projectile.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is filled with excitement and anticipation as the three bold companions prepare to depart Earth. The tone is adventurous, with countdown tension and camaraderie before the launch.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Captain Nicholl and President Barbicane have military backgrounds (Gun Club artillerymen), but the mission itself is a civilian scientific venture. Michel Ardan is entirely civilian.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Michel Ardan jokes about bringing dogs to show 'lunar relatives what good manners earth dogs have' and talks about bringing back a cross-bred 'moon mongrel,' framing the journey like a frontier expedition to an unknown land.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The travelers must endure a massive cannon launch with special padding, water cushions, and collapsible partitions to survive. They are sealed in total darkness in a metal prison, highlighting how different space travel is from Earth conditions.",
    },
    {
        "chapter": "The First Half Hour",
        "q1": "No contestation",
        "q1_justification": "There is no contestation over space. The chapter focuses on the travelers recovering from the launch impact and confirming they are in motion, with no rivalry or conflict over space itself.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The three travelers are temporarily present in space inside their projectile, which is described as a transiting vehicle. They are on a mission to reach the moon, not establishing any permanent presence.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The travelers confirm they left Earth just thirteen minutes ago and are already over 5,000 miles away, traveling at roughly 25,000 miles per hour toward the moon on a journey of a few days.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers behave exactly as they would on Earth. Nicholl pays Barbicane $9,000 in cash for lost bets, Barbicane writes a formal receipt, and Michel marvels at how 'American' these financial formalities are even in space.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in ordinary Earth language. Michel makes a joke about French resilience versus Americans, using everyday cultural references with no change in language.",
        "q6": "Manageable but risky",
        "q6_justification": "The travelers survive the launch but suffer injuries: Barbicane has a bleeding shoulder wound, all three were knocked unconscious, and the interior temperature rose to 113 degrees Fahrenheit from atmospheric friction. They recover but the dangers are real.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three people are in space. The chapter emphasizes this is a first-ever journey, with witnesses on Earth watching the drama and the travelers themselves uncertain if they survived.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order in space is discussed. The chapter focuses on the immediate aftermath of launch and confirming their trajectory.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is driven by suspense and discovery as the travelers recover from the launch, determine they are in motion, and make their first observations of space through the portholes, cheering when they confirm they have left Earth.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter focuses entirely on the civilian scientific mission. The travelers are concerned with survival, trajectory verification, and observation, with no military elements present.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The travelers open portholes to look at the unknown void, observe a near-collision with a large meteor, and gaze at the Earth receding behind them, evoking the experience of frontier explorers leaving familiar territory behind.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The travelers experience extreme heat from atmospheric friction, total darkness in space, a near-collision with a meteor, and encounter the vast blackness of the void. The environment is fundamentally unlike Earth.",
    },
    {
        "chapter": "Chapter 3",
        "q1": "No contestation",
        "q1_justification": "There is no conflict over space. The chapter describes the travelers settling into their routine aboard the projectile, taking inventory, and enjoying meals in a cooperative and peaceful atmosphere.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Barbicane takes up residence in the projectile 'as if he were destined to live there in perpetuity,' but this is temporary habitation inside a transit vehicle on a mission to the moon, not permanent settlement.",
        "q3": "Short interplanetary journey",
        "q3_justification": "Captain Nicholl notes they have about eighty-eight hours remaining to reach the moon. The journey is measured in days, making it a short interplanetary trip.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Michel Ardan cooks French-style meals with beef broth, steak, tea, and Burgundy wine. The travelers discuss Earth geography and behave identically to how they would in a comfortable room on Earth.",
        "q5": "Same languages as Earth",
        "q5_justification": "All conversation is in ordinary Earth language. Michel sings old French songs, and the travelers use everyday cultural references with no linguistic changes.",
        "q6": "Manageable but risky",
        "q6_justification": "The projectile provides adequate shelter with food for a year and water for months. However, space outside is either scorching in sunlight or freezing in shadow, and the travelers depend entirely on their sealed environment and air-producing device.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Michel Ardan declares they are the only citizens of their 'miniature cosmos,' emphasizing that only three people exist in space. He says 'over and beyond ourselves, humanity is no more.'",
        "q8": "Other / Unsure",
        "q8_justification": "No political order exists in space. Michel jokes that they are the entire population of a new world, but no governance structure is established.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter describes the travelers inspecting instruments, observing the cosmos through portholes, and marveling at the unique sight of the starry heavens, the sun, and the moon from space. The tone is one of wonder and exploration.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is entirely domestic and scientific. The travelers eat meals, check instruments, inspect supplies, and observe space. There are no military activities or references.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Barbicane packed provisions for a year in case they land in a barren lunar sector, and they inspect seeds and tools for transplanting on the moon. This mirrors frontier settlers preparing to establish themselves in unknown territory.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The travelers depend on a chemical device to produce oxygen and potassium hydroxide to absorb carbon dioxide. The sun alternately floods or abandons their shell, and the void outside is described as perfectly silent and dark. The physical environment is fundamentally alien.",
    },
    {
        "chapter": "Chapter 4",
        "q1": "No contestation",
        "q1_justification": "There is no conflict over space. The chapter is devoted to mathematical calculations about the projectile's velocity, with the travelers debating algebra rather than competing over territory or resources.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers remain inside their projectile in transit to the moon. Their presence in space is temporary and mission-based, with no settlement or territorial holding.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The journey covers about 200,000 miles to the moon. Barbicane calculates velocities and distances within the Earth-Moon system, confirming a trip measured in days.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers engage in mathematical discussion exactly as they would in a university lecture hall. Michel Ardan jokes about algebra, Barbicane teaches, and Nicholl calculates, all using Earth intellectual traditions.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue uses standard Earth language. The mathematical notation and scientific terminology are identical to what would be used on Earth.",
        "q6": "Manageable but risky",
        "q6_justification": "Barbicane's calculations reveal a potential crisis: the initial velocity may be insufficient to reach the neutral point, meaning they could fall back to Earth. This discovery creates alarm, showing the journey is risky but they are managing the situation through calculation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the three travelers are in space. The chapter references the Cambridge Observatory experts who remained on Earth, emphasizing how isolated and rare this space journey is.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order in space is discussed. The chapter focuses entirely on mathematical problems about velocity and trajectory.",
        "q9": "Adventure / exploration",
        "q9_justification": "Despite the mathematical content, the chapter builds dramatic tension as the travelers discover they may not have enough velocity to reach the moon, creating a suspenseful moment in their exploration narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is purely scientific, with the travelers performing mathematical calculations about their trajectory. There is no military element whatsoever.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The travelers are calculating whether they can reach their destination like navigators on an ocean voyage or explorers charting a course into unknown territory, using mathematics as their compass.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter emphasizes that the projectile travels in a perfect vacuum where motion cannot be sensed and inertia governs everything. The laws of physics in space are fundamentally different from everyday Earth experience.",
    },
    {
        "chapter": "Chapter 5",
        "q1": "No contestation",
        "q1_justification": "There is no conflict over space. The chapter involves the travelers resolving their velocity crisis, discussing the temperature of space, and disposing of a dead dog's body through a porthole.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers continue their transit mission inside the projectile. They discuss potentially landing on the moon but have no established settlement or territory in space.",
        "q3": "Short interplanetary journey",
        "q3_justification": "Barbicane confirms they are already over 125,000 miles from Earth after thirty-two hours of travel, more than halfway through their journey to the moon.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Michel Ardan speculates about moonpeople having the same artists, writers, and philosophers as Earth. Barbicane argues lunar civilization would mirror Earth's but be more advanced. All cultural references are Earth-based.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in standard Earth language. The discussion about moonpeople implies they might have their own civilization but no distinct space language is mentioned.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The chapter describes the extreme cold of space at -76 to -256 degrees Fahrenheit, the danger of losing air through the porthole, and the need to quickly dispose of Satellite's body before nitrogen escapes. Survival requires constant resource management.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three people are in space. Michel comments that they are the sole inhabitants of their world, and the death of the dog Satellite reduces even their small party.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structure in space is discussed. The travelers speculate about moonpeople but no governance of space itself is addressed.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter combines scientific discussion about space temperatures and ether with the dramatic moment of ejecting Satellite's body into the void. The tone remains one of bold exploration and discovery.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is entirely focused on scientific discussion about space conditions, the death of a dog, and survival logistics. No military elements appear.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Michel suggests they should have turned the projectile into Noah's ark with domestic animals for the moon, and Nicholl agrees that oxen and horses would be useful on lunar lands. This frames the moon as a frontier to be settled and farmed.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter details extreme cold in space, the vacuum that causes objects to flatten, the need to carefully manage air pressure when opening portholes, and the concept of ether filling the void. The physical environment is radically unlike Earth.",
    },
    {
        "chapter": "Chapter 6",
        "q1": "No contestation",
        "q1_justification": "There is no contestation over space. The chapter consists of scientific discussions about the moon, eclipses, heat generation from motion, and what would happen if the earth stopped orbiting.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers are five hours past the halfway point of their journey, still in transit. They discuss observations of the moon but remain temporary visitors in space inside their projectile.",
        "q3": "Short interplanetary journey",
        "q3_justification": "After fifty-four hours of travel, the travelers have covered nearly seven-tenths of the distance to the moon. The journey is measured in hours, confirming a short interplanetary trip.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers engage in intellectual parlor conversation about physics, comets, and eclipses exactly as educated men would in a 19th-century salon. Their cultural framework is entirely Earth-based.",
        "q5": "Same languages as Earth",
        "q5_justification": "All conversation is in standard Earth language. Scientific terminology and cultural references are identical to what would be used on Earth.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Barbicane explains that a sudden stop would generate enough heat to vaporize the projectile. The sun's unfiltered rays and the extreme cold of space are discussed at length, showing a harsh environment requiring constant technological mediation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the three travelers are in space. They observe the moon growing larger but remain the sole human presence beyond Earth.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structure in space is discussed. The chapter is entirely devoted to scientific questions and answers about celestial mechanics.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is structured as a scientific Q&A session between the travelers as they approach the moon, combining the excitement of discovery with educational discussion about space phenomena.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is purely scientific discourse about heat, eclipses, comets, and the moon. No military themes or elements are present.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Michel speculates about moonpeople and whether they sent projectiles to Earth, while discussing the moon's surface features as terrain to be explored. The conversation frames the moon as an unknown frontier to investigate.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter emphasizes that space is a vacuum where heat cannot spread, sunlight is unfiltered, and a sudden stop would vaporize the projectile. Objects float alongside the shell after being ejected, demonstrating a physical environment fundamentally unlike Earth.",
    },
    {
        "chapter": "Chapter 7",
        "q1": "No contestation",
        "q1_justification": "There is no real contestation over space. While Michel, Nicholl, and Barbicane get into a heated argument, it is caused by oxygen intoxication, not genuine conflict over space territory or resources.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers are on the final day of their transit to the moon, still inside the projectile. Michel fantasizes about colonizing the moon, but they have not yet arrived or established any presence.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The travelers expect to arrive at midnight that very evening, December 5, completing their journey in about four days. They are mere hours from the moon.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers eat French meals with wine from Medoc, discuss building republics modeled on American government, and sing 'Yankee Doodle' and the 'Marseillaise.' Their cultural framework is entirely Earth-based.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in standard Earth language. The travelers sing national anthems in their respective languages and discuss plans using ordinary Earth vocabulary.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The travelers depend on the Reiset and Regnault air device, which malfunctions by producing excess oxygen, causing dangerous intoxication. Barbicane warns that going outside would cause the body to inflate and explode in the vacuum. Space is harsh and resource-intensive.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three travelers are in space. They joke about being the only citizens of a new republic and electing Barbicane president, emphasizing their total isolation.",
        "q8": "Other / Unsure",
        "q8_justification": "In their intoxicated state, the travelers joke about establishing a republic on the moon with Michel as congress, Nicholl as senate, and Barbicane as president, but this is not a real political order.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter captures the excitement of approaching the moon on their final day, combined with the dramatic complication of oxygen intoxication that nearly causes a fight. The tone is adventurous with a comedic edge.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter focuses on the travelers' approach to the moon, their meals, discussions about colonization, and an accidental oxygen malfunction. No military activity is depicted.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Michel declares they will 'lay claim to the moon in the name of the United States,' colonize it, farm it, and populate it. He explicitly frames the journey as colonial expansion, wanting to add the moon as a fortieth state.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The travelers experience dangerous oxygen intoxication from their air device, weightlessness as they approach the neutral gravity point, and Barbicane warns that exposure to the vacuum would cause the body to explode. The physical environment poses constant challenges.",
    },
]

country = 'France'
book_title = 'Around the Moon'
csv_path = 'data/results/France_Around_the_Moon.csv'

with open('data/questions.json', 'r', encoding='utf-8-sig', errors='replace') as f:
    questions = json.load(f)

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

print('Done with batch 1.')
