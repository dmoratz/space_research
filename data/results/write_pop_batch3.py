import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 12",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter follows the State Prosecutor reading Maxim's dossier and plotting to use him as a political tool.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim is referenced in the Prosecutor's dossier as a unique individual of unknown origin — still a sole visitor.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced. The Prosecutor's dossier describes Maxim's background but not his cosmic origins.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter reveals the inner workings of the totalitarian state through the Prosecutor's perspective: political machinations, power struggles between the Unknown Fathers, and the cynical use of mind-control.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication is in the alien language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The political environment is ruthless: the Prosecutor navigates deadly power struggles, and Maxim is a prisoner being traded between factions.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Prosecutor's files reference multiple nations and the complex political landscape of Saraksh.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is narrated from the State Prosecutor's perspective as he reads Maxim's dossier, plots against rival Unknown Fathers, negotiates with Strannik for custody of Maxim, and plans a political double-cross. Pure political intrigue.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Prosecutor is a civilian official maneuvering within a military-political power structure. Strannik operates in intelligence.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The colonial parallel continues: an outsider is treated as a political asset by competing factions within the alien power structure.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The chapter is set in government offices and corridors of power, a recognizable political environment but with alien social norms and mind-control technology underlying it.",
    },
    {
        "chapter": "Chapter 13",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. Maxim is in a penal colony and discovers the Fortress.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor, now imprisoned in a penal colony on the planet.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The penal colony system, the Fortress with its mysterious dog-like creatures, and the revelation that the Creators themselves are degens who use the towers to control the population — all reveal a deeply alien social order.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in the alien language. Maxim is fluent.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The penal colony is in a radioactive wasteland. The Fortress contains dangerous dog-creatures. Prisoners face forced labor, radiation exposure, and potential death. The environment is extremely hostile.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple nations on Saraksh remain established. The penal colony system serves the Creators' state.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Maxim survives a penal colony, discovers the Fortress with its eerie dog-creatures, and learns the devastating truth: the Creators are degens themselves who built the towers to enslave the non-immune majority. The revelation is horrifying.",
        "q10": "Mostly military",
        "q10_justification": "The penal colony is run by military guards. The Fortress is a military installation. The chapter is dominated by military detention and forced labor.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "A penal colony in a radioactive wasteland, with forced labor and mysterious fortifications, echoes colonial penal settlements.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Radioactive wasteland, mysterious dog-creatures in the Fortress, mind-control revelation, and extreme environmental contamination constantly challenge survival.",
    },
    {
        "chapter": "Chapter 14",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. Maxim escapes south in a tank with Guy.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor, now fleeing southward through the planet's wasteland.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Maxim encounters mutant communities in the southern wastes — people physically transformed by radiation who have built their own distinct social structures outside the Creators' control.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in the alien language, including with the mutant communities.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The southern wasteland is heavily irradiated and contaminated. Maxim and Guy travel through dangerous terrain in an armored tank, encountering mutant communities struggling to survive.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The mutant communities in the south represent additional autonomous groups alongside the previously established nations.",
        "q9": "Adventure / exploration",
        "q9_justification": "Maxim and Guy drive a tank through uncharted southern wasteland, encountering mutant villages and navigating dangerous irradiated terrain. The chapter is driven by exploration and discovery of unknown regions.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Maxim uses a military tank but encounters civilian mutant communities. Guy accompanies him as a reluctant military companion.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Traveling into uncharted irradiated territory and encountering indigenous mutant communities parallels frontier exploration narratives.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The irradiated southern wasteland, mutant populations physically transformed by radiation, and the need for an armored tank for travel make the environment fundamentally hostile.",
    },
    {
        "chapter": "Chapter 15",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter is set in a mutant community in the south.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim visits the mutant community as a temporary guest.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The mutant community has its own governance, led by the Wizard and the Duke, with distinct social norms and a philosophical worldview shaped by their radiation-induced mutations and isolation from the Creators' state.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in the alien language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The mutant community survives in irradiated southern territory, dealing with physical mutations, limited resources, and hostility from the Creators' state.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The mutant community is yet another autonomous polity on Saraksh, alongside the Creators' state, Khonti, the Island Empire, and others.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on a community meeting where the Wizard challenges Maxim's plan to destroy the towers, arguing that removing mind-control would cause chaos. The Duke offers Maxim a bomber. The chapter is a philosophical and political debate about intervention.",
        "q10": "Entirely civilian",
        "q10_justification": "The mutant community is entirely civilian. The Wizard, Duke, and other community members are non-military.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "An outsider negotiates with an indigenous community for resources and support, echoing colonial frontier diplomacy.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The mutant community's physical transformations, the irradiated environment, and the isolation from mainstream civilization make this a fundamentally different environment.",
    },
    {
        "chapter": "Chapter 16",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. Maxim flies a bomber, is shot down, and explores a submarine.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Maxim remains a sole visitor, now traveling by air and sea.",
        "q3": "Other / Unsure",
        "q3_justification": "The space journey is not referenced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Maxim discovers the Island Empire's submarine operations, revealing yet another alien society with its own brutal military culture and territorial ambitions.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All communication in alien languages. The Island Empire may use a different dialect or language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Maxim is shot down by missiles, crashes into the sea, explores a hostile submarine, and encounters the Island Empire's brutal military. Constant survival pressure throughout.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Maxim remains the sole known Earthling.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Island Empire is confirmed as an aggressive naval power, adding to the established multipolar landscape of Saraksh.",
        "q9": "Adventure / exploration",
        "q9_justification": "Maxim flies a bomber over unknown territory, is shot down by rockets, crashes into the sea, swims to a submarine, and explores its interior. The chapter is driven by high-stakes exploration and survival.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Maxim operates a military bomber but encounters the Island Empire's military submarine as an individual explorer, not as part of any organized force.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Solo exploration of uncharted sea territory and encounter with a hostile foreign military power echoes frontier naval exploration.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Air combat with alien missiles, sea survival after a crash, and hostile submarine exploration make the environment fundamentally challenging.",
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

print('Done batch 3.')
