import json, csv, os

chapters_data = [
    {
        "chapter": "THE POET'S TALE- 'Hyperion Cantos'",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Shrike kills dozens in the City of Poets. General Glennon-Height's rebellion threatens Asquith. The Ouster invasion looms over Hyperion. Evacuations empty cities.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Worldweb connects hundreds of worlds via farcasters. Silenus's home spans 38 rooms on 36 worlds. Heaven's Gate, Hyperion, Renaissance Vector, Tau Ceti Center are all settled. Colonies expand continuously.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Silenus travels by Phase Three ramship taking 129 shipboard years and 167 standard years of time-debt to reach Heaven's Gate. His mother and Old Earth die while he sleeps. The separation is total and generational.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Old Earth aristocratic culture persists alongside Hegemony datasphere culture, the Caribou Herd farcaster set lifestyle, colonial frontier culture on Hyperion, and the Shrike Cult. Earth literary traditions coexist with far-future technologies.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters communicate in standard English. Silenus quotes Keats, Byron, Milton freely. No translation barriers exist between characters from different worlds or eras.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Heaven's Gate has toxic atmosphere killing inhabitants by age 40, acid rain, and lethal conditions. Hyperion features the Shrike, tesla trees, grass serpents, and harsh desert. The Sea of Grass requires windwagons to cross safely.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Billions live across the Worldweb. Farcaster homes span dozens of worlds. Interstellar publishing, travel, and commerce are routine. Space habitation is completely ordinary for the population.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony governs the Worldweb. The Kingdom of Windsor-in-Exile operates independently under Sad King Billy. Hyperion's Home Rule Council governs locally. The Ousters, Shrike Temple, and Templar Brotherhood are autonomous entities.",
        "q9": "Drama",
        "q9_justification": "The Poet's Tale is primarily a biographical drama about artistic creation, the loss and recovery of a muse, commercial publishing pressures, and the relationship between art and violence. The horror of the Shrike is secondary to the literary journey.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The SDF patrols the Time Tombs region. FORCE:space offers protection. But the narrative centers on civilian life: artists, poets, colonists, publishers. Military presence is peripheral to the artistic colony's story.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Sad King Billy's seedships colonize Hyperion like conquistadors. The City of Poets rises on frontier terrain. Indigenies are displaced. The narrative mirrors colonial expansion with artists as settlers building a new civilization.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Heaven's Gate requires atmospheric protection to survive. Hyperion has alien flora, a too-small sun, green-blue sky, deadly grass serpents, and varying gravity. Worlds across the Web differ significantly in gravity and environment."
    },
    {
        "chapter": "THE SOLDIER'S TALE- The War Lovers",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Battle of South Bressia lasts 97 days with nuclear weapons, plasma bombs, and massive casualties. The Ousters scour North Bressia killing 14 million. Qom-Riyadh sees revolution and orbital strikes. The hospital ship is destroyed.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Bressia has 400 million inhabitants across two continents. Mars has established cities and slums. Qom-Riyadh has 30 million settlers. The Hegemony Worldweb spans hundreds of worlds. Ousters control vast regions of interstellar space.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Bressia is 7+ standard months from the Web by Hawking drive. The hospital ship Merrick takes weeks between worlds. Kassad accrues 18 months time-debt. Mars is connected by farcaster but culturally distant from the core worlds.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Palestinian refugee culture persists on Mars. The New Bushido blends samurai honor codes with future military ethics. Qom-Riyadh maintains Islamic traditions. Ouster culture has diverged dramatically. Central European settlers colonized Bressia.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Standard English is spoken throughout, but military slang pervades (grunts, spezzes, jump rats). Ouster language sounds like reversed Ancient English. Qom-Riyadh maintains Arabic religious terminology alongside Standard.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Kassad endures 97 days of brutal urban warfare on Bressia. The hospital ship is destroyed in orbit. He survives atmospheric reentry in a jury-rigged ejection seat. The Shrike's time-manipulation creates lethal combat conditions throughout.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Bressia alone has 400 million people. Mars has established cities. Hundreds of worlds are settled across the Worldweb. Space habitation is completely ordinary for billions of humans.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Hegemony governs the Worldweb. The Ousters are an independent spacefaring civilization. Bressia, Qom-Riyadh, and other worlds maintain varying degrees of independence. Hyperion has its own SDF.",
        "q9": "Military / war",
        "q9_justification": "The entire chapter follows Kassad through military campaigns: OCS training simulations of historical battles, the Island War on Maui-Covenant, revolution on Qom-Riyadh, the 97-day Battle of South Bressia, and combat with Ousters on Hyperion.",
        "q10": "Mostly military",
        "q10_justification": "The narrative is almost entirely military: command school training, multiple combat campaigns, orbital warfare, ground invasions. Civilian life appears only as backdrop or collateral damage in military operations.",
        "q11": "Like the ocean / naval",
        "q11_justification": "FORCE:space uses naval terminology: torchships, fleet formations, assault boats, orbital pickets. The Battle of Bressia involves fleet actions, JumpShips, and systematic naval-style campaigns. Ship-to-ship combat mirrors naval engagements.",
        "q12": "Moderately different (regular adaptation needed)"  ,
        "q12_justification": "Mars has lower gravity requiring physical adaptation. Bressia has different geography and climate. Hyperion has alien environment with anti-entropic time tides. Ousters have physically adapted to zero-gravity over centuries."
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

print('Done batch 2.')
