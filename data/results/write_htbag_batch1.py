import json, csv, os

chapters_data = [
    {
        "chapter": "PROLOGUE",
        "q1": "No contestation",
        "q1_justification": "The prologue is set entirely on future Earth, with children playing at a lake near a boarding school. No outer space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "Space territory and habitation are not addressed in this Earth-set prologue featuring children at play.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted or referenced. The chapter takes place entirely on Earth with no mention of interplanetary travel.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The prologue depicts future Earth society directly: a boarding school, children with advanced toys, a pastoral setting suggesting a utopian future civilization.",
        "q5": "Same languages as Earth",
        "q5_justification": "All characters speak the same Earth language. No alien or space-specific languages appear in this Earth-set prologue.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is a lake and forest on Earth with no environmental hazards.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not discussed. The children are on Earth with no reference to how common space presence might be.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown. The prologue is entirely terrestrial with no governance structures depicted beyond a school.",
        "q9": "Adventure / exploration",
        "q9_justification": "The children play adventure games with toy crossbows and air rifles, explore a Forgotten Road, and role-play medieval scenarios including a dangerous William Tell game.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter depicts children at a boarding school playing. There is no military presence or context whatsoever.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is not depicted as a domain in this chapter. The entire setting is terrestrial.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is shown to compare with Earth. The chapter takes place on Earth itself.",
    },
    {
        "chapter": "Chapter ONE",
        "q1": "No contestation",
        "q1_justification": "Earth observers operate covertly on the alien planet with no competing powers contesting control of space. The 250 observers are hidden among the local population.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The 250 Earth observers are on a temporary research mission from the Institute of Experimental History. They maintain outposts like the Drunkard's Lair but have no permanent settlements.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata has been on the planet for five years, far from Earth. The separation is profound: observers are deeply isolated, and extraction requires a commando team. Earth feels distant and unreachable.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The alien planet has a medieval feudal society with a king, feudal lords, and Gray Sturmoviks (fascist militia). This is radically different from the advanced communist Earth society the observers come from.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The alien planet has its own languages distinct from Earth. Rumata speaks the local language fluently while using Russian with fellow observers like Don Kondor and Don Hug.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The planet is physically Earth-like with breathable atmosphere, normal gravity, forests, and oceans. Environmental survival is not an issue; the dangers are social and political, not environmental.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only 250 Earth observers are present across nine continents of the planet. They are hidden among millions of locals, making their presence exceptionally rare.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The planet has multiple kingdoms: Arkanar, Irukan, Soan, the Empire, and barbarian regions. Earth operates separately as a distant unified authority sending observers.",
        "q9": "Political / diplomatic",
        "q9_justification": "Rumata navigates the political crisis in Arkanar, meets with fellow observers to discuss strategy, and grapples with Don Reba's fascist regime. The tone is political intrigue and ethical dilemma.",
        "q10": "Entirely civilian",
        "q10_justification": "The Earth observers are from the Institute of Experimental History, a civilian research organization. Their mission is observation and study, not military operations.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Earth observers study a less-developed alien civilization, reminiscent of colonial-era anthropologists. The observers must not interfere, echoing Prime Directive-style frontier ethics.",
        "q12": "Almost Earth-like",
        "q12_justification": "The planet is physically nearly identical to Earth: same atmosphere, gravity, flora, fauna, and the alien inhabitants are biologically human. Rumata passes easily as a local nobleman.",
    },
    {
        "chapter": "Chapter TWO",
        "q1": "No contestation",
        "q1_justification": "No contestation over outer space is depicted. The chapter focuses on Rumata's daily activities in the medieval city of Arkanar.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata operates as a covert observer in Arkanar, maintaining a house but as part of a temporary research mission, not a permanent settlement.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata has been stationed on the planet for years, deeply separated from Earth. His isolation is palpable as he navigates the alien society alone.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Arkanar's society features feudal aristocrats, the School of Patriots (fascist indoctrination), harbor restrictions, and crime lords like Waga Koleso, all radically unlike Earth.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Rumata communicates in the local Arkanarian language throughout the chapter, visiting the school, armorer, and harbor district. The planet has its own distinct languages.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment poses no survival challenge. Rumata walks through the city, visits shops and the harbor. All dangers are human-made, not environmental.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Rumata is the sole Earth observer in Arkanar. His presence among thousands of locals is vanishingly rare.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple political entities are referenced: Arkanar's kingdom, the harbor with ships forbidden from leaving, and Waga Koleso's criminal network operating as a parallel power structure.",
        "q9": "Political / diplomatic",
        "q9_justification": "Rumata places scholars as teachers at the School of Patriots to protect them, navigates feudal social dynamics, and meets the crime lord Waga to inquire about the missing Dr. Budach.",
        "q10": "Entirely civilian",
        "q10_justification": "Rumata's activities are entirely civilian: breakfast with nobles, visiting schools, an armorer's shop, and conducting intelligence-gathering as a researcher, not a soldier.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Rumata operates as an advanced civilization's representative among a less-developed society, using gold and influence to navigate local politics, echoing frontier-era dynamics.",
        "q12": "Almost Earth-like",
        "q12_justification": "The alien city of Arkanar resembles a medieval European city with harbors, shops, streets, and familiar social structures. The physical environment is indistinguishable from Earth.",
    },
    {
        "chapter": "Chapter THREE",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. The chapter focuses on Rumata's emotional turmoil, the death of Father Hauk, and his relationship with Kyra.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata remains a temporary observer. His transmitter circlet connects him to Earth historians, emphasizing his role as a visiting emissary rather than a settler.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata tells Kyra about a wonderful country beyond the oceans, beyond the seven mountains, called Earth. The distance is mythologized as impossibly far, emphasizing profound separation.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The alien society murders intellectuals by hanging them from crossbeams. Kyra's brother comes home with blood on his hands from patrol. The society is brutally different from Earth.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Kyra speaks the local Arkanarian language. Rumata describes Earth to her in terms she can understand, highlighting the linguistic and cultural gulf between worlds.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment remains benign. Rumata walks through streets, enters his house. All threats are from the fascist regime, not the natural environment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Rumata transmits via his circlet to historians on Earth, but he is essentially alone. His alien origin is known to no one in his household.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The kingdom of Arkanar operates under Don Reba's regime while other kingdoms exist beyond its borders. The political landscape has multiple competing entities.",
        "q9": "Drama",
        "q9_justification": "The chapter is deeply emotional: Father Hauk is lynched, Kyra flees her violent home in tears, and Rumata struggles with rage and impotence. He tells Kyra fairy tales about Earth to comfort her.",
        "q10": "Entirely civilian",
        "q10_justification": "Rumata operates as a civilian observer. His transmitter records events for historians. There is no military dimension to the Earth presence.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Rumata's inability to intervene while witnessing atrocities mirrors the ethical dilemmas of colonial-era observers among indigenous peoples, watching suffering without acting.",
        "q12": "Almost Earth-like",
        "q12_justification": "The planet's physical environment is indistinguishable from Earth. Streets, houses, weather, and biology are all Earth-like. Rumata describes Earth to Kyra as a better version of the same world.",
    },
    {
        "chapter": "Chapter FOUR",
        "q1": "No contestation",
        "q1_justification": "No space contestation is depicted. The chapter revolves around Rumata's failed seduction mission, Baron Pampa's arrival, tavern brawls, and Dona Okana's death.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata continues his temporary observer role. He uses Casparamid (Earth anti-alcohol medication) secretly, underscoring his visitor status with hidden advanced supplies.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata's isolation is stark as he uses Earth medication covertly and wakes on an empty lot, completely separated from his home world and its comforts.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The social order features court salons with chaperones, elaborate seduction rituals, tavern brawls with Gray officers, and summary execution of Dona Okana after torture, all alien to Earth norms.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All dialogue occurs in the local language of Arkanar. The alien planet's language is used throughout conversations at the salon, tavern, and court.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment poses no survival challenge. Rumata navigates salons, taverns, and streets. Dangers are entirely social.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Rumata is the only Earth person present throughout the chapter's events. His alien origin is completely concealed.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The chapter references multiple political entities including Arkanar's court, Don Reba's security apparatus, the Soanian embassy, and Irukanian connections.",
        "q9": "Drama",
        "q9_justification": "The chapter is driven by emotional intensity: Rumata's disgust during the seduction attempt, Baron Pampa's marital grief, a night of drunken despair, and Dona Okana's shocking death by torture.",
        "q10": "Entirely civilian",
        "q10_justification": "All Earth-related activity is civilian. Rumata's espionage mission is scholarly observation, not military action. Even his brawls are personal, not military operations.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Rumata's degradation through immersion in the alien culture, using local customs for intelligence gathering, mirrors frontier agents going native in colonial settings.",
        "q12": "Almost Earth-like",
        "q12_justification": "The planet continues to be physically Earth-like. Taverns, horses, salons, weather, and biology are all familiar. The differences are cultural, not environmental.",
    },
    {
        "chapter": "Chapter FIVE",
        "q1": "No contestation",
        "q1_justification": "No space contestation occurs. The chapter details court politics, the persecution of intellectuals, and the royal dinner where Budach treats the king.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Rumata continues as a covert observer at court, spending gold to rescue scholars and maintain his cover as a noble don.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Rumata has been in Arkanar five years, deeply embedded. His Earth origin is implied when Don Reba notes he received no money from Estorian estates, hinting at his non-local origins.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The chapter catalogues the systematic destruction of intellectuals: burned observatory, hanged physicians, exiled poets, destroyed bookshops. The royal court is barbaric with its 100-person feasts.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Rumata converses with the poet Gur and other courtiers in the local language. The alien civilization's language and literary tradition are highlighted through poets like Zuren and Gur.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The physical environment remains benign. The palace, dining hall, and corridors present no environmental hazards. All dangers are political.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Rumata operates alone at court. His rescue operations for scholars are solo efforts, emphasizing how few Earth observers exist.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Multiple political entities interact: Arkanar, Irukan (Budach's origin), Soan (where exiled scholars flee), and Don Reba's security apparatus as a state-within-a-state.",
        "q9": "Political / diplomatic",
        "q9_justification": "Rumata executes a political maneuver to force Don Reba to produce Budach before the king. The chapter centers on court politics, persecution of intellectuals, and power struggles.",
        "q10": "Entirely civilian",
        "q10_justification": "The Earth mission remains entirely civilian. Rumata's interventions are scholarly rescue operations, not military actions.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Rumata smuggles intellectuals across borders and uses gold from Earth to influence local politics, paralleling colonial-era agents operating in pre-modern societies.",
        "q12": "Almost Earth-like",
        "q12_justification": "The palace, court rituals, dining customs, and natural environment closely mirror medieval Earth. The planet is physically identical to Earth.",
    },
]

country = 'Russia'
book_title = 'Hard to Be a God'
csv_path = 'data/results/Russia_Hard_to_Be_a_God.csv'
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
