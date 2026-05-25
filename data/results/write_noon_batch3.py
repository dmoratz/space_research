import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 11 - The Assaultmen",
        "q1": "No contestation",
        "q1_justification": "No competing powers contest space. The Assaultmen explore Vladislava cooperatively under Director Bader's unified authority, with a shared mission to study alien artifacts.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Tariel orbits Vladislava temporarily. Bader maintains a far-space base with observatories and workshops, but these are research outposts, not permanent settlements.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "EN 17 is many parsecs from Earth. Bader sent the button with Captain Bykov half a subjective year ago, and Gorbovsky said goodbye to his mother fifteen years before. The separation from Earth is profound.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The crew maintains Earth culture: eating kasha and milk, singing songs, joking in multiple Earth languages. Gorbovsky dreams of meadows and streams on Earth.",
        "q5": "Same languages as Earth",
        "q5_justification": "The crew speaks Russian, English, Japanese, and German. Bader inserts German words, Falkenstein speaks Japanese, and Dickson speaks English. All are standard Earth languages.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Vladislava's atmosphere is lethal: wild horizontal currents, crystalline dust, unimaginable lightning, magnetic field surges. Sterling died attempting landing. Gorbovsky's hands tremble uncontrollably after each run.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only a handful of Assaultmen explore the frontier. The Tariel carries a tiny crew: Gorbovsky, Falkenstein, Dickson, Waseda, and visiting Sidorov. They represent the vanguard of human exploration.",
        "q8": "Single unified authority",
        "q8_justification": "Bader serves as general plenipotentiary of the Cosmonautical Council and director of the far-space base. A single unified authority coordinates all exploration.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is pure exploration adventure: examining million-year-old alien satellites, making dangerous atmospheric descent runs into Vladislava, Sidorov's unauthorized landing, and the desperate escape.",
        "q10": "Entirely civilian",
        "q10_justification": "The Assaultmen are civilian scientists and explorers. Sidorov is a biologist, Dickson a psychologist, Waseda a physicist. No military context exists.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Assaultmen are explicitly frontier explorers, pushing into unknown alien worlds. They examine traces of alien civilizations, echoing archaeological expeditions in colonial frontier territories.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Vladislava is an orange-black planet of a blue star with a wild atmosphere of crystalline dust storms, inexplicable magnetic surges, seething petroleum on the surface, and enormous geysers. Utterly unlike Earth.",
    },
    {
        "chapter": "Chapter 12 - Deep Search",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is set entirely in Earth's ocean. No space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory or habitation is portrayed. The chapter follows Kondratev herding whales and hunting giant squid in Earth's ocean.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. Kondratev is now an Oceanic Guard whale herder operating in Earth's seas.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The advanced 22nd-century Earth society is shown through the Oceanic Guard: whale herding, plankton cultivation, and deep-sea operations with sophisticated submarines.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian and Japanese. Trainees Akiko and Belov speak standard Earth languages.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The chapter takes place in the deep ocean with giant squid, whales, and submarines.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not discussed in this ocean-set chapter.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown. The chapter depicts the Oceanic Guard's operations.",
        "q9": "Adventure / exploration",
        "q9_justification": "Kondratev leads trainees on a deep-sea hunt for a giant squid, with tense underwater pursuit, equipment failures, and dangerous encounters in the ocean depths.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter depicts civilian oceanic operations.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed. The ocean setting has its own frontier dynamics but is not space.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is Earth's deep ocean.",
    },
    {
        "chapter": "Chapter 13 - The Mystery of the Hind Leg",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is set entirely on Earth in Australia. No space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed. The chapter follows journalist Slavin visiting the CODD supercomputer in Australia.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. The chapter is entirely Earth-set, dealing with a computing mystery about seven-legged sheep.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Advanced 22nd-century Earth is shown: the CODD supercomputer, automated farming, dinosaur footage reconstruction, and mechanical monster creation for planetary exploration.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian and English. No space-specific languages appear.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The chapter takes place at a computer facility in the Australian desert.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not discussed in this Earth-set chapter.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Comedy / satire",
        "q9_justification": "The chapter is comic: the CODD computer produces bizarre results including seven-legged sheep, reconstructed dinosaur footage, and self-replicating mechanical monsters, baffling its operators.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter depicts civilian computing and journalism.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed in this Earth-set chapter.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is the Australian interior.",
    },
    {
        "chapter": "Chapter 14 - Candles Before the Control Board",
        "q1": "Other / Unsure",
        "q1_justification": "The chapter is set entirely on Earth. No space or contestation over space is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is portrayed. The chapter follows the Great Encoding of Academician Okada's brain onto crystalline quasibiomass.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. The chapter is about achieving immortality through brain encoding on Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The advanced 22nd-century Earth society is shown through its most ambitious scientific project: encoding a human brain to achieve functional immortality.",
        "q5": "Same languages as Earth",
        "q5_justification": "All dialogue is in Russian and Japanese. No space-specific languages appear.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The chapter takes place in a laboratory on Earth.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not discussed in this Earth-set chapter about brain encoding.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Drama",
        "q9_justification": "The chapter is intensely dramatic: the dying Academician Okada undergoes the Great Encoding as colleagues watch, hoping to achieve the first successful transfer of human consciousness to quasibiomass.",
        "q10": "Other / Unsure",
        "q10_justification": "No space-related activity occurs. The chapter depicts a civilian scientific procedure.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is a laboratory on Earth.",
    },
    {
        "chapter": "Chapter 15 - Natural Science in the Spirit World",
        "q1": "No contestation",
        "q1_justification": "No contestation over space occurs. The Institute for Space Physics conducts cooperative research with full World Council support.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is set on Kotlin Island on Earth. Space is referenced through sigma-deritrinitation theory and D-ship physics, but no space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs in this chapter. Peters mentions his son Harry who went to Venus and died there, but this is backstory.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The advanced Earth society is shown: the Institute for Space Physics, espers working as long-distance communicators with space expeditions, and the World Council providing energy for experiments.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Russian and English. Peters sings English ditties. No space-specific languages appear.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is directly depicted. The sigma-deritrinitation experiment involving spacecraft collision is referenced but occurred in the past.",
        "q7": "Other / Unsure",
        "q7_justification": "Space habitation is not the focus. Peters mentions Venus colonization through his son Harry, but the chapter centers on Earth-based physics research.",
        "q8": "Single unified authority",
        "q8_justification": "The World Council provides energy for experiments and governs space-related research. A single unified Earth authority coordinates all activity.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on the espers' suffering in isolation chambers, Peters mourning his son who died on Venus, and the tension between scientific ambition and human cost. Old Sieverson's grumbling adds pathos.",
        "q10": "Entirely civilian",
        "q10_justification": "All activity is civilian: the Institute for Space Physics, esper doctors, and scientific experiments. No military context exists.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is directly portrayed. The chapter is about theoretical physics research on Earth.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted. The setting is Kotlin Island in the Gulf of Finland.",
    },
]

country = 'Russia'
book_title = 'Noon: 22nd Century'
csv_path = 'data/results/Russia_Noon__22nd_Century.csv'
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
