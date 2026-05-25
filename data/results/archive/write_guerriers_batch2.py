import json, csv, os

chapters_data = [
    {
        "chapter": "Chapitre Ix",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Aphykit is held captive in a slave trade network run by the criminal Camorre organization. Tixu and Maïtrelly launch a violent rescue mission in the desert of Rajiatha-Na, culminating in a battle with Glaktus Quemil's men using weapons like brûlentrailles and ondemorts.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter takes place on Point-Rouge, a settled world with cities, deserts, auction markets, and criminal organizations. Multiple other worlds (Syracusa, Deux-Saisons) are referenced as distinct inhabited territories within the Confédération de Naflin.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Characters travel between worlds via déremat (matter transmitters), with Point-Rouge described as a distant world. The distances are so vast that instantaneous teleportation is the only viable means of interplanetary travel.",
        "q4": "Distinct space culture",
        "q4_justification": "Point-Rouge has its own creole language (prouge), a unique slave trade economy at the chairmarché, and a criminal underworld (Camorre) distinct from Earth norms. The auction of human beings and local customs reflect a culture far removed from terrestrial society.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in nafle interplanétaire (the universal confederal language), but Point-Rouge also has its own creole dialect called prouge and local slang, showing linguistic diversity alongside a common tongue.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The desert of Rajiatha-Na is described as an extreme environment with scorching heat, and Point-Rouge's underworld is dangerous. Survival requires resources and protection, though the planet itself is habitable with settlements and cities.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Point-Rouge has established cities, markets, criminal networks, and a functioning society. Living on various worlds across the Confédération is presented as completely normal and unremarkable for the characters.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Confédération de Naflin encompasses multiple worlds, each with its own local governance. Point-Rouge has its own social order, while Syracusa has seigneurs, and the Camorre operates as a transnational criminal organization across worlds.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter centers on Aphykit's captivity by a slave trader, a tense rescue operation in the desert, and violent combat. The tone is suspenseful and action-driven, with survival at stake throughout.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Maïtrelly leads a military-style rescue operation with armed guards, using military-grade weapons in the desert. However, Point-Rouge's civilian economy (slave markets, commerce) is equally prominent in the chapter.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Point-Rouge is depicted as a lawless frontier world with slave trading, criminal organizations, and desert landscapes. The rescue mission in the wilderness of Rajiatha-Na evokes frontier-style expeditions into hostile territory.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Point-Rouge has a harsh desert environment but is otherwise habitable with cities and settlements. The physical conditions differ from Earth but are manageable with existing technology and infrastructure.",
    },
    {
        "chapter": "Chapitre X",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "A political conspiracy against the Scaythes is violently crushed when Connétable Pamynx infiltrates the meeting via corrupted protecteurs de pensées. All conspirators are massacred through mental death and assassins de Pritiv, demonstrating ruthless strategic struggle for power.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter is set on Syracusa/Vénicia, a richly developed world with court politics, estates, and elaborate social structures. Multiple other worlds in the Confédération are referenced as part of the conspiracy network.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Syracusa is presented as a fully self-contained world with its own centuries-old aristocratic traditions. Earth (Terra Mater) is a distant memory, and interplanetary distances require déremat technology to traverse.",
        "q4": "Distinct space culture",
        "q4_justification": "Syracusan society has elaborate court rituals, aristocratic titles (seigneurs, dames), the kreuzien Church as a dominant institution, and traditions like protecteurs de pensées (thought-protectors). This culture is entirely unique and not derived from Earth.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters use nafle interplanétaire for communication, but Syracusan society also features archaic formal speech patterns and local terminology (vieux syracusain) reflecting the world's distinct cultural heritage.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The environment is politically lethal rather than physically harsh. The Scaythes can kill through mental attack, and the kreuzien Church exercises oppressive control. Surviving requires navigating a dangerous political landscape.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Syracusa has a fully developed society with merchants, aristocrats, churches, and conspiracies. Living across multiple worlds is entirely routine for all characters in the chapter.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Syracusa is governed by seigneur Ranti Ang with its own political hierarchy. The conspirators come from different worlds, and the kreuzien Church operates as a separate power structure alongside secular governance.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter revolves entirely around political intrigue: a secret conspiracy meeting, infiltration by the Scaythe agent Pamynx, and the subsequent massacre of conspirators. The focus is on power, loyalty, and political maneuvering.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter depicts civilian political life on Syracusa with merchants and aristocrats. The assassins de Pritiv and Scaythe enforcement represent a military/security presence, but the setting is primarily courtly and civilian.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Syracusan society with its aristocratic houses, court intrigues, and hierarchical power structures resembles historical naval empires with admiralties and fleet politics. The seigneurial system mirrors naval-era colonial governance.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Syracusa/Vénicia appears Earth-like with gardens, estates, and comfortable living conditions. The physical environment is habitable and does not pose significant challenges different from Earth.",
    },
    {
        "chapter": "Chapitre Xi",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Maïtrelly and his guards are killed by assassins and Scaythes on a base rooftop. Chevalier Long-Shu Pae and guerrier Filp Asmussa intervene using the cri de mort martial technique, but Long-Shu Pae is ultimately killed by a Scaythe who feigned defeat.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter references the Order absourate operating across multiple worlds, with characters moving between planets. The Confédération spans many settled worlds, each functioning as distinct territories.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Characters use déremat codes to transfer instantly between worlds separated by vast interstellar distances. Tixu uses Maïtrelly's code 'Vieil-ange' to escape, indicating immense distances bridged only by teleportation.",
        "q4": "Distinct space culture",
        "q4_justification": "The chapter features the Order absourate with its unique martial arts (Xui, cri de mort), the concept of antra (son de vie/sound of life), and a spiritual warrior tradition entirely unlike anything on Earth.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in a common language (nafle interplanétaire) while the Order absourate uses specialized terminology (cri de mort, antra, son de vie) that functions as a distinct professional vocabulary.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Characters face lethal threats from assassins and Scaythes with devastating mental powers. Long-Shu Pae, a master warrior, is killed despite his combat skills. The Scaythes' power exceeds even the Order's abilities, creating constant mortal danger.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "All events unfold across multiple inhabited worlds as a matter of course. Characters transfer between planets routinely, and space habitation is the unremarkable backdrop to the conflict.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Order absourate, the Confédération, and the Scaythe-backed kreuzien Church all operate as distinct power structures across multiple worlds, each with their own authority and jurisdiction.",
        "q9": "Military / war",
        "q9_justification": "The chapter is dominated by combat: rooftop assassinations, martial arts duels using the cri de mort, and the death of multiple warriors including the chevalier Long-Shu Pae. The tone is intensely martial throughout.",
        "q10": "Mostly military",
        "q10_justification": "Nearly every character in the chapter is a combatant: assassins, Scaythes, guerriers and chevaliers of the Order absourate, and military guards. The action is entirely focused on lethal combat and warrior traditions.",
        "q11": "Totally unique domain",
        "q11_justification": "The combat involves psychic martial arts (cri de mort), mental warfare by Scaythes, and spiritual sound-based powers (antra). These capabilities have no analogue in naval, air, or other traditional military domains.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The physical setting appears habitable with rooftops, bases, and breathable atmosphere. The main dangers come from hostile actors rather than environmental conditions.",
    },
    {
        "chapter": "Chapitre Xii",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Menati Ang stages a coup against his brother seigneur Ranti with Scaythe and kreuzien Church support. Ranti is killed by Scaythe mental execution, and Sibrit's two sons are murdered, representing a violent power struggle for control of Syracusa.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Syracusa is depicted as a major governed world with palaces, political dynasties, and institutional power structures. The coup has implications for the broader Confédération of inhabited worlds.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Syracusa functions as a fully autonomous world with its own deep political history and dynasties. Earth is never referenced; the distances between worlds in the Confédération are bridged only by déremat technology.",
        "q4": "Distinct space culture",
        "q4_justification": "Syracusan palace culture features unique institutions like fécondation E.U.I.V. (ex-utero-in-vitro conception), the kreuzien Church as kingmaker, prophetic dreams, and an aristocratic system with seigneurs entirely alien to Earth traditions.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in the common confederal language while Syracusan court life employs formal and archaic speech patterns specific to the world's aristocratic traditions.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "While the physical environment of the palace is comfortable, survival requires navigating lethal political intrigue. The Scaythes execute people through mental attack, and the kreuzien Church enables violent coups, making the political environment extremely dangerous.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Syracusa has a fully developed civilization with palaces, dynasties, religious institutions, and political intrigue spanning generations. Space habitation is the unremarkable norm.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter shows competing power centers: seigneur Ranti's legitimate government, Menati's faction, the kreuzien Church, and the Scaythes (through Pamynx), all vying for control of Syracusa within the broader Confédération.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on a palace coup: Menati's political machinations, the Church's role as power broker, Sibrit's prophetic warnings, and the violent overthrow of the legitimate seigneur. The focus is entirely on political power.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The setting is a royal palace with aristocrats, prophetic dreams, and political scheming. The Scaythe execution and coup represent military-style force, but the context is primarily civilian governance and court politics.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The seigneurial system with its dynastic houses, palace intrigues, and power struggles between aristocratic factions resembles historical naval-era empires with their court politics and colonial hierarchies.",
        "q12": "Almost Earth-like",
        "q12_justification": "The Syracusan palace environment with gardens, chambers, and comfortable living quarters is depicted as essentially Earth-like. No significant physical environmental differences are mentioned in this chapter.",
    },
    {
        "chapter": "Chapitre Xiii",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chapter recounts the Guerre des Pensées (War of Thoughts) between Afrisiens and Ameurynes that devastated Earth, the exodus led by Bertelin Naflin, and the Scaythes' return to exterminate Ameurynes. The city of Exod is destroyed, representing total civilizational conflict.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The backstory describes Bertelin Naflin leading humanity's exodus from Earth to found the Confédération across multiple star systems. The narrative spans from Terra Mater to a vast interstellar civilization.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Terra Mater (Earth) is presented as a near-mythical origin world, separated by millennia and vast distances from the Confédération. Young Shari on Earth's plateau knows nothing of the starfaring civilization his ancestors founded.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Terra Mater has regressed to a primitive theocracy where amphanes (priests) execute women for adultery via chant de mort. Meanwhile the Confédération represents an entirely separate civilization. Both are radically different from modern Earth culture.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The mahdi/fou des montagnes speaks to Shari in their local language on Terra Mater, while recounting the history of the Confédération where nafle interplanétaire serves as the common tongue. The divergence between Earth and space languages is total.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Terra Mater is ruled by murderous amphanes who execute dissenters. The Guerre des Pensées devastated Earth. The Scaythes destroy the city of Exod. Survival pressure is extreme and constant across the chapter's timeline.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The backstory describes billions of humans living across the Confédération founded by Naflin's exodus. Space habitation became the norm for most of humanity after abandoning Earth.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter describes the Confédération de Naflin as a collection of distinct worlds, the absourate Order as a separate institution, and the Scaythes as an external hostile power, all constituting distinct political entities.",
        "q9": "Military / war",
        "q9_justification": "The chapter recounts the Guerre des Pensées (a civilization-ending war), the destruction of Exod, and the Scaythes' campaign of extermination. Shari's mother is executed in a ritualized act of violence. War and destruction dominate the narrative.",
        "q10": "Mostly military",
        "q10_justification": "The chapter's main content is warfare: the War of Thoughts, the Scaythes' extermination campaign, the amphanes' violent theocratic rule, and the destruction of cities. Civilian life is shown only to be destroyed.",
        "q11": "Totally unique domain",
        "q11_justification": "The Guerre des Pensées is fought with psychic powers (pierres volantes, chant de mort), not conventional weapons. The conflict between absourates, Scaythes, and amphanes operates through mental and spiritual abilities with no analogue in traditional military domains.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Terra Mater is recognizably Earth-like with mountains (Hymlyas), plateaus, and breathable air, but the pierres volantes and psychic phenomena represent physical differences. The broader Confédération requires adaptation to varied planetary environments.",
    },
    {
        "chapter": "Chapitre Xiv",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Marquinat is under kreuzien occupation with Scaythe inquisitors patrolling the streets. Dame Armina Wortling is publicly tortured with a croix-de-feu, and temples are destroyed. The atmosphere is one of systematic oppression and resistance.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Tixu arrives on Marquinat via déremat, a fully settled world with cities like Duptinat, shepherd communities, and established infrastructure. Multiple other worlds (Orange, Oursse, Deux-Saisons) are referenced as part of the Confédération.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Tixu travels between worlds via déremat teleportation. His past spans multiple planets (Orange for childhood, Oursse for training, Deux-Saisons for posting), all separated by interstellar distances requiring instantaneous transport.",
        "q4": "Distinct space culture",
        "q4_justification": "Marquinat has its own culture with orfèvres (sacred goldsmiths), bergers (shepherds) with distinct traditions, and the kreuzien Church imposing its order. Tixu's meditation with the antra reflects unique spiritual practices of this civilization.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in nafle interplanétaire, but Marquinat has local idioms and the shepherd Stanislav speaks with a distinctive regional manner. Different worlds (Orange, Oursse) also have their own cultural-linguistic flavors.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Marquinat under kreuzien occupation is dangerous, with public torture, Scaythe mental probing of citizens, and temple destruction. The antra protects Tixu from Scaythe detection, but ordinary people face severe oppression.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Marquinat has a fully functioning society with cities, craftsmen, shepherds, and an occupying religious authority. Tixu's personal history spans multiple inhabited worlds, all treated as ordinary places to live and work.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Marquinat has its own local governance now under kreuzien occupation. The CILT (interplanetary transport agency) operates across worlds, and the Order absourate, the Confédération, and the kreuzien Church each represent distinct political entities.",
        "q9": "Drama",
        "q9_justification": "The chapter is deeply personal, following Tixu's meditation and flashbacks to his childhood, mother's death, and career across multiple worlds. The witness of public torture and occupation creates emotional weight rather than action-driven narrative.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Marquinat shows both civilian life (shepherds, craftsmen, city commerce) and military occupation (kreuzien soldiers, Scaythe inquisitors, croix-de-feu torture). The domain is contested between civilian normalcy and military control.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The kreuzien occupation of Marquinat with public torture, temple destruction, and inquisitorial patrols mirrors colonial occupation of frontier territories. The resistance and oppression dynamic evokes colonial-era conflicts.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Marquinat is described with cities, countryside, and shepherds in a landscape that is habitable and broadly Earth-like. The environment does not pose significant physical challenges beyond the human-created dangers.",
    },
    {
        "chapter": "Chapitre Xv",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Filp's entire family (seigneur Dons Asmussa of Sbarao) has been massacred. The Order absourate is internally conflicted, with the bureau de Pureté suppressing heterodox ideas and covering up Long-Shu Pae's death. Strategic tension pervades the monastery.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Selp Dik hosts the Order absourate's monastery. Filp comes from Sbarao (his family's seigneurie), and multiple other worlds are referenced. The Confédération's extensive territorial network is the background to all events.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Selp Dik is a distinct world housing the Order's ancient monastery. Filp's homeworld Sbarao is separately governed and far enough that his family's massacre happened without his knowledge until after the fact.",
        "q4": "Distinct space culture",
        "q4_justification": "The Order absourate on Selp Dik has a unique monastic culture with the collège des sages, bureau de Pureté, chevalier tonsure ceremonies, and the crypte des archives. Aphykit's antra (fading life-sound) represents a wholly distinct spiritual tradition.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters communicate in the confederal common language, while the Order uses specialized terminology (crypte des archives, bureau de Pureté, chevalier tonsure) that constitutes a distinct professional and spiritual vocabulary.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Aphykit carries a virus that resists treatment, and her antra is fading. The Order's internal politics are dangerous, with the bureau de Pureté monitoring members. Filp's family has been wiped out, showing the broader conflict's lethality.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Order's monastery on Selp Dik, Filp's seigneurial family on Sbarao, and the broader Confédération all reflect a civilization where interplanetary habitation is completely ordinary.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Order absourate governs Selp Dik as an autonomous institution. Sbarao has its own seigneurie. The collège des sages and bureau de Pureté represent internal power structures, while the kreuzien Church and Scaythes are external threats.",
        "q9": "Drama",
        "q9_justification": "The chapter focuses on Filp's internal conflict between loyalty to the Order and Long-Shu Pae's heterodox teachings, his grief over his family's massacre, and his growing attraction to Aphykit. The tone is introspective and emotionally driven.",
        "q10": "Mostly military",
        "q10_justification": "The Order absourate is a warrior monastery with martial hierarchies (guerrier, chevalier), disciplinary tribunals (bureau de Pureté), and combat training traditions. Nearly all activity in the chapter relates to this martial institution.",
        "q11": "Totally unique domain",
        "q11_justification": "The Order absourate combines monastic spirituality, psychic martial arts, and the antra tradition in a way that has no analogue in naval, air, or other conventional military domains. The crypte des archives and Xui discipline are wholly original.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Selp Dik's monastery environment is habitable and comfortable, with treatment facilities for Aphykit. No significant physical environmental differences from Earth are described in this chapter.",
    },
    {
        "chapter": "Chapitre Xvi",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Babsée betrays Tixu to the Scaythes for career advancement. Tixu must escape mercenaries hunting him through the city. Anidoll has been arrested, and his daughters are captured. Menati Ang's imperial coronation represents the consolidation of Scaythe-backed tyranny.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter takes place on Marquinat with its city Duptinat, while referencing Selp Dik (Tixu's destination) and Syracusa (Menati's coronation broadcast everywhere). The Confédération's vast territorial network is the backdrop to all events.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Tixu attempts to use an ancient déremat in Anidoll's grenier to transfer to Selp Dik despite extreme risk, demonstrating that worlds are separated by distances only traversable through teleportation technology.",
        "q4": "Distinct space culture",
        "q4_justification": "The chapter features the CILT transport agency, ancient déremat technology in hidden attics, the Scaythes' regime broadcast of imperial coronation, and Anidoll's daughters carrying on their father's orfèvre traditions, all reflecting a wholly distinct civilization.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tixu and Babsée communicate in the common confederal language, while Marquinat has local customs and the orfèvre family uses specialized vocabulary. Menati's coronation is broadcast in the universal language across all worlds.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Tixu is betrayed, hunted by mercenaries, and must use a dangerously ancient déremat to escape. Anidoll has been arrested. The daughters are captured. The Scaythe regime's reach is total, making survival extremely precarious.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Duptinat is a functioning city with agencies, shops, and residents. The imperial coronation is broadcast across all worlds simultaneously, showing an interconnected interstellar civilization where space habitation is the norm.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Menati Ang's imperial coronation represents a new centralized authority, while Marquinat has local governance, the CILT operates independently, and the Order absourate on Selp Dik remains a separate entity. Multiple polities coexist and compete.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is driven by betrayal, pursuit, and desperate escape. Tixu's antra gives him a vision of the trap, he flees mercenaries through the city, and he risks his life using an ancient unstable déremat. The pacing is tense and survival-focused.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter features both civilian elements (Babsée's CILT agency, the orfèvre family, city life) and military/security forces (mercenaries, Scaythe agents, the imperial regime). The domain is contested between civilian normalcy and authoritarian control.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Tixu navigates an occupied territory where the imperial regime hunts dissidents, locals are arrested, and resistance operates underground. The dynamic of occupation, betrayal, and flight mirrors colonial frontier conflicts.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Duptinat is a habitable city with streets, buildings, and normal urban infrastructure. The physical environment is not significantly different from Earth; the dangers are entirely human-created.",
    },
]

country = 'France'
book_title = 'Les Guerriers du Silence'
csv_path = 'data/results/France_Les_Guerriers_du_Silence.csv'

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
