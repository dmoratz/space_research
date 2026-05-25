import json, csv, os

chapters_data = [
    {
        "chapter": "front_matter",
        "q1": "Other / Unsure",
        "q1_justification": "The front matter contains only the title page, copyright information, and original Russian title. No narrative content.",
        "q2": "Other / Unsure",
        "q2_justification": "No narrative content. Purely bibliographic.",
        "q3": "Other / Unsure",
        "q3_justification": "No narrative content depicting any journey.",
        "q4": "Other / Unsure",
        "q4_justification": "No narrative content depicting any society.",
        "q5": "Other / Unsure",
        "q5_justification": "No narrative content depicting language dynamics.",
        "q6": "Other / Unsure",
        "q6_justification": "No narrative content depicting any environment.",
        "q7": "Other / Unsure",
        "q7_justification": "No narrative content depicting space habitation.",
        "q8": "Other / Unsure",
        "q8_justification": "No narrative content depicting political order.",
        "q9": "Other / Unsure",
        "q9_justification": "The front matter is bibliographic material, not a narrative chapter with a genre.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative content depicting any domain.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative content depicting any domain characterization.",
        "q12": "Other / Unsure",
        "q12_justification": "No narrative content depicting any environment.",
    },
    {
        "chapter": "Introduction",
        "q1": "Other / Unsure",
        "q1_justification": "The Introduction contains Theodore Sturgeon's critical essay about the Strugatskys and a framing radio interview with Dr. Pilman establishing the Visitation premise. These are paratextual materials, not narrative chapters.",
        "q2": "Other / Unsure",
        "q2_justification": "No narrative action. The Pilman interview establishes that six Visitation Zones exist on Earth, but no territory in space is discussed.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. The Pilman Radiant indicates the Visitors came from the direction of Deneb, but no journey is shown.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The Visitation is discussed abstractly.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. The Visitors left no communication.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is directly depicted in this framing material.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is discussed. The Visitors came and left.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is depicted.",
        "q9": "Other / Unsure",
        "q9_justification": "This is a critical essay and framing interview, not a narrative chapter.",
        "q10": "Other / Unsure",
        "q10_justification": "No narrative action depicting civilian or military domains.",
        "q11": "Other / Unsure",
        "q11_justification": "No narrative domain characterization.",
        "q12": "Other / Unsure",
        "q12_justification": "No space environment is depicted in this paratextual material.",
    },
    {
        "chapter": "Chapter 1",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Zone and its alien artifacts are contested by multiple parties: stalkers illegally extract artifacts, the International Institute conducts sanctioned research, Captain Quarterblad's border patrol hunts stalkers, and black marketeers like Ernest fence stolen goods. An ongoing rivalry pervades.",
        "q2": "Other / Unsure",
        "q2_justification": "The novel is set on Earth. The Visitation Zones are alien-altered areas on Earth's surface, not territory in space. Nobody inhabits or holds territory in space.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. The aliens visited Earth and left; humans do not travel to space in this chapter.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The setting is the Earth city of Harmont, where human society copes with the alien Zones' aftermath.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. The alien Visitors left no communication; all dialogue is in Earth languages.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Zone kills constantly: mosquito mange spots crush anything entering them, the silver web kills Kirill via apparent heart failure, burning fluff and witches' jelly are lethal. Redrick notes that coming back alive is 'a success' and with swag 'a miracle.'",
        "q7": "Other / Unsure",
        "q7_justification": "Nobody lives in space. The Visitors came and departed; no human space habitation is depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No political order exists in space. The Zone on Earth is under international scientific and military control.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is dominated by a tense Zone expedition: Redrick navigates lethal hazards (mosquito mange, an unknown shimmer), Kirill walks into a silver web and dies of apparent heart failure afterward. The atmosphere of constant dread, Kirill's death, and Redrick's grief pervade.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The Institute is a civilian scientific organization, but military security is omnipresent: Captain Herzog heads security, armed sergeants guard the facility, patrol cars with machine guns and searchlights ring the Zone, and Captain Quarterblad's border patrol hunts stalkers.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Zone is treated as a dangerous frontier: stalkers are prospectors risking death for alien artifacts, Ernest is a frontier fence, the Institute slowly pushes its research road deeper into the Zone. The economy of Harmont revolves around Zone exploitation.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The Zone contains physics fundamentally unlike Earth: graviconcentrates (mosquito mange) crush objects, empties are pairs of copper disks held apart by invisible force, the silver web kills on contact, witches' jelly dissolves matter, and burning fluff is lethal. The environment defies all known physical laws.",
    },
    {
        "chapter": "Chapter 2",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Redrick stalks the Zone illegally at night, sells swag to foreign buyers Throaty and Bones in a hotel room, is ambushed by Captain Quarterblad's forces at the Borscht bar, escapes, and turns himself in. Multiple parties contest control of Zone artifacts.",
        "q2": "Other / Unsure",
        "q2_justification": "The novel remains set on Earth. No space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is shown. The chapter depicts Earth's stalker subculture and black market.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All communication is in Earth languages.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Zone's lethality is shown through Burbridge's legs, destroyed by witches' jelly to the point of requiring amputation. A zombie-like moulage walks from the cemetery toward town. The Zone's dangers extend beyond its borders.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Night stalking through the cemetery with a crippled Burbridge, a zombie figure stumbling among the graves, the desperate escape from Captain Quarterblad's trap at the Borscht, and Redrick's decision to hide the lethal porcelain container. Horror and survival tension throughout.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Patrol cars with searchlights guard the Zone perimeter, Captain Quarterblad commands UN troops, while civilian stalkers and black market dealers operate in the shadows. Redrick bridges both worlds.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Redrick is a frontier smuggler: stalking the Zone at night for alien artifacts, selling contraband to foreign buyers, evading military patrols. The entire economy of exploitation mirrors frontier resource extraction.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Witches' jelly turns Burbridge's legs boneless below the knee. A perpetual motion hoop spins endlessly on Bones's finger. Moulages (zombie-like reconstructions) walk from the Zone. The porcelain container holds colloidal gas that dissolves all matter it touches.",
    },
    {
        "chapter": "Chapter 3",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Noonan, revealed as an intelligence agent, investigates how Burbridge smuggles thousands of Zone artifacts past his surveillance. Lemchen reveals six thousand items have leaked from Zones worldwide. Multiple nations, criminal networks, and institutions compete for Zone materials.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is depicted. The chapter is set entirely on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted. Pilman discusses the Visitors' origin from the direction of Deneb, but no journey is shown.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. Pilman's 'roadside picnic' theory suggests the Visitors were indifferent to humanity, leaving no cultural contact.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. The Visitors left no communication; Pilman notes they may not have even noticed humanity.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Pilman describes the Currigan Labs catastrophe: colloidal gas from the Zone killed thirty-five people and crippled over a hundred when it escaped containment. Zone mutations deform stalkers' children. Emigrants from Zone areas cause statistical spikes in disasters wherever they settle.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation. Pilman's theories all concern alien artifacts left on Earth.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order. The chapter discusses Earth institutions managing Zone aftermath.",
        "q9": "Drama",
        "q9_justification": "The chapter centers on Noonan's moral crisis as spy, his philosophical conversation with Pilman about humanity's place in the cosmos, and the devastating visit to Redrick's home where Monkey has deteriorated beyond recognition and the father sits as a moulage. Emotional weight outweighs action.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Noonan operates as an intelligence agent under Lemchen while maintaining civilian cover. The chapter reveals the intertwined military-intelligence-civilian infrastructure around the Zone: patrol guards, UN troops, institute scientists, and criminal networks.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Pilman's 'roadside picnic' metaphor frames the Zone as a frontier left by indifferent passers-by. Noonan discovers Burbridge runs 'Sunday school' picnics near the Zone to train young stalkers, echoing frontier apprenticeship in resource extraction.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Pilman catalogs Zone phenomena defying known physics: eternal batteries violating thermodynamics, black sprays with inexplicable light-delay properties, magnetic traps of unexplained power, moulages violating the second law of thermodynamics, and mutation effects with no identifiable radiation source.",
    },
    {
        "chapter": "Chapter 4",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Redrick's expedition to the Golden Ball is shaped by the broader contestation: Burbridge mapped the path using decades of stalker knowledge and sacrificed lives, Throaty and Bones want the porcelain container, and the Institute's automated stalkers encroach on Zone territory.",
        "q2": "Other / Unsure",
        "q2_justification": "No space territory is depicted. The chapter takes place entirely in the Zone on Earth.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey is depicted.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is shown. Redrick and Arthur are Earth humans navigating an alien environment.",
        "q5": "Other / Unsure",
        "q5_justification": "No space language dynamics. All communication is between two Earth humans.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The deepest Zone is a continuous death trap: a heat anomaly nearly incinerates both men, a mosquito mange lurks by the embankment, a lightning-filled depression with green slime nearly kills them, and the meatgrinder invisibly crushes Arthur to death. The landscape is littered with the remains of previous stalkers.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space political order is shown.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is a sustained ordeal of survival: a heat anomaly burns them, lightning in the depression deafens them, and the meatgrinder invisibly crushes Arthur. Redrick knowingly uses Arthur as a human minesweeper. The moral horror of the sacrifice and Redrick's desperate prayer at the Golden Ball combine survival terror with existential dread.",
        "q10": "Entirely civilian",
        "q10_justification": "Redrick and Arthur are civilians deep in the Zone with no military presence. This is an illegal expedition far beyond any institutional control.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Redrick is the ultimate frontier explorer: alone with a sacrificial companion in uncharted alien territory, following a hand-drawn map, seeking a legendary treasure. The path is marked by the remains of previous explorers (Whip, Four-Eyes, Poodle).",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The deep Zone has physics entirely unlike Earth: heat anomalies that incinerate without fire, graviconcentrates that flatten helicopters, a depression with autonomous lightning, a meatgrinder that invisibly twists and crushes a human body, and the Golden Ball itself—an alien artifact of unknown purpose that stalker legend says grants wishes.",
    },
]

country = 'Russia'
book_title = 'Roadside Picnic'
csv_path = 'data/results/Russia_Roadside_Picnic.csv'
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
