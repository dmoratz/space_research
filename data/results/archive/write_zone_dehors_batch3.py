import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter XVI",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Volte resistance plans to contact the double agent Kohtp to save Capt from the Cube, while the government employs advanced psychological torture techniques against Capt in his cell, showing intense strategic struggle between the state and the resistance.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon is a fully governed permanent settlement orbiting Saturn with established urban infrastructure, surveillance systems, streets, and a functioning government that controls territory through the Clastre ranking system.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Cerclon orbits Saturn, and Capt recalls the childhood trauma of arriving on the station, suggesting a major one-time migration from Earth. The chapter references Earth as a distant origin point with documentary footage of Cerclon viewed from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "Cerclon has developed its own unique social order with the Clastre ranking system, the Volte resistance movement, surveillance infrastructure like the Terminor, and distinct cultural practices such as clameurs and coded communications that have no Earth equivalent.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak French with distinctive slang and neologisms like 'plosses,' 'collex,' 'radzone,' 'murécrans,' and 'brax,' but the underlying language remains recognizably French with space-specific vocabulary layered on top.",
        "q6": "Manageable but risky",
        "q6_justification": "Life on Cerclon requires managed oxygen supply and protection from ammonia rafales, as citizens must visit cabines de réox when the air quality drops. The satellite Vigital 4 monitors the radzone, suggesting environmental hazards exist but are managed through infrastructure.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Cerclon is home to millions of permanent residents with a full urban society including shops, boulevards, parks, media, and government. Living in space is completely ordinary for the population, many of whom were born there.",
        "q8": "Single unified authority",
        "q8_justification": "Cerclon is governed by a single President and his government apparatus including ministers like P, with a unified surveillance and ranking system (the Clastre) controlling all citizens. The Volte is an underground resistance, not a recognized polity.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on political maneuvering: the resistance strategizes to contact a double agent, the President instructs his psychologist on how to psychologically manage Capt as a political prisoner, and Boule meets Kohtp to convince him to publicly denounce the government.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The setting is primarily civilian with urban life, surveillance cameras, shops, and civilian infrastructure. Police and security forces exist but the space station is not a military installation; the conflict is political resistance versus a civilian government's security apparatus.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space on Cerclon is characterized through surveillance networks, the Terminor tracking system, nanocameras implanted on optic nerves, satellite monitoring (Vigital 4), and panoptic control systems rather than through naval, aerial, or frontier metaphors.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The environment requires managed oxygen supply, protection from ammonia rafales, and engineered atmospheric systems. The radzone outside Cerclon's circles is hostile, and the station's artificial environment with halogene lighting and recycled air requires ongoing adaptation."
    },
    {
        "chapter": "Chapter XVII",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Capt's trial in the geodome is a massive political confrontation broadcast to four billion viewers across the solar system. The Volte launches coordinated 'cobra' attacks during the trial, spectators physically clash with security, and the vote on Capt's incubation ends at a razor-thin 50.7% for death.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The trial takes place in a geodome holding 65,000 spectators with advanced gravimetric technology. References to lunar bases, Jupiter modules, Venus orbit, and Uranus pioneers confirm multiple permanent governed settlements across the solar system.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The broadcast reaches viewers on Earth, lunar bases, Starlight, Jupiter modules, and Uranus, indicating humanity has spread far across the solar system. An African viewer's question highlights the vast distance and separation between Earth's problems and Cerclon's society.",
        "q4": "Distinct space culture",
        "q4_justification": "Cerclon has developed a unique culture with its own political philosophy (the Volte), entertainment systems (virtue), the Clastre ranking system, and a society where citizens vote on life-or-death sentences via remote control. Capt's speeches articulate a vision of 'extraterrestrial' humanity fundamentally different from Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "All dialogue is in French with space-specific slang and neologisms like 'murécrans,' 'radzoniens,' 'cyborx,' and 'Arachnas 08.' The African questioner communicates directly with Capt without translation, confirming shared language with local variations.",
        "q6": "Manageable but risky",
        "q6_justification": "The geodome's gravimetric systems pose real physical danger as Capt falls from his platform and spectators risk ejecting into void. The environment is technologically managed but carries inherent risks, and the Arachnas chemical capsule implanted in Capt shows the vulnerability of bodies to technological manipulation.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Four billion viewers watch from across the solar system including Earth, lunar bases, Starlight, Jupiter, Venus orbit, and Uranus. Space habitation is completely normalized with permanent populations across multiple worlds and stations.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The broadcast reaches distinct political entities: Cerclon (governed by the President), Starlight, bases on various planets, and Earth nations. The President of Starlight comments on Cerclon's decisions, and Admiral Sperkov speaks from the Urania, suggesting multiple independent space polities.",
        "q9": "Political / diplomatic",
        "q9_justification": "The entire chapter is a televised political trial where Capt delivers philosophical speeches about freedom, norms, and revolution while the government orchestrates the spectacle for political advantage. The President strategizes behind the scenes about image management and crowd manipulation.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The trial is a civilian-political event broadcast as entertainment. Security agents manage the geodome, but the setting is fundamentally civilian: media companies organize the event, citizens vote, and the conflict is political rather than military.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The trial unfolds in a networked media spectacle broadcast across the solar system, with real-time voting via remote control, chemical capsules controlling Capt's emotions via neurotransmitters, and the President monitoring 'impaffect' matrices through expert systems.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The geodome uses modified gravity that allows spectators to float and requires constant gravitational field management. Capt stands on a tiny disk in zero-gravity suspension, and engineers fear gravitational collapse, showing the physical environment requires continuous technological adaptation."
    },
    {
        "chapter": "Chapter XVIII",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chapter depicts all-out confrontation: the Volte launches a multi-front assault on the astroport to prevent Capt's execution, including attempts to breach a plasma wall, aerial combat with stolen vessels, an escalade of the Cube, and violent clashes with police resulting in multiple deaths and casualties.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon is a fully developed permanent settlement with industrial entrepots, an astroport with hundreds of vessels, government buildings, and infrastructure supporting millions. The Cube itself is a massive permanent structure of compacted industrial waste hundreds of meters tall.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The chapter references Cerclon III and the transfer of Slift via carcéronef between Cerclons, indicating a system of settlements around Saturn far from Earth. The perihelion of Saturn causes magnetic storms affecting operations, emphasizing the alien orbital environment.",
        "q4": "Distinct space culture",
        "q4_justification": "The Cube execution method, the Clastre system, the radzone culture, and the Volte resistance represent a unique society with no Earth parallel. The chapter describes Voltés from Cerclon II and III with distinct brassards, tourists arriving via Cosporteurs, and vagabonds of space.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate in French with heavy slang: Slift's distinctive speech patterns, military jargon like 'carcéronef,' technical terms like 'plasmur' and 'bornes à plasma,' and Volte-specific codes. The language is recognizably French with extensive space-culture vocabulary.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The Cube (Zhext) is described in horrifying detail: temperatures up to 300°C, lethal radiation, acid infiltrations, magnetic fields crushing materials, oxygen deprivation, and complete darkness. Even trained vérificateurs in full suits risk death beyond 50 meters, and mutant rats survive only thirty minutes.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter describes a massive urban society with three hundred thousand people gathering on the esplanade, tourists from nearby satellites, volunteers from Cerclons II and III, and an established industrial zone. Space habitation is completely normal for this civilization.",
        "q8": "Single unified authority",
        "q8_justification": "The government controls the execution, the police, the astroport, and the military response from a centralized command. The President grants or denies grace, ministers coordinate operations, and P commands the security forces. Cerclon operates under a single hierarchical authority.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is dominated by survival horror as Capt faces imminent execution in the Cube, described in terrifying scientific detail. Simultaneously, the Volte mounts a desperate multi-pronged assault against overwhelming force, with crashes, deaths, and the emotional agony of watching Capt lowered into the pit.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter features direct military-style confrontation: police escadres with optireurs, helicopter gunships, plasma wall barriers, stolen vessels in aerial combat, and armed militia. The astroport is militarized with copters firing paralysing rounds, while civilians form the resistance attacking with industrial equipment.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Cube is described as an unexplored frontier within the station itself, with urban legends, unknown interior conditions, and the sense of venturing into uncharted hostile territory. The vérificateurs are explorers penetrating dangerous depths, and the chapter evokes frontier survival against a hostile wilderness of industrial waste.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Cube presents radically hostile physical conditions: extreme temperatures, lethal radiation, crushing magnetic fields, acid, and zero visibility. The magnetic storms from Saturn's perihelion affect all operations, and even outside the Cube, the environment requires managed oxygen, plasma barriers, and gravimetric technology."
    },
    {
        "chapter": "Chapter XIX",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Capt fights for survival inside the Cube while outside, Kamio observes the futile multi-front battle. Slift escapes capture in a dramatic carcéronef hijacking, evading pursuit through Saturn's atmosphere. The government deploys massive force while the resistance suffers crashes and deaths.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon remains a fully governed settlement, while the chapter reveals multiple Cerclons (Cerclon III) as separate governed territories. Slift's escape through Saturn's stratosphere and landing in the Dehors demonstrates the extent of territorial infrastructure around the planet.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The setting is deep in the Saturn system with Slift navigating through Saturn's high atmosphere to evade radar. References to the vast distances between Cerclons and the isolation of the Dehors reinforce the enormous separation from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The Cube experience reveals a culture that has mythologized its own industrial waste into a living entity with legends of Zorlk, golems, cosmic portals, and the belief that the Zhext is Cerclon's unconscious. Capt's hallucinatory journey through folded space-time zones is uniquely Cerclonnian.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Slift's distinctive argot continues with phrases like 'gars,' 'plot,' 'percute,' and 'putain de chaos terrifiant.' Technical and cultural neologisms abound but the base language remains French with space-cultural slang layered throughout.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Capt endures near-constant lethal threats inside the Cube: freezing ice, volcanic heat eruptions, acid pools, radiation exposure, oxygen deprivation, crushing compression waves, and complete darkness. He survives only through desperate improvisation, climbing with magnetized shoes and navigating by sound and touch.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter references multiple populated Cerclons, police operations across Saturn's orbital space, and an established civilization generating massive quantities of industrial waste. Space habitation is entirely normalized for this society.",
        "q8": "Single unified authority",
        "q8_justification": "The government coordinates police operations, carcéronef transfers, and military pursuit across multiple Cerclons from centralized command. P issues orders to lieutenants about Slift's transfer, demonstrating hierarchical single-authority governance over the Saturn system.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is pure survival horror as Capt navigates the nightmarish interior of the Cube: hallucinations, electroluminescent auroras, cryogenized corpses, volcanic eruptions of waste, near-drowning in acid, and the discovery of Zorlk's frozen body. His text literally degrades into garbled symbols as consciousness fragments.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Military-style operations continue with police carcéronefs, escort fusees, and coordinated pursuit of Slift through orbital space. Meanwhile, the Cube itself is a civilian industrial waste site, and the resistance uses improvised civilian means alongside stolen military equipment.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Cube is portrayed as an unexplored wilderness frontier containing entire compressed ecosystems: cities, mountains, oceans of metal, and volcanic eruptions. Capt's journey through it mirrors frontier exploration of unknown hostile territory, discovering Zorlk's body like finding a fallen pioneer.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Capt's body is devastated by the Cube: severe radiation exposure (87 on the Geiger counter), burns, frostbite, hallucinations, muscle failure, and near-death. The text itself fragments into garbled characters representing the breakdown of perception in this radically non-Earth environment."
    },
    {
        "chapter": "Chapter XX",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Capt emerges from supposed death to lead a massive popular uprising: 700,000 people march through Cerclon, destroying police barricades, crushing the escadre 7, and pulling down a helicopter by cable. The President strategically allows the movement to proceed as part of his long-term political calculus.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon is a fully developed city of seven million with cosmarchés, centers of rencontres, Subvirtue entertainment complexes, and complete urban infrastructure. The chapter ends with the founding of the first settlement in the Dehors, extending habitation beyond the original station.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Saturn's proximity during perihelion is noted, and the setting is entirely within the Saturn system. References to Cerclon III, Starlight, and the vast separation from Earth's problems confirm the long-distance nature of this habitation.",
        "q4": "Distinct space culture",
        "q4_justification": "Cerclon has a fully distinct culture: the Clastre ranking system, the cosmarché with autoroulant Caddies and Topvision eye-tracking, Subvirtue virtual reality complexes, mirécrans that embellish reflections, and a society where citizens vote on executions via remote control. The Volte proposes an even more radically different culture for Anarkhia.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "All communication is in French with extensive space-cultural slang: Slift's argot, consumer terminology like 'cosmarché,' 'Caddie autoroulant,' 'mirécran,' and political vocabulary specific to Cerclon. The language is recognizable but heavily inflected with local culture.",
        "q6": "Manageable but risky",
        "q6_justification": "Life in Cerclon proper is comfortable but the Dehors is extremely dangerous: the first settlers die from asphyxiation due to inadequate oxygen supply. Capt himself is severely irradiated and needs urgent hospital treatment. The managed environment of Cerclon contrasts with the lethal risks just outside.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Cerclon has seven million inhabitants living entirely ordinary urban lives with shopping, entertainment, transportation, and media. The chapter depicts the mundane normalcy of space habitation through Capt's wanderings through cosmarchés and centers of rencontres.",
        "q8": "Single unified authority",
        "q8_justification": "The President exercises supreme authority, manipulating his ministers, sacrificing P as a political fusible, and strategically allowing the Volte movement to proceed as part of his long-term policy. The government maintains centralized control even while appearing to yield.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter interweaves Capt's philosophical journey through Cerclon's consumer society with the President's Machiavellian political strategy. The climax is Capt's political speech proposing the founding of Anarkhia, a new political order, while the President calculates how to use the movement for his own ends.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Most of the chapter depicts civilian life: cosmarchés, bars, virtual reality centers, and urban wandering. The violent confrontation with police barricades and the escadre 7 represents military-style force, but the overall setting is civilian society with security apparatus.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter culminates in the founding of Anarkhia in the Dehors, explicitly framed as frontier colonization: pioneers building cabanes in hostile territory with inadequate oxygen, dying of asphyxiation, and establishing 'the first villages' in an uncharted wilderness. The term 'Hornautes' evokes explorers.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Cerclon's managed environment requires constant technological maintenance (oxygen turbines, mirécrans, digicodes), while the Dehors demands extreme adaptation with oxygen pipelines, masks, and magnetic storm protection. Capt's radiation sickness demonstrates the physical dangers of exposure beyond the managed zone."
    },
    {
        "chapter": "Chapter XXI",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter chronicles ongoing strategic conflict: the mafia seizes Gomorrhe and threatens Mirajeu, Slift is captured and sent to a reeducation camp, Brihx's daughter is kidnapped and killed in a rescue raid, Obffs is assassinated by a precision micromissile, and sinister rumors systematically target the Bosquet leadership.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Anarkhia I has grown into a polycity of 400,000 Hornautes with named cities (Magnitogorsk, Horville, Gomorrhe, Virevolte, Mirajeu), infrastructure, schools, economies, and governance systems. The Dehors is being permanently settled and governed through anarchist principles.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The setting remains in the Saturn system, with references to tourists arriving from Starlight by fusée and artists coming from other Cerclons. The Dehors extends into unexplored territory where Obffs is buried at the extreme limit of oxygen reserves, emphasizing remoteness.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Anarkhia I has invented entirely novel social systems: Horville's moneyless anarchist economy, Gomorrhe's Sadean sexual commune, Mirajeu's month-long immersive historical role-playing, and Virevolte's rotating Terreurs/Ouvreurs/Liants governance. These have no Earth precedent whatsoever.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Slift's distinctive argot ('percute,' 'plot,' 'costumés,' 'leurzigues'), Volte-specific terminology, and space-cultural neologisms layer onto French. Communication remains in French throughout, with characters from different cities and backgrounds all sharing the same base language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Life in the Dehors demands constant struggle: oxygen shortages cause nighttime suffocation and child deaths, meteorite showers threaten settlements, the government rations air quality, and Brihx's daughter nearly dies from asphyxiation. Building requires hauling materials by hand across hostile terrain.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Half a million Hornautes work in the Dehors daily, with 200,000 sleeping there. The population includes families with children, elderly, artists, workers, and tourists from across the solar system. Space habitation extends from the established Cerclon cities to the frontier settlements of Anarkhia.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Anarkhia I operates as an independent polycity with its own governance, economy, and social systems, distinct from Cerclon's government. The chapter also references Starlight, multiple Cerclons, American interests, Israeli mafia, and Solarien religious communities as separate power centers.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is fundamentally about political organization: building new societies from scratch, negotiating oxygen supply with the government, combating mafia infiltration, and managing the internal tensions of anarchist communities. The assassination of Obffs and rumors targeting the Bosquet are political warfare.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter depicts civilian nation-building: constructing cities, establishing schools, creating economies, and developing art. Military elements include Slift's militia, the mafia conflict, and Obffs's assassination, but the dominant activity is civilian construction and governance.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The entire chapter is an extended frontier narrative: pioneers building cities from scratch in hostile territory, struggling with oxygen supply, fighting off criminal elements, establishing new governance systems, and pushing deeper into unexplored desert. The term 'Hornautes' explicitly evokes pioneer explorers.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Dehors is extremely physically challenging: insufficient oxygen causes nightly suffocation and deaths, meteorite showers destroy settlements, the environment requires constant oxygen pipeline maintenance, and construction at Virevolte must be done by hand across treacherous terrain inaccessible by vehicle."
    },
    {
        "chapter": "Chapter XXII",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter reveals that Capt has been an unwitting surveillance tool with nanocameras in his eyes, used by the government to assassinate Obffs and capture Slift. The climax sees the Bosquet hack into the government's oxygen system and ignite the cube gouvernemental, destroying the seat of power in a strategic coup.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Anarkhia I is now a mature polycity of 400,000 with autonomous oxygen production, roads between cities, water systems, and sustainable communities. The settlements have proven permanent and self-governing, with the first anniversary demonstrating stability.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The setting remains entirely in the Saturn system. The chapter references the broader solar system with mentions of Urania's military ambitions toward Jupiter using Saturnian bases as relays, confirming the vast distances separating these space communities from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Anarkhia's mature society operates entirely without money, government, police, or traditional law. The Déconnectés hacker community, the political philosophy of 'compression' as governance, and Capt's self-blinding to destroy the surveillance state represent a social order radically unlike anything on Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The dialogue features hacker jargon ('mocodes,' 'fréquenceur vidéo,' 'pont-levis'), Volte political vocabulary, and space-cultural neologisms, all built on a French linguistic foundation. Blusq's community speaks rapid technical French with computing terminology.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The Dehors remains resource-intensive: oxygen must be produced by a dedicated usine and distributed through canalisations that can explode under pressure conflicts. The environment outside Cerclon requires constant infrastructure maintenance, and the chapter opens noting the ongoing challenges of survival.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter describes a mature, settled civilization spanning multiple communities across the Saturn system. 400,000 people live in Anarkhia with established infrastructure, while Cerclon continues as a major urban center. Space habitation is entirely ordinary.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Anarkhia operates as an independent polity with its own infrastructure and governance, alongside Cerclon's government. The chapter also references Starlight, Urania's military interests, American strategic ambitions, Israeli mafia, and Solarien sects as distinct power centers competing for influence.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter delivers a horrifying revelation that Capt's eyes contain nanocameras that were used to guide the missile killing Obffs. Capt's frenzied self-blinding with a pen is viscerally horrific. The subsequent race against time to hack the government's systems and destroy the cube gouvernemental creates intense thriller tension.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on civilian hacker communities, political philosophy, and investigative work. The destruction of the cube gouvernemental uses civilian oxygen infrastructure rather than military weapons. Military elements are referenced (Urania, American bases) but the action is driven by civilian actors.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The chapter's climax depends entirely on networked digital warfare: the Déconnectés hack the Terminor network, exploit video frequencies to discover the nanocamera, infiltrate the government's oxygen control systems through a phone-line bridge, and remotely ignite the cube gouvernemental. Space control is exercised through information networks.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Capt's nanocameras are grafted onto his optic nerves and have become organically fused with his eyes, making removal impossible without permanent blindness. The oxygen system that sustains all life can be weaponized through network manipulation. The Dehors remains physically hostile, requiring dedicated oxygen production and distribution infrastructure."
    }
]

country = 'France'
book_title = 'La Zone du Dehors'
csv_path = 'data/results/France_La_Zone_du_Dehors.csv'

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
