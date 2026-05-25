import json, csv, os

chapters_data = [
    {
        "chapter": "Chapitre Xvii",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter revolves around intense political and strategic maneuvering. Harkot secretly plots to overthrow Pamynx, forges an alliance with the muffi Barrofill against the connétable, and discusses the upcoming military assault on the Absourate Order on Selp Dik, revealing constant power struggles over control of the empire.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The chapter describes the new empire ruling over 'mondes recensés' (catalogued worlds) across the Milky Way, with Scaythes deployed on all settled worlds, an imperial palace on Syracusa, and plans for further matricial expansion across conquered territories.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Earth (Terra Mater) is referenced only as a distant historical origin. The story takes place entirely in a far-future interstellar civilization spanning many worlds across the Milky Way, with no connection to Earth remaining.",
        "q4": "Distinct space culture",
        "q4_justification": "Syracusan court culture with its elaborate A.P.D. mental control, Scaythe protectors of thought, the Kreuzian Church's rituals, and the complex social hierarchies of courtisans represent a wholly distinct civilization with no Earth parallels beyond basic human nature.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Characters from different worlds communicate readily, suggesting a common language (nafle), but references to specific cultural terms like 'acaba,' 'colancor,' and Church terminology indicate local linguistic variation alongside the shared language.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The chapter takes place entirely in palatial urban environments on Syracusa. Space itself poses no survival challenge; characters walk through streets, visit palaces, and live comfortably. The threats come from political actors, not environmental conditions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Billions of humans live across multiple settled worlds as described by the text. Menati Ang rules over 'des milliards d'êtres humains' spread across catalogued worlds, and interstellar habitation is entirely routine.",
        "q8": "Single unified authority",
        "q8_justification": "The chapter depicts a single imperial authority under Emperor Menati Ang, with the connétable Pamynx and the Kreuzian Church as pillars of this unified empire that has replaced the former Naflin Confederation.",
        "q9": "Political / diplomatic",
        "q9_justification": "The entire chapter is a political thriller: Harkot manipulates the muffi by revealing assassination plots, negotiates a secret alliance, and schemes to replace Pamynx as the power behind the throne. The focus is on intrigue, deception, and political maneuvering.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter focuses on civilian political intrigue at the imperial court and the Church. While Scaythe tueurs mentaux and assassins of Pritiv are mentioned in the context of the upcoming battle on Selp Dik, the main action is diplomatic and conspiratorial.",
        "q11": "Totally unique domain",
        "q11_justification": "Space in this chapter is characterized as an arena for psychic warfare and mental domination rather than any traditional military domain. The Scaythes use telepathic powers, mental protection, and inquisition rather than naval, air, or conventional military frameworks.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The settled worlds described are habitable with manageable differences. Syracusa has five nocturnal satellites and different flora, but humans live comfortably without special technology. The physical environment is not a major concern.",
    },
    {
        "chapter": "Chapitre Xviii",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter depicts the imperial armies arriving on Selp Dik to prepare for battle against the Absourate Order. Scaythes and mercenaries of Pritiv impose a curfew on Houhatte, and Tixu is hunted by an inspobot, reflecting constant strategic conflict across space.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The new empire controls multiple worlds and projects military force to Selp Dik to destroy the last bastion of resistance. Deremats transfer soldiers across interstellar distances, and the imperial bullovision broadcasts across all worlds, demonstrating extensive territorial control.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Tixu is transferred from another world to Selp Dik via deremats (teleportation machines), a journey spanning interstellar distances. Earth is a forgotten ancestral homeland referenced only in legends. The distances are effectively irrelevant due to transfer technology.",
        "q4": "Distinct space culture",
        "q4_justification": "Selp Dik has its own unique Selpidian culture centered on ocean fishing, the legends of fées d'Albar, monagres, and the sacred annual festival with ritual sacrifice and communal festivities entirely unlike any Earth tradition.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Kwen Daël and Tixu communicate in 'nafle' (the common tongue), but the Selpidians have their own local expressions and legends. The Tchutchu tribe on Nouhenneland speaks its own language, showing local variation alongside the shared lingua franca.",
        "q6": "Manageable but risky",
        "q6_justification": "Tixu nearly drowns after being transferred into the open ocean and must fight for survival against the elements until rescued by a monagre. The ocean environment is harsh but survivable with help, and the planetary environments are generally livable.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Multiple planets are inhabited by distinct human populations. Selpidians live on Selp Dik, Orangiens on Orange, and the imperial bullovision broadcasts to all worlds. Interstellar habitation is completely ordinary.",
        "q8": "Single unified authority",
        "q8_justification": "The new empire under Menati Ang and Pamynx has conquered or absorbed all former polities. The Selpidian recteurs are forced to submit to imperial military authority, and the Kreuzian Church operates as the empire's religious arm across all worlds.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows Tixu's survival adventure: nearly drowning, being rescued by a monagre, arriving on Selp Dik, exploring Selpidian culture, evading the inspobot through a spiritual awakening, and using psychic vision to locate Aphykit in the monastery.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter mixes civilian life (Selpidian fishing culture, festivals, daily existence) with military occupation as imperial forces arrive with mercenaries, Scaythes, and impose martial law on the civilian population of Houhatte.",
        "q11": "Totally unique domain",
        "q11_justification": "The interstellar domain is traversed via deremats (matter teleportation) and characterized by psychic warfare with Scaythe mental powers. Tixu's spiritual journey through the 'antra' and silence represents a completely unique framework unlike any conventional military domain.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Selp Dik is a mostly oceanic planet with a single continent, different from Earth but habitable. The ocean is vast and dangerous, but humans live comfortably on land. The planet has its own flora and fauna (monagres, mouettes jaunes) but requires no special technology.",
    },
    {
        "chapter": "Chapitre Xix",
        "q1": "Total war / constant conflict",
        "q1_justification": "This chapter depicts the devastating battle between the Absourate Order and the imperial armies on Selp Dik. Thousands of chevaliers are slaughtered by Scaythe mental killers, and the chapter describes a one-sided massacre with total annihilation of the Order.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The empire has sent its armies across interstellar space to destroy the Absourate Order's last bastion on Selp Dik. The narrative references the imperial conquest of numerous worlds and the Order's former role in the Naflin Confederation spanning many star systems.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Filp Asmussa's homeworld Sbarao is referenced as a distant place with its own lordship and traditions. The story takes place across a galaxy-spanning civilization where Earth is only a mythological reference, indicating extreme distances from any original point.",
        "q4": "Distinct space culture",
        "q4_justification": "The Absourate Order's monastic culture with its rigid hierarchy, chevalier rituals, tonsure ceremonies, cri de mort sonic weaponry, and Xui meditation practices represents a wholly unique space civilization with no Earth equivalent.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The Order uses the dead language of 'Terra Mater' in sacred rituals alongside the common spoken language. Filp, from Sbarao, communicates easily with Choud Al Bah and others, suggesting a shared lingua franca with specialized religious terminology.",
        "q6": "Manageable but risky",
        "q6_justification": "Selp Dik's coastal environment is described with ocean, beaches, and a temperate monastery setting. The physical environment is habitable, but the human-made dangers of war are extreme. The planet itself does not pose survival challenges.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The monastery houses over 10,000 members from various worlds. Filp is from Sbarao, others from different planets. Interstellar habitation and travel are completely unremarkable in this civilization.",
        "q8": "Single unified authority",
        "q8_justification": "The new empire has systematically conquered all opposition. This chapter shows the destruction of the Absourate Order, the last independent institution, completing the empire's total dominion over the catalogued worlds.",
        "q9": "Military / war",
        "q9_justification": "The chapter's climax is the great battle of Houhatte where the imperial armies annihilate the entire Absourate Order. The narrative depicts the preparations for war, Filp's knighting before battle, the massacre, and the death of thousands of chevaliers.",
        "q10": "Mostly military",
        "q10_justification": "Nearly the entire chapter revolves around military concerns: Filp's prechevaleresque retreat for battle readiness, the Order's war mobilization, the sage's battlefield speech, and the devastating one-sided combat that destroys the Order.",
        "q11": "Totally unique domain",
        "q11_justification": "The battle is fought with psychic weapons: the chevaliers' 'cri de mort' (death cry) sonic attacks against the Scaythes' mental killing powers. Mercenaries use disc weapons. This warfare is unlike any conventional naval, air, or frontier paradigm.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The battle takes place on a beach with ocean tides, stone monastery walls, and a temperate climate. Selp Dik is environmentally habitable and similar enough to Earth-like conditions that no special adaptation is needed.",
    },
    {
        "chapter": "Chapitre Xx",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter depicts Tixu's desperate rescue of Aphykit from the doomed monastery while the battle rages outside. The chevalier Nobeer O'An reveals the Order's internal murders and sets fire to the archives, and the aftermath shows the total destruction of the Order and monastery by imperial forces.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The imperial army brings deremats and heavy weapons to Selp Dik, demonstrating the ability to project military force across interstellar space. After the battle, the entire monastery is reduced to ashes by ray cannons, showing the empire's absolute territorial control.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrative references an island beyond the known ocean and multiple worlds across the galaxy. Earth exists only as ancient history. The civilization spans distances so vast that only teleportation technology makes them traversable.",
        "q4": "Distinct space culture",
        "q4_justification": "The chapter reveals the dark inner workings of the Absourate Order: the assassination of Mahdi Seqoram 42 years ago by the four sages, the cover-up, and the crypte des archives containing forbidden knowledge. This is a unique monastic culture with no Earth parallel.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tixu and Kwen Daël communicate easily, and Nobeer O'An speaks to Tixu without language barriers. The Selpidian pêcheur uses local expressions while the chevalier uses Order terminology, all within a shared common language.",
        "q6": "Manageable but risky",
        "q6_justification": "Tixu navigates the dangerous monastery foundations, fights a deranged chevalier, descends through collapsing tunnels with Aphykit on his shoulders while fire spreads through the galleries. The environment becomes lethal due to the fire and structural collapse, but the planet itself is habitable.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Thousands of people lived in the monastery, Selpidians populate the continent, and the empire operates across many inhabited worlds. Interstellar habitation is the unremarkable norm.",
        "q8": "Single unified authority",
        "q8_justification": "The empire's total destruction of the monastery and execution of every member of the Order demonstrates absolute single authority. Harkot notes this is part of the ongoing imperial plan, with no rival power remaining.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a survival thriller: Tixu descends into dark tunnels, encounters a mad chevalier who tries to strangle him, escapes a raging fire in the collapsing foundations, and rappels down the monastery wall with Aphykit as the structure crumbles around them.",
        "q10": "Mostly military",
        "q10_justification": "The chapter takes place during and after the military destruction of the Absourate Order. Imperial forces systematically destroy all survivors with momifying rays and level the monastery with heavy cannons. Military action dominates the narrative.",
        "q11": "Totally unique domain",
        "q11_justification": "The warfare involves Scaythe mental killing powers and ray cannons that reduce entire buildings to ash. Harkot perceives an elusive psychic presence he cannot identify. The military domain operates on psychic and energy-weapon principles unlike any conventional framework.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Selp Dik's ocean, tides, and coastal geography are Earth-like enough that humans live without special technology. The aquasphère navigates the ocean easily, and the monastery sits on a peninsula accessible by sea.",
    },
    {
        "chapter": "Chapitre Xxi",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter reveals the muffi and Harkot conspiring against connétable Pamynx during celebrations of the empire's military victory. The political intrigue between the emperor, the Church, and the Scaythes represents ongoing strategic struggle for control of the empire.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The epigraph describes Kreuzian missionaries spreading to every planet, city, and village. Pamynx inspects planetary organizations across the empire, and the muffi describes spreading the Kreuzian faith across all worlds, demonstrating vast territorial occupation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The conversation references threats dispersed across the entire universe of known worlds. Pamynx travels from planet to planet inspecting the empire. Earth is only referenced as the ancestral origin of the Ma-Jahi province, showing extreme separation from any origin point.",
        "q4": "Distinct space culture",
        "q4_justification": "The Syracusan imperial court with its sohorgo dance performances, elaborate courtisan fashions (nacrelle-painted teeth, crown-eau), protecteurs de pensées system, and the Kreuzian Church's inquisitorial apparatus represent a fully distinct interstellar civilization.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "All characters at the imperial court communicate in a common language, but specialized terminology abounds: A.P.D. (auto-psykè-défense), acaba classifications, Kreuzian religious terms, and distinct provincial references like Ma-Jahi indicate linguistic variation.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The chapter takes place entirely in luxurious palatial settings: the Amphithéâtre with floating loges, the imperial gardens with exotic flora, and elegant reception rooms. No environmental hazards or survival pressures are present.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The empire spans countless inhabited worlds with established cities, governments, and cultural institutions on each. Dame Sibrit plans to return to the province of Ma-Jahi on another world, treating interstellar travel as routine.",
        "q8": "Single unified authority",
        "q8_justification": "The new empire under Menati Ang rules all known worlds. The chapter shows the Church, the connétable, and the emperor as the three pillars of this single imperial authority, with the muffi and Harkot scheming to redistribute power within this structure.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is dominated by political maneuvering: Menati Ang's frustrated courtship of Dame Sibrit, the muffi's urgent secret audience proposing to overthrow Pamynx, and Harkot's manipulation of events from the shadows as protector of Dame Sibrit.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The setting is the imperial court during victory celebrations with dance performances, poetry, and courtisan society. Military matters are discussed only in the political context of Pamynx's role and his potential replacement.",
        "q11": "Totally unique domain",
        "q11_justification": "The power dynamics operate through psychic warfare (Scaythe mental protection and inquisition), spiritual manipulation (Kreuzian Church infrastructure), and political intrigue rather than any conventional military domain metaphor.",
        "q12": "Almost Earth-like",
        "q12_justification": "Syracusa's environment in this chapter appears entirely comfortable: gardens with exotic trees, a palace with fountains, five satellites providing nocturnal light, and a blue sun (Soleil Saphyr). The physical differences are cosmetic rather than challenging.",
    },
    {
        "chapter": "Chapitre Xxii",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Imperial forces hunt the fugitives, eventually invading the île des monagres with deremats. Tixu saves Kwen Daël from execution using the antra, and the mercenaries massacre all the monagres. The chapter depicts ongoing pursuit and violent conflict between imperial forces and the protagonists.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The imperial occupiers control Selp Dik, imposing edicts and executing dissenters on croix-de-feu. The Kreuzian Church has established missions on the planet. Imperial control extends to remote islands as deremats are deployed to hunt fugitives anywhere.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The island is isolated in a vast brume-covered ocean. Tixu and Aphykit eventually learn to teleport via thought across interstellar distances, visiting multiple worlds in the final chapter. Earth exists only as the faintest ancestral memory.",
        "q4": "Distinct space culture",
        "q4_justification": "The chapter depicts the unique Selpidian culture with its monagre legends, ocean-based way of life, and féelle mythology. Tixu develops a completely new spiritual practice through the antra, creating an unprecedented form of consciousness-based travel.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tixu and Aphykit communicate easily, and Tixu speaks with Selpidians in a common language. However, local terms persist: Selpidian ocean terminology, the spiritual vocabulary of the antra, and Aphykit's Syracusan speech patterns.",
        "q6": "Manageable but risky",
        "q6_justification": "The île des monagres is exposed to storms, cold brume, and limited food (only algae). Aphykit nearly dies from her virus before the monagre-provided algae cure her. The environment is survivable but demanding without civilization's comforts.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Multiple inhabited worlds are referenced. Imperial forces deploy across planets routinely. Tixu and Aphykit's thought-travel takes them to various inhabited worlds, all with established human populations, showing interstellar habitation as normal.",
        "q8": "Single unified authority",
        "q8_justification": "The empire exerts authority even on remote Selp Dik, executing dissidents and hunting fugitives. The Kreuzian cardinal, Scaythe inquisitors, and Pritiv mercenaries operate together as instruments of the single imperial authority.",
        "q9": "Adventure / exploration",
        "q9_justification": "Tixu's spiritual journey of self-discovery on the island, his developing teleportation abilities, his rescue of Kwen Daël, and the dramatic escape with Aphykit as imperial forces close in create an adventure narrative centered on exploration of both physical and spiritual frontiers.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The chapter alternates between Tixu's peaceful spiritual development on the island and the military occupation of Selp Dik. Imperial forces conduct executions and eventually assault the island with mercenaries and Scaythes, intruding on civilian space.",
        "q11": "Totally unique domain",
        "q11_justification": "Tixu develops the ability to teleport using thought alone, fusing with a deremat's essence through meditation. The antra provides psychic protection against Scaythe inquisition. This represents a completely unique domain of consciousness-based travel and warfare.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The île des monagres has a brume-covered climate, rocky terrain, and an ocean teeming with giant cetaceans. While different from Earth, the environment supports human life with basic provisions, and the algae provide both food and medicine.",
    },
    {
        "chapter": "Chapitre Xxiii",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter reveals through Cardinal Molanaliphul's letter and eyewitness testimonies that Tixu and Aphykit's mysterious appearances across multiple worlds are causing alarm in the Church and empire. The contestation is indirect: a simmering resistance through spiritual awakening rather than open warfare.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The testimonies come from planets Ja-Hokyo, Alemane, Orange, and Nouhenneland, all under imperial and Kreuzian control. Missionaries, inquisitors, and croix-de-feu are present across all worlds, demonstrating the empire's extensive territorial occupation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Tixu and Aphykit travel across multiple star systems using only thought. The testimonies span planets in different systems. Terra Mater is referenced as the location of Shari's mountain retreat, an ancient and remote world. The distances are interstellar and immense.",
        "q4": "Distinct space culture",
        "q4_justification": "The chapter showcases diverse planetary cultures: Ja-Hokyoist traditions, Alemane village life under Kreuzian oppression, Orange fabric manufacturing, Nouhenneland's Tchutchu tribal society, and Shari's amphane culture. Each world has its own distinct civilization.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Tixu speaks 'nafle' with the Nouhenneland explorer but the Tchutchu tribe has its own 'langue tchutchu.' The testimonies are from people across different worlds who all communicate in a common language for official proceedings, while maintaining local tongues.",
        "q6": "Manageable but risky",
        "q6_justification": "Shari and the fou des montagnes live in mountain wilderness, surviving on berries and roots. The Nouhenneland jungle is hostile with the Tchutchu tribe capturing intruders. The various planetary environments are habitable but present moderate challenges.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The four testimonies from different inhabited worlds, the imperial inquisition's interplanetary reach, and the references to settled civilizations on every planet mentioned confirm that space habitation is entirely normalized across the known universe.",
        "q8": "Single unified authority",
        "q8_justification": "The Kreuzian Church and imperial inquisition operate across all worlds described. The cardinal's report to the muffi demonstrates a single ecclesiastical-imperial authority structure governing the known universe, though primitive tribes like the Tchutchus remain outside its direct control.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter follows Tixu and Aphykit's interstellar quest to find the mysterious teacher, visiting world after world. Shari's story of taming the flying stone and the final meeting at the mountain torrent create a narrative of spiritual adventure and discovery.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter is predominantly civilian: witnesses describe everyday life disrupted by mysterious appearances. The Kreuzian inquisition and croix-de-feu represent an oppressive military-religious presence, but the focus is on civilian reactions and spiritual journeys.",
        "q11": "Totally unique domain",
        "q11_justification": "Tixu and Aphykit travel between worlds using pure thought, without any machine or vehicle. Shari flies on a stone through mental communion with matter. This consciousness-based traversal of interstellar space is a completely unique conceptualization of the domain.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter depicts varied but habitable worlds: Ja-Hokyo's mountain torrents, Alemane's villages, Orange's manufacturing towns, Nouhenneland's tropical jungles, and Terra Mater's Hymlya mountain range. Each is distinct but supports human life without extraordinary technology.",
    },
]

