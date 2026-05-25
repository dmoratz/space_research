import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 6",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Kiichiro Toenji opposes the project through Joyful Homeland. Apple 7 suffers a debris strike that kills Shinji Tai. Media attacks Tae as reckless. Police investigate professional negligence. The rivalry is corporate, legal, and personal rather than military.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Apple 7 carries 6 crew on a mission to the Moon. Xiwangmu 6 is purchased from China for eventual surface use. These are temporary missions, not permanent settlements.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "Apple 7 travels from Earth orbit toward the Moon. After the debris strike, they loop around the Moon on a free return trajectory. All travel is within the Earth-Moon system.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society exists. The crew are on a temporary mission. The chapter focuses on the crisis aboard Apple 7 and its aftermath on Earth.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters speak Japanese. Ground control communicates in Japanese. The satellite spotter speaks Spanish/Portuguese. Standard Earth languages throughout.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The CO2 scrubber fails. A debris cloud from a Russian tethered satellite strikes the spacecraft, killing Shinji with a plasma jet through his suit. The crew faces constant survival pressure throughout the chapter.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only 6 crew are aboard Apple 7. Space habitation remains exceptionally rare in this near-future setting.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The Japanese private venture uses a Chinese-built habitat module. Russian space debris causes the crisis. Earth's national frameworks and their legacies (military satellites, debris) shape space activity.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is driven by survival crises: the CO2 scrubber failure, the debris collision, Shinji's death, and the crew's struggle to survive and return home. The satellite spotter's frantic warning and ground control's desperate measures create thriller tension.",
        "q10": "Entirely civilian",
        "q10_justification": "All personnel are civilian: corporate crew, a pilot, an engineer. Ground control is civilian. The police investigation and media coverage are civilian. No military presence.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Extensive Apollo 13 comparisons frame the crisis. The spacecraft operates like a ship in distress. The free return trajectory mirrors a ship limping to port. Shinji's body is laid to rest on the Moon like a burial at sea.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Zero gravity, CO2 buildup, space debris traveling at 8 km/s, plasma jets from impacts, vacuum exposure, and the impossibility of rescue all demonstrate how profoundly different space is from Earth.",
    },
    {
        "chapter": "Chapter 7",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Joyful Homeland attacks the project with arguments about space debris. Financial pressures mount as banks refuse lending. Tae collapses from overwork after being refused help by multiple space agencies. The contestation is commercial and political.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Construction crews live on the Moon for months at a time in Xiwangmu habitats. Concrete production, bulk shooting of permafrost, and construction of buildings are underway. The base is becoming a permanent settlement.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All travel is Earth-Moon. The tug ferries supplies. Apple missions transport crew. The journey is routine near-Earth travel.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Japanese corporate culture extends directly to the Moon: Gotoba engineers, ELE management, TGT rockets. Henderson notes the international nature (Russian design, Chinese build, Japanese operation) but it is fundamentally Earth institutions in space.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Japanese and English. Henderson speaks English. Jiang speaks Chinese. Standard Earth languages throughout.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Lunar construction requires enormous resources: concrete kilns, solar arrays, bulk shooters. The dozer communication failure from temperature-related frequency shift, the Turtle engine explosion, and extreme surface conditions all highlight the harsh environment.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Small construction crews rotate on the Moon for months. Both Sixth Continent and Liberty Island have permanent staff. Space habitation is uncommon but no longer exceptionally rare.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Japanese consortium, American Liberty Island, and Chinese Kunlun operate as extensions of their Earth-based institutions. Henderson mentions NASA competition. Tae negotiates with ESA, Arabsat, and Russian space agencies.",
        "q9": "Drama",
        "q9_justification": "The chapter's emotional core is Tae's collapse from overwork, Sohya's confrontation revealing her true motivations (seeking father's approval), the father-daughter reconciliation, and the worldwide outpouring of support. Character drama dominates.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: construction crews, corporate management, auditors, a chef, a Catholic priest. No military presence on the Moon or in any space operations.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter depicts frontier settlement: building permanent structures, rotating construction crews, dealing with supply logistics, engine failures, and the struggle to sustain operations far from home.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Construction in one-sixth gravity, temperature extremes causing equipment failures, communication blackouts in shadow zones, Turtle engine explosions, and the constant challenge of sustaining human life on the Moon.",
    },
    {
        "chapter": "Chapter 8",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Tension exists with Liberty Island over leased heliostats and ENG research access. Their unauthorized experiment nearly kills Sohya and Tae. But the Americans also rescue them. The conflict is institutional friction, not strategic struggle.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Sixth Continent is nearly complete: cathedral, Great Hall, three habitat wings, SELS module, spaceport, greenhouse, and kitchen. It functions as a permanent, governable settlement with staff and arriving guests.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All travel is Earth-Moon. Tae arrives from Vancouver via routine Apple flights. The journey is short and increasingly routine.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The base replicates Earth institutions: a hotel lobby, restaurant kitchen, bridal room, cathedral, maître d', chef from Antarctica, assistant Shinto priest. Society is recognizably Earth-like transplanted to the Moon.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Japanese and English. Caroline Cadbury speaks English. Standard Earth languages throughout.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Broken electrolysis electrodes threaten oxygen supply. The permafrost vault is -220°C. Liberty Island's experiment causes explosive sublimation. A solar flare traps everyone. The environment is harsh despite the base's comforts.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Sixth Continent and Liberty Island both have permanent staff. Base crew, bridal crew, a journalist, and guests are present. The population is small but established.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Japanese Sixth Continent and American Liberty Island operate as extensions of their respective Earth institutions. Tension over heliostats reflects Earth-based institutional rivalries transplanted to the Moon.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Sohya and Tae are trapped in the permafrost vault by Liberty Island's experiment. They face explosive sublimation, a solar flare preventing rescue, and must calculate lunar eclipse timing to escape. The tension is life-threatening and sustained.",
        "q10": "Entirely civilian",
        "q10_justification": "All personnel are civilian: base crew, chef, maître d', priest, construction supervisor, NASA scientists. No military presence at either base.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Two settlements (Sixth Continent and Liberty Island) coexist with institutional friction over shared resources. The frontier conditions create danger and interdependence, like neighboring colonial outposts.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Cooking boils over in low gravity, champagne fountains, wedding dress friction problems, -220°C vault temperatures, solar flare radiation, permafrost explosive sublimation, and the ENG structure emerging from the ice all demonstrate a fundamentally different environment.",
    },
    {
        "chapter": "Chapter 9",
        "q1": "No contestation",
        "q1_justification": "The chapter is a peaceful epilogue: Ryuichi and Reika's wedding, international cooperation, the Architects approaching peacefully. Sohya notes the Architects' creation has only been used to create, not destroy.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Sixth Continent is fully operational with weddings, banquets, greenhouse, permanent staff, and visiting guests from multiple nations. Kunlun and Liberty Island also operate. Star Road enables mass launches.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All current travel is Earth-Moon. Star Road's mass driver could enable interplanetary launches, and the Architects are approaching from half a light-year, but present-day space activity remains near-Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The wedding ceremony mirrors an Earth church wedding with Catholic vows. The reception features champagne, French cuisine, international guests. Society on the Moon is directly transplanted from Earth.",
        "q5": "Same languages as Earth",
        "q5_justification": "Conversations occur in Japanese, English, and Chinese. Aaron conducts the ceremony in English. Jiang speaks Japanese. Standard Earth languages throughout.",
        "q6": "Manageable but risky",
        "q6_justification": "The base is comfortable enough for weddings and celebrations, but low gravity still causes cooking challenges and champagne fountains. The environment is manageable with adaptations but not without risk.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Sixth Continent hosts staff, wedding guests, and visitors from Liberty Island and Kunlun. Multiple bases operate. The population is small but growing, with plans for expansion.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Japanese Sixth Continent, American Liberty Island, and Chinese Kunlun all operate as extensions of Earth institutions. China announces helium-3 mining. International cooperation coexists with national programs.",
        "q9": "Drama",
        "q9_justification": "The chapter is emotional drama: Ryuichi and Reika's wedding, Sohya and Tae's romantic resolution, Aaron's sermon, the reveal of the approaching Architects, and the promise of first contact. Relationships and hope drive the narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "The wedding reception, greenhouse, scientific research, and international socializing are entirely civilian. No military presence. Even the discussion of the Architects emphasizes peaceful contact.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Multiple nations establish permanent outposts. Star Road opens new frontiers. The anticipation of first contact with the Architects mirrors the frontier experience of encountering unknown civilizations.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Low gravity affects cooking, pouring champagne, and walking in wedding dresses. The base is livable but requires constant adaptation. The greenhouse, cathedral, and banquet hall create familiar spaces within an alien environment.",
    },
]

country = 'Japan'
book_title = "The Next Continent"
csv_path = "data/results/Japan_The_Next_Continent.csv"
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

print('Done batch 2.')
