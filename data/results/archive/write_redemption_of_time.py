import json, csv, os

chapters_data = [
    {
        "chapter": "Prologue",
        "q1": "Other / Unsure",
        "q1_justification": "A solitary ghost-like figure at the end of the universe creates an artificial world from a mini-universe wormhole. There is no contestation—only a lone creator acting in the void as stars die and galaxies dim around it.",
        "q2": "Other / Unsure",
        "q2_justification": "No space habitation depicted. The ghost floats in the void and creates a temporary artificial world, but there is no settlement, station, or habitation framework.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The setting is the terminal era of the universe—billions of light-years from any living civilization. The Milky Way is described as a faint, ancient light from a long-dead galaxy. Distance is absolute and cosmic.",
        "q4": "Other / Unsure",
        "q4_justification": "No society depicted. The ghost is entirely alone; the human species and all civilizations have long since disappeared.",
        "q5": "Other / Unsure",
        "q5_justification": "No communication or language interaction occurs. The ghost speaks only to itself.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The universe is dying—stars are extinguishing at an unimaginable rate, galaxies dimming, civilizations winking out. The ghost must create an entire artificial world (atmosphere, sun, biosphere) from pure energy just to have a habitable environment.",
        "q7": "Other / Unsure",
        "q7_justification": "A single entity exists in the entire observable region. Space habitation is not a relevant concept at the end of the universe.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order exists. There is only one being in the cosmos.",
        "q9": "Drama",
        "q9_justification": "A lyrical, poetic prologue in which a lone ghost at the end of time creates an artificial Earth as a memorial to the vanished human civilization. The tone is elegiac and contemplative.",
        "q10": "Other / Unsure",
        "q10_justification": "No civilian or military domain activity is depicted.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain to draw an analogy for.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The end of the universe: stars dying across a ten-billion-light-year sphere, a ghost creating matter from a wormhole connected to a galactic black hole, unfolding dimensions from a singularity. Physics and environment are fundamentally unlike any Earth experience."
    },
    {
        "chapter": "Part I",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The entire section is structured around Tianming's decades-long psychological war with the Trisolarans—torture, resistance, attempted suicide, forced collaboration. Beyond this personal conflict, the narrative reveals the Trisolaran strategic deception of Earth, the droplet attack, and the cosmic-scale war between the Master (Spirit) and the Lurker.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Tianming exists as a brain-in-a-jar aboard a Trisolaran ship, later receiving a cloned body in an artificial garden environment. He and AA live temporarily on Planet Blue. All space presence is transient—a ship, an alien planet without infrastructure.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Planet Blue is 300 light-years from Earth and 700 years in the future. Cheng Xin orbits overhead but is unreachable due to the black domain's reduced lightspeed. The Spirit traversed the universe. Distances are generational and effectively one-way.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Trisolaran society is revealed in unprecedented detail: individuals are ant-sized with collective intelligence, transparent thoughts become commercially disrupted by cloud computing (based on Tianming's digitized brain), mating involves bodily splitting. The Spirit represents a consciousness from the ten-dimensional universe. Radically alien on multiple levels.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The Trisolarans communicate with Tianming by injecting electrical signals directly into his brain and displaying floating text. The Spirit communicates through ideabstractions—a form of total-concept transmission that transcends language entirely.",
        "q6": "Other / Unsure",
        "q6_justification": "Planet Blue is largely benign (Earth-like atmosphere, water, vegetation). The Trisolaran ship environment is psychologically hostile but physically comfortable. The section does not primarily depict space environmental challenges.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Tianming and AA inhabit Planet Blue—two humans on an entire alien world. Tianming was the sole human aboard the Trisolaran Fleet. Space habitation by humans is extraordinarily rare.",
        "q8": "Other / Unsure",
        "q8_justification": "No conventional space political order is depicted. The Trisolarans undergo revolution and counter-revolution, but this is an alien civilization's internal politics rather than a space polity.",
        "q9": "Drama",
        "q9_justification": "An intensely personal narrative: Tianming confesses his tortured history to AA—decades of Trisolaran psychological warfare, his complicity in Earth's destruction, his encounter with the Spirit. AA reveals she is a clone of Ai Xiaowei, Tianming's childhood friend. The section is driven by emotional revelation and character depth.",
        "q10": "Other / Unsure",
        "q10_justification": "Space activity does not fit a civilian/military framework. Tianming is a captive-turned-collaborator, not a soldier or civilian.",
        "q11": "Other / Unsure",
        "q11_justification": "The narrative involves psychological warfare, espionage, and cosmic revelation rather than conventional domain operations.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Planet Blue exists in a black domain where lightspeed is reduced to kilometers per second. The Spirit's projection is an infinite fractal structure visible through opaque walls. Trisolarans are revealed as ant-sized beings. Ideabstractions transmit millions of concepts simultaneously. Physics is fundamentally unlike Earth experience."
    },
    {
        "chapter": "Part II",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The section reveals the full scope of the cosmic war between the Master and the Lurker—a conflict spanning from the ten-dimensional universe through eight successive dimensional collapses. Tianming is conscripted as a Seeker to find and destroy the Lurker. The strategic struggle is literally universe-defining.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "The mini-universe (Universe 647) is a 1km cube—too small for real territory. Tianming's rebuilt body traverses the grand universe alone at lightspeed. There is no habitation in any conventional sense; space cannot be held or settled in this context.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Distances span billions of light-years. The Wild Duck Cluster is 6,000 light-years away but described as practically the same neighborhood. Tianming's mission will take billions of years. Time and distance are at the absolute cosmic extreme.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The mini-universe has a management AI (Sophon). The history revealed through ideabstractions shows civilizations across eight dimensional universes—fire phoenixes, shade dragons, flower kingdoms. The Master is the unified consciousness of the ten-dimensional universe. All social orders depicted are radically non-human.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Sophon translates ideabstractions into human language for Tianming. The Master communicates through ideabstractions that transmit millions of concepts simultaneously. All cross-species communication is technology-mediated.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The grand universe is being progressively two-dimensionalized. Tianming can only survive because his body has been rebuilt as a machine of pure energy. Without the Master's intervention (immortal body, ring, mini-universe), existence in space would be instantly lethal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Tianming is the sole human Seeker—possibly the last Seeker of any species. Only 19 mini-universes have been active in the three-dimensional universe. Space exploration is limited to a handful of rebuilt beings across the entire cosmos.",
        "q8": "Other / Unsure",
        "q8_justification": "No conventional political order exists. The Master and the Lurker are cosmic forces in a binary standoff, not polities. The mini-universe is managed by an AI.",
        "q9": "Drama",
        "q9_justification": "The section is structured as a philosophical dialogue during a tea ceremony: Tianming and Sophon discuss the nature of time, the meaning of eternal recurrence, the history of the ten-dimensional universe. Tianming breaks free of the Master's mental seal through philosophical insight. The drama is intellectual and existential.",
        "q10": "Other / Unsure",
        "q10_justification": "The domain of activity transcends civilian/military categories entirely. Tianming is a cosmic agent on a metaphysical quest.",
        "q11": "Totally unique domain",
        "q11_justification": "The conflict operates across the supermembrane between universes, involves dimension reversal and vacuum decay, and spans mini-universes that exist outside normal space-time. No conventional analogy applies.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The ten-dimensional universe with infinite lightspeed, dimension reduction across eight successive universes, the supermembrane underlying all reality, quasars as remnants of galactic-scale energy weapons, vacuum decay—physics is fundamentally alien to any Earth experience."
    },
    {
        "chapter": "Part III",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Abyss-Gazers' homeworld is destroyed by Tianming altering the gravitational constant, dragging it into the star abyss. The Lurker launches its trap, activating its galaxy-spanning sky calyx weapon system. The Master initiates a fake dimension reversal. The cosmic war reaches its climax with total existential stakes.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Abyss-Gazers possess over 100,000 awayworlds and 30 million seeds (warships) spanning half the universe. They have cleansed hundreds of civilizations to expand their territory. Their space occupation is explicitly imperial in scale.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Singer's seed is forty billion structures from the homeworld. The Lurker's dark matter network spans hundreds of millions of light-years. Tianming and Helena traverse billions of light-years. Distances are at the maximum cosmic scale.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Abyss-Gazers are a deeply alien species: they have indurates and pliants (sexes), organs of cogitation, dehydration biology, earth-bearing turtles as infrastructure, a King who has lived 1.3 billion time grains. Their society is theocratic-monarchical, built around guarding a weapon left by their Creator.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The big eye enables instantaneous telepresence communication across forty billion structures. Singer communicates with the King via vessel body and direct organ-of-cogitation exchange. Tianming and Helena communicate in Latin. All communication is technology-mediated.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Singer's seed is trapped by a dual-vector foil. The homeworld's gravitational constant is increased twelvefold, causing it to fall into the star abyss. The entire universe faces two-dimensionalization. Survival pressure is constant and existential at every level.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "For the Abyss-Gazers, space habitation across 100,000+ worlds and 30 million seeds is completely ordinary. Singer has spent his entire career on a seed traversing the universe. Space habitation is the norm, not the exception.",
        "q8": "Single unified authority",
        "q8_justification": "The King is the supreme authority of the Abyss-Gazers, with sole power to activate the world engines. The Council of Elders and other bodies are subordinate. The Lurker is a single Great Mind that reabsorbs all its partitioned nodes into one unified intelligence.",
        "q9": "Military / war",
        "q9_justification": "The section is dominated by warfare at cosmic scale: Singer cleansing Star-Plucker worlds, Tianming destroying the Abyss-Gazers' homeworld, the Lurker's trap and the Master's counter-trap, the activation of the sky calyx weapon system, the fake dimension reversal. The Coda resolves the war's aftermath.",
        "q10": "Mostly military",
        "q10_justification": "The Abyss-Gazers' entire civilization exists to protect a military countermeasure weapon. Singer is a cleanser (military role). The seeds are warships. Tianming acts as a military agent. The Lurker's sky calyx is a weapons system. All space activity serves military purposes.",
        "q11": "Totally unique domain",
        "q11_justification": "The conflict involves altering fundamental physical constants, supermembrane flash attacks, converting galaxies into pure energy, dimension reversal, and dark matter weapon networks spanning the observable universe. No conventional domain analogy can capture this.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Star abysses with altered gravitational constants, earth-bearing turtles as living infrastructure, the sky calyx (a galaxy-spanning dark matter weapon that blooms with light), supermembrane attacks, vacuum decay, the artificial world of Provence constructed from pure matter at the end of the universe. Physics is fundamentally unlike anything on Earth."
    },
]

country = 'China'
book_title = 'The Redemption of Time'
csv_path = 'data/results/China_The_Redemption_of_Time.csv'
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
