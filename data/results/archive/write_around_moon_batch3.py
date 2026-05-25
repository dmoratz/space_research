import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 16",
        "q1": "No contestation",
        "q1_justification": "There is no conflict or rivalry in this chapter. The travelers observe the moon's southern hemisphere and discuss scientific measurements of lunar mountains, with no contestation over space.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The chapter describes the moon's terrain purely as a scientific curiosity to be observed from the projectile. There is no attempt or ability to inhabit or hold territory; the travelers are merely passing by.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The projectile is orbiting the moon at close range, having completed a loop around it. The journey from Earth to the Moon took only a few days, placing it as a short interplanetary trip.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers maintain their Earth identities, social roles, and cultural habits entirely. Michel Ardan distributes dinner of cold cuts and bread, and they use Earth scientific knowledge and instruments throughout.",
        "q5": "Same languages as Earth",
        "q5_justification": "The three travelers communicate in the same languages they use on Earth. There is no indication of any different language being needed or used in space.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter notes dangers such as meteor collisions and the condensation of vapor on windows, but the travelers survive and manage conditions. The cold and darkness are challenging but not immediately lethal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men are traveling in space aboard the projectile. This is an unprecedented and singular voyage with no other humans in space.",
        "q8": "Other / Unsure",
        "q8_justification": "There is no political order or governance in space discussed in this chapter. The travelers are three private individuals observing the moon, and no territorial or political claims are made.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter focuses on scientific observation and exploration of the moon's southern hemisphere, with detailed descriptions of lunar mountains and measurement techniques. It is firmly in the adventure/exploration genre.",
        "q10": "Entirely civilian",
        "q10_justification": "The three travelers are civilians engaged in a scientific expedition. There is no military presence or military framing of the space journey in this chapter.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Space is described as an 'ocean of ether' with meteors compared to reefs. The travelers are likened to navigators at sea who have no way of avoiding obstacles, using distinctly naval metaphors.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter depicts absolute darkness, extreme cold causing vapor to condense and ice over windows, the vacuum of space, and the danger of meteor collisions. The physical environment is fundamentally hostile and unlike Earth."
    },
    {
        "chapter": "Chapter 17",
        "q1": "No contestation",
        "q1_justification": "There is no conflict over space in this chapter. The travelers peacefully observe the lunar surface and discuss geological features like Tycho crater and Newton crater.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The moon is described as a dead world with no organic life. Barbicane concludes that surface features show no human achievements, only geological ones. Michel Ardan imagines a city in Tycho's crater but this is pure fantasy.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The projectile passes over the moon's south pole at only thirty miles altitude, and the entire Earth-Moon journey has taken only a few days, making it a short interplanetary journey.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers behave exactly as educated European and American gentlemen of the 19th century would on Earth. They discuss astronomy, compare lunar features to Earth landmarks, and maintain their cultural norms.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication among the travelers is in their native Earth languages. No new language or communication method is introduced for space travel.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The chapter describes extreme temperature shifts from intense cold to intense heat as they re-emerge into sunlight, requiring careful management of gas and air supplies. The moon itself is depicted as a desolate, dead world.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men are in space. The chapter emphasizes how unprecedented their close-up observations of the moon are, with no other humans having achieved this.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structure in space is discussed. The chapter focuses entirely on scientific observation of the lunar surface.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is devoted to exploring and observing the moon's surface features including craters, mountains, and plains. Michel Ardan even imagines discovering ruins of a lunar city, reinforcing the exploration theme.",
        "q10": "Entirely civilian",
        "q10_justification": "The space journey is a civilian scientific expedition. Tycho crater is compared to a natural fortification, but this is a geographic metaphor, not a military context.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Michel Ardan imagines building a city inside Tycho's crater as a refuge. The travelers survey the lunar landscape like explorers mapping new frontier territory, assessing its features and potential.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The moon's surface features stark blacks and whites with no diffuse light, silent avalanches in vacuum, no vegetation, and no signs of life. The environment is described as a dead world radically unlike Earth's living surface."
    },
    {
        "chapter": "Chapter 18",
        "q1": "No contestation",
        "q1_justification": "The chapter consists of scientific discussion about Tycho's rays, the question of lunar life, and the moon's geological history. There is no conflict or contestation in space.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers unanimously conclude that life cannot currently exist on the moon due to insufficient atmosphere, dried-up seas, and extreme temperature variations. The moon is declared unlivable.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The projectile continues its elliptical orbit around the moon, moving farther away but still within the Earth-Moon system. The journey remains a short interplanetary one of only a few days' duration.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers conduct a formal scientific debate with parliamentary procedures, entering their decision into Barbicane's notebook as proceedings of a meeting. This mirrors Earth academic and political conventions exactly.",
        "q5": "Same languages as Earth",
        "q5_justification": "The travelers converse entirely in their Earth languages throughout their scientific debate. No different language is used or needed in space.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The chapter describes the transition from extreme cold to intense heat as the projectile moves into sunlight. The discussion of the moon's uninhabitable conditions reinforces how harsh space environments are.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the three travelers are in space. Their discussion of life on the moon underscores how isolated and unprecedented their journey is.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structure or governance of space is discussed. The chapter focuses on scientific questions about the moon's habitability past and present.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter combines exploration of the lunar surface with scientific investigation, as the travelers debate whether life existed on the moon and observe various craters and basins.",
        "q10": "Entirely civilian",
        "q10_justification": "The discussion is purely scientific and civilian. The travelers are private citizens conducting astronomical and geological research, with no military dimension.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The discussion of whether the moon was once inhabited and whether it could support life parallels frontier exploration narratives about discovering and assessing new territories for settlement potential.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Barbicane describes the moon as having minimal atmosphere, dried-up seas, inadequate water, abrupt temperature shifts, and 354-hour day-night cycles. The environment is fundamentally hostile to human existence."
    },
    {
        "chapter": "Chapter 19",
        "q1": "No contestation",
        "q1_justification": "There is no conflict or rivalry in space. The chapter focuses on the travelers' attempts to alter their trajectory and their existential plight of falling back toward Earth.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers cannot land on the moon despite wanting to. They discuss the impossibility of controlling the projectile's motion, underscoring their complete inability to establish any presence on the moon.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The projectile is traveling between the moon and Earth, a distance of about 195,000 miles. The journey has lasted only days, placing it firmly as a short interplanetary trip.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers maintain their Earth personas completely. Michel Ardan invokes French and American national character, they eat breakfast with Chambertin wine, and discuss their predicament using Earth-based logic and humor.",
        "q5": "Same languages as Earth",
        "q5_justification": "The travelers communicate in their Earth languages throughout. Michel Ardan makes references to being French and his companions American, with no language barriers or changes.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The travelers face imminent death from multiple causes: potential eternal orbit, falling back to Earth at 144,000 miles per hour, and limited air supply. They fire rockets in a desperate attempt to alter course, highlighting constant survival pressure.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men are in space, and they face the very real prospect of dying there. Their experience is singular and unprecedented.",
        "q8": "Other / Unsure",
        "q8_justification": "There is no political order or governance in space. The chapter deals entirely with the travelers' survival crisis and orbital mechanics.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is dominated by the travelers' desperate attempts to survive. They fire rockets at the neutral point to try to reach the moon, only to discover they are falling back to Earth at lethal speed. Nicholl declares 'We're done for.'",
        "q10": "Entirely civilian",
        "q10_justification": "The three travelers are civilians. Although they use rockets originally designed for the mission, the context is civilian survival rather than any military operation.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The projectile's trajectory is discussed in terms borrowed from celestial navigation, with concepts like periselene and aposelene paralleling maritime navigation terms. The travelers are at the mercy of gravitational currents like sailors on the ocean.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The travelers experience weightlessness at the neutral point, absolute silence in the vacuum where no explosion is audible, and the terrifying physics of a fall from 195,000 miles. The environment is fundamentally unlike anything on Earth."
    },
    {
        "chapter": "Chapter 20",
        "q1": "No contestation",
        "q1_justification": "The chapter shifts to the crew of the USS Susquehanna conducting ocean soundings. There is no conflict over space; the officers discuss the moon travelers with admiration and curiosity.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The officers discuss the travelers as having arrived on the moon temporarily. One imagines them camped in a lunar valley, describing a temporary visit rather than permanent settlement.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The officers note the travelers left ten days ago and discuss the relatively short Earth-to-Moon journey, reinforcing that it is a brief interplanetary trip.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The officers imagine the travelers behaving exactly as they would on Earth: Nicholl surveying, Barbicane writing notes, and Michel Ardan smoking cigars. Earth society is projected directly into space.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication, both aboard the Susquehanna and imagined on the moon, is in English. The midshipman suggests using giant letters for visual communication, implying the same language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The projectile crashes into the ocean with tremendous force, nearly destroying the Susquehanna. The officers debate whether the travelers died from asphyxiation, burning during reentry, or the impact, emphasizing extreme danger.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men made the journey. The Susquehanna's crew discusses them as unique adventurers, though one officer envisions future colonization missions.",
        "q8": "Other / Unsure",
        "q8_justification": "No political governance of space is discussed. The officers speculate about future moon trips but in terms of exploration, not governance.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter frames the moon journey as a grand adventure. The officers speculate about what the travelers discovered, and the dramatic splashdown of the projectile near the warship adds excitement.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The USS Susquehanna is a military vessel, but it is conducting civilian scientific work (ocean soundings for telegraph cables). The moon mission itself is a civilian endeavor discussed admiringly by military officers.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The entire chapter takes place aboard a naval warship. The projectile splashes down in the ocean, and the recovery effort will be a naval operation. Space travel is framed through a distinctly maritime lens.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The projectile's fiery reentry, described as a blazing meteor, and its violent ocean impact demonstrate how the space environment and return to Earth are extremely dangerous and unlike normal human experience."
    },
    {
        "chapter": "Chapter 21",
        "q1": "No contestation",
        "q1_justification": "There is no conflict or rivalry over space. The chapter focuses on the reaction to the projectile's return, the Gun Club's debate over what happened, and J. T. Maston's comedic fall into the telescope.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers' journey is confirmed as a temporary visit that has ended with their return to Earth. The projectile fell into the Pacific, and all discussion centers on recovering the travelers from a completed mission.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The entire round trip from Earth to the Moon and back has taken only about twelve days (launched late November, splashed down December 12), confirming a short interplanetary journey.",
        "q4": "Basically Earth society in space",
        "q4_justification": "All events take place on Earth with Earth institutions responding: the Navy, the Gun Club, the Cambridge Observatory, and telegraph networks. Earth society dominates entirely.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in English via telegraph and in person. No different language is used or referenced for space-related communication.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The crew debates whether the travelers died from asphyxiation, burning up during reentry, or impact. The projectile entered the atmosphere as a mass of flame and struck the ocean near a warship, highlighting extreme danger.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three people made the journey, and the entire world watches anxiously. The event is treated as unprecedented and singular.",
        "q8": "Other / Unsure",
        "q8_justification": "No political governance of space is discussed. The chapter deals with Earth-based institutions reacting to the travelers' return.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter treats the moon journey as a grand adventure, with dramatic tension about whether the travelers survived. J. T. Maston's comedic telescope fall and frantic telegraph communications add to the adventure narrative.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The USS Susquehanna (a military vessel) is central to the recovery effort, and the Secretary of the Navy issues orders. However, the Gun Club and the mission itself are civilian enterprises.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The recovery operation is entirely naval. The Susquehanna races to San Francisco, telegrams are sent, and the projectile must be fished from the ocean. Space travel is framed through maritime recovery operations.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The projectile's reentry turned it into a blazing meteor, and its ocean impact nearly destroyed a warship. The crew debates multiple ways the travelers could have died, underscoring how different space conditions are from Earth."
    },
    {
        "chapter": "Chapter 22",
        "q1": "No contestation",
        "q1_justification": "There is no conflict over space. The chapter focuses entirely on the cooperative international effort to rescue the travelers from the ocean.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers' journey was a temporary mission now concluded. The entire chapter is about recovering them from the ocean after their return from the moon.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The journey is over and the travelers are being rescued from the Pacific. The round trip took roughly two weeks, confirming it as a short interplanetary journey.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The chapter is set entirely on Earth. The rescue involves American engineers, naval vessels, diving equipment, and telegraph communication, all entirely Earth-based institutions and technology.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication during the rescue operation is in English. No space-related language differences are present.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The projectile is submerged nearly five miles deep in the ocean, and J. T. Maston warns the travelers will soon run out of air. The rescue is a race against time to save them from asphyxiation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three people made the space journey. The massive international rescue effort for just three individuals underscores how rare and exceptional space travel is.",
        "q8": "Other / Unsure",
        "q8_justification": "No political governance of space is discussed. The chapter deals with the Earth-based rescue operation.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a tense survival narrative. The rescue team searches desperately for the sunken projectile, fails for days, and nearly gives up. J. T. Maston's realization that the shell floats provides the dramatic turning point.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The USS Susquehanna, a naval warship, conducts the rescue, but the operation is directed by civilian Gun Club members and engineers like Murchison. The Union government funds the effort.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The entire rescue operation is a naval undertaking with diving chambers, grappling hooks, sounding lines, and a warship. The projectile is treated like a sunken vessel to be salvaged from the deep.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The projectile sank nearly five miles into the ocean after its space journey. The travelers are trapped in a sealed metal prison at crushing depths, completely dependent on technology for survival."
    },
    {
        "chapter": "Chapter 23",
        "q1": "No contestation",
        "q1_justification": "There is no conflict in space. The chapter celebrates the travelers' triumphant return and describes the founding of a space transportation company, all in a spirit of cooperation and enthusiasm.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers completed a temporary visit around the moon and returned to Earth. The chapter discusses future plans for repeated journeys, but these are envisioned as trips rather than permanent habitation.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The completed journey from Earth to the Moon and back is summarized as having taken only about two weeks. The chapter looks forward to future journeys as routine trips.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers return to Earth society and are celebrated with an enormous nationwide banquet. A stock company is formed with familiar corporate roles. Earth society extends directly into space planning.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in English. The travelers' notes are published by the New York Herald, and all celebrations and business dealings use Earth languages.",
        "q6": "Manageable but risky",
        "q6_justification": "The travelers survived their journey and are found playing dominoes when rescued, suggesting the conditions were ultimately manageable. However, the chapter acknowledges the dangers and describes the venture as one of unprecedented risk.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three people made the journey, and they are celebrated as demigods. The formation of a transportation company hints at making space travel more common, but currently it remains exceptionally rare.",
        "q8": "Other / Unsure",
        "q8_justification": "No political governance of space is established. The chapter describes a commercial company for space travel but no actual political order in space.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter concludes the adventure narrative with the triumphant rescue and celebrates the travelers' unprecedented exploration. It looks forward to future space adventures with the founding of a transportation company.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is entirely civilian. The travelers are celebrated as civilian heroes, their notes are published commercially, and a civilian stock company is formed for future space travel.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter envisions future space travel as colonial expansion, asking whether humanity will visit planets and stars. A commercial transportation company is formed, paralleling frontier-era railroad and shipping companies.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter summarizes the travelers' observations that the moon is a dead, lifeless world fundamentally unlike Earth. Their journey required constant technological support to survive in the alien environment of space."
    }
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

print('Done with batch 3.')
