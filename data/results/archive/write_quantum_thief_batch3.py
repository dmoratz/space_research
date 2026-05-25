import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 15 - The Thief and the Goddess",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter centers on a tense negotiation between Jean, Mieli, and the cryptarch Robert, who represents a powerful faction controlling the Oubliette. There is ongoing rivalry between the cryptarchs, the tzaddikim, and the zoku colony, with each faction maneuvering for advantage.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is a permanent, governed settlement on Mars with its own immigration system, civil servants, and political factions. The cryptarchs maintain territorial control through their master key over the exomemory system.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The characters operate in a far-future solar system where Earth is a distant memory. Jean was in the Dilemma Prison for an eternity, and the Sobornost guberniyas are described as vast, separate domains. The separation from Earth is essentially total.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Oubliette's society is built on cryptographic privacy protocols (gevulot), citizens cycling between embodied life and serving as Quiet machines, and exomemory systems. The cryptarchs secretly control all memories through a panopticon system, which is fundamentally unlike any Earth society.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate in what appears to be a shared language with specialized terminology like gevulot, tzaddikim, cryptarchs, gogols, and co-memories. The underlying language is recognizable but heavily inflected with unique space-culture vocabulary.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter takes place within the controlled environment of the Oubliette, where survival is not a primary concern. However, the temporary Watch system can shut down visitors who run out of Time, as demonstrated when Jean tricks the Pellegrini into becoming a black statue.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Oubliette is a functioning city on Mars with a full civilian population. Multiple factions (Sobornost, zoku, Oort Cloud dwellers) inhabit various parts of the solar system. Living in space is completely ordinary for this civilization.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter reveals multiple competing power structures: the cryptarchs who secretly rule the Oubliette, the tzaddikim resistance, the zoku colony, the Sobornost (represented by Mieli's employer the Pellegrini), and Oort Cloud factions. Each has distinct governance and goals.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is driven by intrigue, betrayal, and suspense. Jean discovers the Oubliette is a panopticon, is physically controlled by Mieli, negotiates under duress with the cryptarch, and ultimately outmaneuvers the Pellegrini through a time-stealing trick in a tense confrontation.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The setting is primarily civilian, involving political negotiations, personal relationships, and espionage. Mieli has military capabilities and the Pellegrini controls her body, but the chapter focuses on civilian power dynamics, cryptographic systems, and political maneuvering.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space and power in the Oubliette are characterized through digital and cryptographic metaphors. The cryptarchs control territory through master encryption keys, gevulot trees, and exomemory manipulation. Perhonen discovers the panopticon through data analysis of encryption hierarchies, making this a networked domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The physical environment features bodies that can be appropriated by cryptarchs, temporary Watches that can turn visitors into statues, Sobornost bodies with enhanced capabilities, Oortian wings and q-dot enhancements, and a complete merging of digital and physical existence."
    },
    {
        "chapter": "Chapter 16 - The Thief and Memory",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Jean works against both the cryptarchs and Mieli's employer by sharing anti-cryptarch co-memories with Raymonde. The tzaddikim are preparing to challenge cryptarch control, and Jean races to recover his secrets before Mieli shuts him down, reflecting ongoing multi-faction rivalry.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is depicted as a permanent, livable settlement with parks, apartments, neighborhoods like Montgolfiersville and the Maze, and a full social life. Jean's flashback shows him living there for years, designing buildings and growing flowers.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Jean's memories reveal he has lived across the solar system for hundreds of years, as a man, gogol, zoku member, and copyfamily, in many bodies and forms. Earth is never referenced as a reachable destination. The separation is total and multi-generational.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter reveals a society where memories can be shared through co-memories, identities can be locked behind gevulot, people cycle through Quiet service, and Jean hid secrets inside friends' exomemories using custom Watches and picotech assemblers. This social order is completely unlike Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak a shared language but use specialized terms like gevulot, co-memory, exomemory, Quiet, and tzaddik freely. Isaac references the Torah, suggesting cultural linguistic continuity, but the vocabulary is heavily modified by space-culture concepts.",
        "q6": "Manageable but risky",
        "q6_justification": "Life in the Oubliette appears comfortable, with parks, apartments, fabbers, and social life. However, risks exist from the cryptarch surveillance system and the cycling through Quiet. The environment itself is managed but the social-technological systems pose dangers.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter depicts everyday life on Mars: friends meeting in parks, drinking vodka, visiting apartments, having relationships. Jean's flashback shows him living as an ordinary citizen for years. Space habitation is completely normalized.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Jean's memories reference stealing from the Sobornost and zokus, living as different faction members, and the Oubliette having its own independent governance. The tzaddikim, cryptarchs, and zoku colony all represent distinct political entities within the city alone.",
        "q9": "Drama",
        "q9_justification": "The chapter is deeply emotional and character-driven. Jean recovers lost memories of his relationship with Raymonde, visits his old friend Isaac knowing he may sacrifice their friendship, and confronts the painful price of reclaiming his past. The tone is melancholic and intimate.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is entirely focused on personal relationships, memory recovery, and emotional decisions. Jean meets Raymonde in a park, visits Isaac for vodka, and retrieves a key-gun. There is no military presence or action in this chapter.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Jean's memory palace is constructed from buildings, people, and entangled qubits, with secrets stored in friends' exomemories protected by cryptography. The entire concept of hiding treasures in a networked digital-physical memory system characterizes space as a cyberspace-like domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Jean recalls existing as a man, gogol, zoku member, copyfamily, and in particles of thinking dust. The physical environment includes bodies that can be remade, exomemories that extend consciousness beyond the body, and picotech assemblers embedded in buildings."
    },
    {
        "chapter": "Chapter 17 - The Detective and the Gordian Knot",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter depicts escalating conflict: the cryptarchs use the Voice to manipulate citizens into attacking zoku members, the tzaddikim publicly challenge cryptarch authority, violent mobs form, and Jean's machine causes an earthquake that reshapes the city. Multiple factions are in open strategic struggle.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is a governed city with distinct districts (Dust District, the Maze), public squares, transportation (spidercabs), and political institutions (the Voice). The zoku colony maintains its own defended territory within the city behind a q-dot bubble.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Eldest reveals that the Oubliette was originally a prison where criminals were placed inside terraforming machines, and the zoku came after the Protocol War to hide from the Sobornost. Earth is a distant historical reference, completely separate from the current civilization.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Eldest reveals the Oubliette was originally a prison, that its entire history including the Revolution was fabricated by the cryptarchs with zoku help, and that the Voice can implant violent false memories directly into citizens' minds. The social order is built on manufactured reality.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate in a shared language with extensive specialized vocabulary: gevulot, exomemory, tzaddikim, cryptarchs, phoboi, Realmspace. The underlying language structure is recognizable but heavily inflected with unique terms from this far-future culture.",
        "q6": "Manageable but risky",
        "q6_justification": "The city environment is normally comfortable but becomes dangerous as the cryptarchs incite mob violence and Jean's machine causes an earthquake. The zoku colony protects itself behind a q-dot bubble. The physical environment is managed but social-political conditions create real danger.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Oubliette contains a massive civilian population filling streets, agoras, and districts. The zoku colony is a separate community within the city. Multiple factions spanning the solar system are referenced. Space habitation is entirely ordinary.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter reveals the full political complexity: cryptarchs secretly ruling, tzaddikim challenging them publicly, the zoku colony as an autonomous enclave that helped create the system, the Sobornost as an external threat, and the Voice as a mind-control tool. The Eldest confirms the zoku made a deal with cryptarchs after the Protocol War.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter builds intense suspense as Isidore races through a city descending into chaos. The Voice implants violent false memories, mobs attack zoku members, an earthquake reshapes the city, and the revelation that the Oubliette was originally a prison creates a sense of horror about the constructed reality.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter shows civilian life disrupted by militarized forces: the cryptarchs deploy the Voice as a weapon, military Quiet are referenced as enforceable threats, tzaddikim use foglet technology in combat roles, and mobs form as proxy forces. The civilian domain is becoming militarized.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The conflict is waged through digital means: the Voice implants memories directly into minds, the cryptarchs use their master key to manipulate the exomemory network, and the tzaddikim distribute viral co-memories as counter-weapons. The battlefield is fundamentally a networked information space.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The physical environment features a walking city that stops moving, buildings with smart-matter skeletons that reshape during an earthquake, a zoku colony that folds and changes shape like origami, and a black needle emerging from the city. The physical reality is fundamentally mutable."
    },
    {
        "chapter": "Interlude 6",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The interlude shows Paul Sernine (Jean's past identity) secretly placing stolen artifacts and a trapped god into Gilbertine's exomemory against her will, while fleeing the Oubliette. The rivalry between Jean's ambitions and the settled community he is exploiting represents ongoing personal and factional disputes.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Gilbertine lives in a Montgolfiersville apartment in the Oubliette, a permanent settlement with established social life, relationships, and governance systems. The city is depicted as a stable, livable environment.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Paul is leaving the Oubliette for offworld destinations, described as going to steal the fire of the gods. The separation from Earth is total; the story takes place entirely within the far-future solar system where Earth is never mentioned as reachable.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Gilbertine's society features gevulot contracts that erase lovers' identities after encounters, exomemory that can be severed and manipulated, Watches that control identity, and the ability to place alien data structures directly into someone's mind. This is a radically different social order.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak a common language but use terms like gevulot, exomemory, Quiet, and co-memory as everyday vocabulary. Gilbertine references the word Virtus on her Watch, suggesting Latin cultural traces, but the language is heavily modified by posthuman concepts.",
        "q6": "Manageable but risky",
        "q6_justification": "Life in the Oubliette is comfortable, with apartments, lovers, and social routines. However, Paul demonstrates the risk of someone with advanced technology cutting off exomemory links and inserting alien data structures into a person's mind, showing hidden dangers beneath the surface comfort.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The interlude depicts ordinary domestic life in the Oubliette: Gilbertine wakes up with a lover, showers, meets friends. Living on Mars is completely unremarkable to the characters.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Paul wears zoku-style clothing and uses technology stolen from the zoku colony, while operating within the Oubliette's governance system. He references going offworld, implying multiple distinct political entities across the solar system. The Sobornost is referenced as a separate faction.",
        "q9": "Drama",
        "q9_justification": "The interlude is an emotional character piece centered on Gilbertine confronting Paul about abandoning Raymonde and their child. It explores themes of loss, betrayal, and the cost of ambition through intimate personal conflict rather than action or thriller elements.",
        "q10": "Entirely civilian",
        "q10_justification": "The interlude is entirely focused on personal relationships and civilian life. Gilbertine confronts Paul about his abandonment of Raymonde. There is no military presence or conflict; the drama is entirely interpersonal.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Paul manipulates Gilbertine's exomemory link, plants a data structure like a vast metallic snowflake in her mind, and uses gevulot to erase her memories of the encounter. Space and power are characterized through digital manipulation of networked memory systems.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The physical environment features exomemory links that extend consciousness, gevulot contracts that selectively erase memories, Watches that control identity, and the ability to plant alien cognitive structures directly into someone's mind. The boundary between physical and digital existence is dissolved."
    },
    {
        "chapter": "Chapter 18 - The Thief and the King",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Jean confronts le Roi, the cryptarch who has been secretly ruling the Oubliette. Le Roi shoots Jean with a q-gun, fires the revolver to activate the memory palace machine, and the tzaddikim are simultaneously battling for control of the city. This is direct, violent strategic struggle.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Le Roi reveals that the Oubliette was originally a prison-turned-terraforming-colony, and that the cryptarchs hacked the panopticon system to create the exomemory and govern the city. The settlement is permanent and has been governed for centuries by le Roi and the cryptarchs.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Le Roi describes the Oubliette's founding as a pre-Collapse penal colony where criminals terraformed Mars. He mentions being unable to leave Mars due to embedded restrictions. Earth is referenced only as ancient history, with the Collapse separating the current civilization completely.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Le Roi reveals the Oubliette was a prison whose inmates hacked the panopticon into the exomemory, fabricated a false history with zoku help, and created a society where one man secretly controls all citizens' memories. The social order is built entirely on manufactured reality and hidden control.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Jean and le Roi communicate in a shared language peppered with specialized terms like gevulot, gogol, q-gun, Sobornost, and Quiet. Le Roi references Sante Prison on Earth, showing linguistic continuity with the past, but the vocabulary is heavily modified.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Le Roi describes the original colonists processing regolith, lighting Phobos with nukes, and melting the ice cap to terraform Mars. Even in the present, Jean's leg is blown off by a q-gun and buildings collapse as the memory palace machine activates. The environment becomes actively hostile.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter references multiple settled locations across the solar system: the Oubliette on Mars, Sante Prison on Earth, the zoku colony, and Sobornost domains. Le Roi has lived on Mars for centuries. Space habitation is entirely normalized.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Le Roi reveals himself as a competing cryptarch who eliminated other cryptarchs, while the tzaddikim, zoku, and Sobornost represent additional independent factions. The pre-Collapse government that created the prison colony represents yet another historical political entity.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a tense confrontation between Jean and the armed cryptarch le Roi, who shoots Jean's leg off, fires the revolver to activate a devastating machine, and kicks Jean in the face. Buildings collapse around them as the memory palaces converge violently.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Le Roi wields military-grade weapons (a zoku q-gun) and the memory palace machine causes massive destruction, but the conflict is fundamentally between civilian power brokers. Le Roi describes himself as a gardener, not a military figure, though he uses extreme violence.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Le Roi's power comes from controlling the exomemory panopticon system. The conflict centers on who controls the digital memory infrastructure. The memory palace machine is activated through quantum-entangled Watches linked to people's exomemories, making this a networked domain conflict.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Jean has a Sobornost body that provides anaesthesia when his leg is blown off. Le Roi uses a q-gun and zoku jewels. The memory palaces are picotech machines embedded in buildings that physically converge, disassembling matter. The physical environment is fundamentally alien."
    },
    {
        "chapter": "Chapter 19 - The Detective and the Ring",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter depicts full-scale military conflict: Mieli battles assault Quiet over the burning city, phoboi swarm toward the Oubliette, the cryptarch-controlled citizens execute memory-inoculated survivors, and the zoku colony debates whether to intervene or flee. Multiple factions are in open warfare.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is a permanent settlement under siege from both internal conflict and external phoboi attack. Mieli observes the stopped city from orbit, the zoku colony maintains its autonomous territory, and orbital control manages traffic. Territory is held but contested.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Mieli operates from orbit around Mars, communicating with her ship Perhonen. The Pellegrini controls things from within the Sobornost network. Earth is never referenced. The characters exist entirely within a far-future solar system completely separated from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter features a warrior from the Oort Cloud negotiating with a goddess who possesses her body, offering a gogol copy of herself as bargaining currency. The zoku debate abandoning the city through silver portals, while Pixil tears out her zoku jewel to leave her collective. This is an utterly alien social order.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate in a shared language with heavy use of specialized terms: gevulot, phoboi, q-dot, metacortex, Realmgate, gogol. The language is recognizable but saturated with far-future technological and cultural vocabulary.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The chapter depicts a city under simultaneous attack from phoboi (hybrid biological weapons breeding through billions of virtual generations), internal civil war, and cryptarch mind-control. Mieli fires antimatter weapons and nano-missiles. Survival is actively threatened from multiple directions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter shows multiple populated locations: the Oubliette with its massive civilian population, orbital stations with sentry fleets, the Oort Cloud civilization Mieli comes from, and the Sobornost guberniyas. Space habitation is completely ordinary.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features at least five distinct political entities in active conflict or negotiation: the Oubliette cryptarchs, the tzaddikim resistance, the zoku colony (debating flight vs. engagement), the Sobornost (represented by the Pellegrini), and the phoboi as autonomous biological threats.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by military action: Mieli makes a combat insertion from orbit, fires antimatter weapons and nano-missiles, battles assault Quiet, and coordinates with Perhonen against the phoboi invasion. Raymonde fights with foglet weaponry. This is a full-scale war chapter.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Military and civilian elements are deeply intertwined. Mieli conducts military operations while Raymonde leads civilian resistance. The Quiet fleet provides military defense, but the city itself is a civilian settlement. Isidore negotiates as a civilian while military conflict rages around him.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Isidore uses a stolen entanglement ring to enter the Realmspace inside the needle. Pixil uses zoku technology to project them into a virtual space. The conflict resolution involves accessing digital/quantum infrastructure rather than purely physical combat. Even the phoboi breed through virtual generations.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The chapter features a walking city that has stopped moving, a black needle made of pseudomatter (quark matter or spacetime foam), phoboi that breed through billions of virtual generations, Mieli being fired at Mars in a q-dot bubble, and Pixil tearing out a biological zoku jewel. The physics and environment are fundamentally alien."
    },
    {
        "chapter": "Chapter 20 - Two Thieves and a Detective",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chapter depicts simultaneous conflicts on multiple fronts: Jean fights le Roi inside the memory palace Realmspace, Mieli and Raymonde battle cryptarch-controlled Quiet and phoboi outside, the zoku rides out against the phoboi horde, and Isidore and Pixil confront le Roi who kills Pixil. This is total, multi-front war.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is a permanent settlement fighting to survive. The chapter ends with Isidore using the Voice to restore order, getting the city moving again. Despite the crisis, the settlement's governance infrastructure (the Voice, the Quiet) ultimately reasserts control.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The action takes place entirely on Mars, within a post-singularity solar system. Perhonen operates in orbit while Mieli fights on the surface. Earth is referenced only through ancient history in the memory palace's automata. The separation from Earth is absolute.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter features consciousness transferred into a virtual Realmspace, wax automata serving as memory constructs, Jean releasing a Dilemma Prison Archon from inside his own virtual body, and Isidore inheriting control of the Voice to command an entire city. This is a completely alien social order.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate in a recognizable language but use extensive specialized vocabulary: Realmspace, q-gun, foglet, Archon, phoboi, metacortex. The underlying communication is comprehensible but laden with far-future terminology.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The chapter depicts constant lethal threats: le Roi shoots Jean and has him dragged to a wax-making workshop, Pixil is killed by le Roi's swordcane, phoboi breach the city walls, and Mieli fights through cryptarch-controlled assault Quiet. Survival pressure is extreme on all fronts.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Multiple populations inhabit space: the Oubliette's citizens, the zoku colony riding out on quantum mounts, the Sobornost-affiliated Perhonen in orbit, and the phoboi as Mars-native organisms. Space habitation is completely normalized across many forms.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The chapter features at least six distinct factions in active conflict: le Roi's cryptarch forces, the tzaddikim, the zoku (who ride out to fight phoboi), the phoboi, the Sobornost (Mieli/Pellegrini), and Jean as an independent actor. Isidore emerges as a new power center.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by combat across multiple fronts: swordfighting in Realmspace, Mieli cutting through Quiet with q-blades, Perhonen lobbing antimatter warheads at phoboi, zoku ghost-riders unleashing nanotech weaponry. This is a full-scale war chapter with constant action.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Military and civilian elements are inseparable. Mieli uses Sobornost military weapons, Raymonde fights with foglet technology, the zoku deploys combat riders, but Isidore resolves the conflict through civilian governance by speaking with the Voice. The domain is thoroughly mixed.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Much of the chapter takes place inside a Realmspace virtual world where Jean releases a software construct (the Archon) to create a Dilemma Prison. The climax occurs when Isidore uses the exomemory network and the Voice to pacify the entire city. The decisive actions are digital/networked.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The chapter features a virtual palace where consciousness exists as software, a needle made of pseudomatter that converts people to data, an Archon that turns walls to glass as it creates a prison, zoku ghost-riders made of shimmer and diamond, and phoboi that are hybrid biot/biological weapons. The physics are fundamentally alien."
    },
    {
        "chapter": "Chapter 21 - The Thief and the Stolen Goodbye",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter is a denouement after the crisis. Jean says goodbye to Isidore and Raymonde peacefully. While Jean mentions the Sobornost will come after the Oubliette, the chapter itself depicts reconciliation and departure rather than active conflict.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Oubliette is healing and resuming normal function. Isidore has inherited the cryptarch key and plans to give the Voice back to the people. Perhonen sits near the city walls, and the city continues to move. The settlement remains permanent and governable.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Jean departs Mars heading for Earth, indicating a long journey. The characters exist in a far-future solar system where travel between planets requires significant effort. Jean asks Perhonen to take her time so he can watch the scenery, suggesting a long voyage.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Isidore is now a Cryptarch controlling the Voice and exomemory of the entire Oubliette. Jean departs in a sentient ship with an Oort Cloud warrior. The Oubliette's governance is being restructured from hidden authoritarian control to something new. The social order remains radically different from Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters communicate naturally in a shared language with familiar terms like revolution, opera, and detective, alongside specialized vocabulary like gevulot, Quiet, and koto brother. The language is recognizable but inflected with unique cultural terms.",
        "q6": "Manageable but risky",
        "q6_justification": "The immediate crisis has passed and the city is healing, but Jean warns Isidore that the Sobornost will come hard and fast. The environment is currently manageable but faces future existential threats. The Diamond Prison needle remains visible above the rooftops.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter depicts multiple civilizations across the solar system as ordinary: the Oubliette on Mars, Jean heading to Earth, the zoku colony, and Mieli from the Oort Cloud. Jean casually says he is going to Earth as if it were a normal destination.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Jean warns about the Sobornost threatening the Oubliette, mentions the zoku will help defend it, and Raymonde wears her Gentleman outfit representing the tzaddikim. Multiple independent political entities continue to exist and interact across the solar system.",
        "q9": "Drama",
        "q9_justification": "The chapter is an emotional farewell. Jean says goodbye to Isidore (who may be his son), has a wordless parting with Raymonde on the red sand, and departs with Mieli. The tone is bittersweet and reflective, focused on character relationships and emotional resolution.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is entirely focused on civilian farewells and departures. Jean visits Isidore in his kitchen, exchanges goodbyes with Raymonde, and boards Perhonen. There is no military action or military presence in this concluding chapter.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Isidore now controls the exomemory and the Voice, a networked system that governs the entire Oubliette. Jean holds the Schrodinger Box containing unknown quantum data. The Diamond Prison needle is visible as a permanent reminder that space is characterized by digital-quantum infrastructure.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter features a sentient ship (Perhonen), a walking city with a diamond prison needle visible above rooftops, zoku transport bubbles, foglet halos worn as clothing, and reliefs on city walls that sing inside Mieli's mind. The physical environment remains very different from Earth."
    },
    {
        "chapter": "Interlude 7",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The interlude reveals intense political conflict among the Sobornost Founders. The Pellegrini is being threatened with gogolcide by other Founders, Chen demands weapons against rivals, and the Engineer is manipulated into creating a Hunter to pursue the escaped prisoners. This is high-level strategic struggle.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Engineer's guberniya is described as a diamond sphere the size of old Earth, containing trillion gogols. The Sobornost spans vast guberniyas, oblasts, and raions. Chen is described as the most powerful Founder with voice stretching across all Sobornost territories. This is empire-scale occupation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Engineer's guberniya is a Dyson-scale structure eating matter and energy from the sun. The Sobornost spans the solar system with vast guberniyas. The Engineer references centuries of history since Minsk University. Earth is a distant memory; the scale of separation is extreme.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Engineer exists as a billion-handed entity tending a garden of growing minds, with gogol copies serving as workers. The Founders are posthuman entities who can split into countless copies. The Pellegrini manipulates through centuries-old relationships. This is a completely alien social order.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The Founders communicate in a recognizable language, using names like Sasha and Josephine, referencing Minsk University and the Great Common Task. However, their vocabulary includes gogol, guberniya, virscape, and Founder codes, reflecting significant linguistic evolution.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The Engineer's machine garden is a paradise of his own design, where he cultivates minds in perfect conditions. The natural environment poses no survival challenge; the threats are entirely political, from other Founders. The virscape is designed for comfort and productivity.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Sobornost Founders inhabit structures the size of planets, containing trillions of gogol copies. The Engineer's guberniya is a diamond sphere the size of Earth orbiting the sun. Living in space at massive scales is completely normalized for this civilization.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The interlude reveals internal Sobornost politics: Chen, the Pellegrini, Anton, Hsien, Chitragupta, and the Engineer are all distinct power centers within the Sobornost alone. Combined with the Oubliette, zoku, and Oort Cloud civilizations, the political landscape is highly fragmented.",
        "q9": "Political / diplomatic",
        "q9_justification": "The interlude is entirely focused on political maneuvering among the Sobornost Founders. The Pellegrini manipulates the Engineer through their old romantic connection, Chen demands cooperation through political pressure, and the Engineer is drawn into factional politics. This is pure political drama.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Engineer's work is primarily civilian (cultivating minds, creating gogols for various purposes). However, the creation of the Hunter is a military act, Chen's warminds are referenced, and the Founders' political conflict has military implications. The domain is mostly civilian with military undercurrents.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The entire interlude takes place in a virscape (virtual reality space). The Engineer manipulates cognitive modules and neural pathways as if tending a garden. The Hunter is created from abstract cognitive architectures. Space is characterized as a fundamentally digital, networked domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The Engineer exists in a virscape inside a diamond sphere the size of Earth. He has a billion hands to tend growing minds made of cogwheels. The Pellegrini appears as a creature of spun silver. The Hunter is assembled from cognitive modules and neural pathway atlases. The physics and environment are completely unlike Earth."
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

print('Done with batch 3.')
