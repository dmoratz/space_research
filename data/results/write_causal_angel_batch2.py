import json, csv, os

chapters_data = [
    {
        "chapter": "Interlude",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter depicts ongoing rivalry among Sobornost Founders, with Josephine navigating backstabbing siblings and a fanatic (Matjek Chen) who wants to conquer death. Jean plans to steal the Kaminari jewel from Chen, indicating strategic disputes over powerful artefacts.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Josephine inhabits computronium beneath a planet's crust and controls a singularity, while the Sobornost guberniyas span the solar system. Jean has been living on Mars, and references to the System map in the sky suggest widespread territorial holdings.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Jean mentions not having seen Josephine for nearly two hundred years, and his visit to her labyrinth temple in the shadow of Kunapipi Mons implies vast distances across the solar system. Earth is a distant memory in this far-future setting.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Josephine exists as a vast computational entity embedded in a planet's crust and a black hole's event horizon, creating images of herself from Hawking radiation. The social order involves gogol copies, copymothers, and branching selves, which is fundamentally alien to any Earth society.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication occurs through gamma rays, vir environments, and direct mind-to-mind contact within virtual spaces. Josephine speaks in a voice made of gamma rays and vaporises Jean into a mindshell, bypassing conventional language entirely.",
        "q6": "Manageable but risky",
        "q6_justification": "Jean requires heavy zoku armour and quantum jewels to survive near Josephine's singularity, and she casually vaporises him to transfer him into a vir. Physical space near black holes is hostile, but advanced technology makes it manageable for those equipped.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter presents existence in space as completely ordinary. Josephine lives in planetary computronium, Jean has been on Mars for centuries, and the System map of interconnected space habitats is visible in the sky like a spiderweb.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter references the Sobornost Founders as competing siblings, the zoku as a separate faction (Jean wears zoku armour), and Mars as an independent settlement. These are distinct political entities with different governance structures.",
        "q9": "Drama",
        "q9_justification": "The chapter is an intimate, emotionally charged encounter between two former lovers. Jean gives Josephine a flower as a way to find him if he is captured, and the scene ends with her deciding to betray him to Matjek Chen. The focus is on relationships and personal motivations.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on personal relationships and political intrigue rather than military operations. However, Josephine mentions warmind gogols that she uses to scan the flower for traps, and she references wars and factional conflicts among Founders.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is characterized through computational and informational metaphors. Josephine exists as distributed computronium, the System is mapped as a spiderweb of connections, and conflict occurs through gogol warfare and information encoding rather than physical naval or aerial combat.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The physical environment includes a black hole singularity, Hawking radiation used as a communication medium, and virtual reality spaces where time runs at picosecond rates. Josephine's body spans a planet's crust and an event horizon, which is fundamentally unlike any Earth experience."
    },
    {
        "chapter": "Chapter 9",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter depicts an active battle between Sobornost raion fleets near 624 Hektor, with pellegrini, hsien-ku, and vasilev forces clashing. The battle turns out to be a coordinated fake designed to trap Mieli, and the All-Defector reveals it has united the factions against external threats.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Sobornost controls fleets of raions throughout the solar system, while the zoku operate ships and habitats. The Jovian Trojan asteroids serve as a contested zone, and multiple factions maintain permanent presence across different regions of the solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The action takes place in the Jovian Trojan belt near asteroid 624 Hektor, far from Earth. The setting is a far-future solar system where Earth is barely relevant, and distances are measured in lightspeed communication delays.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The social order involves posthuman factions like the Sobornost copyclans, zoku game-theory collectives with entanglement jewels, and entities like the All-Defector that can model and absorb opponents. Mieli uses combat autism and has a fusion reactor in her thighbone.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication occurs through coded military protocols, qupt links (quantum communication), and EM whispers. The All-Defector communicates via Sobornost military protocol targeted at Mieli's systems. Language differences are irrelevant due to technological mediation.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Mieli is ejected into hard vacuum on Hektor's surface with a pierced side, bleeding and losing blood that boils in vacuum. She has only ten minutes to survive without external life support, and faces antimatter explosions, kinetic missile barrages, and gamma ray bombardment.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Hundreds of raion ships operate throughout the Trojans, the zoku crew lives aboard the Zweihander in its miniature forest habitat, and space operations are routine. Living and fighting in space is completely ordinary for all characters.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter features the pellegrini, hsien-ku, and vasilev Sobornost copyclans as distinct factions, plus the zoku (specifically the Liquorice-zoku and Great Game). The All-Defector represents yet another emergent power that has co-opted some of these factions.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by a space battle between Sobornost fleets, followed by intense personal combat between Mieli and the All-Defector on Hektor's surface. Mieli overloads her fusion reactor in a desperate last stand.",
        "q10": "Mostly military",
        "q10_justification": "The entire chapter is focused on military operations: fleet engagements, electronic warfare, kinetic missile volleys, and personal combat. Mieli operates as a military operative on a Great Game intelligence mission to capture a Sobornost political officer.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The battle involves electronic warfare ghosts fighting through firewalls, ghostgun bullets carrying war gogols, and information warfare alongside physical combat. The All-Defector operates by modeling opponents computationally and the battle is as much about data and software as physical weapons.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment includes hard vacuum on an asteroid with 0.13 km/s escape velocity, antimatter explosions, combat in quicktime where milliseconds are experienced as minutes, and Mieli's body containing fusion reactors and q-dot weapons integrated into her physiology."
    },
    {
        "chapter": "Chapter 10",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Jean le Flambeur is pursued by the Great Game Zoku as glittering ships arrange in the sky above the newly rebuilt Sirr on Saturn's Irem Plate. The chapter also references the Collapse as a past catastrophic conflict and Jean's ongoing disputes with multiple factions.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter is set on Saturn, on an artificial continent called the Irem Plate larger than Earth. The city of Sirr is rebuilt there with its entire desert ecosystem. References to the Sobornost Station, Mars, and other settled regions confirm extensive territorial occupation throughout the solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The chapter takes place on Saturn, and Tawaddud and Dunyazad have been brought from Earth (preserved in a book) to this distant location. Earth's civilization has collapsed, and the characters now inhabit an artificial world in the outer solar system, completely separated from their origin.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter juxtaposes the quasi-medieval culture of Sirr (with its Secret Names, jinn, and muhtasib councils) against the zoku collective society and the Sobornost upload civilization. Jean has been the Flower Prince of the Aun, digital desert entities. These are radically alien social orders.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters from Sirr use Arabic-influenced terminology (muhtasib, qarin, mutalibun, Banu Sasan) while Jean and the zoku use different vocabulary. They communicate directly but their cultural and linguistic frameworks differ significantly, suggesting a shared lingua franca with strong local variation.",
        "q6": "Manageable but risky",
        "q6_justification": "The Irem Plate provides a habitable environment with diffuse sunlight and breathable air inside transport bubbles. However, the wildcode desert is dangerous, the Aun are unpredictable entities, and zoku pursuit ships arrive threatening Jean's safety.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "An entire city with its population is being rebuilt on an artificial continent on Saturn. The zoku civilization spans Saturn's moons and rings, with transport bubbles and Realmgates as ordinary infrastructure. Living in space is completely normalized.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter features the zoku who rule Saturn, the Sobornost (referenced through the Founders and their Station), the people of Sirr as an independent community, and the Aun as autonomous digital entities. These are distinct political groupings with different governance.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter centers on Jean le Flambeur rebuilding the city of Sirr on Saturn, learning about his role in the Collapse from the Aun, and preparing for his next quest. Tawaddud's exploration of the reborn city and Jean's ongoing journey give it an adventure tone.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on civilian activities: rebuilding a city, exchanging gifts, personal conversations, and philosophical revelations. However, the arrival of zoku pursuit ships and references to the Sobornost invasion introduce a military element.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is characterized through information and computation. The city of Sirr is grown from a smartmatter seed, the Aun are digital entities born from wildcode, and Jean's conflict involves zoku entanglement networks and Notch-zoku identity rather than physical naval or territorial metaphors.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment is an artificial Plate on Saturn with interlocking geometric ground tiles, soletta twilight, dynamic support beams, and a wildcode desert that spawns sapphire-fingered jinni. Cities are grown from fractal seeds and people are restored from quantum information in books."
    },
    {
        "chapter": "Interlude (2)",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chapter depicts the Collapse: a catastrophic global event triggered by Jean's financial weapon that destroys the world's markets, causes cities to fall from the sky, unleashes wildcode that consumes minds, and forces a mass exodus to space. This is total civilizational conflict.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Sobornost Founders fled to space in nanosatellite swarms and built guberniyas. Josephine references the first war where they fought to liberate uploaded minds, and the Founders vowed to expand and build resources unbound by Earth. The system-wide infrastructure is extensive.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The chapter spans centuries of history, from Earth to the far-future solar system. The Founders fled to orbit and expanded through space, and Josephine's memories cross vast temporal and spatial distances. Earth is a lost origin point.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter describes a world of gogol labour markets, quantum financial instruments determining who lives or dies, black box uploading, and corporate entities repossessing human bodies. The zoku escape on crowdfunded ships while gogols are beamed to the Sobornost. This is radically alien.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication occurs through beemee feeds, lifestreams, smartbed interfaces, and direct mind-technology links. Josephine's bed provides annotations in her field of vision. Language as such is mediated entirely through technology.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The Collapse creates extreme hostility: weather ghosts make winds dance like whips, Sirr falls from the sky, wildcode consumes minds, repo bots reclaim bodies, and upload cities shut down. Survival pressure is constant and overwhelming during this catastrophic event.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter describes gogol labour markets, virtual economies, mass uploading, and the Founders living in nanosatellite swarms in orbit. The great exodus at the Collapse sends the zoku and gogols into space. Space habitation is already widespread before the crisis.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The pre-Collapse world features struggling nation states, corporations, liquid democracies, the Sobornost Founders, and the infant zoku, all competing. The quantum markets create a complex web of financial entities controlling life and death across multiple political structures.",
        "q9": "Drama",
        "q9_justification": "The chapter is a deeply emotional backstory about Josephine's last birthday, her relationship with Jean, and the catastrophic consequences of his gift. The intimate scene of an elderly woman being uploaded while the world burns around her is intensely dramatic.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter spans both civilian and military spheres. The first war involved an army Josephine built, but the Collapse is triggered through financial manipulation rather than military action. The aftermath involves both military responses (hsien-ku fleets) and civilian catastrophe.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The central conflict is waged through quantum financial markets and information systems rather than physical military force. Jean's weapon is a machine made of money that collapses global markets, and the wildcode is a digital plague that consumes minds through networked systems.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The chapter describes quantum markets with entangled derivatives, gogol labour economies, black box uploading via cranial devices, and wildcode that rewrites reality. Even on Earth, the physical environment has been transformed by technology into something fundamentally unlike baseline human experience."
    },
    {
        "chapter": "Chapter 11",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter reveals that the Sobornost civil war is a sham concealing preparations for an invasion of Supra City. The Great Game Zoku is gathering intelligence and preparing defenses, indicating ongoing strategic rivalry between the Sobornost and zoku factions.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The zoku inhabit the vast infrastructure of Supra City on Saturn with Strips, Plates, and Realmgates. The Sobornost controls the Inner System with guberniyas and Hawking drives. Mieli recalls her Oort Cloud koto. Multiple factions hold extensive territories across the solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Mieli is from the Oort Cloud and now resides in Supra City on Saturn. Her lover Sydan is trapped in a black hole on Venus. These vast distances across the solar system represent extreme separation from any Earth-centric frame of reference.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Zoku society operates through entanglement jewels, quantum collectives, Realms, and Circles with elaborate rules. Mieli has levels in different zoku (Level Twelve Badass). Social disputes are resolved by rock-paper-scissors. A rebirth party features zombies, werewolves, and egg hunts as cultural norms.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Characters communicate through qupt links alongside spoken language, with zoku jewels transmitting subliminal emotional content. Barbicane holds parallel spoken and qupted conversations simultaneously. Communication technology makes conventional language barriers irrelevant.",
        "q6": "Benign / easily survivable",
        "q6_justification": "Supra City provides a comfortable, Earth-like environment with forests, rivers, warm air, and paper lanterns. Mieli's new body was rebuilt after the battle, and the habitat is designed for pleasant living. The environment itself poses no survival challenges.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Supra City is a vast civilization on Saturn with elaborate social structures, parties, and everyday life. The Gun Club Zoku builds warships casually, kaijuforms walk around, and rebirth parties are social events. Space habitation is completely ordinary.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter features multiple zoku (Great Game, Liquorice, Gun Club, Big Game, Dancing Cat, Huizinga) as distinct sub-polities within Supra City, plus the Sobornost as an external threat assembling forces in the Broken Places of Jupiter-that-was.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on Mieli's emotional recovery after near-death, her conflicted feelings about her mission and Sydan, and the social dynamics of a rebirth party. The personal drama of her internal conflict and interactions with Zinda and Barbicane drive the narrative.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter alternates between civilian party scenes and military intelligence briefings. Mieli discusses the coming Sobornost invasion with her zoku team, while simultaneously attending an elaborate social gathering with the Gun Club Elder Barbicane.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is characterized through networked, game-theory frameworks. The zoku operate through entanglement levels and quantum jewels, intelligence is processed through spimescapes, and the coming war is discussed in terms of game levels and entanglement scores rather than naval or air power metaphors.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Mieli's rebuilt body contains a metacortex and tactical gogols with unfamiliar interfaces causing phantom pains. The environment includes Realms, Realmgates, transport bubbles, and Strips with solettas. While habitable, the physical reality constantly requires technological adaptation."
    },
    {
        "chapter": "Chapter 12",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Jean is pursued by over two hundred zoku ships forming a Ganimard-zoku specifically created to catch him. He escapes through Saturn's atmosphere using the Aun's wildcode desert as a weapon, while Barbicane threatens him with information retrieval specialists.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The action spans Saturn's Plates, Strips, and deep atmosphere. The zoku control Supra City and its infrastructure, while the Notch-zoku maintain territories like Vipunen the Elder's hurricane-body storm. Jean references Mars and the Oubliette as other settled regions.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The chapter takes place entirely in the Saturn system, far from Earth. Jean navigates between Plates, dives into Saturn's sub-troposphere, and references his past life on Mars. Earth is only a distant memory accessed through the Leblanc's Realm environments.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Society operates through zoku collectives that spontaneously form new organizations (the Ganimard-zoku) to pursue a single thief. Jean uses a Notch-zoku identity built through concept mining and notchcube grinding. The Leblanc's Library stores past selves like a Sobornost concept.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Jean and Barbicane communicate through qupt links that carry not just words but sensory impressions like aftershave smell and hollow brass echoes. Ship-to-ship communication uses coded protocols and entanglement beams. Technology mediates all communication.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Jean must use a Hawking drive and wildcode desert allies to escape through Saturn's atmosphere, dodging antimatter fire and electronic warfare. The environment requires constant technological support, but with proper equipment survival is achievable.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Over two hundred diverse ships from multiple zoku chase Jean through Plate space, including Dyson trees, Replicators, and baseline quicksuits. The wildcode desert on Irem is populated by body thieves and Aun. Space habitation is completely routine.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter features the Great Game Zoku, the Notch-zoku (with Elder Vipunen), the newly formed Ganimard-zoku, the Evangelion-zoku, and references to the Sobornost as a separate civilization. These are distinct polities with different governance and objectives.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is a classic heist-and-chase adventure. Jean escapes a massive zoku fleet, dives into Saturn, then explores the Leblanc's hidden Library through the crystal stopper book, discovering his past selves in a quest for Prime authorization.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "While the chase involves warships and weapons, the conflict is essentially a police action by the Ganimard-zoku detective collective against a thief. Jean's exploration of his own past in the Leblanc's Realms is entirely personal and civilian in nature.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The pursuit involves information attacks boring into firewalls, electronic warfare, and body thieves manipulating collective volition through code fragments and stories. Jean's key breakthrough comes through navigating virtual Realm environments and accessing digital memory archives.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment includes Saturn's sub-troposphere layers, wildcode deserts spawning mountain-sized jinni, Plate-scale artificial continents, and Realm environments where virtual reality is indistinguishable from physical reality. The Leblanc navigates using a Hawking drive through gas giant atmospheres."
    },
    {
        "chapter": "Chapter 13",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter references the impending Sobornost invasion and the zoku's preparations, but the immediate focus is on Mieli and Zinda's personal interactions during an egg hunt. Mieli probes for information about the Kaminari jewel, indicating ongoing strategic rivalry.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Supra City spans vast Strips and Plates around Saturn, with the Sobornost controlling the Inner System. Mieli references Venus where Sydan is trapped, and the zoku civilization encompasses multiple moons and ring structures. Territory is held across the entire solar system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Mieli is on Saturn while Sydan is trapped in a black hole on Venus. The Kaminari-zoku departed the known Universe entirely. Earth is a distant historical reference. The distances and separations are extreme and effectively permanent.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Zoku children are born with a designed purpose (Zinda was made specifically for Mieli). Social conflicts are resolved through entanglement mechanics, and individuals can remove their quantum jewels to strip away their collective identity. This is a fundamentally alien social structure.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication occurs through spoken language supplemented by qupt links and entanglement connections through zoku jewels. Zinda boosts Mieli's entanglement levels by touching jewels together. The technology makes conventional language barriers irrelevant.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The environment is a comfortable woodland garden on a Saturn Strip with warm night air, a river, paper lanterns, and gentle breezes. The party Circle provides a safe, pleasant setting with no environmental hazards.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The characters casually enjoy a party on Saturn's infrastructure, discussing theoretical computer science and the nature of the Universe over champagne. Living on artificial worlds around Saturn is completely normalized everyday experience.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Zinda describes multiple distinct groups: the Sobornost with their Great Common Task, the various zoku collectives (Great Game, Spooky, Kaminari), and references to pre-Collapse nation states and corporations. The political landscape features multiple competing polities.",
        "q9": "Drama",
        "q9_justification": "The chapter is driven by the romantic and emotional drama between Mieli and Zinda. Mieli confesses her true motives, Zinda reveals she was made specifically for Mieli, and their intimate encounter is complicated by guilt, deception, and conflicting loyalties.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter is set entirely at a civilian party and focuses on personal relationships. However, discussions of the Sobornost invasion, the Kaminari jewel as a strategic asset, and Mieli's intelligence-gathering mission provide a military undercurrent.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Zinda explains the Kaminari jewel in terms of computational complexity (NP-complete problems, Planck locks, quantum gravity computers, closed timelike curves). Space and reality are characterized as computational substrates rather than physical domains like ocean or air.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "While the party environment is comfortable, the underlying reality involves zoku jewels that define identity, Planck-scale physics that constrains computation, and bodies that can be rebuilt from scratch. The physical environment is technologically mediated and fundamentally different from Earth."
    },
    {
        "chapter": "Chapter 14",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Jean le Flambeur confronts his past self (a partial) in the Gallery, learning about the failed theft of the Kaminari jewel and the Great Game's deception. The Ganimard-zoku pursues him outside, and his partial threatens to release more le Flambeurs from the Prison.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter references the Sobornost's system-wide control, the zoku civilization, Mars and its Oubliette, and the Prison. The past self describes System-wide operations spanning the solar system, confirming extensive territorial occupation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Jean's origin story begins in a North African desert on Earth, but the main narrative takes place aboard a ship in Saturn's depths. The journey from that Earth childhood to the far-future solar system represents an extreme, effectively unreachable distance in both space and time.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter reveals a society where people store past selves in crystal galleries, where evolutionary algorithms are used to create new versions of individuals, and where a zoku jewel computes the Universe's coherent extrapolated volition. This is radically alien to any Earth social order.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Jean communicates with his past partial self through the Leblanc's virtual Realm environment, where the ship's systems mediate all interaction. The partial provides information through encoded quantum whisky and Prime authorization keys embedded in drinks.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Jean is hunted by the Ganimard-zoku and must hide in Saturn's sub-troposphere. His past self describes the Kaminari jewel quest as extremely dangerous, and the Dilemma Prison is referenced as a harrowing experience. Survival requires constant resourcefulness and advanced technology.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Jean casually inhabits a ship with virtual Realm environments, his past self describes System-wide thievery as routine, and the Society zoku simulated an entire parallel biosphere to produce whisky. Space habitation is completely ordinary and mundane.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter references the Sobornost, the Great Game Zoku, the Kaminari-zoku, the Ganimard-zoku, the Society zoku, and the Oubliette on Mars. These represent multiple distinct political entities with different structures and goals.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is a classic heist narrative. Jean explores the Gallery of his past selves, learns about the Kaminari jewel and its true nature, outsmarts his past self by stealing his key, and declares his intention to save Mieli and end his thieving career.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on Jean's personal quest and his confrontation with his past self, which is a civilian matter. However, the Ganimard-zoku pursuit and references to the Sobornost invasion provide military context.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The Kaminari jewel works by computing the Universe's coherent extrapolated volition through quantum gravity. The Gallery is a virtual-physical hybrid space storing selves as information. Space is characterized as a computational domain where reality itself can be reprogrammed.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment includes a crystal gallery storing consciousness in glass cells, a ship's Realm that is indistinguishable from physical reality, and a jewel that can rewrite spacetime itself. The Planck locks, quantum gravity computers, and false vacuum bubbles represent physics fundamentally unlike Earth experience."
    }
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

print('Done with batch 2.')
