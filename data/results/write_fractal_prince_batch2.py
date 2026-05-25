import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 11",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Jean battles Sumanguru's mind inside a virtual environment, traps him using firmament code, and then faces a rain of Hunters that destroy a zoku router with antimatter. The chapter is dominated by intense conflict between Sobornost entities and zoku technology.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter references Perhonen traveling the Highway towards Earth, the Sobornost controlling vast networks, and Mieli being an Oort Cloud warrior. Multiple factions hold territory across the solar system.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Perhonen's wings catch the solar wind to push back toward Earth via the Highway, implying a lengthy interplanetary journey. The characters operate far from Earth in deep space.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter depicts gogols (mind copies), virtual environments called virs, Founder codes, Oortian vaki technology, and the Sobornost way of separating worlds and minds. Society is built on mind uploading and digital existence far removed from Earth norms.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Jean, Mieli, and Perhonen communicate seamlessly across Sobornost, Oortian, and zoku technological frameworks. Communication happens through mental links, ship interfaces, and virtual environments rather than natural language barriers.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Space is filled with dangers including Hunter swarms, antimatter explosions, gamma rays, and pions. Perhonen must use anti-meteorite lasers and q-dot bubbles to retrieve Jean from debris, showing survival requires significant technological resources.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The characters live aboard a spaceship as routine, with Mieli piloting and Jean existing in virtual and physical forms interchangeably. The Sobornost operates vast fleets and the Highway is a regular transit corridor.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features Sobornost Founders, zoku collectives, Oortian warriors, and the Pellegrini goddess as distinct competing factions. Jean uses Sumanguru's Founder codes against the Hunters, illustrating the complex factional dynamics.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter opens with Jean bound and tortured in a virtual interrogation, then escalates to a tense escape involving Hunter swarms and antimatter destruction. The mood is one of suspense and survival.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter blends military elements like Hunter swarms, combat autism, and strangelet triggers with the personal dynamics between Jean, Mieli, and Perhonen. The ship serves both as a living space and a combat vessel.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Much of the conflict takes place inside virtual environments (virs) and through digital manipulation of Founder codes. Jean traps Sumanguru using a firmament vir and manipulates Hunters through digital deception rather than physical combat.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment includes virtual reality spaces, antimatter explosions in vacuum, the Highway manifold, and a ship that opens magnetic wings miles wide to catch solar wind. The physical setting is entirely unlike any Earth experience."
    },
    {
        "chapter": "Chapter 12",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter reveals the Axolotl as a body thief who caused the night of the ghuls, and the Repentants are hunting Tawaddud. There is ongoing tension between jinni, body thieves, and the ruling families of Sirr, though no open warfare in this chapter.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Sirr is depicted as a permanent city on Earth with established governance, family houses, and infrastructure. The City of the Dead houses jinni in server tombs maintained by ghul labor, indicating settled and governed territory.",
        "q3": "Other / Unsure",
        "q3_justification": "This chapter is set entirely on Earth in the city of Sirr and its City of the Dead. There is no space journey depicted, though brief references to spaceships fleeing during the Collapse appear in Zaybak's backstory.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Sirr's society features jinni (AI entities) living in tombs, ghuls as mindless servants, body thieves who possess humans through stories, entwinement between human and jinn minds, and the concept of qarin-muhtasib partnerships. This is radically different from any Earth society.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in a common language, but Tawaddud is noted for knowing ancient tongues and secret words to confuse jinni. The Names function as a specialized linguistic system alongside ordinary speech.",
        "q6": "Manageable but risky",
        "q6_justification": "The City of the Dead is dangerous with aggressive ghuls who grab and crowd Tawaddud, and wildcode threatens from the desert. However, life in Sirr is sustainable with the protection of Seals and the Aun's systems.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "While this chapter is Earth-based, it references the broader setting where uploaded minds, Sobornost guberniyas, and space habitation are commonplace. Zaybak's memories reference spaceships in the sky during the Collapse.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter reveals multiple power centers: the ruling muhtasib families, the Repentants, the jinni of the City of the Dead, the Banu Sasan, body thieves, and the distant Sobornost. Even within Sirr, factions compete.",
        "q9": "Drama",
        "q9_justification": "The chapter is an emotionally rich story of Tawaddud's relationship with Zaybak the Axolotl, her entwinement with the qarin Arcelia, and the discovery that Alile was possessed. It focuses on personal relationships and emotional revelations.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter focuses on civilian life in Sirr's City of the Dead, personal relationships between Tawaddud and Zaybak, and the investigation of Alile's death through entwinement with a qarin. No military presence features.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The athar functions as an information layer overlaid on reality, jinni exist as digital entities in server tombs, and entwinement merges minds through networked connections. The body thief vector is a story transmitted through this network.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Earth in this era features wildcode desert, nanoscale technology in the atmosphere (foglets), digital overlay (athar), and jinni inhabiting server tombs. The physical environment has been significantly altered from baseline Earth but remains habitable."
    },
    {
        "chapter": "Chapter 13",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chapter depicts a massive space battle between Sobornost fleets and zoku ships near a cosmic string, with raion ships destroyed, millions of gogols lost, strangelet missiles fired, and Gun Club ships deploying black holes. The warmind is then betrayed and devoured by a Dragon.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Sobornost deploys a fleet of two hundred raion ships plus an oblast ship, controls guberniyas described as planet-sized constructs, and fights the zoku for territory. Both sides maintain vast military and territorial presence across the solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The battle takes place near a cosmic string in deep space, far from Earth. The warmind references the Broken Places of Jupiter-that-was, and the chen discusses events spanning millennia of Deep Time. The distances and timescales are extreme.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Sobornost society is organized around copybrothers, gogol hierarchies governed by xiao, metaselves that constrain thought, and the Great Common Task ideology. The chen maintains Dragons in sandboxed environments and uses a vir made entirely of language.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The warmind communicates through Code, virs, and the firmament with his copybrothers and the chen. Communication is technologically mediated through mindshells, metaselves, and demiurge gogols that translate perceptions.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The environment includes cosmic strings more massive than Earth, antimatter explosions, strangelet missiles, Hawking radiation from black holes, and topological defects in spacetime. Survival requires massive technological infrastructure.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The warmind coordinates millions of gogols across hundreds of ships as routine military operations. The Sobornost maintains permanent fleets, guberniyas, and vast populations of uploaded minds living entirely in space.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features Sobornost copyclans (warmind, chen, pellegrini, vasilev), zoku collectives (including the Kaminari), Gun Club zoku, and internal Sobornost politics between Founders. The chen betrays the warmind for his own faction's goals.",
        "q9": "Military / war",
        "q9_justification": "The entire chapter depicts a space battle from the warmind's tactical perspective, including fleet maneuvers, weapon systems, Nash equilibria calculations, and culminating in betrayal. It reads as a military science fiction battle sequence.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "Every element of the chapter is military: fleet coordination, weapons deployment, tactical analysis, chain of command, and the Protocol War against the zoku. The warmind exists solely as a military entity.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The space battle features fleets of ships in formations, pincers converging on enemy vessels, swarms surrounding targets like shoals of fish, and an admiral-like warmind coordinating from a flagship oblast. The tactics mirror naval warfare.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The setting includes cosmic strings warping spacetime, Planck-scale black holes, strangelet missiles converting matter, Hawking radiation, and topological defects. The physics are fundamentally alien to Earth experience."
    },
    {
        "chapter": "Chapter 14",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Fast Ones attack Tawaddud and Sumanguru with needle guns, steal the qarin Arcelia, and someone destroys Arcelia with a barakah gun during pursuit. The chapter features violent conflict driven by political intrigue around the Sobornost Accords.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Sirr is shown as a complex, governed city with multiple Shards, markets, rukh ship armadas, Fast One parasite cities, and established ruling families. It is a permanent, self-governing settlement on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "This chapter takes place entirely on Earth in the city of Sirr. There are references to the Gourd frame visible in the sky and Sobornost presence, but no space journey occurs.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Sirr features Secret Names that control nanotechnology, Fast Ones as miniature warriors with cities-within-cities, flying carpets made of utility fog, jinni servants, barakah guns that speak the Anti-Name, and the muhtasib system. Society is radically alien.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tawaddud and Sumanguru communicate in a common language, but the Secret Names function as a specialized ancient command language for controlling the athar and wildcode. The Names of the Aun represent a distinct linguistic layer.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The wildcode desert threatens anyone without Seals, barakah guns can destroy protective Seals leaving people vulnerable to wildcode, and the environment requires constant technological protection through foglets and jinn rings.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Gourd frame around Earth is visible in the sky, Sobornost envoys visit routinely, and the broader context establishes that space habitation is widespread. Sumanguru is a Sobornost gogol visiting Earth.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features the Gomelez family, Fast Ones of Qush and Misr, Sobornost representatives, muhtasib families, mutalibun crews, and unknown conspirators. Power is distributed among many competing groups.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is an action thriller featuring a Fast One ambush, a high-speed carpet chase through the city, near-death from chimera bird tethers, and the dramatic destruction of Arcelia. The pacing is tense and fast.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The setting is a civilian city with political intrigue, but the Fast One attack is a military-style assault and the barakah gun is described as a muhtasib weapon. Sumanguru brings Sobornost military technology to a civilian context.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The athar functions as an augmented reality overlay where Tawaddud tracks Arcelia, uses Secret Names as commands, and navigates using jinn rings. The conflict involves both physical and digital dimensions simultaneously.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Earth's environment includes wildcode that attacks unprotected humans, the athar as a pervasive digital overlay, utility fog carpets, and foglet-based technology. Human bodies require constant Seal protection from environmental nanotechnology."
    },
    {
        "chapter": "Chapter 15",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter outlines a strategic heist plan to steal the Kaminari jewel from Matjek Chen, involving infiltration of Earth and the Sobornost. Jean and Mieli discuss the Pellegrini's manipulation, and the plan involves deceiving multiple factions.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter references Earth under Sobornost control with the Gourd array, guberniyas ruled by god-kings, the Oort Cloud settlements, and Mars. Multiple civilizations hold permanent territory across the solar system.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Jean is being launched toward Earth via a thoughtwisp, compressed and propelled by ship lasers. Perhonen is traveling to Earth separately. The journey involves significant distance and the thief will travel without a body.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter describes Oortian sauna rituals in zero-gravity, insurance heavens from the 2060s, body thieves in Sirr, Sobornost Founder codes, and the Pellegrini as a goddess ruling a guberniya. Society has splintered into radically different cultural forms.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Jean, Mieli, and Perhonen communicate in a common language, but the thief mentions needing Seals to move on Earth and the muhtasib system of Sirr as linguistically distinct. Cultural and technological terminology varies between factions.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Earth is described as a dark place of pain requiring Seals for protection from wild nanites. Jean must be launched as a compressed thoughtwisp, and Mieli must infiltrate as a mercenary. Survival on Earth requires specific technological protections.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Living aboard Perhonen, performing Oortian sauna rituals in space, and launching minds as thoughtwisps are treated as routine. The Sobornost operates across the entire solar system with space habitation as the norm.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter names multiple distinct polities: the Pellegrini's guberniya, Sobornost hsien-kus, Chen's domain, the muhtasib families of Sirr, Oortian kotos, and mercenary companies. Each operates independently with competing interests.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is a planning scene for a heist adventure: Jean outlines the mission to infiltrate Earth, find Chen's secret gogol, and steal the Kaminari jewel. The tone is one of preparation for a daring caper.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on a civilian heist plan, personal relationships, and Oortian cultural rituals. However, Mieli's mercenary cover and the Pellegrini's military resources provide a military backdrop.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean's plan involves downloading his mind into Sobornost networks, using Founder codes as digital disguises, and finding a hidden gogol in an insurance heaven. The heist operates primarily through digital infiltration rather than physical force.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Jean must travel as a bodiless mind in a thoughtwisp, Earth requires Seal protection from wild nanites, and the Oortian sauna operates in zero-gravity with vacuum exposure. Physical existence is constantly mediated by technology."
    },
    {
        "chapter": "Chapter 16",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter reveals that Dunyazad likely orchestrated the attack on Sumanguru and the destruction of the qarin, is connected to zoku agents, and asks Tawaddud to implant a device in Sumanguru. Political conspiracy and betrayal drive the entire chapter.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Gomelez palace is depicted as a well-governed family stronghold with kitchens, guest quarters, living areas, and political infrastructure. Sirr is presented as a permanent, governed city with established institutions.",
        "q3": "Other / Unsure",
        "q3_justification": "The chapter is set entirely within the Gomelez palace in Sirr on Earth. References to the Sobornost, the Gourd, and the Cry of Wrath provide context, but no space journey is depicted.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Society features muhtasib families governing through Secret Names, Sobornost gogols as diplomatic envoys, Repentant guards, political astronomers studying Sobornost, and Dragons as non-conscious AI entities. Tawaddud's mother leaped from a balcony during the Cry of Wrath.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "All characters communicate in a shared language, but Sumanguru reveals specialized Sobornost terminology like Dragons, Deep Time, and cognitive architecture. The Secret Names represent a distinct specialized language system in Sirr.",
        "q6": "Manageable but risky",
        "q6_justification": "Life in the Gomelez palace is comfortable with kitchens, guest quarters, and servants. However, the Cry of Wrath backstory shows existential threats, and Tawaddud's mission to implant a device in Sumanguru carries personal danger.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Sumanguru describes the Sobornost guberniyas as cages for Dragons housing vast populations, and discusses Deep Time where communities leap forward generations. Space habitation and digital existence are normalized across the solar system.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter explicitly names competing factions: Gomelez family, masrurs, zoku agents, Sobornost copyclans (hsien-kus, sumangurus, pellegrinis, vasilevs), and the Aun. Dunyazad is revealed as possibly working with the zoku against Sobornost.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on political maneuvering: Cassar Gomelez discusses diplomatic strategy with the Sobornost, Dunyazad manipulates Tawaddud for espionage, and Sumanguru reveals Sobornost political history. Every scene involves political calculation.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter is focused on civilian politics, family dynamics, and diplomacy. Sumanguru's military background and the Cry of Wrath are referenced, but the primary action is political intrigue within a civilian household.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Sumanguru describes guberniyas as virtual machines boxing off Dragons, gogols operating within mindshells and metaselves like layers of an onion. The Sobornost domain is characterized as nested digital environments rather than physical territory.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The environment features wildcode that mutated Kafur's body, the athar as a pervasive digital overlay, Sobornost bodies with sub-skin machinery, and zoku technology implants. Human bodies are constantly interfaced with or challenged by technology."
    },
    {
        "chapter": "Chapter 17",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Mieli arrives at Earth and encounters the Gourd being built around it, with Sobornost machines eating the Moon. Tensions between Oortians, Sobornost factions, and mercenary companies are present but no active fighting occurs in this chapter.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter describes Oortian kotos in the Kuiper belt, Jovian polises, the zoku, Sobornost guberniyas planet-sized, and the Gourd being built around Earth. Multiple civilizations occupy permanent territories across the entire solar system.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Mieli and Sydän's backstory describes traveling from the Oort Cloud through the Highway manifold, past the Kuiper Belt, to Venus and eventually Earth. This represents a journey spanning the entire solar system over significant time.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Oortian culture features ice-shaping with vaki, ancestor spirits as phonons, Great Works as coming-of-age rituals, and myths about Earth as a burning place of pain. The kotos live in vacuum with secondskins and algae-based life support.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Mieli communicates with the mercenary recruiter and Perhonen in a shared language. Oortian terminology like vaki, koto, and koito-specific cultural references represent dialect differences rather than separate languages.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Oortian environment requires secondskins and vacuum suits for survival. Earth is surrounded by the Gourd and described as terrifying. Mieli spent her life in vacuum, and the wildcode desert on Earth requires special protection.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Mieli grew up in the Oort Cloud, builds ice habitats as a coming-of-age ritual, and Sydän dreams of visiting Venus and Earth as tourism. Multiple civilizations across the solar system treat space habitation as ordinary.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter names Oortian kotos, Sobornost copyclans (hsien-kus, vasilevs), Jovian polises, zoku, mercenary companies like the Teddy Bear Roadside Picnic Company, and the muhtasib families of Sirr. The political landscape is extremely fragmented.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows Mieli's journey from Oort to Earth, with flashbacks to building the Chain and exploring the solar system with Sydän. The tone is one of exploration and arriving at a new, mysterious destination.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Mieli arrives at Earth as a mercenary seeking employment, docking at a military mercenary hub within the Gourd. The chapter blends civilian backstory of ice-building with military preparation for the desert mission.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Oortian kotos are described like frontier settlements, building habitats from ice in the darkness. Mieli arrives at Earth as a mercenary frontiersman. The Sobornost is expanding its Gourd around Earth like colonial infrastructure.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The chapter depicts life in the Oort Cloud in vacuum with ice habitats, zero-gravity gardens, and secondskins. The Gourd around Earth is over 100,000 km in diameter. The Silver Road from Earth to the Moon represents fundamentally non-Earth-like physics."
    },
    {
        "chapter": "Chapter 18",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Jean infiltrates hsien-ku systems disguised as Sumanguru, manipulating and threatening them. The Pellegrini takes over Gourd systems. The backstory shows Jean recruiting Chen for revolutionary activities. Strategic deception pervades every interaction.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Gourd array around Earth houses the hsien-ku ancestor virs simulating all of human history. The Sobornost controls guberniyas, and Jean references multiple settled locations including Mars, Earth, and Venus. Territory is held across the system.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Jean has traveled from deep space to the Gourd around Earth as a compressed thoughtwisp. The ancestor vir spans centuries of simulated time. The chapter references events across millennia and vast distances.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The hsien-ku operate ancestor virs simulating all of human history, spawning and erasing entire simulated worlds. Jean navigates a 4D interface, and the blat system replaces market economics within Sobornost. Society is fundamentally post-human.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Jean communicates within simulated historical environments (1990s Vienna, pre-Collapse Paris) through technologically mediated virs. The hsien-ku physics engine translates everything, and a mysterious masked girl communicates across the 4D ancestor space.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Operating within the hsien-ku virs requires maintaining elaborate disguises and risking detection. Jean's real body situation is precarious, and the Pellegrini must hack the Gourd's systems. Survival depends on complex technological manipulation.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Gourd around Earth is an enormous inhabited structure, hsien-kus maintain vast ancestor simulation systems, and Jean casually moves through Sobornost networks. Living in space-based digital infrastructure is completely normalized.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features hsien-ku copyclans, the Pellegrini faction, sumangurus, chens, vasilevs, zoku, and pre-Collapse corporations like Jannah. Political tensions between pellegrinis and vasilevs are mentioned, and the hsien-ku plays blat games.",
        "q9": "Adventure / exploration",
        "q9_justification": "Jean infiltrates the hsien-ku ancestor virs in a heist-like investigation, exploring simulated historical Paris to find clues about Chen's childhood upload. The chapter reads as a detective adventure through digital history.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on Jean's civilian espionage within academic hsien-ku ancestor virs. The sumanguru disguise implies military authority, but the actual activities are investigation and social engineering rather than combat.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The entire chapter takes place within digital simulations: a Viennese cafe vir, a 4D ancestor simulation, and simulated 2060s Paris. Jean exists as a bodiless ghost navigating networked virtual environments. Space is characterized as a digital domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Jean operates as a bodiless entity in a 4D ancestor vir with time as a navigable dimension. The Gourd is an enormous structure around Earth. The physical environment is entirely virtual, with simulated realities that can be spawned and erased at will."
    },
    {
        "chapter": "Chapter 19",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Tawaddud and Sumanguru (Jean in disguise) sneak out of the Gomelez palace, evade jinni surveillance, and seek the Axolotl at the Palace of Stories. The chapter involves espionage, deception, and the ongoing political conspiracy around Dunyazad's betrayal.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Sirr is shown as a complex vertical city with Shards, tram systems, the Palace of Stories underground, and established governance. The city is a permanent, governed settlement with extensive infrastructure.",
        "q3": "Other / Unsure",
        "q3_justification": "The chapter is set entirely on Earth in Sirr. Jean communicates briefly with Perhonen in the Gourd, but the narrative is grounded on Earth with no space travel depicted.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Palace of Stories is an underground world where forbidden stories are traded, jinni take forbidden female forms, body thieves operate, and entwinement is performed. Kafur's wildcode-ravaged face and the masked society represent a radically alien social order.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in a shared language, but Secret Names function as specialized commands. The Palace of Stories trades in stories and Names as currency, representing a distinct cultural-linguistic system alongside common speech.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Climbing the outside of the Shard exposes them to wildcode that causes sparks in Jean's vision and damages his body. His q-tool dies from wildcode corruption. Survival outside the city's protections requires special gear and medicines.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Jean casually communicates with Perhonen in orbit and references his instantiation from Gourd systems. The Sobornost presence around Earth and space-based infrastructure are treated as normal background elements.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features the Gomelez family, Banu Sasan underground society, the Palace of Stories community, jinni factions, masrurs, Repentants, and Sobornost. Kafur runs an independent domain, and Tawaddud navigates between all these groups.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows an adventurous nighttime descent down the Shard, evasion of surveillance, and exploration of the underground Palace of Stories. The tone combines heist elements with exploration of a hidden underworld.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Palace of Stories is a civilian underground establishment. Jean carries a Sobornost mind-bullet weapon, and the masrurs are mentioned as attacking soul trains, but the chapter focuses on civilian social dynamics and investigation.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Tawaddud uses Secret Names to duplicate athar signatures and deceive jinni surveillance. The Palace of Stories trades in digital entities and forbidden data. The athar functions as a pervasive network layer that must be navigated and manipulated.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Wildcode actively attacks Jean's body during the climb, corrupting his technology and causing neurological effects. Kafur's face has been destroyed by wildcode infection. Earth's environment constantly challenges human biology through pervasive nanotechnology."
    },
    {
        "chapter": "Chapter 20",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter depicts the rivalry between Oortian culture and Sobornost ideology through Mieli and Sydän's journey. The Bekenstein quake shows Sobornost consuming cities and minds. Sydän's defection to the Sobornost represents an ideological contest.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter spans Venus with its wind cities and guberniya-sized constructs, the Oort Cloud with its kotos, and references to the Belt, Jupiter, Saturn, and the Oubliette on Mars. Civilizations hold territory across the entire solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Mieli and Sydän travel from the Oort Cloud to Venus, a journey of light-hours taking months. The distances are so vast that Oortians mythologize Earth. The journey represents extreme separation from their home.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Amtor City on Venus is a bubble city riding hot winds 50 km above the surface, where godlings fly naked in acid clouds and pilgrims come to be uploaded into Sobornost singularities. Oortian culture with its ice-shaping and ancestor spirits is equally alien.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Mieli and the grey-haired boy communicate easily, as do Mieli and Sydän. Oortian terms like vaki, koto, and secondskin represent cultural vocabulary differences rather than separate languages. The Pellegrini speaks the same language.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Venus has three-hundred-mile winds, searing heat, and sulfuric acid clouds. The Bekenstein quake collapses matter into a black hole that destroys the landscape. Mieli suffers compound fractures, a punctured lung, and internal bleeding from the blast.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Wind cities on Venus host pilgrims and posthumans from across the solar system. Amtor City floats in the atmosphere as a functioning civilization. Oortians travel to the Inner System, and guberniyas are planet-sized inhabited constructs.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features Oortian kotos, Venusian godlings, Sobornost guberniyas, the Pellegrini as a ruling goddess, zoku from Jupiter and Saturn, Belt communities, and the Oubliette on Mars. Multiple independent polities coexist.",
        "q9": "Drama",
        "q9_justification": "The chapter is an emotionally intense love story: Mieli and Sydän's relationship, Sydän's betrayal and sacrifice to the Sobornost singularity, and Mieli's desperate deal with the Pellegrini to get her back. The drama of loss drives the narrative.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on the civilian experiences of love, pilgrimage, and personal loss. The Sobornost's Bekenstein quake is a technological-religious event rather than military. Mieli's mercenary service is referenced but occurs offscreen.",
        "q11": "Totally unique domain",
        "q11_justification": "Venus with its wind cities, Bekenstein quakes creating black holes, and the Pellegrini's temple on a metallic plain defy conventional domain analogies. Space here is characterized by physics-defying phenomena unique to this far-future setting.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Venus features 300-mph winds, sulfuric acid atmosphere, and cities floating 50 km up. A Bekenstein quake collapses matter to Planck scale, creates a black hole, and triggers a planetary-scale explosion. The physics are fundamentally unlike Earth."
    }
]

country = 'Finland'
book_title = 'The Fractal Prince'
csv_path = 'data/results/Finland_The_Fractal_Prince.csv'

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
