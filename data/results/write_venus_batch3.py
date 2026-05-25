import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter Thirteen",
        "q1": "No contestation",
        "q1_justification": "There is no military or political conflict in this chapter. Ransom rides a fish across the ocean, encounters passive water-people who ignore him, and has a philosophical conversation with Weston/the Un-man about death and the nature of the universe. The only physical conflict is Weston dragging Ransom underwater at the end.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom is a lone visitor to Perelandra (Venus) on a mission. He has no permanent settlement and is adrift on the ocean riding a fish. The planet has no human infrastructure or territory held by Earth people.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom is on Venus, completely cut off from Earth. He mentions that Germans may be bombing London, indicating wartime Earth is far away. He has no space-ship access and no way to return, reflecting major separation from Earth.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Perelandra has water-people who share the planet but have no interaction with humans, floating islands, and a cosmic spiritual hierarchy governed by Maleldil. The social order is nothing like Earth society, with a King and Queen who are the only two humans on the entire planet.",
        "q5": "Other / Unsure",
        "q5_justification": "Language is not a significant theme in this chapter. Ransom and Weston speak English to each other. The broader Perelandrian context uses Old Solar, but language differences are not explored here.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Ransom is adrift on an open ocean with no food except alien seaweed that dangerously alters his consciousness, no shelter, and must cling to a tiring fish. He faces drowning, hunger, and exhaustion. The environment is survivable but demands constant effort.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom and Weston are humans on Venus. Ransom is essentially a lone explorer on an alien world, making human presence in space exceptionally rare in this narrative.",
        "q8": "No political order / ungoverned",
        "q8_justification": "There is no political structure governing space in this chapter. Ransom is adrift on an alien ocean with no government, institutions, or political authority present. The only reference to Earth politics is a passing mention of the war.",
        "q9": "Adventure / exploration",
        "q9_justification": "This chapter is primarily an adventure narrative with Ransom riding a fish across an alien ocean, encountering strange water-people, eating alien seaweed, and engaging in philosophical exchanges with Weston before a dramatic underwater abduction.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military presence or framework in this chapter. Ransom is a civilian philologist, and Weston is a scientist. The only mention of military matters is a brief reference to the war on Earth and bayonet wounds.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Space travel and the Perelandrian setting are characterized through oceanic imagery. Ransom rides a fish across vast seas, encounters water-people, and the chapter is dominated by waves, currents, ocean vastness, and maritime survival challenges.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Perelandra's environment is radically different from Earth: vast oceans with no visible land, phosphorescent water-people, seaweed that alters human consciousness, floating islands, and alien biology. Ransom's body is constantly challenged by the conditions."
    },
    {
        "chapter": "Chapter Fourteen",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The conflict in this chapter is personal rather than political or territorial. Ransom fights and kills the Un-man in a physical struggle, then is pursued by an unknown creature through caves. This is interpersonal combat, not a contest over space itself.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom remains a lone visitor trapped in subterranean caves on Venus. He has no settlement, infrastructure, or territorial claim. He is simply trying to survive and find his way out of the caverns.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom is deep inside Venus's cave system with no way to contact or return to Earth. He is completely separated from his home world, trapped underground on an alien planet with no space-ship in reach.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The subterranean world of Perelandra features giant multi-segmented cave creatures, rivers of fire, vast underground caverns, and a spiritual cosmology involving demons and divine forces. This is completely unlike any Earth society.",
        "q5": "Other / Unsure",
        "q5_justification": "Language is not meaningfully addressed in this chapter. Ransom speaks English and recites literary works from memory. The Un-man speaks broken English. No distinct space language issues arise.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Ransom is trapped in pitch-black caves with no food, navigating by touch, climbing dangerous cliffs, wading through underground rivers, and facing extreme heat near a fire pit. He faces the Un-man and a giant cave creature. Survival pressure is constant and severe.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom is alive as a human on Venus after killing the Un-man. He is completely alone in the underground caves, the sole human being on the entire planet.",
        "q8": "No political order / ungoverned",
        "q8_justification": "There is no political structure whatsoever in the subterranean caves. Ransom is alone in a lawless, ungoverned wilderness deep beneath the surface of an alien planet.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "This chapter is dominated by survival horror: Ransom fights for his life underwater, strangles the Un-man in pitch darkness, navigates terrifying caves blind, and faces a monstrous multi-segmented creature in a fire-lit cavern. The tone is intensely suspenseful.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military element in this chapter. Ransom is a civilian academic fighting for survival. His combat with the Un-man is personal and spiritual, not military in nature.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The underground caves evoke frontier exploration imagery: Ransom navigates unknown territory, climbs uncharted cliffs, follows waterways through darkness, and encounters unknown creatures. It resembles exploring an uncharted wilderness rather than naval or aerial domains.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The underground environment features pitch-black caves with rivers of fire, giant multi-segmented creatures, translucent ice-like rock formations, and subterranean waterways that lead through the planet's interior. The physics of light, heat, and geology are fundamentally alien."
    },
    {
        "chapter": "Chapter Fifteen",
        "q1": "No contestation",
        "q1_justification": "This chapter is entirely peaceful. Ransom convalesces beside a mountain stream, explores the mountain landscape, encounters gentle creatures like tiny mammals and a shy singing beast, and climbs to a sacred valley. There is no conflict of any kind.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom is still a lone visitor on Perelandra recovering from his ordeal. He finds a coffin-like vessel prepared for his return to Earth, confirming his presence is temporary. He has no settlement or territory.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom is on Venus, completely separated from Earth. He discovers a transport vessel for returning home, but he remains profoundly distant from Earth with no communication possible. The journey between worlds is vast.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The mountain ecosystem features ripple-tree forests, tiny scale-model mammals, a large singing beast that is nursed by a different species, crystal cliffs, and a sacred valley with red lilies. The world operates on principles entirely unlike Earth society, governed by spiritual beings (eldila).",
        "q5": "Other / Unsure",
        "q5_justification": "Ransom carves an inscription in Old Solar using Roman letters, blending Earth and Perelandrian language. Language is mentioned but not as a barrier or significant theme in the chapter.",
        "q6": "Manageable but risky",
        "q6_justification": "During convalescence, Ransom finds abundant food from grape-like fruit clusters and clean water. The mountain environment is beautiful and hospitable. His main physical concern is a heel wound that will not stop bleeding, but the environment itself is gentle and sustaining.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Ransom is the sole human on Venus. He is completely alone on the mountain, the only person of his species on the entire planet, making human presence in space exceptionally rare.",
        "q8": "No political order / ungoverned",
        "q8_justification": "The mountain wilderness has no political order. Ransom is alone with animals and the natural landscape. The eldila appear at the end but have not yet established any governance structure in this chapter.",
        "q9": "Adventure / exploration",
        "q9_justification": "This chapter focuses on exploration and discovery as Ransom recovers and then explores the mountain landscape, encountering new flora and fauna including ripple-trees, tiny mammals, and the singing beast. He climbs to a sacred valley at the summit.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military element whatsoever. Ransom is a civilian exploring a peaceful mountain landscape, recovering from wounds, and encountering gentle wildlife. The tone is pastoral and contemplative.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Ransom's solitary exploration of uncharted mountain terrain, discovering new species and landscapes, and carving an inscription on a cliff wall all evoke frontier exploration imagery. He is a lone explorer in virgin wilderness.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mountain features crystal/translucent cliffs, ripple-tree forests with streaming blue fronds, tiny scale-model mammals, and a massive singing beast unlike anything on Earth. The landscape with rose-red peaks, golden sky-roof, and sacred lily valley is profoundly alien."
    },
    {
        "chapter": "Chapter Sixteen",
        "q1": "No contestation",
        "q1_justification": "This chapter is a peaceful coronation ceremony. The eldila of Mars and Venus appear, animals gather, and the King and Queen arrive to assume rulership of Perelandra. There is no conflict, competition, or contestation of any kind.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The King and Queen are crowned as rulers of Perelandra, establishing permanent governance over the planet. Perelandra (the eldil) transfers authority to them, and they plan to fill the world with their children, indicating permanent habitation and territorial governance.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom is on Venus, separated from Earth by interplanetary distance. The eldila discuss traveling between worlds and Deep Heaven. The Oyarsa of Mars has visited Earth (Thulcandra), indicating vast interplanetary distances are traversed.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The social order involves eldila (angelic planetary rulers), a King and Queen who are the Adam and Eve of Venus, and a cosmic hierarchy under Maleldil. The coronation ceremony with thirty-foot-tall burning white eldila and gathering animal processions is entirely unlike any Earth society.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Communication occurs in Old Solar, the shared language of the solar system. The Oyarsa of Mars mentions learning the divided tongues of Earth from Ransom. Old Solar serves as a lingua franca while Earth has its own local languages.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The mountain top environment is peaceful and beautiful with a pool, lilies, and gentle light. The King and Queen thrive naturally. The environment poses no survival threats during this ceremonial chapter.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom, the King, and the Queen are humans present. Ransom is the sole Earth human on Venus, and the King and Queen are native Perelandrians. Human presence in space remains exceptionally rare.",
        "q8": "Single unified authority",
        "q8_justification": "The chapter establishes a single unified authority over Perelandra: the King (Tor) and Queen (Tinidril) are crowned as Oyarsa-Perelandra, receiving absolute dominion over the planet from the eldil who previously administered it.",
        "q9": "Drama",
        "q9_justification": "This chapter is a dramatic coronation ceremony with profound theological and philosophical content. The arrival of the King and Queen, the appearance of the eldila in visible form, and the formal transfer of planetary authority create a solemn dramatic atmosphere.",
        "q10": "Entirely civilian",
        "q10_justification": "The coronation is entirely civilian and spiritual in nature. There is no military presence, weaponry, or martial framework. Authority is transferred through a ceremonial and religious process.",
        "q11": "Totally unique domain",
        "q11_justification": "Space in this chapter is characterized as Deep Heaven, a spiritual realm governed by eldila and cosmic hierarchy under Maleldil. It does not resemble naval, aerial, frontier, or cyber domains. The framing is theological and cosmological, entirely unique.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The environment features thirty-foot-tall burning white eldila, colors beyond the human spectrum, a sense that the planet itself is rushing through space, and a landscape with rose-red lily peaks and a golden sky. The physical reality is profoundly different from Earth."
    },
    {
        "chapter": "Chapter Seventeen",
        "q1": "No contestation",
        "q1_justification": "This chapter contains no conflict. It depicts the continuation of the coronation, philosophical speeches about the Great Dance of the universe, the King and Queen's plans for Perelandra, and Ransom's peaceful departure back to Earth.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The King declares plans to govern from the Holy Mountain for ten thousand years, fill the world with children, build structures on the Fixed Land, and eventually expand into Deep Heaven. Permanent habitation and governance of Venus is being established.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom has been on Venus for over a year (a full orbit of Arbol/the Sun). He is placed in a coffin-like vessel for the return journey to Earth, emphasizing the vast interplanetary distance and major separation from home.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The King plans to make beasts into speaking beings (hnau), tear the sky curtain, and transform human bodies to be like eldila. The society envisioned is a cosmic spiritual civilization with no parallel on Earth, governed by theological principles entirely alien to terrestrial social orders.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The King, Queen, eldila, and Ransom communicate in Old Solar, the shared language of the solar system. Ransom notes that what Perelandra calls the beginning, Earth calls the Last Things, showing cultural-linguistic variation within a shared framework.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The mountain top is peaceful and sustaining. The King washes Ransom's foot. The environment is gentle and hospitable. Ransom's only physical concern is his bleeding heel, which the King suggests will heal slowly due to the life-giving properties of Perelandra.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom is present as an Earth human, alongside the two native Perelandrians. He departs alone in the transport vessel. Human presence in space remains exceptionally rare, limited to a single explorer.",
        "q8": "Single unified authority",
        "q8_justification": "The King (Tor-Oyarsa-Perelendri) rules as the single unified authority over all of Perelandra. He names places by decree, plans governance from the Holy Mountain throne, and his word is described as law unchangeable.",
        "q9": "Drama",
        "q9_justification": "This chapter is a dramatic philosophical and theological culmination featuring the King's grand speeches about the future of Perelandra, the mystical vision of the Great Dance, and Ransom's emotional farewell. The tone is solemn, elevated, and deeply dramatic.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military element. The King's plans for Perelandra involve building, creating, nurturing beasts, and spiritual development. Even the future siege of Earth mentioned by the King is framed in spiritual rather than military terms.",
        "q11": "Totally unique domain",
        "q11_justification": "Space is described as Deep Heaven, a spiritual-cosmological realm where the Great Dance of all creation unfolds. The King plans to tear the sky curtain and make Deep Heaven familiar to his descendants. This framing is entirely unique, not resembling any terrestrial military domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter describes the Great Dance as a vision of intertwining light-cords in multiple dimensions, colors beyond the human spectrum, and a year passing in what felt like moments. The King speaks of transforming human bodies to be like eldila. The physical reality transcends Earth experience."
    }
]

country = 'France'
book_title = 'Voyage To Venus'
csv_path = 'data/results/France_Voyage_To_Venus.csv'

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

print('Done.')
