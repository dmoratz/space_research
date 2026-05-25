import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 01 - The Thief and the Prisoners Dilemma",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Sobornost controls the Inner Solar System and runs the Dilemma Prison through Archons. Mieli and the pellegrini break Jean out against the Archons' will, and Archon bladeships pursue them, indicating ongoing rivalry between factions rather than total war.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Sobornost is described as the upload collective that rules the Inner Solar System. Mieli comes from the Oort Cloud, and the Prison is a diamondoid torus nearly a thousand kilometers in diameter, indicating widespread permanent occupation of space.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The story takes place in a far-future solar system where Earth is a distant memory. The Prison is in the Neptunian Trojan belt, and characters reference old Earth as a historical artifact. The solar system is vast and humanity is spread across it.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Society has transformed completely: minds are uploaded and copied, prisoners play iterated game theory simulations, the Sobornost is a collective of uploaded minds, and Oortian culture has its own deities like Kuutar, Ilmatar, and the Dark Man. Nothing resembles Earth society.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate in what appears to be a common language with specialized terminology like gevulot, gogol, and Sobornost vocabulary. Jean and Mieli converse easily, though Oortian and Sobornost cultures have distinct jargon.",
        "q6": "Manageable but risky",
        "q6_justification": "Space travel requires sophisticated ships like Perhonen with life support, and vacuum is lethal. However, technology makes survival routine for those with proper equipment. Jean's new body functions in the ship, and the spidership provides habitable conditions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Humanity has fully dispersed across the solar system. The Highway is described as a constant torrent of ships. There are Oortian communities, Sobornost guberniya worlds near the sun, and the Prison houses millions of minds. Living in space is completely normal.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Multiple distinct factions are named: the Sobornost upload collective, the Oortian cultures, the zoku, and various independent entities. The Sobornost itself has multiple Founders. Mieli serves a specific Sobornost goddess (the pellegrini) with her own agenda.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is a heist/adventure narrative: Jean le Flambeur is broken out of a virtual prison by Mieli for a mysterious theft mission. The tone combines action, wit, and intrigue as Jean escapes and begins a new caper.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on a prison break and civilian characters. Mieli has military background from the Protocol War and the Archon bladeships pursue them, but the primary activities are civilian: theft, escape, and personal relationships.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is deeply intertwined with digital reality. The Prison is a virtual environment running game theory simulations. Jean's body contains proteomic computers and computronium. The spimescape provides an augmented information layer over physical space.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The physical environment requires artificial bodies, spiderships with q-dot sails, and zero-gravity habitation. Jean's new body has diamond machines in its bones and proteomic tech in its cells. Weightlessness, vacuum, and the need for smartmatter habitats dominate."
    },
    {
        "chapter": "Chapter 02 - The Thief and the Archons",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Archon bladeships aggressively pursue Perhonen with nanomissiles, forcing Mieli to destroy an asteroid with a strangelet bomb to escape. The combat is intense and strategic, with adaptive weapons and countermeasures.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Highway is described as a sea of ships including zoku generation ships, Sobornost thoughtwisps, and calmships with green biomes inside. Multiple factions occupy and control different regions of the solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The chapter ends with Jean and Mieli heading toward Mars via the Highway, a gravitational artery for long-distance travel. Earth is a distant historical reference. The solar system's scale is emphasized by lightsecond measurements between objects.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Archon thinks in terms of game theory and turning matter into Prisons. The Sobornost Founders are god-kings with a trillion subjects. Mieli performs Oortian rituals with fabbed food. Society is built around uploaded minds, copyclans, and posthuman collectives.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Jean and Mieli communicate naturally in a shared language, but specialized terms pervade their speech: spimescape, q-dots, quptlink, copyfather, copybrothers. The Archon thinks in its own conceptual language about games and patterns.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The ship is nearly destroyed by nanomissile infection that turns matter into Prison-substance. Mieli must use a strangelet bomb on an asteroid to create a particle wind for propulsion. Survival in space requires constant technological intervention.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Highway teems with diverse ships: overclocked zoku generation ships, whalelike calmships with miniature suns, Sobornost thoughtwisps like fireflies. Living in space across the solar system is entirely ordinary for posthumanity.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The Highway hosts ships from multiple factions: zoku generation ships, Sobornost thoughtwisps, calmships. The Sobornost Founders are seven distinct entities whose faces adorn their ships. The pellegrini operates semi-independently.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is dominated by a thrilling space chase and Jean's clever trick to neutralize the Archon nanomissile using misdirection. It ends with the duo toasting and setting course for Mars, advancing the heist adventure plot.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Archon pursuit involves military-grade weapons like nanomissiles and strangelet bombs, and Mieli uses combat autism. However, the protagonists are civilians on a theft mission, and the Highway is full of civilian traffic.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean defeats the Archon by trapping it in a simulated spimescape, exploiting inattentional blindness in Sobornost minds. Combat involves information warfare: nanomissiles that convert matter into virtual prison environments. The digital and physical are inseparable.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The ship reconfigures itself into a hard cone for combat. Jean gains root access to his body's diamond machines and proteomic tech to navigate zero-g and extract a nanomissile. The physical environment of space demands radical technological adaptation."
    },
    {
        "chapter": "Chapter 03 - The Detective and the Chocolate Dress",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter focuses on a gogol piracy case in the Oubliette, a relatively peaceful walking city on Mars. The conflict is criminal rather than military: a daughter helped pirates steal her father's mind. The tzaddik vigilantes maintain order.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is a permanent, self-governing walking city on Mars with its own political system (the Voice), economy (Time-based), and culture. Citizens live full lives cycling between Noble and Quiet states.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Mars is clearly separated from Earth by significant distance. The Oubliette is an independent society with its own culture. Earth is referenced historically but plays no active role. Offworlders are tourists who arrive via beanstalk.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Oubliette operates on cryptographic privacy (gevulot), shared exomemory, Time-based economy, and mandatory cycling between human life and machine labor as Quiet. Citizens have privacy senses. This social order is completely unlike Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak a common language but with Oubliette-specific terminology: gevulot, exomemory, co-memory, blink, tzaddik, Noble, Quiet, Time. The specialized vocabulary reflects their unique social structures.",
        "q6": "Manageable but risky",
        "q6_justification": "Life inside the Oubliette is comfortable and civilized, with shops, parks, and cafes. However, Mars itself requires quicksuits for surface excursions, and the city must constantly defend against phoboi. The environment is managed but not benign.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Oubliette is a thriving city with shops, restaurants, parks, and a complex society. Offworlders visit as tourists. Living on Mars in walking cities is completely normal; the chapter depicts everyday urban life.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The Oubliette is self-governing with its own Voice democracy system. The zoku colony operates independently within the city. Sobornost agents (vasilevs) infiltrate. The tzaddikim are independent vigilantes. Multiple powers coexist.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows detective Isidore solving a murder-mystery involving gogol pirates, a chocolate dress encoding stolen mind data, and a dramatic confrontation with the killer. It reads as a detective adventure.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is entirely civilian: a detective investigating a crime, a chocolate shop, a family apartment, tzaddik vigilantes. There is no military presence or military framing of space.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The Oubliette runs on cryptographic protocols (gevulot), shared digital exomemory, and privacy encryption. Crime involves stealing minds through optogenetic uploads and encoding data in chocolate crystals. The domain is defined by information architecture.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Mars has lower gravity that old-timers struggle with, requires terraforming, and the city walks on robotic legs. The environment is livable but distinctly non-Earth: pale Martian light, thin atmosphere, and cherry trees on walking platforms."
    },
    {
        "chapter": "Chapter 04 - The Thief and the Beggar",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter depicts daily life in the Oubliette with no military conflict. The main tensions are interpersonal: Jean escapes Mieli, encounters Time beggars in the agora, and searches for hidden memories. Competition is social rather than military.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is depicted as a well-governed walking city with shopping streets, public agoras, a Maze district, parks, and robust social institutions. The city maintains territory as it walks across Mars.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Jean and Mieli traveled from the Neptunian Trojan belt to Mars. Earth is a distant memory referenced only historically. The Oubliette is a fully independent society, completely separated from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Oubliette has Time-based currency tied to Watches, cryptographic privacy, public agoras where all is remembered, Time beggars desperate for moments of Noble life, and a Maze that physically shifts. The social order is entirely alien to Earth norms.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak a shared language with heavy Oubliette jargon: gevulot, exomemory, co-memory, Time, Noble, Quiet, agora, the Maze. Jean uses French expressions. Communication is understandable but culturally loaded.",
        "q6": "Manageable but risky",
        "q6_justification": "Life in the Oubliette is comfortable with cafes, shops, and parks, but the city walks across Mars requiring adaptation. Mieli suffers in the gravity with her enhancements suppressed. The environment is managed but requires adjustment for offworlders.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Oubliette is a bustling city with shopping districts, restaurants, spidercab transport, parkroullers, and tourists from other worlds including Quick Ones and Ganymede-zoku polymorphs. Living on Mars is entirely ordinary.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The Oubliette governs itself via the Voice. The zoku colony exists within the city. Tourists arrive from Belt habitats and other worlds. Sobornost influence lurks in the background. Multiple independent polities coexist across the solar system.",
        "q9": "Adventure / exploration",
        "q9_justification": "Jean chases a mysterious boy version of himself through the shifting Maze, discovers a hidden Watch in a robot garden, and evades Mieli. The chapter is a treasure-hunt adventure driven by mystery and personal discovery.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter depicts entirely civilian activities: shopping, walking through parks and streets, chasing a boy through neighborhoods, finding a hidden object, and interacting with a gardener. No military elements appear.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean tricks Mieli using a gevulot co-memory hack, substituting a recorded memory for real interaction. The city runs on exomemory and cryptographic privacy. Space is navigated through information layers and digital protocols.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Mars has lower gravity that Mieli struggles with, requiring suppression of her Oortian enhancements. Jean notes the low-gravity loping gait of Martians. Bright Phobos serves as a star overhead. The environment is habitable but distinctly Martian."
    },
    {
        "chapter": "Chapter 05 - The Detective and the Zoku",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter focuses on social dynamics at a zoku party. The only conflicts are interpersonal: Isidore's relationship tensions with Pixil, cultural friction between Oubliette and zoku, and an encounter with a journalist. No military or political conflict.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The zoku colony on Mars is a permanent settlement with diamond buildings, a vault of treasures, and its own social hierarchy. It exists alongside the Oubliette as an autonomous enclave with its own governance.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The zoku originally came from the outer planets and lost a war to Sobornost. Earth is referenced only as ancient history. The Eldest mentions building a city on Saturn. Humanity is spread across the solar system, far from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The zoku organize through quantum entanglement for perfect coordination, originating from gaming clans. They use resource optimization, entanglement rituals, and jewel-embedded identities. The Eldest reveals her true form as a shimmering entity of dust motes and jewels.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate in a shared language but with extensive zoku-specific terminology: entanglement, Tangleparty, Epic Mount, Realm, qupting. Oubliette terms like gevulot and exomemory are also used. Gaming jargon pervades zoku speech.",
        "q6": "Manageable but risky",
        "q6_justification": "The zoku colony is comfortable and the party is festive. Life on Mars is managed with technology. However, the Eldest mentions losing a war and being refugees. The environment within the colony is safe but Mars itself requires walking cities.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The zoku have built cities on Saturn and established colonies on Mars. The party is attended by posthuman beings in various forms. Living across the solar system is completely ordinary for these civilizations.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The zoku colony is a distinct polity within the Oubliette. The Eldest describes surviving the Collapse, building on Saturn, and losing a war to Sobornost. Multiple factions with different governance models coexist on Mars alone.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on interpersonal drama: Isidore's relationship with Pixil, meeting her tanglemother who warns him away, being tricked by a journalist, and navigating cultural differences between Oubliette and zoku societies.",
        "q10": "Entirely civilian",
        "q10_justification": "The entire chapter takes place at a costume party with drinking, socializing, gaming, and romantic relationships. There is no military presence or framing. The zoku's war history is mentioned only in passing.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The zoku colony manipulates reality with augmented layers and Realmspaces. Entanglement protocols enable quantum coordination. The vault stores digital creatures given physical form. Space is characterized by networked, game-like structures.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Inside the zoku colony, reality is overlaid with spimes and augmented reality. The physical environment shifts through portals and discontinuities. Mars requires walking cities and quicksuits for surface access. Regular adaptation to non-Earth conditions is needed."
    },
    {
        "chapter": "Interlude 1",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The King of Mars kills his old friend Andre for making deals with outside powers, indicating high-stakes political struggle. Andre warns that the Sobornost Founders will eventually consume them. The chapter depicts espionage and assassination.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette has a spaceport with a beanstalk connecting to orbit. The King governs Mars through memory manipulation. The city receives visitors from across the solar system. Permanent governance of Martian territory is well-established.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The King has a compulsion implanted in him that says he will never leave Mars. Visitors arrive from the Belt, Saturn, and the Realm. Earth is only referenced historically. The solar system's distances create fundamental separation.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The King controls Mars through memory manipulation and exomemory surveillance. He can look through others' eyes and erase people from existence with a q-gun. The social order is built on digital memory, hidden rulers, and posthuman power structures.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The King and Andre converse in a shared language with Oubliette-specific terms. The spaceport receives aliens from diverse backgrounds described with specialized vocabulary: Realm avatars, Belt people, Quick Ones, Saturnian zoku folk.",
        "q6": "Manageable but risky",
        "q6_justification": "The spaceport is a functioning hub receiving diverse visitors. Life on Mars is managed, but the King's assassination of Andre shows that political dangers lurk beneath the surface. The physical environment is controlled.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The spaceport is full of diverse visitors from across the solar system: Realm avatars, Belt people, Quick Ones, Saturnian zoku. Interplanetary travel and habitation is completely normalized.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The King governs Mars secretly while the Oubliette has its own visible governance. Andre warns about the Founders growing stronger. Visitors come from the Belt, Realm, and Saturn. The political landscape is deeply fragmented with hidden power structures.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The interlude has a thriller tone: the King stalks an old friend through a spaceport, navigates a memory trap, and executes Andre with cold efficiency. The atmosphere is tense and conspiratorial.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The spaceport is a civilian facility, but the King uses a military-grade q-gun to assassinate Andre. The underlying power struggle hints at strategic military considerations, but the setting and most characters are civilian.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The King operates through memory manipulation, looking through others' eyes via exomemory. He detects a recursive memory trap. He erases Andre from exomemory entirely. Space is characterized as an information domain where memory is power.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The spaceport has a beanstalk reaching to orbit, and visitors from different gravity environments adapt to Martian conditions. Guest gevulot must be worn. The physical environment requires regular technological adaptation."
    },
    {
        "chapter": "Chapter 06 - The Thief and Paul Sernine",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter depicts ongoing tensions between factions: Mieli is attacked by Time beggars and rescued by a tzaddik, while Jean works to contact Sobornost gogol pirates operating covertly on Mars. The pellegrini maneuvers carefully to avoid association with the mission.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is a fully functioning city with hotels, public avenues, fabbers, and a complex social order. The walking city holds and governs its territory on Mars with its own laws and institutions.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Mieli's journey from Oort to Mars required long preparation. Jean discusses the Oubliette's post-Collapse history and how someone brought a billion gogols from Earth. The pellegrini communicates through a mental temple on Venus. Earth is entirely historical.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter details the Oubliette's gevulot system: nested cryptographic privacy hierarchies, Time-based economy, exomemory, and co-remembering. Mieli visits the pellegrini in a virtual Venus temple. Society is built on privacy protocols and digital memory.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Jean explains Oubliette customs to Mieli using specialized terms: gevulot, exomemory, co-remembering, quantum cash, Watches. They converse easily in a shared language but the cultural vocabulary is extensive and unique.",
        "q6": "Manageable but risky",
        "q6_justification": "Life in the Oubliette is comfortable with hotels and fabbers, but Mieli is attacked by desperate Time beggars. The pellegrini's virtual Venus temple sits above a crater where temperatures exceed 700 Kelvin. Space is survivable but carries risks.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Jean describes how the Oubliette was founded by someone who brought a billion gogols for terraforming. The Sobornost operates across the Inner Solar System. Living on Mars in the walking city is completely normal everyday life.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter reveals layers of competing interests: the Oubliette's government, the secret King, the tzaddikim, Sobornost vasilevs operating as gogol pirates, the pellegrini's copyclan, and the zoku colony. The political landscape is deeply multipolar.",
        "q9": "Adventure / exploration",
        "q9_justification": "Jean and Mieli investigate the Watch's clues, discover Paul Sernine's identity through a hidden mechanism referencing Arsene Lupin stories, and plan to contact gogol pirates. The chapter advances the heist plot with puzzle-solving and intrigue.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter is primarily civilian: hotel rooms, street scenes, detective work on the Watch. The tzaddik uses combat utility fog, and Mieli has concealed military enhancements, but the setting and activities are civilian.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean explains how gevulot works as a cryptographic privacy hierarchy with nested public/private key pairs. The Watch stores quantum cash states. Mieli visits the pellegrini in a virtual mental temple. Space is defined by information architecture.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Mieli struggles with Martian gravity and must hide her Oortian enhancements. The hotel provides fabbers for material needs. Mars requires walking cities and technology sniffers monitor for prohibited tech. Regular adaptation to the Martian environment is needed."
    },
    {
        "chapter": "Interlude 2",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "This quiet interlude depicts Xuexue smiling at a robot and having a peaceful conversation with Paul Sernine. There is no conflict in the present, though Xuexue's backstory involves pre-Collapse violence and exploitation.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is depicted as a stable, governed community where Xuexue works in a kindergarten and visits the robot garden weekly. The society has maintained itself since the Revolution, governing its Mars territory.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Xuexue was brought from Earth to Mars as one of the King's billion gogols. Earth is referenced only in her traumatic backstory of uploading children in China. Mars is a completely separate civilization from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Xuexue's backstory reveals how cheap gogol uploads from Earth were transported to Mars. The Oubliette's gevulot system allows people to make conversations that only the participants will remember. Cycling between Noble and Quiet is accepted as normal.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Paul and Xuexue converse easily. Oubliette-specific terms like gevulot, Quiet, Noble, Kingdom, and Revolution are used naturally. The language is shared but carries the weight of a unique cultural context.",
        "q6": "Manageable but risky",
        "q6_justification": "The robot garden in the Oubliette is peaceful and pleasant. Life in the city is comfortable for residents. However, Xuexue's backstory of being uploaded in China and the Kingdom era's exploitation show that conditions were once far harsher.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Xuexue has lived on Mars for over a century, working as a kindergarten teacher. The Oubliette is a fully normalized society. Paul is described as a visitor but living on Mars is completely ordinary for humanity.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Xuexue's backstory references competing pre-Collapse powers uploading minds. The Oubliette was founded as the Kingdom, then revolutionized. The zoku, Sobornost, and other factions exist across the solar system.",
        "q9": "Drama",
        "q9_justification": "The interlude is an intimate character drama: Xuexue shares her dark past of selling children's minds to upload farms, and Paul carries unnamed guilt. The tone is reflective and emotional, focused on redemption and human connection.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter depicts a kindergarten teacher smiling at a robot and having a personal conversation with a stranger. There is no military presence or framing. Even Xuexue's backstory is about civilian exploitation.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Xuexue's backstory describes the upload economy: scanning children's brains to create gogols for cloud software farms. The Kingdom robots may contain slow gogols running inside them. The domain is deeply intertwined with digital minds and virtual existence.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The setting is a garden on Mars within a walking city. The environment is pleasant but clearly non-Earth: the red gladiator robots are Kingdom-era relics, and the city is carried on robotic legs. Regular adaptation to Martian conditions is part of life."
    },
    {
        "chapter": "Chapter 07 - The Detective and His Father",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter focuses on Isidore's personal struggles: fallout from the newspaper article, visiting his Quiet father, and receiving a mysterious job offer. Conflict is social and emotional rather than military or political.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is depicted in rich detail as a permanent settlement: apartments, restaurants, the Maze, the Inverted Tower, and the surface below where Quiet build phoboi ramparts. The city governs and maintains its territory.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Earth is referenced only in the context of ancient history and the Kingdom era. Mars has its own fully independent civilization. Phobos has been converted into a star. The separation from Earth is complete and ancient.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Isidore visits his father who is a ten-metre tall insect-bodied Quiet building walls on the Martian surface, communicating through tiny sand sculptures. The Noble/Quiet cycle, gevulot privacy, Time economy, and exomemory define a radically alien social order.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak a shared language with extensive Oubliette terminology. The newspaper article is readable, Isidore talks with his flatmate normally, and the mysterious woman uses standard speech with Oubliette concepts.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The surface of Mars requires quicksuits for visits. The Quiet labor beneath the city in orange dust, building phoboi walls. Atlas Quiet are skyscraper-sized machines maintaining the city. The Martian surface is hostile, requiring massive infrastructure.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Oubliette is a fully functioning city with apartments, restaurants, newspapers, and universities. The surface below teems with diverse Quiet performing terraforming, construction, and defense. Living on Mars is completely normalized.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter reveals more of the Oubliette's internal politics: the Voice system, tzaddikim, cryptarchs, newspapers, and the mysterious woman's unnamed employer. The zoku colony exists nearby. Multiple power structures compete within and around Mars.",
        "q9": "Drama",
        "q9_justification": "The chapter is character-driven drama: Isidore deals with unwanted fame from the newspaper, visits his Quiet father in an emotionally wrenching scene, destroys his architectural models in frustration, and receives a mysterious offer involving Jean le Flambeur.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter depicts entirely civilian life: apartments, restaurants, newspapers, university studies, family visits. The Quiet perform civilian labor. Even the mysterious job offer is civilian in nature.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Isidore's life is mediated by exomemory, gevulot, and co-memories. The newspaper exploits analog holes in the privacy system. The mysterious woman's gevulot is impenetrable. The domain is defined by information and privacy protocols.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The Martian surface requires quicksuits for visits. The city walks on giant legs, and Phobos is a converted star. Isidore's father is a ten-metre insect-bodied Quiet. The physical environment is distinctly non-Earth but managed through technology."
    },
    {
        "chapter": "Interlude 3",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The interlude depicts a drunken conversation between Isaac and Paul in a synagogue. There is no conflict beyond personal struggles. Paul wrestles with an internal compulsion related to his nature as a thief.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is stable enough that two men can break into a synagogue for a fourteen-hour drinking session. The city has religious buildings, bars, and a functioning civil society. It governs its territory on Mars.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Isaac references Earth history and religion carried to Mars. Paul is an offworlder living on Mars. The synagogue represents Earth cultural heritage transplanted to a completely separate Martian civilization.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Paul describes having created something bigger than himself that compels him to take things, referencing embodied cognition and many minds and bodies. The Oubliette's Noble/Quiet cycle and gevulot system underpin a society unlike anything on Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Isaac and Paul converse naturally in a shared language, discussing religion, relationships, and personal struggles. Oubliette-specific terms like Quiet, gevulot, and phoboi walls appear naturally in their dialogue.",
        "q6": "Manageable but risky",
        "q6_justification": "The synagogue is a comfortable indoor space. The phoboi walls are mentioned as a dangerous frontier. Life within the city is manageable, but the broader Martian environment requires constant defense and infrastructure.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Isaac has lived through multiple cycles as a Quiet on Mars. Paul is an offworlder who has integrated into Oubliette society. Living on Mars is so normalized that people have religious communities and bars.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Isaac references Fedorovist propaganda and the Revolution. Paul is from offworld with connections to multiple factions. The Oubliette maintains its own governance alongside other solar system powers.",
        "q9": "Drama",
        "q9_justification": "The interlude is an intimate dramatic conversation between two friends. Paul confesses his inner struggle with compulsion and theft. Isaac offers blunt advice about cutting out addiction. The tone is personal and reflective.",
        "q10": "Entirely civilian",
        "q10_justification": "Two friends drink and talk in a synagogue. There is no military presence or framing. The phoboi walls are mentioned but the chapter is entirely about personal civilian life.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Paul describes creating something bigger than himself that operates through multiple minds and bodies, referencing the digital/posthuman nature of identity. The synagogue's gevulot is manipulated to grant them entry. Information architecture underlies the physical world.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The synagogue is described with stained-glass windows and an eternal q-dot light, blending Earth cultural architecture with Martian technology. The phoboi walls outside defend against Martian threats. The environment is adapted but distinctly non-Earth."
    }
]

country = 'Finland'
book_title = 'The Quantum Thief'
csv_path = 'data/results/Finland_The_Quantum_Thief.csv'

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
