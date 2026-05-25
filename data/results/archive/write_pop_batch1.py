import json, csv, os

chapters_data = [
    {
        "chapter": "front_matter",
        "q1": "Other / Unsure",
        "q1_justification": "The front matter contains the title page, table of contents, and copyright information. No narrative content or space portrayal.",
        "q2": "Other / Unsure",
        "q2_justification": "No narrative content. The front matter is purely bibliographic.",
        "q3": "Other / Unsure",
        "q3_justification": "No narrative content depicting any journey.",
        "q4": "Other / Unsure",
        "q4_justification": "No narrative content depicting any society.",
        "q5": "Other / Unsure",
        "q5_justification": "No narrative content depicting language dynamics.",
        "q6": "Other / Unsure",
        "q6_justification": "No narrative content depicting any environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No narrative content depicting space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No narrative content depicting political order.",
        "q9": "Other / Unsure",
        "q9_justification": "The front matter is bibliographic material, not a narrative chapter with a genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative content depicting any domain.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative content depicting any domain characterization.",
        "q12": "Other / Unsure",
        "q12_justification": "No narrative content depicting any environment.",
    },
    {
        "chapter": "INTRODUCTION",
        "q1": "Other / Unsure",
        "q1_justification": "Theodore Sturgeon's introduction is a critical essay about the novel's literary merits. No narrative depicting space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "The introduction is literary criticism, not narrative content depicting space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No narrative journey is depicted in this critical essay.",
        "q4": "Other / Unsure",
        "q4_justification": "No narrative society is depicted. Sturgeon discusses the novel's themes abstractly.",
        "q5": "Other / Unsure",
        "q5_justification": "No narrative language dynamics are depicted in this essay.",
        "q6": "Other / Unsure",
        "q6_justification": "No narrative environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No narrative space habitation is discussed.",
        "q8": "Other / Unsure",
        "q8_justification": "No narrative political order is shown.",
        "q9": "Other / Unsure",
        "q9_justification": "This is a critical essay, not a narrative chapter with a genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative domain is depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative domain characterization is present.",
        "q12": "Other / Unsure",
        "q12_justification": "No narrative environment is depicted.",
    },
    {
        "chapter": "Chapter 1",
        "q1": "No contestation",
        "q1_justification": "Maxim arrives alone on an alien planet after a crash-landing. There is no competition between space powers for this world; he is a solitary visitor.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim is the sole representative of Earth civilization, stranded after his ship is destroyed by a mysterious attack. His presence is involuntary and temporary.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Maxim's spaceship is destroyed shortly after landing, leaving him completely cut off from Earth with no means of return. The alien planet feels irreversibly separated from his home world.",
        "q4": "Other / Unsure",
        "q4_justification": "Maxim encounters only a radioactive wilderness and two fugitives at a campfire. The broader alien society is not yet revealed in this chapter.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Maxim cannot communicate with the natives at all. He and Zef share no common language, relying on gestures and drawings. The alien language is completely distinct from any Earth tongue.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The planet features a radioactive river, polluted environment, gnarled trees, and driverless military robot-tanks roaming abandoned roads. Survival requires constant vigilance.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim is the only Earthling on the planet. He crash-landed alone and his ship was destroyed, making him the sole space traveler in this world.",
        "q8": "Other / Unsure",
        "q8_justification": "The chapter shows only wilderness and two fugitives. The planet's political structures are not yet revealed.",
        "q9": "Adventure / exploration",
        "q9_justification": "Maxim explores an alien world after crash-landing: wading through a radioactive river, encountering an abandoned road with robot-tanks, and making first contact with native inhabitants around a campfire.",
        "q10": "Entirely civilian",
        "q10_justification": "Maxim is a civilian explorer from Earth. The natives he meets, Zef and his companion, are fugitives. No military operations occur.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim is a lone explorer crash-landed on an unknown alien world, navigating dangerous terrain and making first contact with indigenous people, echoing frontier exploration narratives.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The planet has radioactive waterways, a dense phosphorescent atmosphere that obscures the sky, autonomous military robots roaming decades after a war, and pervasive contamination. The environment constantly challenges human survival.",
    },
    {
        "chapter": "Chapter 2",
        "q1": "No contestation",
        "q1_justification": "No competition between space powers occurs. Maxim is brought to a Legion outpost as a curiosity, not as part of any space rivalry.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains the sole space visitor, now at a military outpost. He draws pictures of his solar system and ship to communicate but is treated as a local anomaly.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Maxim's drawings of his solar system and spaceship are incomprehensible to the natives. The dense atmosphere prevents seeing stars, so no one even believes in outer space.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter reveals the 'ecstasy' episode: mass mind-control causing frenzied singing and loyalty displays. Guy beats Zef during the episode. This totalitarian mind-control society is radically unlike Earth.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Maxim is called 'Mac Sim' because the natives parse his name differently. He can barely communicate, drawing pictures instead of speaking. The alien language is entirely distinct.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The environment is polluted and radioactive. The Legion outpost is a militarized border zone in a post-nuclear landscape.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim is the sole Earthling, examined as a medical curiosity by Dr. Zogu and Captain Tolot at the outpost.",
        "q8": "Single unified authority",
        "q8_justification": "The chapter shows only the Legion operating under the All-Powerful Creators. Other nations are not yet mentioned.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The mind-control ecstasy episode dominates: soldiers suddenly begin singing hymns in frenzied devotion, Guy violently beats Zef, and Maxim witnesses mass psychosis. The horror of involuntary mind-control pervades.",
        "q10": "Mostly military",
        "q10_justification": "The chapter is set at a Legion military outpost. Captain Tolot commands, legionnaires undergo ecstasy formations, and Maxim is processed as a military matter.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim navigates an alien military society as a complete outsider, unable to communicate, being processed and directed by authorities who don't understand his origins.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mind-control radiation episodes, the dense atmosphere hiding the sky, and the post-nuclear militarized landscape make this world fundamentally challenging for human experience.",
    },
    {
        "chapter": "Chapter 3",
        "q1": "No contestation",
        "q1_justification": "No space contestation occurs. Maxim is confined in a research facility being studied as a curiosity.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim is the sole space visitor, now confined and studied. His mentograms of Earth are broadcast as entertainment, but no one understands their significance.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Maxim's mental images of Earth are shown on television as 'Magic Journey' entertainment. The natives cannot comprehend that these depict a real, distant world.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Maxim is confined and exploited for entertainment via mentoscope technology. His mental images of Earth are broadcast as fiction. The society treats him as a specimen.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Fishface/Nolu teaches Maxim basic language skills. The alien language must be learned from scratch; it shares nothing with Earth languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The city is polluted and suffocating. Maxim is confined in a facility with mentoscope equipment probing his mind.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the only Earthling, studied by Professor Megu as a unique specimen.",
        "q8": "Single unified authority",
        "q8_justification": "Only the Creators' state apparatus is shown: the research facility, the TV broadcast system, all under centralized control.",
        "q9": "Drama",
        "q9_justification": "Maxim realizes his treatment is not genuine communication but entertainment exploitation. His frustration at being a captive spectacle and his inability to convey his true nature drive the chapter's emotional core.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter takes place in a civilian research facility. Professor Megu and Fishface are civilian researchers.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim is treated as an exotic specimen by a civilization that cannot comprehend his origins, paralleling colonial encounters where indigenous people were put on display.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The city environment is recognizably urban but polluted and suffocating, with alien technology like mentoscopes. Regular adaptation to the air quality and social norms is needed.",
    },
    {
        "chapter": "Chapter 4",
        "q1": "No contestation",
        "q1_justification": "No space contestation occurs. Maxim escapes his confinement and explores the alien city independently.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor exploring the alien urban environment on foot.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced in this chapter. Maxim is focused entirely on navigating the alien city.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Maxim encounters hostile strangers, demanding payment systems he doesn't understand, and an oppressive urban atmosphere. The social order is alien to him.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Maxim now speaks basic phrases but struggles to communicate fully. The language barrier remains significant.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The city is polluted and dangerous. A man threatens Maxim with a knife-cane; an old woman demands payment. The urban environment is hostile to an outsider.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim is the sole Earthling, navigating the alien city alone.",
        "q8": "Single unified authority",
        "q8_justification": "The city operates under the Creators' authority. Other political entities are not discussed.",
        "q9": "Adventure / exploration",
        "q9_justification": "Maxim escapes confinement and explores the alien city on his own, encountering cafes, hostile strangers, and meeting Rada. The chapter is driven by exploration and discovery.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is set entirely in the civilian city. No military presence is shown.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim explores an alien urban environment as a complete outsider, unable to fully understand customs, currency, or social norms.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The city is recognizably urban but with alien customs, aggressive strangers, and unfamiliar social dynamics. Maxim must constantly adapt.",
    },
    {
        "chapter": "Chapter 5",
        "q1": "No contestation",
        "q1_justification": "No space contestation occurs. The chapter focuses on Guy's decision to recommend Maxim for Legion service.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim's status as a lone outsider continues. Guy considers recommending him for the Legion.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not discussed. The chapter is focused on Legion recruitment procedures.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Legion recruitment system, with its mind-control testing and blood loyalty rituals, represents a radically different social order.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Maxim speaks the alien language imperfectly. Guy must advocate for him to the Legion captain despite communication gaps.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The militarized society with its mind-control infrastructure makes daily life harsh and controlled.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole Earthling, being processed into the alien military system.",
        "q8": "Single unified authority",
        "q8_justification": "The Legion operates under the All-Powerful Creators. No other political entities are discussed in this chapter.",
        "q9": "Drama",
        "q9_justification": "Guy is torn between recommending Maxim and flagging concerns about his unknown background. The chapter centers on Guy's moral dilemma and his loyalty to both Maxim and the Legion.",
        "q10": "Mostly military",
        "q10_justification": "The chapter revolves around Legion recruitment procedures. Captain Chachu and Guy discuss Maxim's candidacy in military terms.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim, a stranger from an unknown land, is being assimilated into the alien military structure, paralleling how frontier outsiders were absorbed into colonial institutions.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The military recruitment system with its mind-control testing is different from Earth norms, requiring constant adaptation by Maxim.",
    },
]

country = 'Russia'
book_title = 'Prisoners of Power'
csv_path = 'data/results/Russia_Prisoners_of_Power.csv'
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
