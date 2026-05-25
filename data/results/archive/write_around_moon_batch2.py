import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 8",
        "q1": "No contestation",
        "q1_justification": "There is no conflict or competition in this chapter. The travelers deal with an oxygen overdose accident caused by Michel's blunder, then experience weightlessness at the neutral point between Earth and Moon. The mood is scientific curiosity and camaraderie.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The three travelers are on a temporary mission inside a projectile heading toward the Moon. Michel jokes about acclimating hens to the Moon, but there is no actual settlement or territory held in space.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The chapter title references 195,285 miles from Earth, the neutral gravitational point between Earth and Moon. This is a relatively short Earth-to-Moon journey taking only days.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers carry Earth culture entirely with them, joking about French entrepreneurship with oxygen rooms, discussing gravity in familiar Earth terms, and referencing European nations. No distinct space culture exists.",
        "q5": "Same languages as Earth",
        "q5_justification": "The three travelers speak their Earth languages naturally. Michel speaks as a Frenchman, and all conversation is conducted without any linguistic adaptation for space.",
        "q6": "Manageable but risky",
        "q6_justification": "The oxygen overdose nearly killed the travelers, showing real danger from their life support systems. However, Nicholl remedied the situation in time. They also face the uncertainty of whether they will reach the Moon or be stranded at the neutral point.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men are traveling through space in this projectile. This is a unique, first-of-its-kind expedition with no other humans in space.",
        "q8": "Other / Unsure",
        "q8_justification": "There is no political order in space depicted in this chapter. The journey is a private scientific expedition by the Gun Club, not a state-controlled venture establishing governance.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter focuses on the adventure of crossing the neutral gravitational point, experiencing weightlessness, and the excitement of potentially reaching the Moon. Michel's enthusiasm and the scientific wonder dominate the tone.",
        "q10": "Entirely civilian",
        "q10_justification": "The expedition is conducted by civilian scientists and adventurers from the Gun Club. There is no military presence or objectives in this chapter.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Michel compares crossing the neutral point to sailors crossing the equator and proposes toasts. The journey to the Moon is framed as frontier exploration, with Michel planning to release hens on the Moon like colonists bringing livestock to a new land.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The travelers experience complete weightlessness at the neutral point, floating in the air with no sense of balance. The oxygen system malfunction shows how the artificial environment constantly challenges them. Barbicane discusses how gravity on the Moon is only one-sixth of Earth's."
    },
    {
        "chapter": "Chapter 9",
        "q1": "No contestation",
        "q1_justification": "There is no conflict between parties in this chapter. The travelers work together to prepare for a potential lunar landing and discuss what caused their course deviation. The only antagonist is the meteor that deflected them.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The travelers are attempting to land on the Moon as visitors. They prepare crash-dampening measures and retro-rockets, indicating a temporary mission rather than settlement.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The projectile is now less than 5,000 miles from the Moon, nearing the end of an Earth-to-Moon journey of roughly 210,000 miles that has taken only days.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers reference Earth institutions like the Cambridge Observatory, recall the Tampa rally, and discuss technical preparations using entirely Earth-based knowledge and social norms.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in the travelers' native Earth languages with no adaptation needed for space communication.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The chapter focuses heavily on survival preparations: reinstalling crash buffers, preparing retro-rockets, and worrying about a fall of 20,740 miles onto the lunar surface. They cannot use their water supply as springs because it may be needed for survival on the Moon.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three people are in space. This remains a singular expedition with no other humans beyond Earth.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structures exist in space. The journey is a private venture, and no governance is discussed or implied.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is driven by the drama of going off course and the adventurous spirit of the travelers as they prepare for an uncertain arrival. Barbicane deduces that a meteor deflected them, adding a sense of cosmic adventure.",
        "q10": "Entirely civilian",
        "q10_justification": "The expedition remains entirely civilian. The retro-rockets and preparations are scientific and practical, not military in nature.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The projectile is compared to a coach, and the travelers discuss their trajectory as explorers venturing into unknown territory. The discovery that a meteor deflected their course evokes the unpredictability of frontier exploration.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The travelers face a potential uncontrolled fall of 20,740 miles onto the Moon's surface with only one-sixth Earth gravity. They must install crash buffers and retro-rockets to survive. The projectile refuses to swing around properly due to competing gravitational forces."
    },
    {
        "chapter": "Chapter 10",
        "q1": "No contestation",
        "q1_justification": "There is no conflict in this chapter. The travelers observe the Moon through spyglasses and discuss the history of lunar cartography. The tone is purely observational and scholarly.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers are now unable to reach the Moon's surface, having been deflected off course. They can only observe from roughly 500 miles away, unable to land or establish any presence.",
        "q3": "Short interplanetary journey",
        "q3_justification": "They are about 500 miles from the Moon after a journey from Earth that took only days. This remains a short Earth-to-Moon trip.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The chapter is a survey of European astronomical history, referencing Galileo, Hevelius, Riccioli, Cassini, and others. The travelers bring entirely Earth-based scholarly culture with them.",
        "q5": "Same languages as Earth",
        "q5_justification": "All conversation and references to lunar maps use Earth languages. The naming conventions discussed are Latin and European in origin.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The travelers face the prospect of running out of air while wandering through infinite emptiness. Their shell is described as wandering at random with limited resources, and they acknowledge they could die of asphyxiation within days.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men are in space, representing all of humanity in lunar observation. The text states they stand for all mankind past and present.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order in space is depicted. The chapter focuses entirely on scientific observation and the history of lunar mapping.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is devoted to exploration and scientific observation of the Moon, cataloging its features and reviewing the history of lunar cartography. The travelers are moonwatchers conducting research.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is entirely focused on civilian scientific observation. All references are to astronomers and scholars, not military figures.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The Moon's features are described using nautical terminology: seas, bays, shorelines, and harbors. The text explicitly compares lunar navigation to dangerous seafaring and mentions lunar seamen and hydrographers.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The Moon is described as an egg-shaped body with features visible through spyglasses. Its surface has mountains, plains, and so-called seas, presenting a world somewhat different from Earth but with recognizable geographic features that can be mapped and studied."
    },
    {
        "chapter": "Chapter 11",
        "q1": "No contestation",
        "q1_justification": "There is no conflict in this chapter. The travelers examine and discuss the Moon's geographic features, seas, and naming conventions in an academic manner. Michel offers whimsical interpretations while Barbicane and Nicholl take measurements.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers are orbiting past the Moon unable to land. The Moon's surface is described as dry and dead, with seas that are actually plains rather than bodies of water, suggesting inhospitability.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The travelers remain in close proximity to the Moon after their short Earth-to-Moon journey of several days.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers interpret the Moon entirely through Earth cultural lenses. Michel compares lunar seas to a French literary parlor game, while Barbicane and Nicholl measure everything using Earth geographic conventions.",
        "q5": "Same languages as Earth",
        "q5_justification": "All lunar features are named in Latin or European languages. The travelers converse in their Earth languages without any linguistic adaptation.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The Moon's surface is described as blistered, cracked, and full of craters. The so-called seas are dry plains, and the landscape is characterized by volcanic activity and extreme geological upheaval, suggesting a hostile environment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three travelers observe the Moon. No other humans exist in space.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structures in space are discussed. The chapter is purely geographic and cartographic in nature.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is dedicated to geographic exploration of the Moon's surface, cataloging seas, continents, and measurements. Michel adds literary adventure with his fanciful interpretations of lunar place names.",
        "q10": "Entirely civilian",
        "q10_justification": "All discussion is civilian and scientific, focused on geography and measurement. No military themes appear.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The Moon's features are extensively described using ocean terminology: seas, bays, coastlines, islands, and shorelines. The Greek Isles comparison and references to navigating lunar waters reinforce the naval characterization.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The Moon has recognizable geographic features like continents, mountains, and plains, but the seas are dry, the surface is volcanic and cratered, and the landscape differs markedly from Earth. It is described as older than Earth's surface but less eroded."
    },
    {
        "chapter": "Chapter 12",
        "q1": "No contestation",
        "q1_justification": "There is no conflict in this chapter. The travelers observe the Moon's mountains and craters in detail, discussing geological formations like Copernicus and Eratosthenes in a purely scientific manner.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers orbit 870 miles above the Moon's surface, unable to land. They study the terrain but cannot establish any presence. Kepler's theory about moonpeople digging craters for shelter is discussed as speculation.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The projectile is 870 miles from the Moon, continuing its orbit after a journey from Earth lasting only days.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Barbicane declares they should proceed as if at the Cambridge Observatory. All analysis uses Earth scientific frameworks, and the travelers reference Earth mountains like the Pyrenees for comparison.",
        "q5": "Same languages as Earth",
        "q5_justification": "All conversation uses Earth languages. Lunar features are named after European scientists like Copernicus, Gay-Lussac, and Eratosthenes.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The Moon's surface is described as volcanic, cratered, and barren. Copernicus is an extinct volcano surrounded by lava fields, and the terrain consists of ultra-steep walls and wild-looking plains. The travelers cannot land safely.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men orbit the Moon, conducting observations that no earthbound telescope could match. Barbicane acknowledges they may never see Earth again.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order in space is discussed. The chapter is focused entirely on lunar geology and mountain classification.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is devoted to scientific exploration of the Moon's surface features, with Barbicane solemnly declaring their observations should benefit humanity. They study craters, mountain chains, and bright rays with great enthusiasm.",
        "q10": "Entirely civilian",
        "q10_justification": "The expedition is framed as pure scientific research. Barbicane compares their projectile to a Cambridge Observatory workroom transferred into space.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The travelers survey uncharted terrain from above like frontier explorers mapping new territory. Barbicane's speech about benefiting fellow mortals and the systematic cataloging of surface features evoke colonial-era surveying expeditions.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The Moon's surface features are recognizable as mountains and craters but differ significantly from Earth. Crater interiors go below ground level unlike Earth craters, the terrain is entirely volcanic, and there are mysterious bright rays whose nature remains unknown."
    },
    {
        "chapter": "Chapter 13",
        "q1": "No contestation",
        "q1_justification": "There is no conflict in this chapter. The travelers observe the Moon's surface features including rills, pigments, and the crater Plato, all in a spirit of scientific inquiry.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers orbit as close as 370 miles but cannot land. Barbicane searches for signs of life but finds only the mineral kingdom represented. No human beings, animals, or trees are visible anywhere on the surface.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The projectile orbits increasingly close to the Moon, reaching within 30 miles of the north pole by chapter's end. The overall Earth-to-Moon journey has taken only days.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers interpret everything through Earth frameworks. Michel sees tilled fields, Barbicane references Earth geology, and all comparisons are to Earth features like the Bay of Bengal or New Brunswick.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in Earth languages. No distinct space language or communication technology is mentioned.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Moon is depicted as completely lifeless with no atmosphere, no twilight, extreme temperature contrasts, and utter darkness where sunlight does not reach. Night follows day instantaneously. The chapter explicitly states only the mineral kingdom exists on the visible surface.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Three travelers alone observe the Moon, and Barbicane notes that even if moonpeople existed, they could not be seen from more than 4.5 miles away.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structures are discussed. The chapter focuses on physical observation of the Moon's barren surface.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is pure exploration as the travelers observe lunar rills, pigments, craters, and the stark black-and-white landscape. They reach their closest approach to the Moon at the north pole before plunging into darkness.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian scientific observation. Michel jokes about farming and fortifications, but these are whimsical comparisons, not military themes.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The travelers survey the Moon like frontier explorers, searching for signs of habitation, vegetation, and water. Michel looks for inhabitants while Barbicane systematically catalogs the barren landscape, evoking explorers surveying an empty frontier.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The Moon has no atmosphere, no twilight, no diffuse light, and extreme temperature contrasts. Night follows day instantaneously. The landscape is only black and white with no chiaroscuro. The chapter states a landscape painter could not render it as it lacks all softening effects familiar on Earth."
    },
    {
        "chapter": "Chapter 14",
        "q1": "No contestation",
        "q1_justification": "There is no conflict between parties. The travelers endure the lunar night together, debating the scientific properties of the Moon's visible versus invisible sides and conducting temperature experiments.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The projectile is trapped orbiting in the Moon's shadow, unable to land. The travelers discuss the Moon's invisible side as potentially habitable but cannot reach it. They are powerless passengers.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The travelers are within roughly 30 miles of the Moon's surface, having completed their short Earth-to-Moon journey in days. However, they are now trapped orbiting.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers discuss Earth scientists Fourier and Pouillet, reference European and polar explorers, and Michel mimics Barbicane's lecturing style. Their culture is entirely Earth-derived.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in the travelers' native Earth languages. Michel and Barbicane banter in their customary manner.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The temperature outside reads -220 degrees Fahrenheit. Ice coats the portholes, and the travelers face freezing to death without gas heating. The lunar night lasts 354.5 hours of complete darkness, and the cold of interplanetary space is lethal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men are in space, trapped in their projectile in the lunar shadow. No other humans are present.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order in space is discussed. The chapter is focused on the physics of the lunar night and survival in extreme cold.",
        "q9": "Adventure / exploration",
        "q9_justification": "Despite the dire cold, the travelers conduct scientific experiments, measuring interplanetary temperature and discussing the properties of the Moon's two hemispheres. The spirit of exploration persists even in darkness.",
        "q10": "Entirely civilian",
        "q10_justification": "All activities are civilian scientific experiments and observations. No military themes appear.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The travelers endure extreme conditions reminiscent of polar exploration. Michel compares their situation to Indians on the Pampas and Eskimos at the pole. The discussion of the Moon's visible side as pleasant to live on evokes colonial assessments of new territories.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Interplanetary space registers -220 degrees Fahrenheit. The lunar night is 354.5 hours of absolute darkness with no twilight or diffuse light. The Moon's conical shadow plunges them into pitch blackness instantaneously. These conditions are fundamentally unlike anything on Earth."
    },
    {
        "chapter": "Chapter 15",
        "q1": "No contestation",
        "q1_justification": "There is no conflict between parties. The travelers discuss mathematical curves, observe a lunar volcano, and narrowly survive a meteor explosion. All interactions are cooperative.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The travelers are unable to reach the Moon and are being carried off along a parabolic or hyperbolic curve into infinite space. They cannot land or establish any presence.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "The travelers now face being carried off into infinity along a parabola or hyperbola, never to return to Earth. What began as a short journey has become a potentially endless one with total separation from Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The travelers discuss Earth mathematics, reference Jupiter's and Saturn's satellites, and Michel jokes about the Boulevard des Italiens. Their cultural frame is entirely Earth-based.",
        "q5": "Same languages as Earth",
        "q5_justification": "All conversation is in the travelers' native Earth languages. Mathematical and scientific terms are standard Earth terminology.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The travelers face death from lack of air, hunger, thirst, or cold. The temperature is extremely low, ice forms on portholes, and they must carefully ration gas for heat. A meteor nearly destroys them, and they are on a course into infinite space.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three men are in space, now potentially lost forever on a trajectory into infinite space.",
        "q8": "Other / Unsure",
        "q8_justification": "No political structures in space are discussed. The chapter focuses on the physics of orbital trajectories and survival.",
        "q9": "Adventure / exploration",
        "q9_justification": "Despite facing potential death, the travelers observe a lunar volcano on the invisible side and glimpse the Moon's hidden face during a meteor explosion. The chapter balances mortal peril with the thrill of discovery.",
        "q10": "Entirely civilian",
        "q10_justification": "The expedition remains entirely civilian. The discussions are scientific, covering orbital mechanics, volcanism, and the possibility of lunar life.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The travelers are compared to sailors who cannot steer their vessel, riding out the unknown like frontier explorers. The brief glimpse of the Moon's hidden side with possible seas, forests, and atmosphere evokes the discovery of new continents.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The travelers face -220 degree temperatures, absolute vacuum, a meteor burning in airless space, and the prospect of infinite drift along a hyperbolic curve. They briefly glimpse the Moon's hidden side showing seas and dark forest-like forms, but the environment remains lethal and fundamentally alien."
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

print('Done with batch 2.')
