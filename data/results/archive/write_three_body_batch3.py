import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 25",
        "q1": "Other / Unsure",
        "q1_justification": "Ye Wenjie's interrogation reveals she murdered Commissar Lei and her husband Yang Weining to protect the secret of her contact with Trisolaris. Earth-based chapter with no space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Drama",
        "q9_justification": "A chilling interrogation in which Ye Wenjie calmly confesses to murdering both Commissar Lei and her own husband Yang Weining by cutting the rope while they repaired equipment on a cliff face, to protect the secret of her first contact with Trisolaris.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 26",
        "q1": "Other / Unsure",
        "q1_justification": "Ye Wenjie raises Yang Dong in a village, returns to Tsinghua, confronts her mother, and meets the three former Red Guards who killed her father. None repent. Earth-based with no space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Drama",
        "q9_justification": "A deeply emotional chapter tracing Ye's recovery in a village, her return to academia, her cold reunion with her mother, and her devastating meeting with her father's killers. None repent, solidifying her conviction that humanity cannot reform itself.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 27",
        "q1": "Other / Unsure",
        "q1_justification": "Ye Wenjie meets Mike Evans, an American billionaire's son planting trees in China to save an endangered swallow species. He espouses Pan-Species Communism. Earth-based environmentalism with no space contestation.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Drama",
        "q9_justification": "Ye Wenjie encounters Mike Evans, a man devoted to saving an endangered bird species. Years later, after inheriting billions, he despairs at humanity's destruction of nature. Ye tells him about Trisolaris, and he pledges to become her comrade.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 28",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Evans builds the Second Red Coast Base on a 60,000-ton ship, confirms contact with Trisolaris, and announces the Trisolaran Fleet has set sail. Ye becomes ETO commander. The contestation is nascent: the fleet has launched but is 450 years away.",
        "q2": "Other / Unsure",
        "q2_justification": "The Second Red Coast Base is on a ship on Earth's ocean, not in space. No space habitation depicted.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Trisolaran Fleet will take 450 years to reach Earth, an extreme generational-scale distance that defines the entire conflict.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted in this chapter.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment experienced by characters.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Political / diplomatic",
        "q9_justification": "The formal founding of the Earth-Trisolaris Organization. Evans presents the confirmed Trisolaran contact and fleet launch to 2000 followers. Ye Wenjie becomes commander in chief. The scene is ceremonial and political.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 29",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "An expository chapter describing the ETO's three factions: Adventists (want humanity destroyed), Redemptionists (worship Trisolaris), and Survivors (want descendants to survive). The contestation is ideological and organizational rather than physical.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Trisolaran Fleet is 450 years from Earth. The alien civilization is 4+ light-years away, connected only by radio. The enormous distance shapes the entire chapter's dynamics.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted directly.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Political / diplomatic",
        "q9_justification": "An expository chapter analyzing the ETO's internal politics: the three factions (Adventists, Redemptionists, Survivors), their ideological conflicts, and the organization's growth among intellectual elites.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 30",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Ye Wenjie reveals that Trisolaris sent two protons to Earth at near-lightspeed, designed to lock down human scientific progress. Evans declared the day of the protons' arrival as the day human science died. This is a strategic attack on humanity's ability to advance.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. The protons are weapons, not habitations.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Trisolaris is 4 light-years away. The protons took 6 years to arrive at near-lightspeed. The fleet will take 450 years. Distance is extreme.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society directly depicted.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "A devastating revelation: Trisolaris has sent two protons to lock down human science forever. Ding Yi's filter analogy explains how micro-dimensions contain vast complexity. The implications for humanity's survival are terrifying.",
        "q10": "Other / Unsure",
        "q10_justification": "The protons are weapons but not part of a traditional military or civilian domain.",
        "q11": "Other / Unsure",
        "q11_justification": "The proton attack doesn't map to conventional domain analogies.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 31",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Operation Guzheng: the military uses Wang Miao's nanofilaments (Flying Blade) to slice through Judgment Day in the Panama Canal, killing all aboard to capture the Trisolaran messages. This is active military conflict against the ETO.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. Operation occurs on Earth in the Panama Canal.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society depicted.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language depicted.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order depicted.",
        "q9": "Military / war",
        "q9_justification": "A military operation of horrifying precision: nanofilaments slice through the ship Judgment Day in the Panama Canal, killing all aboard. The operation successfully captures the Trisolaran messages. Intensely violent and tactical.",
        "q10": "Other / Unsure",
        "q10_justification": "Military operation is terrestrial, not in the space domain.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment depicted."
    },
    {
        "chapter": "Chapter 32",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Told from the Trisolaran perspective. A listener at Post 1379 receives Earth's message and sends a warning ('Do not answer!'), defying orders. The princeps plans invasion. Strategic struggle between civilizations is central.",
        "q2": "Other / Unsure",
        "q2_justification": "Trisolaran listening posts are on the surface of Trisolaris, not in space. No space habitation depicted.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Alpha Centauri is 4 light-years from Earth. Messages take 4 years each way. The fleet must travel for hundreds of thousands of Trisolaran hours. Extreme distance.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Trisolaran society is depicted in detail: individuals dehydrate to survive Chaotic Eras, the elderly are forcibly burned, emotions are suppressed, and reproduction involves bodily merging. Radically alien.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The Trisolaran computer automatically translates Earth's self-interpreting coded message. Communication between civilizations is mediated by coding technology.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Trisolaris endures Chaotic Eras where temperatures are lethal. The listener's post must maintain constant temperature. Those who can't work are dehydrated and burned. Extreme survival pressure.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation depicted. The fleet is mentioned but not shown in space.",
        "q8": "Single unified authority",
        "q8_justification": "Trisolaris is governed by a princeps and consuls in a single authoritarian authority. The princeps unilaterally orders fleet deployment and execution of 6000 responsible for the listener's breach.",
        "q9": "Drama",
        "q9_justification": "A deeply moving parallel to Ye Wenjie's story: a lonely Trisolaran listener, out of compassion for Earth, sends the warning 'Do not answer!' His motivations mirror Ye's despair but in reverse. The princeps condemns 6000 and orders the fleet to launch.",
        "q10": "Mostly military",
        "q10_justification": "The Trisolaran response is primarily military: fleet deployment toward Earth, execution of those responsible for the breach, and strategic planning for invasion.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Trisolaris views Earth as a habitable frontier to colonize, driven by the existential need to escape their dying system. Parallels colonial expansion.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Trisolaris has three suns, chaotic eras of extreme temperature, dehydration biology, and a fundamentally alien physical environment."
    },
]

country = 'China'
book_title = 'Human Split_Three Body Problem'
csv_path = 'data/results/China_Human_Split_Three_Body_Problem.csv'
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

print('Done with batch 3.')
