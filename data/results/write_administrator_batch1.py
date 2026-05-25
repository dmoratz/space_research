import json, csv, os

chapters_data = [
    {
        "chapter": "The Flame and the Blossom",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Patrol Commander Thompson challenges the Administrator's authority and wants military access to the planet, but there is no open armed conflict. Tensions exist between colonies needing judgments, but Kurobe cancels them.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "Planet Sarulunin is classified Class III Type B (minimum interference, revert to original condition). The Administration Complex exists but human presence is minimal and deliberately restricted.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The story takes place on planet Sarulunin in System 925, requiring interstellar travel. The Terran Federation spans many star systems, implying vast distances and major separation from Earth.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Administrator Kurobe lives among the Sarulunia, plant-based intelligent beings with a complex lifecycle. He develops a deep emotional and telepathic bond with Amilla, a native motile, bridging two radically different cultures.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "SQ-class robots serve as translators between the Administrator and the Sarulunia. Communication between species is mediated entirely through robotic translation technology.",
        "q6": "Manageable but risky",
        "q6_justification": "Sarulunin is habitable for humans with its forests and breathable atmosphere, but the alien biosphere with its unique plant-based lifecycle and seasonal flowering events poses ongoing risks requiring careful management.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Only the Administrator, his robot staff, and occasional military visitors like Thompson are present. The human population is tiny and specialized, consisting of one Administrator and support systems.",
        "q8": "Single unified authority",
        "q8_justification": "The Terran Federation governs all colonial worlds through the Administrator System, which replaced earlier military rule under Kalgeist. A single chain of command runs from the Federation to each world's Administrator.",
        "q9": "Drama",
        "q9_justification": "A deeply personal drama about Administrator Kurobe torn between duty as an impartial official and his growing emotional bond with Amilla, a native who will eventually flower and lose consciousness.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Administrator system is civilian governance, but Patrol Commander Thompson represents the military Forces that previously controlled colonial worlds and still seek influence.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Administrator governs a distant colonial world with a native population, mediating between human interests and indigenous rights, directly paralleling frontier colonial governance.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Sarulunin has alien plant-based lifeforms and a unique biosphere, but the environment is breathable and habitable. Humans can live there with standard infrastructure support.",
    },
    {
        "chapter": "A Distant Noon",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Multiple layers of conflict: colonists secretly cannibalize natives, colonists distribute weapons to rival native communities out of spite, a combined fleet attacks Gugenge's merchant ships, and a coup overthrows and kills the reformer Gugenge.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "About 300 unofficial colonists have established a small 'Kingdom of Nenegia' that the Administrator struggles to control. The settlement is unauthorized and difficult to govern.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Planet Nenegin is another world in the Terran Federation's interstellar domain, requiring long-distance space travel. The Administrator is profoundly separated from Earth.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "The unofficial colonists have created a hybrid 'Kingdom of Nenegia' with the Administrator as ceremonial king. They wear anachronistic clothing and interact extensively with the native Nenegia, though exploitatively.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The Administrator communicates with the native Nenegia through robot translators. The SQ robot hierarchy handles all cross-species communication.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Nenegin features eternal rain, perpetual darkness, mud, and volcanic activity. The environment causes 'color-sense compensation effect' hallucinations in humans, making survival resource-intensive.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "Only about 300 unofficial colonists and one Administrator with robots inhabit the planet. Space habitation here is rare and specialist.",
        "q8": "Single unified authority",
        "q8_justification": "The Terran Federation's Administrator System is the governing authority, even though the colonists have created an unauthorized settlement. The Administrator remains the formal authority.",
        "q9": "Drama",
        "q9_justification": "A tragic drama about the unintended consequences of colonial interference: Gugenge's promising reforms are destroyed when colonists distribute weapons to rivals, and the 'distant noon' of civilization may never arrive.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Administrator governs as a civilian official with robot support. There is no military presence, but the robots have enforcement capabilities used against smuggling and cannibalism.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Colonists exploit native Nenegia through swindling and even cannibalism, directly paralleling the worst aspects of historical colonial expansion and frontier exploitation.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Nenegin's eternal darkness, constant rain, volcanic activity, and lack of color cause severe psychological effects including hallucinations. The environment constantly challenges human habitation.",
    },
    {
        "chapter": "The Wind in the Ruins",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Tensions exist between Cadet Thomas and the colonists, and spirits frighten people, but there is no armed conflict. The main disputes are bureaucratic and philosophical rather than violent.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Tayuneine has established colonial cities with a City Hall Manager and infrastructure. The world is peaceful enough that it is classified Class IV Type S2, and colonists live comfortably.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Tayuneine is an interstellar colony world within the Federation, requiring long-distance space travel. Inspector Samielle arrives from Federation space for inspection.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "Colonists on Tayuneine live in cities with Earth-like governance structures. The peaceful environment has made them content and slightly adapted to the world's atmosphere and fragrances, but culture remains essentially human.",
        "q5": "Same languages as Earth",
        "q5_justification": "The native inhabitants are extinct for thousands of years. All communication is between humans in their own language, with no alien languages present.",
        "q6": "Benign / easily survivable",
        "q6_justification": "Tayuneine is described as a beautiful, peaceful, flower-covered world. It is so comfortable that every Administrator who serves there loses ambition and resigns, suggesting an almost idyllic environment.",
        "q7": "Moderately common (noticeable settlements/populations)",
        "q7_justification": "Multiple colonial cities exist on Tayuneine with sufficient population to have City Hall managers, administration structures, and communities that gather at ruins.",
        "q8": "Single unified authority",
        "q8_justification": "The Terran Federation governs through the Administrator System. The Inspector system is being developed as an oversight mechanism, but authority remains centralized.",
        "q9": "Drama",
        "q9_justification": "A contemplative drama exploring governance, the meaning of peace, and mysterious spectral phenomena. The conflict is philosophical rather than physical, centering on what authentic governance means.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The Administrator and colonists are all civilian. Cadet Thomas and Inspector Samielle represent Federation oversight but not military force. The robots provide security.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "A colonial world governed by an outside Administrator, with colonists who have settled on a world whose native inhabitants are extinct, paralleling frontier settlement.",
        "q12": "Almost Earth-like",
        "q12_justification": "Tayuneine is described as beautiful with flowers, pleasant fragrances, and comfortable living. The environment is so benign that Administrators resign to stay, suggesting near-Earth conditions.",
    },
    {
        "chapter": "Bound Janus",
        "q1": "Total war / constant conflict",
        "q1_justification": "The story escalates from smuggling to a naval battle killing dozens, assassination attempt on the Administrator by Gun'gazea, destruction of SQ1 by infiltrators, and culminates in full-scale ground warfare between armies.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Gun'gazen supports nearly ten million colonists across nine island governments with cities, industries, and shipyards. The Gun'gazea have over 200 nations on Babel continent with populations up to 150,000 each.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Gun'gazen is an interstellar colony world. The Inspector arrives by starship, and the Forces of Kalgeist III are five hours away. The Federation spans multiple star systems with profound distances.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Human colonists and Gun'gazea native civilization coexist with extensive (though restricted) interaction. Smuggling creates trade relationships, and the Administrator serves as a cultural bridge between two distinct civilizations.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "SQ2A translates all communication between the Administrator and Gun'gazea, whose rapid speech is impossible for humans to follow. The robot translation system makes cross-species communication possible.",
        "q6": "Manageable but risky",
        "q6_justification": "Gun'gazen is resource-rich and habitable, supporting ten million colonists and extensive native civilization. However, the extreme heat, heavy metal content in food, and the hostile jungle of Babel continent create ongoing risks.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Nearly ten million colonists inhabit the Rhamphorynchus Archipelago with nine governments, cities, and industrial development. Hundreds of thousands of Gun'gazea populate the Babel continent.",
        "q8": "Single unified authority",
        "q8_justification": "The Terran Federation governs through the Administrator System as the single recognized authority. Though the colonists are forming an independence movement and the Gun'gazea have their own nations, the formal political order is the unified Federation.",
        "q9": "Political / diplomatic",
        "q9_justification": "The core narrative is a political struggle between Administrator Sei and ex-Administrator Mischer over governance of Gun'gazen. Diplomatic negotiations with Gun'gazea D'o councils and colonial representatives drive the plot, though it culminates in warfare.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Administrator system is civilian but employs combat robots. The story features naval battles, an assassination attempt, ground warfare with Gun'gazea warriors, and the Forces of Kalgeist III are called in as military reinforcement.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Gun'gazen is a classic colonial world with settlers exploiting native territory and resources, an independence movement echoing colonial rebellions, and a two-faced Administrator mediating between colonists and natives.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Gun'gazen is hot with heavy metal-rich biosphere requiring processed food for humans, but ten million colonists live comfortably with cities and industries. Environmental differences are manageable with technology.",
    },
]

country = 'Japan'
book_title = "Administrator by Taku Mayumura"
csv_path = "data/results/Japan_Administrator_by_Taku_Mayumura.csv"
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
