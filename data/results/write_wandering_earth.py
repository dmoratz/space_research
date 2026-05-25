import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 1 - The Reining Age",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Spaceship Faction and Earth Faction are in ongoing rivalry, with physical fights among children, Tung's father imprisoned for insurgency against the Unity Government, and the factions having fought for almost 400 years. The conflict is ideological and political but not yet open war.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Earth itself is being moved through space as a permanent, governed settlement. The entire planet is humanity's vessel, with 12,000 Earth Engines and a Unity Government administering the population. The Moon is pushed away to enable Earth's acceleration.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The journey to Proxima Centauri is 4.3 light-years, projected to take 2,500 years and 100 generations. The exodus is explicitly one-way and multigenerational, with the narrator noting his bones will be dust long before arrival.",
        "q4": "Distinct space culture",
        "q4_justification": "Society has fundamentally changed: children fear the Sun and have never seen night or stars, education is restructured, the Unity Government controls all, and history before the Reining Age is called the 'Pre-Solar Age' and treated as mythical paradise. The cultural framework is entirely shaped by the exodus.",
        "q5": "Same languages as Earth",
        "q5_justification": "No language differences are mentioned. The narrator, teachers, and children all communicate normally. Place names (Shijiazhuang, Taihang Mountains) and concepts are described in standard language without any linguistic adaptation.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Surface temperatures reach 160-180 degrees from Earth Engine heat, requiring thermal suits for any outdoor activity. Boiling rain scalds exposed skin (grandfather's skin burned off). Tidal floods from engine acceleration swallowed two-thirds of Northern Hemisphere cities. Massive planetary engineering is required for survival.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "All of humanity lives on Earth as it travels through space. The entire planet is a vessel; space habitation is not a choice but the universal human condition. Children are born into this reality and consider it normal and natural.",
        "q8": "Single unified authority",
        "q8_justification": "The Unity Government is the sole governing authority for all of humanity, controlling the Earth Engines, education, and the exodus plan. Opposition (the Spaceship Faction) exists but is suppressed, with members imprisoned for insurgency.",
        "q9": "Drama",
        "q9_justification": "A first-person coming-of-age narrative following the narrator from birth through childhood, including an emotional school trip, encounters with fear and wonder, and the departure from the solar system. The tone is reflective and elegiac, anchored in personal experience.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter depicts civilian life: school, family, a class trip. The Unity Government maintains order and suppresses insurgency (Tung's father imprisoned), but the focus is on education, daily life, and the civilian experience of the exodus.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The chapter is pervaded by ocean/voyage metaphors: the school trip involves an actual ship crossing the Pacific, Proxima Centauri is described as a 'heavenly lighthouse on the distant shores of the wild sea of the night,' and Earth's journey is framed as a voyage through a 'sea of woes.'",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Surface temperatures of 160-180 degrees require thermal suits, rain is boiled by plasma beams, tidal floods destroy cities, the Earth's rotation has been halted eliminating day/night cycles, and 12,000 engine towers taller than Everest dominate the landscape. The physical environment is fundamentally transformed but still recognizably planetary."
    },
    {
        "chapter": "Chapter 2 - The Exodial Age",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The Spaceship vs Earth Faction rivalry continues as background tension but produces no open conflict in this chapter. The main challenges are natural: asteroid belt passage, volcanic eruptions, and Jupiter's gravitational tides. The narrator's father serves in a military fleet but its role is defensive against natural hazards.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Humanity lives in permanent subterranean cities, each housing over a million inhabitants, spread across the continents. The Unity Government administers these cities with organized evacuation procedures, civil affairs offices, and Exigency Laws. Earth remains a governed, permanent settlement.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Earth completes 15 orbits around the Sun before achieving escape velocity via Jupiter slingshot. The narrator reflects that even if they escape, they are on 'the first rung of an unfathomably tall ladder' with bones turning to dust long before arrival. The journey is explicitly multigenerational.",
        "q4": "Distinct space culture",
        "q4_justification": "Religion has vanished, love is treated as trivial distraction, procreation requires a lottery, education focuses exclusively on science and engineering, genetic memory engineering is standard, and Aphelion Day replaces traditional holidays. The narrator notes people of the Pre-Solar Age are incomprehensible to them.",
        "q5": "Same languages as Earth",
        "q5_justification": "The narrator marries a Japanese woman (Kayoko) with no language barrier mentioned. Civil affairs, military, and social interactions all occur without any linguistic adaptation or translation technology. Standard place names and terminology persist.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Thermal suits with nuclear batteries are required on the surface. Volcanic eruptions destroy subterranean cities (18,000 die in magma flooding). Asteroid bombardment produces 300-foot waves and meteor strikes. The ocean freezes solid at aphelion. Subterranean living a third of a mile underground is mandatory for survival.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "All of humanity lives on Earth as it orbits the Sun in increasingly elliptical paths before escaping via Jupiter slingshot. A space fleet operates in Low Earth Orbit. Underground cities are the universal human habitat. Space travel is the entire species' condition.",
        "q8": "Single unified authority",
        "q8_justification": "The Unity Government controls all aspects of life: procreation rights via lottery, Exigency Laws governing evacuations (age-based priority), military space fleet, civil affairs, and Olympic Games revival. No competing political entities exist.",
        "q9": "Drama",
        "q9_justification": "A life-spanning personal narrative encompassing the narrator's parents' indifference to love, marriage to Kayoko during a sled race, father's death in asteroid defense, mother's death in magma flooding, and the birth of a son during the Jupiter encounter. Survival set-pieces punctuate an essentially dramatic arc.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The space fleet actively defends Earth from asteroids using anti-matter bombs, and the narrator's father dies in military service. Simultaneously, civilian life continues with schools, Olympics, marriages, and subterranean city governance. Both domains are prominently depicted.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The sled race crosses a frozen Pacific Ocean. The narrator feels like 'a deep sea diver finally seeing the light of the surface.' The asteroid bombardment produces 300-foot ocean waves. Jupiter's encounter causes gravitational tides. Earth's journey is consistently framed as an ocean voyage.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Jupiter fills the entire sky during the flyby, its Great Red Spot dominating the heavens. The ocean freezes and thaws cyclically. Anti-matter bomb flashes blind from space. Meteors bombard the surface. Impact dust blocks the Sun for years. The atmosphere and physical environment are utterly unlike any Earth experience."
    },
    {
        "chapter": "Chapter 3 - Rebellion",
        "q1": "Total war / constant conflict",
        "q1_justification": "A global armed rebellion erupts against the Unity Government. The Americas, Africa, Oceania, and Antarctica fall to rebels. The government's defensive lines in Asia collapse after mass defections. The chapter depicts full-scale civil war culminating in the surrender and mass execution of 5,000 government loyalists.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Earth continues as a permanent governed settlement, with subterranean cities, an Earth Bridge control center the size of a city, and organized military operations across continents. Even during civil war, the infrastructure of governance persists.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Earth has escaped the solar system via Jupiter slingshot and is heading into deep space toward Proxima Centauri. The journey of 2,500 years continues. The Sun is now barely the size of a baseball when viewed through telescopes.",
        "q4": "Distinct space culture",
        "q4_justification": "Society is defined by factional identity (Earth Faction vs rebels), execution by freezing on the surface, the Earth Bridge as sacred political center, and collective singing of 'My Sun.' The culture has no Earth precedent—it is entirely shaped by the exodus and the existential question of the Sun's fate.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters communicate in standard language without any linguistic barriers or adaptations. Rally speeches, military communications, and personal conversations show no language evolution or differentiation.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Surface temperatures are more than 150 degrees below freezing. Thermal suits with nuclear batteries are essential—removing the battery is used as a method of execution. The Earth's surface is described as Mars-like desolation with frozen salt marshes and ruined cities.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "All of humanity lives on Earth as it travels through interstellar space. The entire species inhabits the planet-vessel. Space habitation is the universal, unquestioned human condition.",
        "q8": "Single unified authority",
        "q8_justification": "The Unity Government is the single authority, though it is overthrown by rebellion during the chapter. The rebels aim to seize control of the same centralized Earth Engine control system, not to create separate polities. The political structure remains a single authority—only its leadership changes.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by global civil war: armed rebellion, continental-scale campaigns, defensive lines collapsing, field army defections, surrender of the government, and mass execution. The narrator serves as a military major. The helium flash at the end vindicates the executed loyalists.",
        "q10": "Mostly military",
        "q10_justification": "The chapter centers on military operations: rebel forces, government armies, laser fire, field hospitals, defections, and siege of the control center. The narrator is a military officer. Civilian life is barely depicted; even Kayoko joins the rebel army and dies in combat.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The rebellion evokes frontier/colonial conflict: vast territorial campaigns across continents, armed citizen militias, ideological factions fighting over the direction of civilization, and the question of whether to press forward into the unknown or return 'home.' The framing resembles colonial-era disputes over settlement direction.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The surface is Mars-like desolation at -150 degrees. The helium flash vaporizes Mercury, Venus, and Mars, transforming the Sun into a red giant visible in the sky. The frozen ocean serves as an execution ground. Mountains have been consumed as fuel. The physical environment is fundamentally alien to any Earth experience."
    },
    {
        "chapter": "Chapter 4 - The Wandering Age",
        "q1": "No contestation",
        "q1_justification": "The brief epilogue depicts no conflict whatsoever. The narrator reflects peacefully on the journey, imagines future arrival at Proxima Centauri, and recalls loved ones. The rebellion is over and the helium flash has settled all disputes.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Humanity continues living in subterranean cities on Earth as it travels through interstellar space. The narrator visits the surface with family, indicating continued organized habitation. The 2,400-year journey plan implies sustained governance.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Earth has passed Pluto's orbit and left the solar system entirely. The remaining journey of 2,400 years includes 500 years of acceleration, 1,300 years of cruising at 0.5% lightspeed, and 500 years of deceleration. The destination is generations beyond the narrator's lifetime.",
        "q4": "Distinct space culture",
        "q4_justification": "The culture is defined by interstellar wandering: songs about future dawn at Proxima Centauri, an elderly narrator who has never known anything but the exodus, and a society whose entire identity is shaped by the multigenerational journey through space.",
        "q5": "Same languages as Earth",
        "q5_justification": "The narrator's daughter-in-law is described as blond-haired and blue-eyed (implying different ethnic background) with no language barrier mentioned. The song lyrics are in standard language. No linguistic evolution or differentiation is depicted.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The atmosphere has frozen solid, forming crystals of solid oxygen and nitrogen on the surface. There is no air. The surface is completely uninhabitable without sealed suits and underground habitation. The Earth Engines must run continuously for 500 years.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "All of humanity lives on Earth traveling through interstellar space beyond the solar system. The narrator's grandchildren are born into this condition. Space habitation is the only human experience.",
        "q8": "Single unified authority",
        "q8_justification": "The chapter implies continued unified governance managing the Earth Engines and the 2,400-year journey plan. No competing authorities or political fragmentation is mentioned. The rebellion from Chapter 3 has been resolved.",
        "q9": "Drama",
        "q9_justification": "A brief, elegiac epilogue in which the aging narrator reflects on the journey, visits the frozen surface with his son and pregnant daughter-in-law, and imagines the arrival at Proxima Centauri with a vision of Kayoko running toward him across green fields. The tone is deeply emotional and contemplative.",
        "q10": "Entirely civilian",
        "q10_justification": "No military activity or presence is depicted. The chapter focuses on family (son, daughter-in-law, future grandchild), personal reflection, and a song about the future. The tone is entirely peaceful and civilian.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Earth's journey continues to be framed as a long voyage, with the song referencing dawn and arrival at distant shores. The chapter title 'The Wandering Age' evokes maritime wandering. The frozen ocean surface forms an alien landscape that the narrator traverses.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The atmosphere has frozen into solid oxygen and nitrogen crystals forming translucent hills on the surface. There is no air. The frozen ocean creates an alien landscape. Stars are dazzlingly bright without atmospheric diffraction. The physical environment is fundamentally unlike any Earth experience."
    }
]

country = 'China'
book_title = 'The Wandering Earth'
csv_path = 'data/results/China_The_Wandering_Earth.csv'

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

print('Done.')
