import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 17",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter depicts ground combat on the war front between the Creators' state and Khonti.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor, now caught up in the planetary war.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter shows the alien planet's total war: tank battalions, nuclear strikes, and Guy's death in combat. The military culture and the willingness to use nuclear weapons on their own planet reflect a radically different social order.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in the alien language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The war front features tank battles, artillery bombardment, nuclear strikes, and mass casualties. Guy is killed. The environment is lethally hostile.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The war between the Creators' state and Khonti confirms the multipolar political landscape.",
        "q9": "Military / war",
        "q9_justification": "The chapter is a sustained combat sequence: tank battles on the front lines, artillery exchanges, a nuclear strike, and Guy's death in the fighting. Pure war narrative.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "The entire chapter takes place on the war front. Every character is a combatant. Guy is killed in action. A nuclear weapon is deployed.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Maxim, an outsider, is caught in a territorial war between alien nations, echoing colonial-era conflicts between empires.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Nuclear warfare on an already irradiated planet, alien tank technology, and mass casualties make the environment fundamentally hostile to human survival.",
    },
    {
        "chapter": "Chapter 18",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter focuses on the State Prosecutor recruiting Maxim for a coup against the other Unknown Fathers.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor, now being recruited as a political tool by the Prosecutor.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced directly in this chapter.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Prosecutor reveals the inner workings of the Unknown Fathers' regime: the mind-control Center's location, the power struggles between rulers, and his plan to use Maxim to destroy the Center and seize power.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in the alien language. Maxim is fully fluent.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The political environment is deadly: the Prosecutor plans a coup, and Maxim is being used as an expendable tool in a power struggle.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling (Strannik's true identity not yet revealed to him).",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The political landscape with multiple nations and factions remains established.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is pure political intrigue: the Prosecutor reveals the Center's location, explains the power structure of the Unknown Fathers, and recruits Maxim for a coup. Maxim agrees but plans to destroy the Center for his own reasons.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Prosecutor is a civilian official planning a military-political coup. Maxim is a civilian acting in a military capacity.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "An outsider is recruited by a local power broker to intervene in the alien political structure, echoing colonial-era manipulation of outsiders.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The chapter is set in urban political environments that are recognizable but governed by alien power dynamics and mind-control technology.",
    },
    {
        "chapter": "Chapter 19",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. Maxim infiltrates and destroys the Center. Strannik is revealed as a fellow Earthling but this does not constitute contestation between space powers.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim and Strannik (revealed as Ernst from Earth's Galactic Security Council) are both temporary visitors to this planet.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Strannik reveals he is also from Earth, having operated undercover for years. The planet Saraksh feels completely cut off from Earth — Strannik has been isolated so long he has almost gone native.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The destruction of the Center — the heart of the mind-control system — reveals the full horror of the alien social order: an entire civilization enslaved by radiation towers controlled by a small cabal of immune rulers.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Strannik reveals he speaks Earth languages too, but all prior communication on Saraksh has been in the distinct alien language. The two Earthlings finally speak a common tongue.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Maxim infiltrates a heavily fortified underground bunker, fights guards, and detonates a thermal bomb. The environment is extremely dangerous.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "The revelation that Strannik is also from Earth means there are at least two Earthlings on Saraksh, but space presence remains exceptionally limited — only two known individuals.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The multipolar political landscape of Saraksh is confirmed, now thrown into chaos by the Center's destruction.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Maxim infiltrates the underground Center, fights through guards, detonates a thermal bomb destroying the mind-control hub, and confronts Strannik who reveals the devastating consequences: millions of citizens will now suffer withdrawal from mind-control. The tension and moral horror are overwhelming.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Maxim acts as an individual agent infiltrating a military installation. Strannik operates as an intelligence agent. The action bridges civilian and military domains.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "An outsider destroys the central infrastructure of an oppressive regime, echoing colonial narratives of revolutionary intervention.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The underground Center with its mind-control technology, the thermal bomb explosion, and the revelation of the planet's full technological oppression represent a fundamentally alien environment.",
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

print('Done batch 4.')
