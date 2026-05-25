import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 7 - The Question of Sex",
        "q1": "No contestation",
        "q1_justification": "This chapter is an investigator's field notes on Gethenian sexuality; no conflict or contestation over space is discussed.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The investigator is a temporary Ekumenical observer on Gethen, with no permanent settlement.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The field notes come from an earlier Ekumenical investigation team, underscoring the vast distances involved in reaching Gethen.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The entire chapter analyzes Gethenian ambisexuality and its profound effects on their society, which is fundamentally unlike any Earth culture.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The notes reference Gethenian terminology (kemmer, somer, kemmering) that has no Earth equivalent.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The notes mention the harsh climate and its effects on Gethenian society, including the observation that Gethenians have never had war.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The investigator is one of very few off-worlders to have visited Gethen; space travel there is exceedingly rare.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Ekumen sending investigators implies a multi-world political structure observing Gethen's distinct nations.",
        "q9": "Other / Unsure",
        "q9_justification": "This chapter reads as academic field notes rather than fitting a standard narrative genre.",
        "q10": "Entirely civilian",
        "q10_justification": "The investigation is purely scientific and civilian; no military presence is mentioned.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Ekumen's scientific investigation of a newly contacted world parallels frontier-era ethnographic study.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The notes describe how Gethen's environment and biology differ drastically from Earth norms.",
    },
    {
        "chapter": "Chapter 8 - Another Way into Orgoreyn",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Genly navigates Karhidish politics and eventually flees to Orgoreyn; tensions simmer but no open conflict erupts.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly continues his role as a temporary envoy, traveling through Karhide with no permanent off-world infrastructure.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Genly's isolation on Gethen, far from any Ekumenical support, reinforces the extreme distance from his home worlds.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Genly observes Karhidish customs, Foretelling traditions, and social structures that are entirely unlike Earth society.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Genly operates in Karhidish and encounters Orgota; both are completely alien languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Travel through Karhide in worsening weather highlights the demanding environment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly remains the sole off-worlder, viewed with suspicion and curiosity.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter depicts Karhide, Orgoreyn, and the distant Ekumen as separate political entities.",
        "q9": "Political / diplomatic",
        "q9_justification": "Genly's journey is driven by the failure of his diplomatic mission in Karhide and his hope for Orgoreyn.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian travel and political maneuvering.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Genly's solitary journey through an alien land echoes frontier exploration.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Gethen's cold and alien customs continue to challenge Genly's Earth-adapted body and mind.",
    },
    {
        "chapter": "Chapter 9 - Estraven the Traitor",
        "q1": "Other / Unsure",
        "q1_justification": "This is an origin myth about the Estraven name and a blood feud; it does not address space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "The myth takes place entirely on Gethen with no reference to space territory.",
        "q3": "Other / Unsure",
        "q3_justification": "No interstellar travel or space journey is referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The myth depicts Gethenian customs of kemmering, hearth-bonds, and blood feuds that are entirely alien.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The myth is told in Karhidish with its own terminology for social bonds and customs.",
        "q6": "Other / Unsure",
        "q6_justification": "While set on Gethen, this myth focuses on interpersonal drama rather than environmental conditions.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation or off-world presence is mentioned.",
        "q8": "Other / Unsure",
        "q8_justification": "The myth concerns local domains and feuds, not interstellar political structures.",
        "q9": "Drama",
        "q9_justification": "The myth is a tragic tale of betrayal, blood feud, and the origin of the Estraven name.",
        "q10": "Entirely civilian",
        "q10_justification": "The feuding parties are civilian hearths and domains, not military forces.",
        "q11": "Other / Unsure",
        "q11_justification": "The myth provides no analogy for space as a domain.",
        "q12": "Other / Unsure",
        "q12_justification": "The myth does not focus on environmental conditions.",
    },
    {
        "chapter": "Chapter 10 - Conversations in Mishnory",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Political factions in Orgoreyn compete for influence over the Envoy; the Karhide-Orgoreyn rivalry continues.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly reveals a starship in orbit but his presence remains that of a temporary diplomatic visitor.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Genly describes the starship in orbit and the vast distances to other Ekumenical worlds.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Orgoreyn's commensality system, the Sarf secret police, and factional politics represent an alien political order.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Conversations occur in Orgota; Genly navigates a completely alien language and its political nuances.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The winter climate of Mishnory is cold and demanding, though urban infrastructure makes it manageable.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is the sole alien; his revelation of the orbiting starship astonishes the Commensals.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Ekumen, Karhide, and Orgoreyn are presented as distinct competing political entities.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is entirely about diplomatic conversations, political factions, and maneuvering over the Ekumen's offer.",
        "q10": "Entirely civilian",
        "q10_justification": "All interactions are diplomatic and political; no military operations are involved.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Ekumen's offer of alliance to a newly contacted world parallels diplomatic expansion into frontier territories.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Genly continues to struggle with the cold and alien social expectations of Gethen.",
    },
    {
        "chapter": "Chapter 11 - Soliloquies in Mishnory",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Estraven's journal reveals the Sarf's surveillance, factional maneuvering, and the ongoing Karhide-Orgoreyn rivalry.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Both Genly and Estraven are temporary presences in Orgoreyn; no permanent off-world infrastructure exists.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Estraven reflects on the vast implications of the Ekumen's offer, implying the enormous distances involved.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Sarf's control, Gaum's seduction attempt during kemmer, and Orgota political culture are deeply alien.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Estraven writes in Karhidish while navigating Orgota society; both are distinct alien languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Winter conditions in Mishnory are harsh, and political danger adds to the hostile environment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly remains the only alien; Estraven is one of few who truly believes his mission.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Karhide, Orgoreyn, and the Ekumen operate as separate political entities with distinct interests.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is Estraven's political journal, documenting factional intrigue and the danger from the Sarf.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Sarf functions as a secret police with quasi-military surveillance capabilities, though society is primarily civilian.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The political maneuvering over whether to welcome or reject the Ekumen echoes frontier-era diplomatic expansion.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The harsh winter and the alien political dangers of Orgoreyn continue to challenge the characters.",
    },
    {
        "chapter": "Chapter 12 - On Time and Darkness",
        "q1": "Other / Unsure",
        "q1_justification": "This is a Yomesh religious text about Meshe's Seeing; it does not address space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "The religious text discusses theology, not space territory or habitation.",
        "q3": "Other / Unsure",
        "q3_justification": "No interstellar journey is referenced in this theological text.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Yomesh religion and its concept of Meshe's all-seeing represent a uniquely Gethenian spiritual tradition.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The text uses Yomesh theological terminology distinct from any Earth religion.",
        "q6": "Other / Unsure",
        "q6_justification": "The text discusses time and darkness philosophically rather than depicting environmental conditions.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed in this religious text.",
        "q8": "Other / Unsure",
        "q8_justification": "The text concerns spiritual rather than political structures.",
        "q9": "Other / Unsure",
        "q9_justification": "This is a religious/philosophical text, not a narrative fitting standard genre categories.",
        "q10": "Entirely civilian",
        "q10_justification": "The text is religious in nature with no military content.",
        "q11": "Other / Unsure",
        "q11_justification": "The text provides no analogy for space as a domain.",
        "q12": "Other / Unsure",
        "q12_justification": "The text discusses metaphysical concepts of time and darkness rather than physical environment.",
    },
    {
        "chapter": "Chapter 13 - Down on the Farm",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Genly is arrested and sent to a prison farm; the conflict is political repression rather than open warfare.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Genly's imprisonment reinforces his status as a vulnerable temporary visitor with no off-world support.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Genly tries to tell a fellow prisoner about other worlds but the concept is nearly incomprehensible, underscoring the vast distance.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Voluntary Farm system with chemical castration, drugging, and communal passivity reveals deeply alien social control.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Genly is forced to speak only Orgota; he catalogues Karhidish words for snow, highlighting distinct alien languages.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The prison farm in extreme winter cold, with inadequate food and clothing, creates constant survival pressure.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Genly is called 'the Pervert' for his alien biology; he is utterly alone as the only off-worlder.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Orgota commensality and its prison system operate as a distinct polity separate from Karhide and the Ekumen.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter depicts imprisonment, forced drugging, a brutal transport in a sealed truck, death, and desperate survival.",
        "q10": "Entirely civilian",
        "q10_justification": "The prison farm is a civilian institution run by guards, not a military operation.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Genly's vulnerability as a lone alien in a hostile land echoes frontier captivity narratives.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The drugs are toxic to Genly's non-Gethenian physiology, and the extreme cold threatens his survival constantly.",
    },
]

country = 'US'
book_title = "The Left Hand of Darkness"
csv_path = "data/results/US_The_Left_Hand_of_Darkness.csv"
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
