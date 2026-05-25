import json, csv, os

chapters_data = [
    {
        "chapter": "Prologue",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Ye Wenjie passes the two axioms of cosmic sociology to Luo Ji at Yang Dong's grave, and Evans's intercepted conversation with Trisolaris reveals the aliens cannot understand human deception. The strategic tension is latent—the Trisolaran fleet is en route but centuries away, and this chapter is expository rather than confrontational.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. Both scenes take place on Earth: a cemetery and Evans's shipboard conversation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Trisolaris is 4 light-years away. The fleet will take over 400 years to arrive. Communication via sophons is instantaneous but physical distance is extreme and generational.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Evans-Trisolaris dialogue reveals that Trisolarans cannot distinguish between thinking and speaking—their thoughts are transparent electromagnetic broadcasts. This makes deception biologically impossible, a radically alien cognitive and social order.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Evans communicates with Trisolaris through sophons that display text directly on his retinas, seamlessly translating between civilizations.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is experienced by any character in this chapter.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is depicted.",
        "q9": "Drama",
        "q9_justification": "A philosophical prologue: Ye Wenjie passes cosmic sociology axioms to Luo Ji at a grave while reflecting on humanity's fate, and Evans's dialogue with Trisolaris explores the fundamental cognitive gulf between species.",
        "q10": "Other / Unsure",
        "q10_justification": "No space domain activity is depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment is depicted."
    },
    {
        "chapter": "Part I",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Wallfacer Project is established at the UN as humanity's strategic response to Trisolaran invasion. Four Wallfacers develop secret plans (Tyler's mosquito swarm, Rey Diaz's super hydrogen bombs, Hines's brain research). Hubble II discovers the ~1000-ship Trisolaran fleet. Zhang Beihai wages political warfare against defeatism in the space force. Strategic struggle permeates the entire section.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Chinese Space Force is being established from naval foundations, and Hubble II operates as an orbital telescope. Space presence consists of military missions and observation outposts, not permanent habitation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Trisolaran fleet is approximately 450 years from Earth. The 4-light-year distance makes physical contact generational. All planning operates on century-scale timelines.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The nascent Chinese Space Force is built explicitly from naval traditions and Earth military culture. No distinct space culture has yet emerged; space activities are direct extensions of terrestrial institutions.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication uses standard Earth languages. The space force uses conventional military terminology adapted from naval traditions. No space-specific language has developed.",
        "q6": "Other / Unsure",
        "q6_justification": "No characters directly experience or describe the space environment in this section. Space remains a distant strategic concern observed from Earth.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The space force is just being established. Very few humans are in space; the focus is on Earth-based planning and political maneuvering for a conflict centuries away.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "China establishes its own Space Force, other nations develop their own programs. The UN PDC coordinates the Wallfacer Project but individual nations retain sovereignty over their space military assets.",
        "q9": "Political / diplomatic",
        "q9_justification": "The Wallfacer Project is announced at a dramatic UN session. The section focuses on diplomatic maneuvering, political appointments, Zhang Beihai's ideological work against defeatism, and the Wallfacers' political positioning rather than direct combat.",
        "q10": "Mostly military",
        "q10_justification": "Space force establishment, military strategic planning, and weapons development dominate the space-related content. Luo Ji's retreat to Garden of Eden is the exception, but the overwhelming focus is military preparation.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The Chinese Space Force is explicitly built from naval foundations, using naval organizational structures, terminology, and traditions. Chang Weisi commands the transition from navy to space force.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment is directly experienced or described in detail by characters."
    },
    {
        "chapter": "Part II",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Intense strategic struggle across three time periods: Tyler's Wallbreaker exposes his plan and he commits suicide; Zhang Beihai murders three aerospace faction leaders with meteorite bullets; a genetic weapon nearly kills Luo Ji; Rey Diaz's mutual destruction plan (crash Mercury into the sun) is exposed and he is stoned to death. Constant high-stakes conflict.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "A space elevator becomes operational and orbital infrastructure is being built, but space presence remains limited to construction missions and temporary military installations. No permanent settlement exists in space.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The Trisolaran fleet remains centuries away. Luo Ji's spell targets star 187J3X1, approximately 50 light-years distant. The distances involved are extreme and generational.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Space activities remain extensions of Earth institutions—national militaries, UN coordination, aerospace industry politics. No distinct space culture has emerged.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication uses standard Earth languages. No space-specific language or dialect has developed.",
        "q6": "Other / Unsure",
        "q6_justification": "No characters directly experience the space environment. The space elevator and orbital construction are mentioned but not experienced from the characters' perspective.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Space presence remains very limited despite the space elevator. The vast majority of action takes place on Earth. Only a small specialist population works in space.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "National aerospace programs compete over propulsion technology (chemical vs. radiation drive). The UN PDC oversees the Wallfacer Project. Nations maintain separate space military interests.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Tyler commits suicide after his Wallbreaker exposure. Zhang Beihai cold-bloodedly murders three aerospace leaders with meteorite bullets. Luo Ji nearly dies from a genetic bioweapon. Rey Diaz is stoned to death by his own people after his planet-destroying plan is revealed. The section is dominated by assassination, betrayal, and existential dread.",
        "q10": "Mostly military",
        "q10_justification": "Military planning dominates: Tyler's kamikaze fleet strategy, Rey Diaz's planet-scale weapon, Zhang Beihai's manipulation of aerospace propulsion decisions, the Faith Center mental seal program for military officers.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Space military planning continues to use naval strategic concepts. The aerospace propulsion debate (chemical vs. radiation drive) mirrors naval debates over ship design. Fleet-building remains the paradigm.",
        "q12": "Other / Unsure",
        "q12_justification": "No space physical environment is directly experienced by characters in this section."
    },
    {
        "chapter": "Part III",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Trisolaran droplet destroys the entire combined human fleet of 2015 warships in approximately 30 minutes by ramming at extreme velocities. The Battle of Darkness sees human ships attacking each other for resources. The Snow Project standoff threatens mutual destruction via broadcasting Trisolaris's position. Conflict is total and existential throughout.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "Three permanent space fleets with 2000+ warships are stationed near Jupiter, but the droplet annihilates nearly all of them. The surviving ships Blue Space and Bronze Age become tiny interstellar colonies struggling to sustain themselves, epitomizing small colonies that are hard to control.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Blue Space and Bronze Age escape into interstellar space at 15% lightspeed, becoming 'dark ships' with no prospect of return. The Trisolaran fleet is still en route. Distances are generational and effectively one-way.",
        "q4": "Distinct space culture",
        "q4_justification": "After 200 years, Earth has underground cities and radically transformed technology. The escaped ships develop their own survival ethics—the Battle of Darkness demonstrates dark forest logic applied among humans. Zhang Beihai's 'Starship Earth' and the ships' independent governance represent an emerging distinct space culture with its own moral framework.",
        "q5": "Same languages as Earth",
        "q5_justification": "Despite 200 years of change, characters communicate in recognizable Earth languages. Luo Ji and Shi Qiang converse normally after awakening from hibernation. No distinct space language has developed.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "The droplet battle kills tens of thousands in vacuum. Escaped ships face extreme resource scarcity driving the Battle of Darkness. Space combat at 30-170 km/s is instantly lethal. The environment imposes constant survival pressure.",
        "q7": "Moderately common (noticeable settlements/populations)",
        "q7_justification": "By Year 205, three independent space fleets with over 2000 warships and their crews represent a noticeable space population. However, the vast majority of humanity still lives in underground cities on Earth.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Three independent space fleets (Asian, European, North American) operate as separate political entities. After the droplet battle, the escaped ships Blue Space and Bronze Age become fully autonomous polities with independent governance.",
        "q9": "Military / war",
        "q9_justification": "The section is dominated by the catastrophic droplet battle destroying 2015 ships, the Battle of Darkness between fleeing human ships, Zhang Beihai's hijacking of Natural Selection, and the Snow Project military standoff with Trisolaris. War is the central narrative mode.",
        "q10": "Mostly military",
        "q10_justification": "The three space fleets are entirely military. The droplet engagement, Battle of Darkness, ship hijacking, and Snow Project standoff are all military operations. Civilian space activity is virtually absent.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Fleet formations, flagship command structures, naval battle tactics, and ship-to-ship combat dominate. The droplet attack resembles a torpedo destroying a naval formation. The fleets are organized and described in explicitly naval terms.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Space combat at extreme velocities (30-170 km/s), the strong-interaction material of the droplet with its perfectly smooth surface, vacuum exposure, and the deep-sea state used for high-G escape maneuvers all present an environment that constantly challenges human bodies and technology."
    },
]

country = 'China'
book_title = 'The Dark Forest'
csv_path = 'data/results/China_The_Dark_Forest.csv'
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

print('Done.')
