import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 15",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Sobornost launches a full-scale invasion of Saturn with seven guberniyas. A kinetic weapon strikes a Plate, all zoku jewels decohere, and the chapter ends with Mieli preparing for combat as raions and nanomissiles descend.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Supra City is a massive permanent settlement around Saturn with Strips and Plates. The Sobornost controls guberniyas across the inner solar system, and the zoku have embedded picotech infrastructure into Saturn's moons like Prometheus for long-term data storage.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Earth is never mentioned as relevant or reachable. The action takes place entirely in the Saturnian system, with factions spread across the solar system in a far-future posthuman civilization completely separated from any Earth-like baseline.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The zoku operate through quantum entangled jewels and collective volition systems, thinking collaboratively in thought-webs of beads and threads. Mieli navigates the Invisible Realm of the Great Game, a fundamentally alien mode of social organization with no Earth parallel.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Characters communicate via qupts (quantum communications), thought-threads, and direct mind-to-mind exchanges in the Invisible Realm. Language barriers are irrelevant as communication is technologically mediated at the quantum level.",
        "q6": "Manageable but risky",
        "q6_justification": "Mieli survives on the surface of Prometheus in a suit with thrusters and weapons. Space is navigable with technology but the sudden decoherence of zoku jewels and the Sobornost invasion show that survival depends heavily on functioning technology.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Billions of beings inhabit Supra City around Saturn. The zoku population is vast and distributed, and the Sobornost guberniyas contain countless gogol minds. Living in space is the default mode of existence for posthumanity.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Multiple distinct factions compete: the Great Game zoku, Ganimard-zoku, Gringotts-zoku, Notch-zoku, Evangelion-zoku, and other zoku subgroups, plus the Sobornost with its seven guberniyas each led by different Founders. Jean le Flambeur operates independently.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a tense thriller as Mieli navigates the Great Game's intelligence apparatus while secretly trying to help the thief, culminating in the terrifying moment when all zoku jewels fail and the Sobornost invasion begins.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Great Game zoku functions as both an intelligence organization and civilian governance structure. Mieli is armed with military weapons on Prometheus, but the broader zoku society includes civilian infrastructure like the Gringotts banking system.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is characterized primarily through virtual Realms, quantum information networks, spimescapes, and thought-webs. The key conflict revolves around quantum data in Saturn's rings, and combat involves metacloaked ships and information warfare.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment includes Saturn's rings as quantum data storage, picotech embedded in moon atoms, spimescapes overlaying physical reality, and the Invisible Realm where thought-beads form collaborative networks. Physical reality is layered with computational abstractions.",
    },
    {
        "chapter": "Chapter 16",
        "q1": "Total war / constant conflict",
        "q1_justification": "The entire Sobornost fleet, controlled by the All-Defector, has invaded Saturn. Jean learns his disruption of the zoku volition system has left Supra City defenseless. Structural damage, strangelet events, and Hawking blasts are devastating the city.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Seven guberniyas occupy Lagrange points around Saturn while Supra City's Plates and Strips represent massive permanent zoku territory. The chapter references settlements on Mars (Sirr on Irem) and across the solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The characters operate entirely within the Saturnian system and broader solar system. Earth is referenced only as ancient history. Jean launches himself at the Sobornost fleet via thoughtwisp at near light speed, showing the vast scales involved.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Jean reveals that the zoku quantum jewel system was teetering near a quantum mechanical boundary, and he pushed it over with algorithmically generated spam zokus. The pellegrini made Mieli as an instrument. Social order is built on quantum entanglement and posthuman manipulation.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Characters communicate through qupts, Realms, and direct neural interfaces. Jean passes Perhonen's dying message to Mieli as a vision of butterflies and fire. Language is irrelevant when thoughts and memories are transmitted directly.",
        "q6": "Manageable but risky",
        "q6_justification": "Jean and Mieli exist comfortably in the Leblanc's Realm environments, but the surrounding space is filled with active combat. The environment is manageable with sufficient technology but the war makes everything precarious.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The entire human civilization lives in space. Supra City houses a massive population, the Sobornost guberniyas contain billions of gogol minds, and Oort is referenced as Mieli's distant home. Space habitation is universal.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features multiple competing entities: the zoku collective, the Sobornost (itself divided among Founders), the pellegrini faction, Jean as an independent agent, and the All-Defector as an emergent threat. The Oubliette on Mars is also referenced.",
        "q9": "Drama",
        "q9_justification": "The chapter is intensely dramatic and emotional. Jean and Mieli confront grief over Perhonen's death, the revelation that Sydan worked for the pellegrini, and Jean's guilt over enabling the Sobornost invasion. The emotional core drives the narrative.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Leblanc is a personal ship used for both escape and combat. The ongoing war engulfs civilian infrastructure like Supra City's Plates, while Jean and Mieli plan a heist rather than a military operation to resolve the crisis.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean travels as a thoughtwisp, a mirror flake of thought pushed by lasers. The chapter's key events unfold in virtual Realms. Jean's plan involves quantum information, Planck branes, and gravitational waves rather than physical territory.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Characters exist as quantum information in photonic crystals, travel as thoughtwisps at relativistic speeds, and inhabit virtual Realms. The physical environment includes guberniyas, mass streams, and the computational substrate of posthuman existence.",
    },
    {
        "chapter": "Chapter 17",
        "q1": "Total war / constant conflict",
        "q1_justification": "Jean travels through the massive Sobornost fleet attacking Saturn, passing through raion formations, kilometre-long oblast ships, and a colossal mirror system designed to redirect stellar lasers. The battle rages on multiple fronts simultaneously.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chen guberniya is a diamond sphere ten thousand kilometres in diameter, an artificial world with a living fractal surface where every dust particle is a gogol. Seven such guberniyas occupy the Saturnian system's Lagrange points.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Jean enters the guberniya as a thoughtwisp travelling at nearly the speed of light. The action takes place deep within the Sobornost's artificial worlds, completely removed from anything resembling Earth or baseline human experience.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Inside the guberniya, gogol minds are governed by xiao, an instinctive respect hierarchy that rewrites perception of reality. Deep Time simulations run for millennia. The chen-gogol Jean encounters has evolved into a centipede-like form through deep vir evolutionary processes.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Jean communicates through Founder codes, qupts, and direct neural manipulation. He overwrites a chen gogol's mind using a story from Axolotl the body thief. Communication operates at the level of mind control and information transfer, not language.",
        "q6": "Manageable but risky",
        "q6_justification": "Within the guberniya's virtual environments, survival depends on having the right codes and mental defenses. Jean navigates using stolen Sumanguru Founder codes but faces constant risk of detection and erasure.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The guberniya contains an entire ecosystem of billions of gogol minds across countless virtual layers. Raions pour from fabber pits in wave after wave. Space habitation at astronomical scales is the norm.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter shows internal Sobornost politics with different Founder factions (Sumanguru, Chen, pellegrini), plus the All-Defector as an independent viral entity controlling the chens. The zoku continue fighting externally.",
        "q9": "Adventure / exploration",
        "q9_justification": "Jean infiltrates the chen guberniya in a daring solo mission, disguising himself with stolen Founder codes, manipulating gogol bureaucracy, and racing to find Matjek before the boy can trigger a doomsday weapon. It is a classic heist-adventure infiltration.",
        "q10": "Mostly military",
        "q10_justification": "The chapter takes place entirely within the Sobornost military machine. Jean passes through raion formations, navigates guberniya military hierarchy, and confronts the All-Defector. The environment is saturated with warminds and combat operations.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean infiltrates the guberniya through virtual layers, flattening virs into corridors, manipulating firmament code, and evolving gogol populations to sift data. The entire infiltration is a cyberspace operation through nested virtual environments.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The guberniya is a ten-thousand-kilometre diamond sphere with a fractal smartmatter surface where every particle is a thinking being. Inside, reality is layered virtual environments governed by Founder codes and firmament. Physics is computational.",
    },
    {
        "chapter": "Chapter 18",
        "q1": "Total war / constant conflict",
        "q1_justification": "Mieli pilots through a Sobornost storm of gamma ray lasers and raion swarms. War rages in both physical space and virtual Realms, where weaponised gogols invade zoku realities. The entire chapter is set during the ongoing total war for Saturn.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Supra City remains a massive settled territory under siege. The Sobornost fleet occupies the Saturnian system. Zoku Realms serve as additional inhabited territories, and the chapter references infrastructure deep within Saturn's metallic hydrogen layer.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The action takes place in the Saturnian system and in virtual Realms. Mieli transforms herself from physical form into quantum information to pass through a Realmgate. Earth is entirely absent from consideration.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Mieli creates a viral zoku using the Kaminari template to manipulate collective volition. The zoku social order operates through entanglement levels, twinking, and quantum coordination. Mieli must game this system to obtain Planck brane tanglematter.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Mieli and Zinda communicate through qupts across vast distances. The viral zoku spreads through quantum-mediated thought transmission. All meaningful communication is technologically mediated.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Mieli must strip the Leblanc down to barely more than its drive sphere to survive, and ultimately sacrifices the ship entirely to escape through a Realmgate. The Sobornost-filled space is actively lethal, requiring extreme measures to traverse.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Massive populations inhabit Supra City, Realms, and guberniyas. Zoku members fight in virtual battlefields and physical space simultaneously. A guerrilla operation runs on reversible computation inside Saturn's metallic hydrogen layer.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features the Great Game zoku, Spooky-zoku, Ganimard-zoku, the newly created Liquorice-zoku, the Sobornost fleet with multiple Founder factions, and the pellegrini as a separate entity. The political landscape is deeply fragmented.",
        "q9": "Adventure / exploration",
        "q9_justification": "Mieli undertakes a daring mission: escaping Sobornost forces, reuniting with Zinda, creating a viral zoku to hack the collective volition system, and obtaining the Planck brane tanglematter. It reads as a high-stakes heist-adventure.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Leblanc is a civilian ship pressed into combat duty. Mieli fights in Realm battles to earn entanglement, then uses the zoku's civilian governance system (volition) for military purposes. The domain blurs military and civilian functions.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Mieli transforms herself into quantum information to pass through a Realmgate. War occurs simultaneously in physical space and virtual Realms. The key objective is obtaining tanglematter through quantum teleportation protocols and volition hacking.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Mieli converts her physical body into a foglet wedge of quantum information. The Leblanc's micro-singularity engine collapses into a white hole. Tanglematter involves EPR states distilled from neutralinos using Saturn as a detector, entangled with supersymmetric matter on another brane.",
    },
    {
        "chapter": "Interlude (3)",
        "q1": "Total war / constant conflict",
        "q1_justification": "The interlude takes place during the ongoing Sobornost-zoku war. The All-Defector describes its plan to remake the entire Universe, motivated by existential competition with hypothetical entities from other spacetimes.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The All-Defector controls the chen guberniya and much of the Sobornost fleet. The pellegrini is referenced as having her own guberniya. The scale of territorial control is planetary and system-wide.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The All-Defector discusses other spacetimes beyond the causal horizon of the Universe itself. The scale of distance and separation extends beyond the solar system to cosmological and even multi-universal scope.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The All-Defector is a game-theoretic anomaly that becomes whoever it encounters, running simulations to predict behavior. Josephine exists as one of many copies, unable to distinguish if she is real or a simulation. Social order has dissolved into computational manipulation.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication occurs through direct mind-to-mind exchange in virtual environments. The All-Defector whispers Founder Codes that reshape reality. Language is irrelevant in this context of pure information exchange.",
        "q6": "Manageable but risky",
        "q6_justification": "Within the virtual environment, physical survival conditions are not the primary concern. The risk is cognitive and existential rather than environmental, as the All-Defector can erase minds at will.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The entire narrative takes place among posthuman entities for whom space habitation is the default. Josephine and the All-Defector exist within guberniyas as uploaded minds, representing billions of gogol inhabitants.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Even within this short interlude, multiple factions are referenced: the pellegrini, the chens (now controlled by All-D), the other Sobornost Founders, and the zoku. The All-Defector itself represents a new independent power.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The interlude is deeply unsettling as Josephine faces the All-Defector, a being that perfectly predicts and controls her. It raises existential horror about simulated consciousness and the impossibility of resistance. The tone is psychological horror.",
        "q10": "Mostly military",
        "q10_justification": "The context is the ongoing total war. The All-Defector's entire purpose is conquest and universal domination. Josephine is effectively a prisoner of war within a military entity.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The entire interlude takes place in a virtual dream-vir. The All-Defector operates as a computational entity running simulations. Space is characterized as a domain of information and game theory rather than physical territory.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment is a virtual reality within a guberniya. The All-Defector discusses remaking spacetime itself and the possibility of viral spacetimes from beyond the causal horizon. Physical reality is subordinate to computational abstraction.",
    },
    {
        "chapter": "Chapter 19",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chapter shows Saturn's rings torn apart, Plates shattered, Strips broken, and von Neumann beasts consuming matter. Zoku forces are decimated and sunbeam mirrors are about to deliver a final blow. Jean sacrifices himself to defeat the All-Defector.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The battle rages across Supra City's Plates and Strips, with the Sobornost occupying Lagrange points. The Aun faction defends the Plate of Irem. The scale of settled territory being contested is enormous.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The action is entirely within the Saturnian system and inside virtual environments within a guberniya. Earth is completely irrelevant to these posthuman conflicts.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Jean battles the All-Defector through a game-theoretic duel involving simulations of consciousness. He creates a Jean le Flambeur-complete computational problem, spawning billions of simulated versions of himself. Social interaction has become pure game theory.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Jean and the All-Defector communicate directly in a shared virtual space. Jean passes escape protocols to Josephine through direct information transfer. All communication is technologically mediated.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The physical space around Saturn is devastated by war, with black holes, X-ray fountains, and von Neumann beasts. Jean exists only as information within a hostile virtual environment where the All-Defector can erase him at will.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Vast populations fight and die across Supra City. Billions of gogol minds inhabit the guberniya. The entire conflict involves posthuman civilizations for whom space is the only habitat.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features the All-Defector, the pellegrini (Josephine), the zoku forces, the Aun faction defending Irem, the Sobornost fleet, and Jean's independent operation. Multiple factions with conflicting goals coexist.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Jean faces the All-Defector in a desperate psychological duel where his every thought is predicted. The tension builds as he tries to create enough simulations of himself to find one escape route among billions, culminating in his apparent sacrifice.",
        "q10": "Mostly military",
        "q10_justification": "The chapter is dominated by the total war around Saturn and Jean's combat with the All-Defector. Von Neumann beasts, sunbeam weapons, kinetic pellet sheets, and Dragon weapons define the military character of space.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean's battle with the All-Defector is fought through simulations, memory associations, and computational problems. He tries to force the All-Defector to run a full simulation of Jean le Flambeur, turning the conflict into a computational resource war.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Saturn's surface shows a boiling black hole shooting X-ray fountains. Jean exists as information within a virtual environment, battling through game theory and spawning simulated copies of himself. The environment is purely computational.",
    },
    {
        "chapter": "Chapter 20",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chen guberniya is destroyed by the dragon jewel. The Sobornost fleet regroups and sunbeam mirrors prepare to annihilate Supra City. Barbicane confronts the Liquorice-zoku at the Arsenal, and Mieli is fired into Saturn via the ekpyrotic cannon.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The pellegrini withdraws her guberniya fleet. The Gun Club's Arsenal on Iapetus contains massive weapons. Supra City remains a vast inhabited territory. The scale of permanent settlement and territorial control spans moons, planets, and artificial worlds.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Mieli is fired into Saturn's core and then transmitted to the Planck brane, a parallel universe. The distance transcends physical space entirely, moving between branes of reality.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Barbicane reveals he manipulated events to destroy the Kaminari jewel and start a new Game. The Liquorice-zoku is a viral creation. Mieli merges with the Kaminari jewel and becomes all possible versions of herself simultaneously, transcending any recognizable social order.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Mieli and Matjek communicate through Liquorice-zoku jewel qupts while Barbicane holds them frozen. The pellegrini speaks and blows a kiss that heals Mieli's scar. Communication operates through quantum and supernatural channels.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Mieli is fired into Saturn's metallic hydrogen core, where the environment is utterly lethal. On the Planck brane, she exists as a bubble-thin boundary in an alien liquid medium where huge entities pass beneath her. Survival requires complete transcendence of physical form.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter features massive populations across Supra City, guberniyas, and moons. Space habitation is universal. Even the Planck brane has been colonized with solitonic computational platforms by the zoku.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The pellegrini withdraws independently, Barbicane acts against his own zoku's volition, the Liquorice-zoku operates as rebels, and the remaining Sobornost Founders regroup. Multiple competing authorities with different agendas persist even at the climax.",
        "q9": "Adventure / exploration",
        "q9_justification": "Mieli's journey to the Planck brane is the ultimate exploration, traveling to a parallel universe to find the Kaminari jewel. She perceives an alien liquid environment, senses a huge entity passing beneath her, and touches the jewel to reshape reality through song.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Arsenal is a military installation, and Barbicane wields military authority. But Mieli's mission is ultimately about using the Kaminari jewel to save everyone, a civilian goal. The pellegrini's withdrawal is a political-military act with civilian consequences.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Mieli is qupted into the gunscape as quantum information, fired through the ekpyrotic cannon, and transmitted via gravitational waves to the Planck brane. The climax unfolds in a purely abstract domain of solitonic states and alien physics.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The Planck brane is governed by alien physics where everything is liquid and perception is flow. Mieli's bubble-self wavers in the wake of vast entities. The ekpyrotic cannon uses four black holes to pulse Saturn's core and transmit gravitational waves between branes of reality.",
    },
    {
        "chapter": "Epilogue",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The war is over but rivalry persists. Josephine plans new conflicts with other Founders and schemes against her Sobornost siblings. The zoku have been transported to a new reality, but the Sobornost factions remain in competition.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Josephine surveys from her guberniya. Supra City has been transported to a new world. The Sobornost Founders still control vast territories. The Dilemma Prison remains as a permanent institution. Territory is held at civilization-scale.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Saturn has vanished entirely, transported to another brane of reality. Mieli and Zinda exist in a new universe completely separate from the old one. Jean is in the Dilemma Prison, location unknown. Separation is absolute and inter-universal.",
        "q4": "Radically different / alien social order",
        "q4_justification": "In the new world, reality is malleable like vaki and Realms can be made without machines. Josephine commands a billion gogols through xiao. The Archon guards the Dilemma Prison as a computational entity seeking patterns. No aspect of society resembles Earth.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Josephine steps into the minds of a billion gogols simultaneously. Mieli and Zinda communicate casually in their new reality. The Archon operates through pure computation. Language as such is irrelevant.",
        "q6": "Benign / easily survivable",
        "q6_justification": "In the new world, Mieli and Zinda lie in warm sunlight eating peaches. Reality is malleable and comfortable. Even in the old universe, Josephine relaxes in her guberniya drinking wine. The epilogue presents space as settled and survivable.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "All of posthumanity lives in space or space-derived environments. Josephine's guberniya, Supra City in the new world, and the Dilemma Prison all represent ordinary habitation for their inhabitants.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Josephine schemes against the hsien-kus and vasilevs, notes Chitragupta and Sasha will be distracted, and the sumangurus need targets. The zoku are in a separate universe. The political landscape remains deeply fragmented among Sobornost Founders.",
        "q9": "Drama",
        "q9_justification": "The epilogue resolves the trilogy's emotional arcs: Josephine grieves Jean while planning her next move, Mieli finds peace with Zinda in a new world, and Jean escapes the Dilemma Prison through a door of light. The tone is reflective and cathartic.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The epilogue shifts away from war. Josephine plans future conflicts but is currently drinking wine. Mieli and Zinda are at peace in their new world. Jean escapes a prison. The military domain has receded.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Josephine steps into a billion gogol minds simultaneously. The Archon seeks computational patterns in the Prison's grid. Reality in the new world is malleable like software. Space remains characterized as a computational-informational domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The new world has malleable reality without machines. Saturn has vanished, leaving only a gravitational shadow. The Dilemma Prison is built of computronium governed by an Archon. The physical environment is fundamentally unlike anything on Earth.",
    },
]

country = 'Finland'
book_title = 'The Causal Angel'
csv_path = 'data/results/Finland_The_Causal_Angel.csv'

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