country = "France"
book_title = "Les Guerriers du Silence"
csv_path = os.path.join("data", "results", "France_Les_Guerriers_du_Silence.csv")

# Load questions
with open(os.path.join("data", "questions.json"), "r", encoding="utf-8-sig", errors="replace") as f:
    questions = json.load(f)

os.makedirs(os.path.join("data", "results"), exist_ok=True)

fieldnames = ["country", "book", "chapter"]
for q in questions:
    fieldnames.append(f"q{q['number']}")
for q in questions:
    fieldnames.append(f"q{q['number']}_justification")

# Resume support: check existing chapters
existing_chapters = set()
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_chapters.add(row["chapter"])

written = 0
skipped = 0

for ch in chapters_data:
    if ch["chapter"] in existing_chapters:
        print(f"Skipping {ch['chapter']} (already in CSV)")
        skipped += 1
        continue

    row_dict = {
        "country": country,
        "book": book_title,
        "chapter": ch["chapter"],
    }
    for q in questions:
        qn = q["number"]
        row_dict[f"q{qn}"] = ch[f"q{qn}"]
        row_dict[f"q{qn}_justification"] = ch[f"q{qn}_justification"]

    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row_dict)

    print(f"Wrote {ch['chapter']}")
    written += 1

print(f"\nDone. Wrote {written} chapters, skipped {skipped}.")
