import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 8",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter is an extended exposition of ocean formations (extensors, mimoids, symmetriads, asymmetriads) and a discussion of two proposed scientific plans.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Station Solaris remains a tiny research outpost with three crew members orbiting the planet.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The chapter references the long history of Solaris research spanning over a century, implying sustained long-distance travel from Earth.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "The scientists operate with Earth scientific frameworks, publishing in Earth journals and following Earth academic conventions. Giese's explorations used Earth-designed protective gear.",
        "q5": "Same languages as Earth",
        "q5_justification": "All scientific literature, discussion, and terminology are in Earth languages. The ocean does not communicate linguistically.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The chapter catalogs the ocean's lethal formations: asymmetriads explode violently (killing Giese in the Eruption of the Hundred and Six), symmetriads can trap and kill explorers, and extensors are canyon-sized phenomena. Snow also warns that the neutrino disruptor could explode the station.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three crew on the station. The chapter references historical expeditions but current presence is minimal.",
        "q8": "Single unified authority",
        "q8_justification": "The Institute of Planetology and unified Solarist academic community govern all research. No competing political authorities.",
        "q9": "Drama",
        "q9_justification": "The chapter is dominated by extensive exposition of ocean formations from Giese's historical explorations, followed by a dramatic debate between the three scientists about whether to use the neutrino disruptor or the encephalogram experiment. Intellectual tension rather than physical danger.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is scientific research. No military presence whatsoever.",
        "q11": "Totally unique domain",
        "q11_justification": "The ocean's formations — extensors, mimoids, symmetriads, asymmetriads — defy all Earth analogies. The ocean is a single sentient organism covering an entire planet, unlike any terrestrial domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Symmetriads are temporary mathematical architectures miles across that rise from the ocean and dissolve. Asymmetriads erupt explosively. Mimoids replicate objects placed near them. The environment is fundamentally unlike anything on Earth.",
    },
    {
        "chapter": "Chapter 9",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter focuses on Rheya's suicide attempt and her discovery that she is not human.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Station Solaris remains a small research outpost.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The separation from Earth is felt in the isolation and impossibility of getting help or leaving easily.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "Kelvin and Rheya's relationship dynamics, emotional responses, and cultural references are entirely Earth-derived.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Earth languages. Rheya speaks as Kelvin's memories shaped her.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Rheya drinks liquid oxygen and dies horribly, then regenerates — demonstrating the psychological and physical harshness of the environment. The visitors are an inescapable torment created by the ocean.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Three crew members plus their visitors. No other human presence.",
        "q8": "Single unified authority",
        "q8_justification": "The unified institutional framework of Solarist research continues to govern the station.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Rheya drinks liquid oxygen in a horrific suicide scene — her body convulses, freezes, and then regenerates before Kelvin's eyes. She then listens to Gibarian's tape and realizes she is not human. The chapter is dominated by body horror and psychological terror.",
        "q10": "Entirely civilian",
        "q10_justification": "Purely scientific and personal drama. No military element.",
        "q11": "Totally unique domain",
        "q11_justification": "The ocean creates living beings from human memories that cannot die. This phenomenon has no terrestrial analogy.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Rheya's body is made of neutrino structures that regenerate from any damage, including drinking liquid oxygen. The ocean creates and maintains these constructs remotely. Physics operates on fundamentally alien principles.",
    },
    {
        "chapter": "Chapter 10",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter is a long philosophical conversation between Kelvin and Snow about the nature of the visitors and human self-deception.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Station Solaris remains a small research outpost.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Snow discusses whether the neutrino structures could survive away from Solaris, implying the vast distance to Earth is a barrier.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "The philosophical debate references Earth philosophy, human psychology, and Earth moral frameworks. The scientists think and argue as Earth intellectuals.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Earth languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The psychological torment of the visitors continues. Snow challenges Kelvin's self-deception about Rheya, and Kelvin agonizes over whether the encephalogram experiment will transmit his unconscious desire to be rid of her.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Three crew members on the station.",
        "q8": "Single unified authority",
        "q8_justification": "Unified institutional authority continues.",
        "q9": "Drama",
        "q9_justification": "The chapter is an extended philosophical dialogue between Kelvin and Snow about human nature, self-deception, and the ethics of the encephalogram experiment. Snow's challenge — 'you are doing all you can to stay human in an inhuman situation' — is the emotional core. Intellectual and emotional tension, not physical danger.",
        "q10": "Entirely civilian",
        "q10_justification": "Purely civilian scientific and philosophical discussion.",
        "q11": "Totally unique domain",
        "q11_justification": "The ocean's ability to probe human minds and create living neutrino constructs defies all terrestrial analogies.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Snow discusses the neutrino structure of visitors and whether they could survive away from Solaris. The environment's fundamental alien nature — a sentient ocean that creates beings from human memories — is central to the chapter's philosophical questions.",
    },
    {
        "chapter": "Chapter 11",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter surveys the history of Solarist studies and performs the encephalogram experiment.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Station Solaris remains a small research outpost. The chapter mentions historical expeditions but current presence is minimal.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The century-long history of Solaris research implies sustained long-distance travel between Earth and Solaris.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "The academic culture described — journals, conferences, schools of thought, academic politics — is entirely Earth-derived. Muntius's critique treats Solaristics as a disguised Earth religion.",
        "q5": "Same languages as Earth",
        "q5_justification": "All scientific literature and discussion are in Earth languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The chapter catalogs over a century of failed attempts to communicate with or understand the ocean, representing an immense resource investment with no return. The psychological toll on researchers is evident.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Three crew on the station. Historical expeditions mentioned but current presence is minimal.",
        "q8": "Single unified authority",
        "q8_justification": "The Institute of Planetology and unified academic community govern Solaris research.",
        "q9": "Drama",
        "q9_justification": "The chapter is dominated by intellectual exposition: the history of Solarist thought, the schism between schools, Muntius's devastating critique of Solaristics as disguised religion. The encephalogram experiment is performed but narrated with quiet tension rather than horror.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is academic research and scientific experimentation.",
        "q11": "Totally unique domain",
        "q11_justification": "Muntius's critique highlights that Solaristics has no terrestrial parallel — it is the study of a phenomenon that defies all human categories.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Gibarian's early work on bio-electronic analogies failed because the ocean's organization is fundamentally unlike any Earth biology. The encephalogram experiment — beaming human brain patterns as X-rays into the ocean — represents an attempt at communication across radically different physical substrates.",
    },
    {
        "chapter": "Chapter 12",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter depicts the aftermath of the encephalogram experiment and Kelvin's terrifying dreams.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Station Solaris remains a small research outpost.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The isolation from Earth is palpable as the crew waits for a response from the ocean with no outside help available.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "The crew's behavior — waiting, drinking, arguing — follows Earth patterns despite the alien context.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in Earth languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Kelvin experiences terrifying dreams of dissolution and alien contact. The ocean produces wings of foam and phosphorescence. Screams come from the laboratory at night. Snow visits drunk and raving. The psychological environment is extremely harsh.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Three crew members, increasingly unstable.",
        "q8": "Single unified authority",
        "q8_justification": "Unified institutional authority continues, though the station crew is increasingly isolated and dysfunctional.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Kelvin has terrifying dreams of dissolution and alien contact. The ocean produces massive wings of foam and phosphorescence in apparent response to the experiment. Screams emanate from the laboratory. Snow visits drunk, raving about mankind's hubris. An atmosphere of dread pervades.",
        "q10": "Entirely civilian",
        "q10_justification": "No military presence. The terror is existential and psychological.",
        "q11": "Totally unique domain",
        "q11_justification": "The ocean's response — wings of foam, phosphorescence, possible communication through dreams — has no terrestrial analogy.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The ocean responds to the encephalogram by producing enormous physical phenomena (wings of foam, phosphorescence) and possibly invading Kelvin's dreams. The boundary between mind and environment dissolves in a fundamentally non-Earth-like way.",
    },
    {
        "chapter": "Chapter 13",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter depicts Rheya's self-chosen destruction and the crew's grief.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Station Solaris remains a small research outpost.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Kelvin and Rheya discuss the impossible plan to return to Earth together, highlighting the vast distance and separation.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "The emotional dynamics — love, sacrifice, grief, deception — are entirely human and Earth-derived.",
        "q5": "Same languages as Earth",
        "q5_justification": "All communication is in Earth languages. Rheya's farewell note is in an Earth language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Rheya is destroyed by Sartorius's neutrino destabilizer at her own request. The visitors no longer return after the ocean's response. The psychological devastation is extreme.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Three crew members. Rheya is gone; the visitors have stopped appearing.",
        "q8": "Single unified authority",
        "q8_justification": "The crew agrees to write a joint report, maintaining unified institutional procedures.",
        "q9": "Drama",
        "q9_justification": "Rheya secretly arranges her own destruction, leaving a farewell note. Kelvin wakes to find her gone. Snow explains what happened. The chapter is driven by grief, sacrifice, and moral reckoning — dramatic rather than horrific.",
        "q10": "Entirely civilian",
        "q10_justification": "No military presence. The destruction of Rheya is a personal choice facilitated by scientific equipment.",
        "q11": "Totally unique domain",
        "q11_justification": "The ocean's cessation of visitor creation after the encephalogram experiment represents a unique form of possible communication or response.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The neutrino destabilizer disintegrates Rheya's non-atomic structure. The ocean has apparently changed its behavior in response to the X-ray encephalogram. The physics of visitors, neutrino structures, and ocean communication remain fundamentally alien.",
    },
    {
        "chapter": "Chapter 14",
        "q1": "No contestation",
        "q1_justification": "No space power rivalry. The chapter is a philosophical meditation on Solaris, God, and Kelvin's future.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Station Solaris remains a small research outpost. Kelvin contemplates returning to Earth but stays.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Kelvin reflects that returning to Earth would mean re-entering a world he can no longer fully engage with, emphasizing the psychological and physical distance.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "Kelvin's philosophical reflections draw on Earth theology and philosophy (the concept of an imperfect God).",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue and reflection are in Earth languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The environment remains harsh: toxic atmosphere, alien ocean, psychological devastation. Kelvin's visit to the old mimoid shows the ocean's alien power as it envelops his hand.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Kelvin, Snow, and Sartorius remain. Kelvin contemplates whether to stay or leave.",
        "q8": "Single unified authority",
        "q8_justification": "The unified institutional framework persists. The crew plans to file a report.",
        "q9": "Drama",
        "q9_justification": "The chapter is a philosophical meditation: Kelvin and Snow debate the concept of an imperfect God, with Snow suggesting Solaris as its cradle. Kelvin visits the old mimoid and touches the ocean. The tone is contemplative and elegiac, not thriller or horror.",
        "q10": "Entirely civilian",
        "q10_justification": "No military presence. Kelvin's visit to the mimoid is a personal, almost spiritual act.",
        "q11": "Totally unique domain",
        "q11_justification": "Snow's concept of Solaris as 'the cradle of your divine child' — an imperfect God emerging from the ocean — frames the domain as utterly unique, beyond any terrestrial analogy.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The old mimoid is a decaying ocean formation. When Kelvin touches the ocean, it envelops his hand, forming shapes around it. The ocean's nature — possibly a nascent imperfect God — represents the most radical departure from Earth experience in the novel.",
    },
]

country = 'Russia'
book_title = 'Solaris'
csv_path = 'data/results/Russia_Solaris.csv'
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
