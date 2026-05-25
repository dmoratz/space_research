import json, csv, os

chapters_data = [
    {
        "chapter": "Prologue",
        "q1": "No contestation",
        "q1_justification": "The Prologue describes Earth's formation over billions of years, from interstellar dust to primordial ocean to the evolution of life. There is no conflict or contestation; it is a poetic geological/evolutionary narrative.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is depicted. The chapter describes Earth's formation from cosmic material but does not portray any inhabitation or territorial presence in space.",
        "q3": "Other / Unsure",
        "q3_justification": "No journey through space occurs. The narrative covers geological time on Earth, from planetary accretion to the emergence of life.",
        "q4": "Other / Unsure",
        "q4_justification": "No society of any kind is depicted. The chapter covers pre-human geological and biological evolution.",
        "q5": "Other / Unsure",
        "q5_justification": "No language or communication is depicted. The chapter predates the existence of any sentient beings.",
        "q6": "Other / Unsure",
        "q6_justification": "Space is referenced only as the origin of Earth's material. No space environment is directly experienced or depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. The chapter describes planetary formation and evolution on Earth's surface.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order exists. The chapter predates all civilization.",
        "q9": "Other / Unsure",
        "q9_justification": "The chapter is a poetic, cosmic-scale prologue describing Earth's formation. It does not fit standard genre categories; it reads as philosophical/scientific prose poetry.",
        "q10": "Other / Unsure",
        "q10_justification": "No civilian or military presence exists. The chapter predates humanity entirely.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed or analogized.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced by any character. The chapter is a cosmological overview of Earth's formation.",
    },
    {
        "chapter": "Chapter 1 - Shadowplay Upon the Sea",
        "q1": "No contestation",
        "q1_justification": "A mysterious sea creature with advanced technology (a pod with manipulation arms, needles, hemispherical cap) lives in the primordial ocean. It hunts fish and observes massive shapes on land. No conflict or strategic struggle occurs.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely in Earth's primordial ocean. The creature's pod resembles spacecraft technology, but no space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. The creature exists in a pod on the ocean floor, and its origins are mysterious but not explicitly extraterrestrial in this chapter.",
        "q4": "Other / Unsure",
        "q4_justification": "No society is depicted. The creature is solitary, living in a technological pod in the ocean.",
        "q5": "Other / Unsure",
        "q5_justification": "No language or communication between beings occurs. The creature is alone.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is entirely underwater on primordial Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is depicted in space. The creature's pod suggests alien technology but space travel is not shown.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order exists. The chapter features a single creature in a pre-civilization setting.",
        "q9": "Other / Unsure",
        "q9_justification": "The chapter is atmospheric and mysterious, depicting a strange creature observing its dying ocean world. It does not fit standard genre categories cleanly.",
        "q10": "Other / Unsure",
        "q10_justification": "No civilian or military domain is depicted. The chapter features a single alien creature.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced. The setting is entirely the primordial ocean.",
    },
    {
        "chapter": "Chapter 2 - Orichalcum",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Plato experiences a vision of Atlantis's destruction: the Planetary Development Committee orders an exodus, the citizens rebel, the city erupts in fire and riots, half the city vanishes into starry void, and Poseidonis the Fifth destroys the kingdom. Gunfire, mob violence, and mass death ensue.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set on Earth (Egypt and visionary Atlantis). Atlantis has advanced technology including nuclear reactors, electric carriages, and loudspeakers, but no orbital or space territory is depicted.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Planetary Development Committee on Astarta 50 directed development of Earth from across the galaxy. Atlas the Seventh orders an exodus to Atlanta, 'land of our forebears,' across the starry sky to another planet, a distance so vast the citizens refuse to contemplate it.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Atlantis is an Earth-based civilization with advanced technology gifted by the House of Atlas. The society has kings, councils, merchants, and standard social structures despite the alien origin of its rulers.",
        "q5": "Same languages as Earth",
        "q5_justification": "Plato and Gladius speak Greek and Arabic. The Elcasians speak their own language with unfamiliar words like 'glaes' and 'taub.' All communication is in Earth languages.",
        "q6": "Other / Unsure",
        "q6_justification": "Space is revealed when half of Atlantis vanishes, replaced by a void filled with stars. But no character experiences space directly; Orionae merely sees the starry void where the city was.",
        "q7": "Other / Unsure",
        "q7_justification": "No one travels through space in the chapter. The House of Atlas 'came down from the sky' in the distant past, but no current space presence is shown.",
        "q8": "Single unified authority",
        "q8_justification": "The Planetary Development Committee on Astarta 50 directs development of Earth via the House of Atlas. Atlas the Seventh and Poseidonis the Fifth exercise absolute authority over the kingdom of Atlantis as agents of the Committee.",
        "q9": "Drama",
        "q9_justification": "The chapter combines philosophical exploration (Plato's journey) with dramatic tragedy (the fall of Atlantis). The council scene, the citizens' rebellion, and the city's fiery destruction are high drama.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Atlantis is predominantly civilian with councils, kings, merchants, and citizens. Soldiers with automatic weapons and cannons appear during the riots, but the society is fundamentally civilian.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is not portrayed as a domain to be traversed. It appears only as a mysterious void replacing half the city.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced as an environment. It is glimpsed through the void where half of Atlantis was, but no character enters or interacts with it.",
    },
    {
        "chapter": "Chapter 3 - Maitreya",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Asura has been at war with Sakra's armies for four hundred million years. Lithium bombs assault the sky-shell of Tovatsue. Siddhārtha witnesses cosmic-scale destruction: galaxies dying, civilizations devastated, and an ongoing battle between Brahmā's forces and Asura's minions.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Tuṣita/Tovatsue is an enormous permanent underground city with manufacturing districts, living quarters, transparent transport cylinders, and nuclear reactors. It is 80 billion light-years across and has 49 satellite cities surrounding the Pearl Palace.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Tuṣita is 160 billion light-years from Yāma. The monks travel through imaginary space to reach it. Distances span millions of light-years between regions. The Brahmin monks discuss coordinates like 713.081 to 429.993.",
        "q4": "Distinct space culture",
        "q4_justification": "Tuṣita has its own cosmological hierarchy: Six Heavens of the Realm of Desire, Four Heavenly Kings, Eight Generals, and defense networks. Citizens once lived to 500 years. The culture is organized around the cosmic struggle against Asura.",
        "q5": "Other / Unsure",
        "q5_justification": "Communication occurs through thought rather than spoken language. Brahmā communicates with Siddhārtha without words. The prince realizes 'where one must rely upon words to convey meaning, one can never have a true dialogue.'",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Tuṣita is under constant bombardment. Spiral galaxies are dying, losing ten billion galaxies in Yāma alone. The capital is heavily defended but decaying. Buildings show severe warping from fire damage, and the city infrastructure is failing.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Only specialists inhabit these cosmic realms: Brahmā, Sakra, the Four Heavenly Kings, Asura, and their respective forces. The monks note that some workers remain in an undamaged corridor, separated from the ruined city.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple cosmic powers govern different domains: Brahmā rules the heavens, Sakra defends Tuṣita with the Four Heavenly Kings, Asura commands invading forces. The Planetary Development Committee exists as a separate authority, with the cakravarti-rājan standing outside the system.",
        "q9": "Adventure / exploration",
        "q9_justification": "Siddhārtha journeys through cosmic realms seeking enlightenment, encountering Brahmā and then Asura. The chapter follows his quest to understand the universe's destruction and find the truth behind Maitreya.",
        "q10": "Mostly military",
        "q10_justification": "The chapter is dominated by cosmic warfare: Sakra's armies, Asura's invading minions, lithium bombs, defense networks, and four hundred million years of conflict. The Four Heavenly Kings and Eight Generals command military forces.",
        "q11": "Totally unique domain",
        "q11_justification": "Space is portrayed as a cosmic-mythological realm where Buddhist heavens are physical places, gravitational fields are weapons, and entire galaxies are battlegrounds. The domain defies conventional analogies.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The environment includes frozen plains at -272.8°C, four suns, gravity bubbles for transport, regions spanning billions of light-years, collapsing galaxies, and spaces where physical form dissolves. Siddhārtha loses his physical body when meeting Brahmā.",
    },
    {
        "chapter": "Chapter 4 - Jerusalem",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter centers on Pontius Pilate's trial and execution of Jesus. The conflict is political and religious rather than strategic: the kohanim want Jesus dead, Pilate reluctantly complies. A supernatural darkness falls during the crucifixion.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is entirely Earth-based, set in Jerusalem and Golgotha. The supernatural events (darkness, the giant figure taking Jesus into the sky) hint at extraterrestrial intervention but no space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. Jesus is taken into the sky by a giant luminous figure, but this is an abduction, not a depicted journey through space.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays Roman-era Jerusalem with its political and religious dynamics.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak in the languages of Roman-era Jerusalem. Pilate and Ceint speak Latin-inflected dialogue. The kohanim speak Hebrew. Jesus speaks Aramaic-style speech. Judas Iscariot is an astronomer who speaks multiple local languages.",
        "q6": "Other / Unsure",
        "q6_justification": "Space is not depicted as an environment. The darkness at Golgotha and the giant luminous figure hint at cosmic forces but no space conditions are portrayed.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. Jesus is taken skyward by the giant figure, but human space presence is not a theme.",
        "q8": "Other / Unsure",
        "q8_justification": "The chapter depicts Earth-based governance: Roman authority in Jerusalem. The Planetary Development Committee is echoed in Judas's overheard voices but not as governance.",
        "q9": "Drama",
        "q9_justification": "The chapter is historical drama centered on the trial and crucifixion of Jesus. Pilate's moral dilemma, Ceint's conflicted belief, and the supernatural darkness at Golgotha create intense dramatic tension.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Roman soldiers guard the execution, the kohanim represent religious authority, Pilate is a political-military administrator, and civilians observe the crucifixion. Jesus's followers are civilians.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is not portrayed as a domain. The supernatural events are not framed as space operations.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced. The darkness and the giant figure suggest cosmic phenomena but no character experiences space conditions.",
    },
]

country = 'Japan'
book_title = "ten billion days and one hundred billion nights"
csv_path = "data/results/Japan_ten_billion_days_and_one_hundred_billion_nights.csv"
questions = [{'number': i} for i in range(1, 13)]
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

print('Done batch 1.')
