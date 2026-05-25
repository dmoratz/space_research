import json, csv, os

chapters_data = [
    {
        "chapter": "front_matter",
        "q1": "Other / Unsure",
        "q1_justification": "Front matter contains title page, table of contents, character list, table of eras, and translator note. No narrative content depicting space.",
        "q2": "Other / Unsure",
        "q2_justification": "No narrative content. Editorial and publishing information only.",
        "q3": "Other / Unsure",
        "q3_justification": "No narrative content depicting any journey or distance.",
        "q4": "Other / Unsure",
        "q4_justification": "No narrative content depicting any society.",
        "q5": "Other / Unsure",
        "q5_justification": "No narrative content depicting language or communication.",
        "q6": "Other / Unsure",
        "q6_justification": "No narrative content depicting any environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No narrative content depicting space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No narrative content depicting political order.",
        "q9": "Other / Unsure",
        "q9_justification": "Front matter with no narrative content; not classifiable by genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative content depicting civilian or military activity.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative content providing any domain analogy.",
        "q12": "Other / Unsure",
        "q12_justification": "No narrative content depicting any physical environment."
    },
    {
        "chapter": "Part I",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Crisis Era is defined by strategic struggle between humanity and Trisolaris. The Staircase Program is a desperate attempt to send a human brain as a spy to the Trisolaran fleet. Nuclear bombs are launched into orbit to accelerate the probe. The Trisolaran sophons constantly surveil Earth. The entire chapter centers on strategic maneuvering in a high-stakes interstellar confrontation.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Space presence is limited to orbital infrastructure for the Staircase Program. Nuclear bombs are placed in orbit and a probe is launched, but there are no settlements or permanent habitation. The space elevator and orbital stations serve the mission only.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Staircase Program aims to intercept the Trisolaran fleet, which is light-years away. The probe is accelerated to about 1% of lightspeed, making the journey effectively one-way and generational in scale. The Trisolaran fleet itself is on a centuries-long voyage to Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "All depicted society is Earth-based. The PIA (Planetary Intelligence Agency) and UN operate as extensions of existing Earth institutions. No distinct space society has formed yet in this era.",
        "q5": "Other / Unsure",
        "q5_justification": "No meaningful space-based language dynamics are depicted. All communication occurs on Earth or via sophon surveillance, using Earth languages.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Space is depicted as lethal vacuum. The Staircase probe requires massive nuclear propulsion infrastructure. Yun Tianming's brain must be cryogenically preserved for the journey. The radiation sail and probe design emphasize the extreme hostility of space travel.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only a handful of people interact with space directly. Yun Tianming's brain is the sole occupant of the probe. Space activity is limited to military-scientific personnel managing the Staircase Program.",
        "q8": "Single unified authority",
        "q8_justification": "The PDC (Planetary Defense Council) and UN coordinate humanity's unified response to the Trisolaran threat. The PIA operates under this unified authority. There is no competing space governance.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is driven by existential dread: Yun Tianming's terminal illness, his euthanasia decision, the desperate gamble of the Staircase Program, and the Constantinople prologue depicting alien high-dimensional technology. Cheng Xin's moral anguish over sending Tianming's brain into space adds to the thriller atmosphere.",
        "q10": "Mostly military",
        "q10_justification": "The Staircase Program is a military-intelligence operation. The PIA is a military intelligence agency. Nuclear weapons are deployed in orbit. Yun Tianming's brain is sent as a spy. Nearly all space activity is military or defense-related.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is portrayed as an existential battleground where espionage and deterrence dominate, not easily analogized to a single real-world domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The Constantinople prologue reveals higher-dimensional physics where objects can be manipulated through extra dimensions. Space travel requires nuclear pulse propulsion at extreme velocities. The environment is fundamentally alien to human experience."
    },
    {
        "chapter": "Part II",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Deterrence Era collapses catastrophically: six droplets simultaneously destroy gravitational wave transmitters, the Trisolaran fleet attacks, humanity is forcibly resettled to Australia under threat of extinction. The dark battles between Bronze Age and other ships involve cannibalism and murder. Blue Space and Gravity engage in interstellar pursuit and conflict.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "By the Deterrence Era, humanity has built space cities and extensive orbital infrastructure around Earth. The fleet includes massive warships. Blue Space and Gravity operate as self-sustaining deep-space vessels. Space has become governable territory.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Blue Space and Gravity flee into deep space on journeys that are effectively one-way. The four-dimensional space fragment exists at extreme interstellar distances. The Trisolaran fleet traverses light-years. These journeys create complete separation from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The 264-year time skip reveals a dramatically changed civilization: feminized aesthetics, space-adapted society, fundamentally different values. The Bronze Age crew developed a distinct spacefaring culture with dark battle ethics. Blue Space crew forms its own deep-space civilization.",
        "q5": "Same languages as Earth",
        "q5_justification": "Despite 264 years of development, human characters communicate in recognizable languages. Cheng Xin understands people after awakening from hibernation. No distinct space language barriers are depicted between human factions.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Space habitation requires massive infrastructure: space cities, warships with advanced life support, hibernation technology. The Great Resettlement shows space infrastructure's fragility. The four-dimensional space fragment poses existential dangers. Deep space travel is resource-intensive but achievable.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "By the Deterrence Era, space cities house significant populations. The fleet employs many people. Space habitation is common though not yet universal. The Great Resettlement forces humanity back to Earth, showing how many had been living in space.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple distinct authorities operate: the Solar System government (with its Swordholder system), the Trisolaran civilization, the escaped fleet ships (Blue Space and Gravity) which form independent entities, and Bronze Age's crew which operated by its own rules.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by military conflict: the deterrence standoff, the droplet attack destroying transmitters, the Great Resettlement under military threat, the dark battles between human ships, and the interstellar pursuit of Blue Space. War and military strategy drive the plot.",
        "q10": "Mostly military",
        "q10_justification": "Nearly all space activity is military: warship fleets, droplet attacks, gravitational wave deterrence systems, interstellar pursuit, dark battles. The Swordholder system is a military deterrence mechanism. Civilian space presence exists but is overshadowed by military operations.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Space warfare closely parallels naval warfare: fleet engagements, pursuit across vast distances, ships as self-contained communities, the dark battles echoing submarine warfare and age-of-sail combat ethics. Blue Space and Gravity operate like ships of the line in deep ocean.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The four-dimensional space fragment fundamentally defies Earth physics: crew members can see inside solid objects, reach through three-dimensional barriers, and perceive reality from a higher dimension. This encounter represents physics completely unlike any Earth experience."
    },
    {
        "chapter": "Part III",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Broadcast Era begins with Trisolaris being annihilated by a photoid (lightspeed projectile) that destroys its star system. The dark forest theory is proven: any civilization that reveals its location is destroyed. Yun Tianming's fairy tales encode survival strategies against cosmic-level weapons. The safety notice discussion reveals the universe as a perpetual battlefield.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter reveals a universe filled with civilizations occupying vast territories. Trisolaris had its own star system with a fleet. The dark forest concept implies countless civilizations holding and defending territory across the galaxy. The safety notice discussion references universe-wide territorial dynamics.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Trisolaris is 4.2 light-years from Earth, and its destruction by photoid takes 3.8 years to observe. Distances are interstellar and effectively unreachable. Yun Tianming communicates from the Trisolaran fleet across light-years.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Sophon reveals Trisolaran society and its transformation. The dark forest universe implies civilizations with radically different social orders shaped by existential threat. The fairy tales encode information about alien technologies and societal structures fundamentally unlike Earth's.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Sophon (the Trisolaran AI android) communicates fluently with humans, mediating between Trisolaran and human civilizations. Yun Tianming encodes messages in fairy tales that must be decoded, but the actual communication is technology-mediated across species.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The destruction of Trisolaris demonstrates that space is lethal at a stellar scale. A single photoid obliterates an entire star system. The dark forest makes all of space a kill zone where revealing your position means annihilation. The environment is fundamentally hostile.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Human space infrastructure continues from the Deterrence Era. The Bunker Project is being planned. Many people live in space cities. The broader universe is implied to be populated by many civilizations with their own space habitation.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple polities exist: Earth's government, the remnants of the Trisolaran civilization (now destroyed), the escaped fleet ships, and the implied countless civilizations across the galaxy operating as independent entities in the dark forest.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is driven by existential horror: watching Trisolaris be annihilated, the revelation that the universe is a dark forest where detection means death, and the desperate search for survival strategies encoded in Yun Tianming's fairy tales. The safety notice concept adds cosmic-scale dread.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Space activity mixes military and civilian: the destruction of Trisolaris is military, while the Bunker Project planning is a civilian survival initiative. Yun Tianming's fairy tale transmission bridges both. Sophon's revelations serve both strategic and scientific purposes.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is portrayed as a dark forest where all civilizations are hunters and prey simultaneously. This unique metaphor doesn't map neatly to ocean, air, frontier, or cyberspace analogies.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Photoid weapons travel at lightspeed and destroy entire star systems. The dark forest operates on physics of interstellar destruction. Dimensional reduction and lightspeed manipulation are discussed as real threats. The physical environment operates on principles fundamentally unlike Earth experience."
    },
    {
        "chapter": "Part IV",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The Bunker Era is relatively peaceful: humanity builds space cities behind gas giants as a precaution, but no active conflict occurs. Wade's attempt to develop lightspeed ships creates internal political tension but is resolved without war. The Trisolaran threat has receded. Contestation is low and primarily internal.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Humanity has built 64 space cities behind Jupiter, Saturn, Uranus, and Neptune. Asia I alone is 30km long and 7km in diameter. These cities represent extensive territorial occupation of the solar system, organized like states with distinct governance.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "Travel between space cities and Earth takes weeks to months. The space cities orbit gas giants throughout the solar system. This creates meaningful separation but not generational distances. Characters can and do travel between locations.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "Life in the space cities closely mirrors Earth life with adaptations. Asia I has simulated landscapes, weather systems, and familiar social structures. People live ordinary lives with jobs, relationships, and daily routines, adapted to cylindrical habitat conditions.",
        "q5": "Same languages as Earth",
        "q5_justification": "No language barriers are depicted in the space cities. Characters communicate normally. The space cities are extensions of Earth civilization with no distinct linguistic evolution.",
        "q6": "Manageable but risky",
        "q6_justification": "The space cities provide comfortable living conditions with simulated environments. However, they exist behind gas giants specifically as shelter from dark forest strikes, highlighting underlying risk. The cities require massive engineering but daily life is comfortable.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Space habitation is completely normalized. 64 space cities house large populations. People live, work, and grow old in space. Characters treat space living as ordinary. The space cities are humanity's primary civilization centers.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The space cities are organized by Earth nation/region: Asia I, Europe IV, etc. The naming convention and governance structure indicate that Earth nation-states and regional identities have extended into space, maintaining terrestrial political organization.",
        "q9": "Drama",
        "q9_justification": "The chapter focuses on personal drama: Cheng Xin's life in the space cities, her relationship with AA, Wade's lightspeed ship ambitions and their political resolution, and everyday human experiences in the Bunker World. The tone is contemplative and character-driven.",
        "q10": "Entirely civilian",
        "q10_justification": "The Bunker Era space cities are entirely civilian. People live normal lives. Wade's lightspeed ship research is a civilian enterprise. There is no active military presence or operations described in the space cities.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Bunker World resembles colonial frontier expansion: humanity spreads across the solar system, building settlements behind gas giants. The space cities function like colonial settlements, establishing human civilization in new territories with Earth-derived social structures.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The space cities simulate Earth-like conditions with simulated gravity, weather, and landscapes inside enormous cylinders. The environment is engineered to be livable with manageable differences from Earth, though the underlying reality of living in space behind gas giants is fundamentally artificial."
    },
    {
        "chapter": "Part V",
        "q1": "Total war / constant conflict",
        "q1_justification": "An alien 'Singer' civilization launches a dual-vector foil that collapses the entire solar system from three dimensions to two. This is total annihilation: every planet, space city, and human being in the solar system is destroyed. The dark forest strike represents the ultimate act of cosmic warfare.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "At the chapter's start, humanity occupies 64 space cities across the solar system. The Singer alien perspective reveals a universe of civilizations holding vast territories. Both the extent of human settlement and the implied galactic civilization network represent extensive occupation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Cheng Xin and AA escape in the lightspeed ship Halo, fleeing the collapsing solar system. The Singer operates from an unimaginably distant civilization. The journey in Halo represents effectively unreachable distances as they leave the solar system permanently.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Singer chapter depicts a completely alien civilization with its own social hierarchy (Singer as a 'cleansing' agent), decision-making processes, and worldview. Their casual destruction of star systems reflects a social order radically different from anything human.",
        "q5": "Other / Unsure",
        "q5_justification": "The Singer's internal monologue uses alien concepts and terminology but is rendered in translation. No meaningful cross-species communication occurs. Language dynamics are not a significant element.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The dual-vector foil makes the entire solar system uninhabitable by collapsing it to two dimensions. Space becomes absolutely lethal. Only lightspeed escape offers survival. The environment transitions from managed habitation to total annihilation.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "At the chapter's opening, space habitation remains normalized with 64 cities. The Singer's perspective implies universe-wide civilizations for whom space habitation is ordinary. Even as the solar system collapses, the premise is that space living was the norm.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Singer reveals a universe of multiple civilizations operating as distinct polities. Humanity's solar system government, the Singer's civilization, and implied countless others represent a highly multipolar cosmic political landscape.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is pure existential horror: the casual alien decision to annihilate the solar system, the slow collapse of three-dimensional space into two dimensions consuming everything, and the desperate lightspeed escape of Cheng Xin and AA. The Singer's cold perspective amplifies the horror.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "The chapter's central event is a dark forest strike: a purely military act of cosmic warfare. The Singer is a military agent performing 'cleansing.' The only other space activity is Cheng Xin's desperate military-style escape. All space activity is war-related.",
        "q11": "Other / Unsure",
        "q11_justification": "The dark forest strike and dimensional collapse have no real-world analogy. The scale of destruction (an entire star system flattened to 2D) transcends ocean, air, frontier, or cyberspace metaphors.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The dual-vector foil collapses three-dimensional space into two dimensions. Characters watch planets, stars, and space cities flatten into a plane. Physics itself is weaponized and altered. This is as far from Earth experience as possible."
    },
    {
        "chapter": "Part VI",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The Galaxy Era is post-conflict. Cheng Xin and AA travel peacefully to DX3906. The Blue Space descendant civilization has settled multiple worlds without depicted conflict. Guan Yifan explores with scientific curiosity. The pocket universe subplot involves existential choice but not direct conflict.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Blue Space civilization has settled four or more worlds, including Planet Blue. Humanity has expanded into interstellar space across multiple star systems. This represents extensive territorial occupation at an interstellar scale.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Cheng Xin and AA travel 286.5 light-years to DX3906 in 52 hours of ship time, but centuries pass in the outside universe. The journey creates complete temporal separation from their origin. Guan Yifan's crew has been separated from Earth for centuries.",
        "q4": "Distinct space culture",
        "q4_justification": "The Blue Space descendants have developed a distinct spacefaring culture over centuries of interstellar colonization. They have their own social structures, values, and way of life shaped by deep space existence. Guan Yifan represents this evolved space culture.",
        "q5": "Same languages as Earth",
        "q5_justification": "Cheng Xin communicates easily with Guan Yifan and the Blue Space descendants despite centuries of separation. No language barriers are depicted, suggesting linguistic continuity or easy mutual intelligibility.",
        "q6": "Manageable but risky",
        "q6_justification": "Planet Blue is habitable and Earth-like. Lightspeed travel is achievable but involves extreme time dilation. The physical environment of settled worlds is manageable, though the broader cosmic threats (dark forest, dimensional collapse, universal heat death) pose existential risks.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Interstellar space habitation is fully normalized. The Blue Space civilization spans multiple worlds. Lightspeed travel enables interstellar colonization. People live on different planets across light-years as a matter of course.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple independent human civilizations exist across star systems: the Blue Space descendants with their multi-world civilization, whatever remains of solar system humanity, and implied other scattered groups. Each operates independently.",
        "q9": "Drama",
        "q9_justification": "The chapter is contemplative and philosophical: Cheng Xin's reunion with Guan Yifan, life on Planet Blue, the pocket universe subplot exploring civilization's responsibility to the cosmos, and the bittersweet conclusion about humanity's place in the universe. Character-driven and reflective.",
        "q10": "Entirely civilian",
        "q10_justification": "All depicted activity is civilian: scientific exploration, settlement of Planet Blue, lightspeed travel, philosophical discussions about the universe's fate. No military operations or conflicts occur.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Interstellar colonization closely parallels frontier expansion: settling new worlds, establishing civilizations across vast distances, small communities building new lives far from their origin. The Blue Space civilization's multi-world spread resembles colonial expansion.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Planet Blue is described as Earth-like and habitable. While lightspeed travel involves extreme time dilation and the broader cosmos operates on alien physics, the actual living environments on settled worlds are manageable adaptations from Earth conditions."
    },
]

country = 'China'
book_title = "Death's End"
csv_path = 'data/results/China_Death_s_End.csv'
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

print('Done.')
