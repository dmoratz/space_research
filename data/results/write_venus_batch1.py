import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter One",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter establishes a cosmic conflict between good and evil eldila, with Earth described as enemy-occupied territory under siege, but the conflict is mostly background and indirect in this chapter, manifesting only as psychological resistance against the narrator.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom previously visited Mars temporarily and is preparing for a mission to Venus. There is no permanent human settlement in space; only brief visits by individuals like Ransom, who returns to Earth afterward.",
        "q3": "Short interplanetary journey",
        "q3_justification": "Mars is described as forty million miles from London, and Ransom traveled there and back. The journey to Venus is upcoming. These are interplanetary trips within the solar system, presented as achievable though extraordinary.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Malacandrian creatures (Pfifltriggi, Hrossa, Sorns) and the eldila represent entirely non-human civilizations with alien social structures. The eldila view planets as mere interruptions in Deep Heaven, a fundamentally different cosmological perspective from Earth society.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The narrator hears Ransom and the eldil speaking a strange polysyllabic language that is not any Earth tongue. Ransom learned languages on Malacandra, and the eldil's speech is described as inorganic and unlike any human voice.",
        "q6": "Manageable but risky",
        "q6_justification": "Space itself (Deep Heaven) is the natural habitat of the eldila and is not portrayed as inherently lethal. However, Earth is described as under siege by hostile eldila, making the cosmic environment dangerous in a spiritual rather than physical sense.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom has traveled to another planet, and the narrator is astonished by this fact. Space travel is presented as an extraordinary, singular event rather than something common.",
        "q8": "Other / Unsure",
        "q8_justification": "Each planet has its own Oyarsa (ruling eldil), but these are not political entities in a conventional sense. Earth is under a bent Oyarsa while Mars has a benevolent one. The political order is more spiritual/cosmic than governmental.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter sets up an adventure narrative as the narrator journeys to Ransom's cottage amid an atmosphere of dread and wonder, preparing for a cosmic mission. The genre blends adventure with theological fantasy.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military presence or military framing of space. Ransom is a scholar, the narrator is a civilian, and the eldila operate outside any military structure. The conflict is spiritual rather than military.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is characterized as Deep Heaven, the natural habitat of spiritual beings (eldila). It is not likened to oceans, air, or frontiers but is presented as a metaphysical realm with theological overtones, making it a unique conceptualization.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The eldila exist as columns of light with no fixed spatial orientation, imposing an alien directional system. Deep Heaven is described as a realm fundamentally different from planetary surfaces, where beings exist in ways that defy Earth-based categories of natural and supernatural."
    },
    {
        "chapter": "Chapter Two",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Ransom explains that the Dark Lord (bent Oyarsa of Earth) is planning an attack on Perelandra, establishing a cosmic conflict. However, the actual conflict has not yet erupted; it is a looming threat discussed in preparation.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom is being sent on a solo mission to Venus in a coffin-like casket, with plans to return afterward. There is no settlement or territorial holding in space; it is purely a temporary visit for a specific purpose.",
        "q3": "Short interplanetary journey",
        "q3_justification": "The journey from Earth to Venus is accomplished by the Oyarsa transporting the casket. Ransom is in suspended animation during transit. The journey itself is not described as extremely long, though the return takes over a year of Earth time.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Ransom fondly recalls Malacandra's utterly alien civilization of Sorns, Hrossa, and other creatures. Venus is expected to be equally alien, with unknown conditions. The eldila operate on principles entirely foreign to human society.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Ransom explains that Hressa-Hlab (Old Solar) is the original common language of all rational creatures in the solar system, lost on Earth. He expects to speak it on Venus, indicating distinct space languages exist across worlds.",
        "q6": "Manageable but risky",
        "q6_justification": "Ransom must travel naked in a sealed casket in suspended animation, with risks acknowledged. He compares it to facing a firing squad. The conditions on Venus are unknown but he is told he will survive, suggesting manageable but uncertain danger.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom has traveled between planets, and he is being sent alone to Venus. The narrator and Humphrey serve as ground support. Space travel remains an extraordinary event limited to a single individual.",
        "q8": "Single unified authority",
        "q8_justification": "Each planet is governed by its own Oyarsa under Maleldil's ultimate authority. The solar system operates under a single hierarchical spiritual authority rather than competing political entities.",
        "q9": "Adventure / exploration",
        "q9_justification": "Ransom is being sent on a solo mission to an unknown planet to confront an undefined threat. The chapter focuses on preparation for departure, farewells, and the uncertainty of what awaits, which is classic adventure/exploration narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "Ransom is a philologist, not a soldier. He is sent by spiritual beings, not a military organization. There is no military infrastructure, weapons, or military chain of command involved in the mission.",
        "q11": "Other / Unsure",
        "q11_justification": "Space travel here is accomplished by an eldil moving a casket through Deep Heaven, a method that has no parallel to naval, air, or frontier domains. The mode of travel is entirely supernatural/spiritual.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Ransom must travel in suspended animation because the human body cannot survive the journey normally. He must go naked on Venus because of heat. The conditions are sufficiently different from Earth that significant adaptation is required."
    },
    {
        "chapter": "Chapter Three",
        "q1": "No contestation",
        "q1_justification": "This chapter focuses entirely on Ransom's arrival and initial exploration of Perelandra's ocean world. There is no conflict, rivalry, or contestation of any kind; only solitary wonder and discovery on an uninhabited floating island.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom arrives alone on Perelandra as a temporary visitor on a mission. He has no settlement, shelter, or infrastructure. He simply swims, walks on floating islands, and sleeps under the open sky.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "While the transit itself was in suspended animation, the chapter opens by noting Ransom's journey involved meaningful separation from Earth. He is deposited alone on a completely alien ocean world with no means of independent return.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Perelandra has no society at all in this chapter. It is an entirely alien world of floating islands on a global ocean with no visible inhabitants, no structures, and no social order. The environment and its biology are utterly unlike anything on Earth.",
        "q5": "Other / Unsure",
        "q5_justification": "No language or communication occurs in this chapter. Ransom is entirely alone on Perelandra, with no one to speak to. The question of language in space does not arise.",
        "q6": "Manageable but risky",
        "q6_justification": "Perelandra's ocean is warm and the water is drinkable. Food grows on the floating islands. However, Ransom faces real dangers from enormous waves, violent storms, exhaustion from swimming, and the unstable footing on floating islands.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Ransom appears to be the sole human on Perelandra. He fears the world may be completely uninhabited. Living in space remains an utterly singular experience limited to one person.",
        "q8": "No political order / ungoverned",
        "q8_justification": "Perelandra appears to have no inhabitants and therefore no political order. Ransom is alone on a floating island in a vast ocean with no sign of governance or organized society.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter is devoted to Ransom's exploration of the alien ocean world, discovering floating islands, tasting alien fruit, experiencing storms, and learning to navigate the undulating terrain. It is pure exploration narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military element whatsoever. Ransom is a lone civilian explorer experiencing an alien world for the first time, with no weapons, orders, or military context.",
        "q11": "Like the ocean / naval",
        "q11_justification": "Perelandra is dominated by a vast ocean with floating islands. Ransom swims, rides waves, and must learn sea-legs on the undulating islands. The entire environment is oceanic, making the naval analogy the most fitting characterization.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Perelandra is a world of floating islands on a global ocean with no solid land visible, a gold-colored sky instead of blue, perpetual warm dimness instead of bright sunlight, total blackness at night with no moon or stars, and alien vegetation. Ransom must learn to walk on constantly shifting surfaces."
    },
    {
        "chapter": "Chapter Four",
        "q1": "No contestation",
        "q1_justification": "There is no conflict in this chapter. Ransom peacefully explores the floating island, befriends a dragon-like creature, discovers bubble trees, eats food, and spots the Green Lady from a distance. All interactions are benign.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom remains a temporary visitor on floating islands with no settlement or infrastructure. The Green Lady also appears to live a nomadic existence on the floating islands with no permanent habitation.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "Ransom is now on Venus, meaningfully separated from Earth with no way to return independently. The distance creates a profound separation, though the transit itself was not consciously experienced.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Green Lady lives among animals as a kind of queen or goddess figure, surrounded by birds, fish, and dragons that attend her in ceremonial formations. This is utterly unlike any Earth social structure.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Ransom speaks to the dragon in Old Solar, the ancient common language of the solar system. When he spots the Green Lady, he recognizes the need to communicate in this alien tongue rather than English.",
        "q6": "Manageable but risky",
        "q6_justification": "The floating islands provide food, water, and warmth, but the constantly shifting terrain makes walking difficult and the rising seas create real physical danger. Ransom struggles with exhaustion swimming between islands in the dark.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom and the Green Lady appear to exist on Perelandra (along with animals). Human presence in space is limited to a single visitor from Earth encountering what may be the sole humanoid inhabitant of Venus.",
        "q8": "No political order / ungoverned",
        "q8_justification": "The Green Lady mentions a King but he is absent and there are only two humanoid beings on the entire planet. There is no governance structure, no laws enforced by institutions, and no political organization.",
        "q9": "Adventure / exploration",
        "q9_justification": "Ransom explores the island, discovers new creatures and plants, and has his first distant encounter with the Green Lady. The chapter is driven by discovery, wonder, and the excitement of first contact.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military presence or framing. The chapter concerns peaceful exploration, interaction with wildlife, and a distant first sighting of another being. Everything is civilian in nature.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The floating islands are described like yachts in harbour, rising and falling with waves. Ransom swims desperately between islands, and the entire landscape is shaped by oceanic forces. The naval/maritime metaphor dominates.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The floating islands constantly shift shape, making walking extremely difficult. The golden sky, alien vegetation, bubble trees, and dragon-like creatures are all fundamentally different from Earth. Night is absolute blackness with no moon or stars."
    },
    {
        "chapter": "Chapter Five",
        "q1": "No contestation",
        "q1_justification": "This chapter consists entirely of philosophical and theological conversation between Ransom and the Green Lady. There is no conflict, competition, or contestation of any kind. The discussion concerns free will, obedience, and the nature of good.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom remains a temporary visitor. The Green Lady lives nomadically on floating islands with no fixed settlement. When asked about home, she gestures to the entire landscape, indicating no permanent territorial claim.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "Ransom is on Venus, separated from Earth with no independent means of return. The Green Lady has never seen Earth. The distance creates meaningful separation between worlds.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Green Lady has no concept of home, death, loneliness, or fixed community. She and the King are the only two of their kind. She does not understand concepts like brothers, sisters, or kindred. Her entire worldview is alien to Earth norms.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Ransom communicates with the Lady in Old Solar, the ancient common tongue of the solar system. She does not know English. The language is shared across worlds but is distinct from any Earth language.",
        "q6": "Benign / easily survivable",
        "q6_justification": "In this chapter the environment is calm and pleasant. The islands float together peacefully, food is available, the climate is warm, and there are no threats. The Lady and Ransom converse comfortably with animals around them.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom and the Green Lady exist on Perelandra as rational beings (the King is somewhere else). The Lady is astonished to learn that Earth has millions of people, confirming that population in this world is minimal.",
        "q8": "No political order / ungoverned",
        "q8_justification": "The Lady and the absent King are the only two rational beings on the planet. When asked about governance, the Lady says the King is the only other person. There is no political structure beyond this primal pair.",
        "q9": "Adventure / exploration",
        "q9_justification": "While this chapter is more philosophical than action-oriented, it remains within the adventure/exploration genre as Ransom discovers the nature of Perelandrian society and theology through his first sustained dialogue with its sole inhabitant.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter is a theological and philosophical conversation between two individuals. There is no military presence, language, or framing of any kind.",
        "q11": "Other / Unsure",
        "q11_justification": "Space is characterized primarily as Deep Heaven, a theological/spiritual realm. The Lady describes planets as little lumps of the low swimming in the high. This is a unique metaphysical characterization unlike any military domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Green Lady is green-skinned and has no concept of death, fixed habitation, or family structure as Earth knows it. The floating island world has no solid ground, no moon, no stars visible through the golden sky. The physical and conceptual environment is fundamentally different from Earth."
    },
    {
        "chapter": "Chapter Six",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The arrival of Weston's spaceship introduces the threat of conflict. Ransom recognizes Weston as dangerous, having witnessed him murder a Malacandrian. Ransom tries to prevent Weston from meeting the Lady, but no actual violence occurs yet.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom visits the Fixed Land temporarily with the Lady, who is forbidden from sleeping there. Weston arrives from Earth in a spaceship. All presence on Perelandra remains temporary with no settlements or territorial holding.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "Weston has traveled from Earth to Venus in a spaceship, confirming interplanetary travel is possible but extraordinary. Both Ransom and Weston are meaningfully separated from Earth with limited ability to return.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Lady's world has a divine law forbidding sleeping on Fixed Land, a concept utterly foreign to Earth. She is horrified to learn humans live on fixed land. Her entire social framework is based on divine commands from Maleldil, radically unlike any Earth culture.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Ransom and the Lady communicate in Old Solar throughout. When Weston arrives, he speaks English to Ransom, creating a multilingual situation. The distinct space language (Old Solar) remains the primary medium for interplanetary communication.",
        "q6": "Manageable but risky",
        "q6_justification": "The Fixed Land is hospitable with streams, turf, and climbable terrain. However, the rising seas threaten to cut off their return, the Lady must leave before nightfall due to divine law, and Weston's arrival introduces human danger.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom and now Weston have traveled to Venus from Earth. The total rational population of Perelandra is the Lady, the absent King, and these two Earth visitors. Space habitation remains exceedingly rare.",
        "q8": "No political order / ungoverned",
        "q8_justification": "The Lady declares herself Lady and Mother of the world but there is no governmental apparatus. The only authority is divine command from Maleldil. No eldila govern this new world, and there are no political institutions.",
        "q9": "Adventure / exploration",
        "q9_justification": "Ransom and the Lady explore the Fixed Land, climbing mountains and surveying the ocean. The chapter builds tension with the arrival of Weston's spaceship and the race to intercept him, combining exploration with emerging conflict.",
        "q10": "Entirely civilian",
        "q10_justification": "Despite the emerging threat from Weston, there is no military apparatus. Ransom is a scholar who laments his lack of combat skills. The Lady is a civilian. Even Weston arrives as a scientist, not a soldier.",
        "q11": "Like the ocean / naval",
        "q11_justification": "The chapter features riding giant fish across the sea to reach the Fixed Land, watching floating islands from a mountaintop, and the arrival of Weston in a small boat. The oceanic environment and maritime activities dominate the chapter.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Fixed Land features enormous green rock pillars rising to mountain heights, alien turf with piebald creatures, and a landscape surrounded by floating islands on a golden ocean beneath a golden sky. The environment is profoundly unlike Earth despite some superficial resemblances."
    }
]

country = 'France'
book_title = 'Voyage To Venus'
csv_path = 'data/results/France_Voyage_To_Venus.csv'

with open('data/questions.json', 'r', encoding='utf-8-sig', errors='replace') as f:
    questions = json.load(f)

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
