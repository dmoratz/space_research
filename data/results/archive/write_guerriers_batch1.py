import csv
import json
import os

# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
questions_path = os.path.join(base_dir, "data", "questions.json")
csv_path = os.path.join(base_dir, "data", "results", "France_Les_Guerriers_du_Silence.csv")

# Load questions
with open(questions_path, "r", encoding="utf-8-sig", errors="replace") as f:
    questions = json.load(f)

# Build fieldnames
fieldnames = ["country", "book", "chapter"]
for q in questions:
    fieldnames.append(f"q{q['number']}")
for q in questions:
    fieldnames.append(f"q{q['number']}_justification")

country = "France"
book = "Les Guerriers du Silence"

chapters_data = [
    {
        "chapter": "Chapitre Premier",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Scaythe Pamynx reveals the Grand Project to overthrow the Confederation of Naflin by force, ordering assassinations of planetary leaders (Sri). The chapter opens with a telepathic killing demonstration and details a conspiracy involving mercenaries of Pritiv and the Syracusain ruling class.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Confederation of Naflin encompasses numerous settled worlds including Syracusa, with references to Terra Mater as the distant origin planet. Multiple planetary systems are governed as member states under the Confederation's political structure.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Terra Mater is referenced as a near-mythical origin world, effectively lost to memory. The settled worlds are spread across vast interstellar distances, connected only by deremats (instantaneous transfer technology), underscoring the enormous separations involved.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Syracusain society is built around telepathic Scaythes, ritual assassinations, and the science inddigue. The social order revolves around planetary Sri (leaders), Scaythe hierarchies, and the Ordre absourate — structures entirely unlike anything on Earth.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in nafle interplanetaire (an interplanetary lingua franca), while Syracusain-specific terms, titles, and cultural vocabulary permeate the dialogue, indicating strong local linguistic variation alongside the shared language.",
        "q6": "Manageable but risky",
        "q6_justification": "Syracusa itself appears habitable and comfortable, with grand halls and populated cities. The environmental hostility is low; the dangers come from political actors rather than natural conditions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter depicts a galaxy where billions of humans live across many worlds as a matter of course. Space habitation is entirely ordinary — characters reference multiple planets and populations without any sense of novelty.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Confederation of Naflin unites multiple sovereign worlds, each with its own Sri (planetary leader) and delegation. The conspiracy targets these separate polities to bring them under Syracusain control, showing a multipolar political landscape.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on political conspiracy: Scaythe Pamynx unveils a plan to overthrow the Confederation through targeted assassinations and covert operations. The focus is on power, intrigue, and the mechanics of the coup.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter features both civilian political structures (the Confederation, planetary delegations) and military elements (mercenaries of Pritiv, Scaythe warriors). Space governance blends diplomatic and martial dimensions.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Humanity's spread across the galaxy is described in terms of colonial satellites and waves of expansion from Terra Mater. The Syracusains' Grand Project to seize control echoes imperial conquest narratives.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Syracusa is described as a habitable world with familiar features (cities, halls, natural landscapes), though the broader galaxy includes diverse planetary environments. The physical setting in this chapter is not drastically alien."
    },
    {
        "chapter": "Chapitre Ii",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "This chapter focuses on civilian life and interplanetary travel logistics. Tixu Oty helps Aphykit arrange transport; there is no open conflict, though the C.I.L.T. monopoly on deremat travel hints at underlying economic competition.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Deux-Saisons and Point-Rouge are fully settled worlds with cities, transport infrastructure, and administrative systems. The C.I.L.T. operates a galaxy-spanning transit network connecting numerous inhabited planets.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Travel between Deux-Saisons and Point-Rouge requires either a navette (taking considerable time) or a deremat (instantaneous but expensive). The vast interstellar distances make conventional travel impractical, reinforcing the sense of extreme separation.",
        "q4": "Distinct space culture",
        "q4_justification": "Deux-Saisons has its own distinct culture: Tixu is an Orangien with specific cultural practices, and the planet's social norms around the C.I.L.T., local commerce, and interpersonal relations differ markedly from Earth norms while still being recognizably human.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tixu and Aphykit communicate in the shared interplanetary language, but Aphykit is identified as Syracusaine with her own cultural-linguistic background. Local terms for technology (deremat, navette) and institutions (C.I.L.T.) reflect shared but specialized vocabulary.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Deux-Saisons is depicted as a difficult world with extreme seasonal cycles that make survival resource-intensive. The environment requires adaptation, and infrastructure like the C.I.L.T. stations reflects the effort needed to maintain civilization there.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Tixu works a routine job at a transit company; Aphykit is a traveler moving between worlds. Living and working on distant planets is completely mundane — no character treats interplanetary existence as remarkable.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Deux-Saisons is described as one of the Marches planets at the periphery of the Confederation. Different worlds have distinct governance, and the C.I.L.T. operates as a powerful interplanetary corporation, suggesting a complex multi-entity political landscape.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows Tixu helping Aphykit embark on a journey to Point-Rouge, with a sense of discovery and movement. The tone is that of a travel adventure as characters navigate transit systems and planetary logistics.",
        "q10": "Entirely civilian",
        "q10_justification": "The entire chapter revolves around civilian life: Tixu's job at the C.I.L.T., commercial travel arrangements, and everyday interactions. There is no military presence or martial activity in this chapter.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Deux-Saisons is a peripheral Marches planet, evoking frontier territory at the edges of the Confederation. The planet's rough conditions and distance from central authority parallel colonial frontier settings.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Deux-Saisons has extreme seasonal variations that require regular adaptation from its inhabitants. The planet's environment is notably different from Earth, with its dual-season cycle shaping all aspects of life there."
    },
    {
        "chapter": "Chapitre Iii",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The assassination of Sri Alexu by Scaythe Pamynx and the mercenaries of Pritiv is discovered during the asma quinquennale. Regent Stry Wortling uncovers a political murder at the heart of the Confederation's diplomatic gathering, revealing deep strategic conflict.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The asma quinquennale brings together delegations from numerous member worlds of the Confederation, each with its own planetary leader. The gathering demonstrates the breadth of human territorial occupation across many governed worlds.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Delegations travel from across the galaxy to Syracusa for the quinquennial assembly, implying vast distances between member worlds. The scale of the Confederation spans interstellar distances that dwarf any Earthly concept of travel.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The asma quinquennale is a uniquely alien political institution. Scaythe telepathic powers, the ritualized political structure of Sri and regents, and the Pritiv mercenary order all represent a social order fundamentally unlike Earth's.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The multi-world diplomatic assembly operates in a common language, yet delegates from different planets bring distinct cultural and linguistic identities. The interplanetary lingua franca enables communication across diverse planetary cultures.",
        "q6": "Manageable but risky",
        "q6_justification": "Syracusa during the asma is depicted as a comfortable, habitable setting — grand halls and diplomatic quarters. The risks in this chapter come from political assassination, not environmental hostility.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The quinquennial assembly draws representatives from across the galaxy as a routine political event. The sheer number of delegations and worlds represented shows that interstellar habitation is completely normalized.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The asma quinquennale is explicitly a gathering of distinct member states of the Confederation, each with sovereign planetary leaders. The political intrigue between Syracusains and other worlds underscores the multipolar nature of the galaxy's governance.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is centered entirely on diplomatic proceedings and political intrigue: the quinquennial assembly, the discovery of a murdered Sri, and the investigation into the conspiracy. It is a political thriller chapter.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The asma is a civilian diplomatic event, though the presence of Scaythe warriors and mercenaries of Pritiv introduces a military undercurrent. The chapter's focus remains on political rather than military activity.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Confederation's structure of distant member worlds sending delegations to a central assembly echoes colonial governance models. The expansion of humanity across the galaxy is framed as a historical process of settlement and political organization.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Syracusa in this chapter appears as a largely Earth-like world with familiar urban and architectural features. The physical environment is not a major factor; the differences are political and cultural rather than environmental."
    },
    {
        "chapter": "Chapitre Iv",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Tixu is attacked by mercenaries and a Scaythe on Deux-Saisons, thrown into a river and left for dead. The violence is part of the broader conspiratorial struggle that spans multiple worlds, showing the conflict reaching even peripheral characters.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Deux-Saisons is a fully settled world with its own ecology, settlements, and population. The mercenaries pursuing Tixu operate across multiple worlds, confirming extensive human territorial presence throughout the galaxy.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Deux-Saisons is a remote Marches world, far from the centers of the Confederation. Tixu's isolation after the attack — stranded in wilderness on a peripheral planet — underscores the vast distances and separation between worlds.",
        "q4": "Distinct space culture",
        "q4_justification": "Kacho Marum and his people live with sacred lizards whose secretions have healing properties, representing a culture uniquely adapted to Deux-Saisons. The mystical calling Tixu receives reflects spiritual traditions specific to this world.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tixu and Kacho communicate despite coming from different cultural backgrounds, suggesting a shared language. However, the local traditions, spiritual vocabulary, and knowledge of sacred lizards reflect deep local cultural and linguistic specificity.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "After being attacked and thrown in the river, Tixu nearly dies in the wilderness of Deux-Saisons. Survival requires rescue by locals with specialized knowledge of the planet's dangerous fauna and healing methods using sacred lizard secretions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Despite the harsh conditions, Deux-Saisons has an established human population including indigenous-style communities like Kacho's people. Living on this world, however difficult, is an accepted part of human galactic civilization.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter shows layers of authority on Deux-Saisons: the Confederation's nominal governance, local communities like Kacho Marum's group, and the mercenaries operating outside official control. Multiple power structures coexist.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Tixu is ambushed, nearly killed, thrown into a river, and must be rescued and healed in the wilderness. The chapter is a survival narrative with thriller elements as Tixu escapes death through the intervention of Kacho and the sacred lizards.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter features both civilian characters (Tixu, Kacho Marum) and military/paramilitary actors (mercenaries of Pritiv, the Scaythe). The violence intrudes upon civilian life on a peripheral world.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Deux-Saisons' Marches location, its rugged wilderness, and the indigenous-style community of Kacho Marum all evoke frontier territory. The planet feels like a colonial periphery where central authority is distant and survival depends on local knowledge.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The wilderness of Deux-Saisons is physically dangerous with its river, hostile fauna, and extreme conditions. Tixu's near-death and the need for sacred lizard medicine to heal him show that human biology is constantly challenged by this world's environment."
    },
    {
        "chapter": "Chapitre V",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Sri Mitsu is assassinated on Point-Rouge as part of the coordinated conspiracy. Maranas is mortally wounded protecting Aphykit, and she must flee through Matana while being hunted. The chapter depicts lethal political violence across yet another world.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Point-Rouge is another fully settled Confederation world with its own city of Matana, political leadership (Sri Mitsu), and distinct population. The assassination campaign targeting multiple worlds confirms the vast territorial scope of human settlement.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Point-Rouge is a distant world with three suns, far from Syracusa and other Confederation centers. Aphykit has traveled across interstellar distances to reach it, and escape from the planet is extremely difficult once the violence begins.",
        "q4": "Distinct space culture",
        "q4_justification": "Point-Rouge has its own Prouge culture, distinct architecture in the old city of Matana, and a unique environment shaped by three suns. The local population has customs and social structures markedly different from other Confederation worlds.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Aphykit, a Syracusaine, communicates with locals on Point-Rouge, indicating a shared interplanetary language. However, Prouge-specific terminology and cultural references show strong local linguistic identity alongside the lingua franca.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Point-Rouge's three suns create an extreme environment. The old city of Matana is depicted as a harsh, labyrinthine urban landscape where survival during the pursuit is difficult. The planet's conditions require significant adaptation.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Point-Rouge has a large settled population with established cities, governance, and social institutions. Living on a planet with three suns is simply normal life for its inhabitants.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Point-Rouge operates as a distinct polity within the Confederation, with its own Sri and local governance. The assassination of Sri Mitsu is aimed at disrupting this independent political entity as part of the broader Syracusain power grab.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a tense survival thriller: Sri Mitsu is killed, Maranas fights and dies protecting Aphykit, and she must flee through Matana's dangerous streets while being hunted. The pacing is urgent and suspenseful.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The assassination targets a political leader, and combat occurs between bodyguards and assassins, but the setting is a civilian city. The violence disrupts ordinary civilian life on Point-Rouge.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Point-Rouge, with its alien three-sun environment and the old labyrinthine city of Matana, feels like a frontier settlement that has developed its own character far from the Confederation's center. The lawlessness during the crisis reinforces this frontier quality.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Point-Rouge's three suns create lighting and climate conditions quite different from Earth. The environment of Matana requires adaptation, though humans have clearly built a functioning civilization there despite the unusual stellar configuration."
    },
    {
        "chapter": "Chapitre Vi",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Grand Bouleversement is a galaxy-wide military coup: Syracusains seize control of the entire Confederation overnight. Dame Armina is captured, her lover killed, and she is tortured. Kreuzian missionaries are deployed across all worlds. This is total war on a galactic scale.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The coup targets every world in the Confederation simultaneously, demonstrating that humanity occupies and governs numerous planets as territorial states. The Syracusains aim to control all of these settled worlds.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Grand Bouleversement spans the entire galaxy, with events occurring simultaneously on worlds separated by enormous interstellar distances. The scale of the coup — coordinated across light-years — underscores the extreme distances involved.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The imposition of Kreuzian missionaries, the Scaythe-led regime, and the violent suppression of existing cultures represent a social order utterly unlike anything on Earth. The chapter depicts forced cultural transformation on a galactic scale.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The coup is communicated and enforced across all worlds, implying a shared interplanetary communication system. Yet the deployment of Kreuzian missionaries to reshape local cultures suggests that significant linguistic and cultural variation exists to be suppressed.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The environment becomes extremely hostile due to the coup: Dame Armina is captured, tortured, and her companion killed. Across all worlds, the political upheaval creates survival pressure for anyone opposed to the new Syracusain regime.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The galaxy-wide scope of the coup confirms that space habitation is completely normalized — the Syracusains must take control of countless populated worlds, each with substantial human populations.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Grand Bouleversement targets multiple distinct sovereign worlds, each with its own governance. The coup's purpose is to eliminate this multipolar political order and replace it with Syracusain hegemony, confirming the pre-existing diversity of space polities.",
        "q9": "Military / war",
        "q9_justification": "The chapter depicts a military coup on a galactic scale: coordinated takeovers, combat, capture, torture, and the deployment of occupation forces (Kreuzian missionaries). It is a war chapter focused on conquest and subjugation.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "The entire chapter is about the military takeover of the Confederation. Every scene involves violence, capture, or the machinery of conquest. Civilian life is destroyed or subjugated by military force.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Grand Bouleversement is fundamentally an imperial conquest: one polity seizing control of many others and imposing its culture through missionaries and military force. This directly parallels historical colonial expansion.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The physical environments on Marquinat and other worlds appear largely habitable, with the chapter's focus on political and military events rather than environmental challenges. The planets are different from Earth but manageable for human habitation."
    },
    {
        "chapter": "Chapitre Vii",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Tixu is captured by vagabonds on Point-Rouge and sold into servitude to francao Metarelly. Aphykit has been captured for the chairmarche slave auction. The chapter depicts a world of criminal violence, human trafficking, and the Camorre underworld.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Point-Rouge is a fully settled world with complex social structures including an organized criminal underworld (the Camorre) and slave markets. The planet's established population and institutions confirm extensive territorial occupation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Tixu, an Orangien from Deux-Saisons, is stranded on Point-Rouge — a world far from his home. The difficulty of escape and the sense of being trapped on an alien world reinforce the extreme distances between planets.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Point-Rouge's underworld features the Camorre criminal organization, chairmarche slave auctions, and vagabond gangs — a social order entirely alien to Earth experience. Metarelly as a francao operates within a unique cultural hierarchy.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tixu (Orangien) and Metarelly (also Orangien) share a cultural-linguistic background, while operating on Point-Rouge among Prouges and others. Communication works across groups but local slang and underworld vocabulary mark distinct sub-cultures.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Tixu is captured, enslaved, and must survive in the criminal underworld of Point-Rouge. The constant threat of violence, the slave trade, and the lawless environment create extreme survival pressure that has nothing to do with natural conditions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Point-Rouge's complex social stratification — including organized crime, slave markets, and diverse immigrant populations from multiple worlds — demonstrates that interstellar habitation is so normalized it has developed its own criminal ecosystems.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "Point-Rouge under the post-coup order shows a highly fragmented power structure: the Camorre, vagabond gangs, francaos, and the remnants of official authority all compete for control. No single entity dominates.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Tixu is captured, sold, and must navigate the dangerous underworld of Point-Rouge. Aphykit faces the chairmarche slave auction. The chapter is a survival thriller set in a criminal environment.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter is set entirely in the civilian criminal underworld — vagabonds, slave traders, the Camorre. While violence is pervasive, it is criminal rather than military. The post-coup military presence is background context.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Point-Rouge's lawless underworld, slave markets, and competing criminal factions evoke a frontier society where central authority has collapsed. The planet operates like a colonial outpost beyond the reach of law.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Point-Rouge's three-sun environment and urban landscape of Matana are physically distinct from Earth. Tixu, as an off-worlder, must adapt to unfamiliar conditions, though the planet supports a large human population."
    },
    {
        "chapter": "Chapitre Viii",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Chevalier Long-Shu Pae receives a mission from the exiled Ordre absourate. Guerrier Filp Asmussa arrives to find Aphykit at the chairmarche. Mercenaries and a Scaythe are spotted at the auction, showing that multiple factions are in strategic conflict over Aphykit.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter references the Ordre absourate's exile, the Syracusain takeover of the Confederation, and Point-Rouge's complex social landscape — all confirming that humanity occupies many worlds organized as states and empires.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Long-Shu Pae is an exile from a distant order, and Filp Asmussa has traveled across interstellar space to reach Point-Rouge. The Ordre absourate's scattered remnants across the galaxy underscore the vast distances separating human populations.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Ordre absourate's philosophy, knight structure, and spiritual practices represent a social order with no Earth parallel. The chairmarche slave auction and the Camorre's operations further demonstrate a radically different civilization.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Long-Shu Pae and Filp Asmussa communicate across their different backgrounds, and both interact with Point-Rouge locals. The Ordre absourate has its own specialized vocabulary and philosophical terminology alongside the shared interplanetary language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Point-Rouge remains a harsh environment, and the social conditions (slave markets, criminal networks, post-coup instability) make survival resource-intensive. Long-Shu Pae and Asmussa must navigate both physical and social dangers.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The chapter treats interstellar travel and multi-world civilization as completely ordinary. Characters from different worlds converge on Point-Rouge without any sense that space habitation is unusual.",
        "q8": "Highly fragmented political landscape (multipolar with many factions, corporations, colonies, microstates)",
        "q8_justification": "The Ordre absourate (exiled knights), the Syracusain regime, the Camorre, mercenaries of Pritiv, and local factions all operate simultaneously on Point-Rouge. The political landscape is deeply fragmented among competing power structures.",
        "q9": "Adventure / exploration",
        "q9_justification": "Long-Shu Pae accepts a quest-like mission, and Filp Asmussa undertakes a search for Aphykit. The chapter has the tone of an adventure as characters converge on the chairmarche with competing objectives.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Ordre absourate knights represent a martial-spiritual order, while the chairmarche is a civilian (if criminal) institution. Mercenaries and a Scaythe add military elements to an otherwise civilian setting.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Point-Rouge continues to feel like frontier territory: lawless, with competing factions, slave markets, and exiled warriors seeking refuge. The planet is a colonial periphery where different groups carve out space beyond central authority.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Point-Rouge's three-sun system and the specific conditions of Matana require ongoing adaptation. Long-Shu Pae's exile on this world and Asmussa's arrival both highlight how the planet's physical conditions differ from their home worlds."
    }
]

# Ensure output directory exists
os.makedirs(os.path.dirname(csv_path), exist_ok=True)

# Read existing chapters to support resume
existing_chapters = set()
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("book") == book:
                existing_chapters.add(row.get("chapter", ""))

analyzed = 0
skipped = 0

for ch in chapters_data:
    chapter_label = ch["chapter"]
    if chapter_label in existing_chapters:
        print(f"SKIP (already in CSV): {chapter_label}")
        skipped += 1
        continue

    row_dict = {
        "country": country,
        "book": book,
        "chapter": chapter_label
    }
    for q in questions:
        qnum = q["number"]
        row_dict[f"q{qnum}"] = ch[f"q{qnum}"]
        row_dict[f"q{qnum}_justification"] = ch[f"q{qnum}_justification"]

    # Validate answers against options
    for q in questions:
        qnum = q["number"]
        answer = row_dict[f"q{qnum}"]
        if answer not in q["answer_options"]:
            print(f"WARNING: Chapter '{chapter_label}', q{qnum}: answer '{answer}' not in valid options!")

    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row_dict)

    print(f"WROTE: {chapter_label}")
    analyzed += 1

print(f"\nSummary: {analyzed} chapters analyzed, {skipped} skipped (already in CSV).")
