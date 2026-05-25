import json, csv, os

chapters_data = [
    {
        "chapter": "THE SCHOLAR'S TALE-",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Ouster invasion approaches Hyperion. The Shrike Church restricts access to the Time Tombs. Sol faces institutional resistance from the Church, the Hegemony bureaucracy, and medical establishments. The treeship Yggdrasill is destroyed in a space battle overhead.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Barnard's World is one of the oldest Web colonies. Hebron is a settled desert world with cities and kibbutzim. Renaissance Vector, Lusus, Freeholm, and dozens of other worlds have established populations. The Worldweb connects hundreds of settled worlds.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rachel's expedition to Hyperion involves four years of transit time. The medical ship takes ten days shiptime with five months time-debt. Sol's final journey on the HS Intrepid to Parvati takes ten days with significant time-debt. These voyages create profound temporal separation.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Jewish traditions persist strongly through Sol's identity, synagogue visits, and the Abraham theological framework. Barnard's World has 19th-century American small-town culture. Hebron maintains kibbutz cooperative culture. The Shrike Church represents a distinct far-future religion. Web media culture contrasts with colonial simplicity.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters communicate in standard English without translation barriers. Sol discusses Kierkegaard, the Talmud, and Old Earth literature freely. No language differences are noted between worlds.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The Time Tombs' anti-entropic fields cause the devastating Merlin sickness. Hebron is a desert world requiring terraforming. Hyperion has lethal Time Tombs, rock eels, and deadly time tides. The Hawking effect causes nausea, vertigo, and hallucinations for conscious travelers.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Barnard's World has millions of inhabitants and is one of the oldest colonies. The Worldweb connects hundreds of settled worlds with billions of people. Farcaster travel between worlds is routine. Space habitation is completely ordinary.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony governs the Worldweb. Hebron operates independently with its own immigration controls and military police. The Shrike Church wields significant political power, closing the Time Tombs to researchers. The Ousters threaten invasion. Hyperion has its own Home Rule Council.",
        "q9": "Drama",
        "q9_justification": "The Scholar's Tale is a deeply personal family drama centered on Sol watching his daughter age backward, losing memories daily. The theological wrestling with the Abraham story, Sarai's death, and Sol's philosophical dialogues with God drive the emotional narrative.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The narrative is overwhelmingly civilian: academic life, family drama, medical research, religious inquiry, kibbutz living. Military appears only peripherally as FORCE torchship transport and Hebron military police. The story centers entirely on civilian experience.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Barnard's World was the second extrasolar colony, settled by seedships. Hebron is a frontier desert world settled by Jewish colonists seeking isolation. Hyperion is an Outback world beyond the Web with restricted access, paralleling remote frontier territories.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Barnard's World has a red sun with hours-long sunsets. Different worlds have varying gravities requiring adaptation. Hebron is a harsh desert world. Hyperion has alien ecology, anti-entropic fields, and a too-small sun. Sol notes strange foods, different gravities, and light from strange suns during travels."
    },
    {
        "chapter": "THE CONSUL'S TALE- Remembering Siri",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Separatist movement opposes Hegemony integration. Mike Osho is killed in a sword fight with Separatist Bertol. Siri's son Albn dies in Separatist activities. The Consul destroys the farcaster, triggering Siri's Rebellion. FORCE invades Maui-Covenant, killing a third of menfolk and all dolphins.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Maui-Covenant has 100,000 colonists across island settlements. The Hegemony Worldweb spans hundreds of worlds with billions of inhabitants. The Los Angeles crew constructs a farcaster to incorporate Maui-Covenant into the Web. Firstsite later grows to 11 million people.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The time-debt between Merin's visits ages Siri decades while he ages months. Their First Reunion: he is 19, she is 26. By the Sixth Reunion she is 70 and he is not yet 23. The 200 light-year distance creates effectively one-way generational separation, destroying relationships across time.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Maui-Covenant has a distinct colonial seafaring culture with dolphin herding, island festivals, catamaran trading, and the All Thing government. This coexists with Hegemony technological culture aboard the Los Angeles. Separatists resist cultural assimilation. Old Earth cultural elements like Shakespeare and Bach persist.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters communicate in standard English. Siri quotes Shakespeare. Merin and colonists converse without translation barriers. The only non-human communication requires a translator disk for dolphins.",
        "q6": "Manageable but risky",
        "q6_justification": "Maui-Covenant is a pleasant tropical ocean world with .93 gravity. Sea storms pose moderate danger during fishing. The main risks are social: sword violence, the rebellion, and FORCE military reprisal. Space travel involves time-debt but is not physically dangerous.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Two hundred billion people live in the Hegemony. Maui-Covenant has 100,000 colonists. The Los Angeles spinship crew routinely travels between worlds. Farcaster construction is a standard infrastructure project. Space habitation is completely ordinary.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony governs the Worldweb. Maui-Covenant has its own colonial government with the All Thing and Council. The Separatists form an opposition faction. After the Rebellion, Maui-Covenant becomes a Protectorate with reduced autonomy. The Ousters exist as a separate civilization.",
        "q9": "Drama",
        "q9_justification": "The Consul's Tale is primarily a love story spanning decades, told through the tragedy of time-debt separating Merin and Siri. The emotional core is their relationship, aging, loss, and the personal cost of political events. Romance and personal drama drive the narrative.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The narrative blends civilian life (sailing, festivals, love, fishing, colonial politics) with military elements: the Los Angeles spinship crew, FORCE construction, the Rebellion, and eventual military invasion. Both domains are integral to the story.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The entire chapter is steeped in ocean imagery: catamarans, harbors, islands, dolphins, fishing boats, sailing, tides, reefs, and lighthouses. The Los Angeles functions like a great naval vessel. The Rebellion is fought at sea. Space is experienced through the metaphor of ocean voyaging.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Maui-Covenant is remarkably Earth-like: a tropical ocean world with .93 gravity, breathable atmosphere, and familiar marine ecology including transplanted dolphins. The environment is pleasant and requires minimal adaptation compared to other Hyperion universe worlds."
    },
    {
        "chapter": "EPILOGUE",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "A space battle rages overhead with fusion weapons and missile clusters. The treeship Yggdrasill is destroyed. Het Masteen disappears with blood covering his cabin. The pilgrims arm themselves and march toward the Shrike at the Time Tombs. Ouster scoutships flee Hegemony pursuers.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The broader context of hundreds of settled Worldweb worlds remains. Hyperion itself has established settlements including the dead city near the Time Tombs and Chronos Keep. The Hegemony and Ousters contest territory in orbital space above.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The pilgrims have traveled far from the Worldweb to reach Hyperion. The destruction of the Yggdrasill eliminates their return route. They are profoundly separated from civilization, marching toward the unknown Time Tombs.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "The six pilgrims represent diverse cultural backgrounds: a Catholic priest, a Jewish scholar, a military colonel, a private detective, a poet, and a diplomat. They reference Yeats, Oz, and military tradition. The Templar Brotherhood represents yet another distinct culture.",
        "q5": "Same languages as Earth",
        "q5_justification": "All pilgrims communicate in standard English. Weintraub sings an ancient Earth song. Silenus quotes Yeats. No translation barriers exist.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The Time Tombs glow with ominous anti-entropic energy. Space battle rages overhead. Het Masteen has been killed or abducted with blood everywhere. The Shrike awaits them in the valley. A storm sweeps down from the mountains. The pilgrims feel crushing spiritual dread.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The background of billions across the Worldweb remains. The space battle overhead involves routine military technology. The pilgrims' journey, while dangerous, exists within a civilization where interstellar travel is normal.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony fleet battles the Ousters in orbit. The Templar Brotherhood's treeship is destroyed as a casualty. The Shrike Church controls pilgrimage access. These represent distinct political entities contesting Hyperion's space.",
        "q9": "Adventure / exploration",
        "q9_justification": "The Epilogue is purely about the pilgrims' final march into the unknown valley of the Time Tombs to confront the Shrike. The tone combines adventure with existential dread as six companions walk abreast into darkness, singing together.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Colonel Kassad wears full battle armor and carries an assault rifle. Lamia carries a pistol. But the group is primarily civilian pilgrims on a spiritual journey. Military combat occurs overhead in space while civilians walk below. Both domains coexist.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The pilgrims march across vermilion sands past a dead city toward the mysterious Time Tombs, evoking frontier exploration into unknown territory. The landscape is alien and uncharted. They leave behind the known world of Chronos Keep for the wilderness.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Hyperion's environment features vermilion sands, alien constellations, anti-entropic fields causing the Tombs to glow, sharp alien shrubs with thorns like claws, and the ominous ozone smell near the Time Tombs. The landscape is fundamentally unlike Earth."
    }
]

country = 'US'
book_title = 'Hyperion_Cleaned'
csv_path = 'data/results/US_Hyperion_Cleaned.csv'
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

print('Done batch 4.')
