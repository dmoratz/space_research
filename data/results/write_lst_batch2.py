import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 6",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Messengers have reached the height of WWII and redirected all combatants against the ET. Five hundred aircraft attack Kiruna. The Chinese Eighth Route Army annihilates the Fushun colony. ET develop geothermal energy silos (400+ worldwide) enabling unlimited time travel. Cutty proposes retreating 100,000 years to defend humanity at its evolutionary origin.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Messengers operate from temporary bases like Oulu in Finland. Cutty's ship is stationed on the Moon. The ET attempt to establish footholds on the Moon. No permanent space settlements exist in this 1943 timestream beyond military installations.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The only off-Earth activity is Cutty's ship on the Moon, dealing with ET trying to establish footholds there. All other action takes place on Earth's surface. The space component is near-Earth only.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays 1943 Earth with its WWII-era nations redirected against the ET. The Messengers operate within Earth's existing military structures.",
        "q5": "Same languages as Earth",
        "q5_justification": "The generals speak their national languages. Orville communicates with Alexandr, Quench, and Cutty in standard language. Hartmann speaks German. No space-specific language exists.",
        "q6": "Other / Unsure",
        "q6_justification": "Space conditions are barely referenced. Cutty fights on the Moon but no environmental details are given. The chapter focuses on Earth-based military operations.",
        "q7": "Other / Unsure",
        "q7_justification": "No one lives in space. Cutty's ship is on the Moon but the chapter focuses entirely on Earth-based operations in 1943.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The 1943 world is organized by Earth nation-states redirected against the ET. Americans, Soviets, Germans, Italians, British, French, Japanese, and Chinese forces cooperate uneasily. Behind the facade, secret agreements and power plays continue.",
        "q9": "Military / war",
        "q9_justification": "The chapter is entirely military: air campaigns from Oulu, carrier operations, geothermal energy discovery, strategic debates about self-replication vs. upstream defense. The Messengers vote on retreating 100,000 years. Orville volunteers to defend 400+ abandoned timestreams alone.",
        "q10": "Mostly military",
        "q10_justification": "Every scene involves military operations or strategic planning. The Allied Air Command Center, carrier deployments, nuclear strikes, and the Messengers' vote on strategy. The only civilian is Hartmann, a pilot. Alexandr's story-writing is the sole non-military activity.",
        "q11": "Like the air / airpower",
        "q11_justification": "The chapter centers on air operations: Stukas, Shturmoviks, Mustangs, Bf 109s, and Macchis launch from Oulu. Carrier operations recover aircraft. The Allied Air Command coordinates multinational air forces. The military framework is explicitly airpower-based.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is barely depicted. The Moon fighting is mentioned but not described. The chapter's physical environment is entirely 1943 Earth.",
    },
    {
        "chapter": "Chapter 7",
        "q1": "Total war / constant conflict",
        "q1_justification": "Eight thousand men have fallen in the march east. Three major battles, eight more by Takahaya, thirty smaller engagements, plus daily clashes. The battle at Toyokawa involves Scorpio catapults, suicide attacks, and thousands of dead. The fortress at Atago is overrun by iron-bodied mononoke with artillery. The retreat costs two-thirds of the army.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely on Earth in 248 AD Japan. No space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. Orville tells stories of other time periods but no spatial travel takes place.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays wartime Japan with Miyo, Orville, Kan, and Takahaya leading the Yamatai armies.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in archaic Japanese. Orville tells Miyo stories of other lands in her language. Kan speaks standard Japanese of the era.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance is depicted. Cutty threatens to seize all antimatter and fight alone, but this is a strategic disagreement, not space governance.",
        "q9": "Military / war",
        "q9_justification": "The chapter is consumed by warfare: the march east, the battle of Toyokawa, building the fortress at Atago, the devastating night attack with ET artillery, the catastrophic retreat. Orville and Miyo's intimacy develops amid constant combat.",
        "q10": "Mostly military",
        "q10_justification": "Nearly every scene involves combat, military strategy, or army movements. Miyo leads from the palanquin. Orville fights on the front lines. Takahaya commands troops. The brief romantic interlude occurs within the military context.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. The fighting is entirely terrestrial.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced.",
    },
    {
        "chapter": "Chapter 8",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Orville returns from 406 timestreams with 370 defeats, the sole survivor of his 25-person team. The Messengers maintain a 100,000-year vigil against sporadic ET attacks. Major battles occur at Nan Madol and in Egypt. Cutty reveals the ET creators' motivation: revenge for a human observation station that nearly destroyed their ancestral microbes.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Messengers' Victoria Base near Lake Victoria has mining operations, factories, and weapons production. It serves as Earth's strongest fortress. Human civilizations develop permanent settlements far ahead of schedule: farming communities in Ethiopia, kingdoms in North America, an ocean empire in the South Pacific.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Cutty launched a probe to Teegarden's Star, 12 light-years away, using a solar sail that took 72,000 years to arrive. The ET creators are from 120 million years in the future. The temporal and spatial distances are effectively infinite and unreachable.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted in this chapter. The Messengers live among proto-humans at Lake Victoria. The civilizations that develop are Earth-based, influenced by the Messengers' presence.",
        "q5": "Same languages as Earth",
        "q5_justification": "Orville and Alexandr communicate via their internal network. The proto-humans have a few hundred words. The Egyptian girl speaks ancient Egyptian. All languages are Earth-based.",
        "q6": "Other / Unsure",
        "q6_justification": "Space is referenced only as the destination of Cutty's probe to Teegarden's Star. No space environment is directly depicted or experienced.",
        "q7": "Other / Unsure",
        "q7_justification": "No one lives in space. The Messengers and proto-humans are all on Earth's surface over a 100,000-year span.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance exists. The Messengers govern their own military operations via majority vote. Earth civilizations develop independently. Cutty functions as a de facto military dictator over the Messenger forces.",
        "q9": "Military / war",
        "q9_justification": "The chapter spans 100,000 years of military vigilance. Orville fought across 406 timestreams. Alexandr fought at Nan Madol. Cutty reveals the ET origins and proposes attacking their home planet. Alexandr is court-martialed for desertion. Every scene relates to the war.",
        "q10": "Mostly military",
        "q10_justification": "The Messengers are military assets maintaining a 100,000-year defensive vigil. Victoria Base is a military installation. Alexandr's court-martial reinforces the military framework. The only civilian elements are the proto-humans and the Egyptian girl.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. The war takes place across time on Earth's surface.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is not experienced. The probe to Teegarden's Star is unmanned. All characters remain on Earth.",
    },
    {
        "chapter": "Chapter 9",
        "q1": "Total war / constant conflict",
        "q1_justification": "The Yamatai armies face annihilation: the fortress falls, the army retreats to Suminoe Harbor where 8,000 men make a last stand against 20,000 iron-bodied mononoke with cannons. Takahaya is killed. Cutty self-destructs at Victoria Base with 37.7 gigatons of TNT. Orville dies in combat. Only the arrival of Omega's temporal army saves the survivors.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set entirely on Earth in 248 AD Japan. Omega's ship descends from the sky but is from the future, not from space habitation. No space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. Omega arrives via temporal travel from the 21st century, not spatial travel. His ship is a time vessel.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays the final battle of the Yamatai armies and Miyo's leadership in extremis.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in Japanese. Miyo speaks through the magatama. Omega speaks to Miyo in her language. Kan speaks archaic Japanese.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The battle takes place on beaches and in surf.",
        "q7": "Other / Unsure",
        "q7_justification": "No one is in space. Omega's ship briefly appears but descends to Earth immediately.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance exists. The chapter focuses on Earth-based military crisis and Miyo's leadership.",
        "q9": "Military / war",
        "q9_justification": "The chapter is the climactic battle: the fall of the fortress, Takahikone's betrayal and death, the last stand at Suminoe, Takahaya's death, Cutty's self-destruction, Orville's death, and Omega's rescue. Every scene is combat or its immediate aftermath.",
        "q10": "Mostly military",
        "q10_justification": "The entire chapter is military: fortress defense, retreat, last stand, naval-style rescue. Miyo commands troops. Kan kills Takahikone. Omega's temporal army destroys the ET. The only civilian element is the refugee women sent west.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. The temporal army arrives from the sky but operates as a planetary strike force.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced. All action takes place on Earth's surface and in coastal waters.",
    },
    {
        "chapter": "Chapter 10",
        "q1": "No contestation",
        "q1_justification": "The war against the ET is effectively won. Omega's ship arrives at Osaka Space Terminal to celebrations. The enemy faces the beginning of the end. The chapter is a peaceful epilogue focused on Omega processing O's memories and meeting Sayo.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The 2010 setting has the Osaka Space Terminal, a massive facility accommodating Omega's flagship. The Global Confederation of Nations and Ministry for Temporal Administration govern. Humanity has permanent space infrastructure.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. The ship arrives at Osaka Space Terminal from temporal operations, not from a spatial voyage.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The 2010 setting shows Earth society with temporal technology: a Global Confederation, Ministry for Temporal Administration, space terminals, and AI Pathfinders. Society is recognizably Earth-like with advanced technology.",
        "q5": "Same languages as Earth",
        "q5_justification": "Omega speaks standard Osakan Japanese. Sayo speaks with a regional accent from east of Osaka. Alpha speaks standard language. All communication is in Earth languages.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The chapter takes place at a space terminal on Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not depicted in this chapter. The focus is on Omega's arrival on Earth and his emotional response to O's memories.",
        "q8": "Single unified authority",
        "q8_justification": "The Global Confederation of Nations governs humanity. The Ministry for Temporal Administration coordinates temporal operations. There is a single unified political authority overseeing the war against the ET across timestreams.",
        "q9": "Drama",
        "q9_justification": "The chapter is a quiet, emotional epilogue: Omega processes O's memories and discovers the void at the core of his being, weeps, then meets Sayo from Makimuku who wears a magatama bead. The resonance with Orville and Miyo's story creates a deeply dramatic moment.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The scene is a civilian celebration at a space terminal. Politicians, young women with bouquets, and crowds welcome the ship. Omega and Alpha are military Pathfinders but the setting is overwhelmingly civilian. The war is ending.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The flagship Secundus Minutius Hora settles into a sea berth at Osaka Space Terminal. Tugs spray water. The gangway extends. The scene has distinctly naval characteristics: a ship arriving in port to a civilian welcome.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is experienced in this chapter. The setting is Earth's surface at a space terminal.",
    },
]

country = 'Japan'
book_title = "The Lord of the Sands of Time"
csv_path = "data/results/Japan_The_Lord_of_the_Sands_of_Time.csv"
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
