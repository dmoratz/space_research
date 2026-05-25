import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter Seven",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Weston threatens Ransom with a revolver and there is tension between them, but no large-scale conflict. The contestation is interpersonal rather than strategic, with Weston claiming philosophical authority while Ransom opposes his ideology.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom and Weston are temporary visitors to Perelandra. Weston sets up a small camp with a primus-stove and tent, but there is no permanent settlement. The Lady and King are the only inhabitants of the world.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Weston travelled more than thirty million miles of space to reach Venus. Ransom is completely cut off from Earth with no way to return on his own, and his previous journey to Malacandra caused a serious breakdown in health during the return.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Perelandra has a fundamentally different social order with only two inhabitants (the Lady and King), no concept of evil or disobedience, no clothing, and a world of floating islands where the Fixed Land is forbidden. The Lady has no understanding of concepts like lying, fear, or death.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Characters communicate in Old Solar, a distinct interplanetary language. Weston has mysteriously acquired fluency in it, and Ransom notes this as surprising since Weston previously had only a smattering of it on Malacandra.",
        "q6": "Manageable but risky",
        "q6_justification": "The Fixed Land lacks the abundant fruit of the floating islands, making Ransom hungry and thirsty. The environment is survivable but less hospitable than the floating islands, and Ransom sleeps uncomfortably on solid ground compared to the soft surfaces he is accustomed to.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom and Weston have traveled to Perelandra from Earth. The Lady and King are the sole native inhabitants of the entire world. Living in space or on other planets is extraordinarily rare.",
        "q8": "No political order / ungoverned",
        "q8_justification": "There is no political structure on Perelandra. The Lady and King are the only inhabitants, governed only by Maleldil's commands. There are no nations, governments, or political entities in space.",
        "q9": "Drama",
        "q9_justification": "The chapter is dominated by intense philosophical and theological debate between Ransom and Weston about the nature of Spirit, God, and the Devil. The dramatic tension builds as Weston descends into possession, culminating in his terrifying seizure.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military presence or framework. Weston is a scientist and Ransom a philologist. Weston's revolver is a personal weapon, not a military one. The conflict is philosophical and spiritual rather than military.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Space travel to Venus resembles frontier exploration and colonial expansion. Weston explicitly discusses interplanetary colonization, and the narrative echoes themes of encountering new worlds and indigenous peoples, with Weston referring to the Lady as a native.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Perelandra's environment is fundamentally different from Earth with floating islands on a golden sea, no fixed land permitted for habitation, perpetual warmth requiring no clothing, and alien flora and fauna. The night is seamless and undimensioned darkness."
    },
    {
        "chapter": "Chapter Eight",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter reveals an ongoing spiritual and ideological contest. Weston (now the Un-man) engages the Lady in a sustained temptation dialogue about disobeying Maleldil's command, while Ransom recognizes this as a direct threat requiring opposition.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom continues as a temporary visitor, riding a fish between islands. The floating islands are transient and cannot be permanently held. There is no infrastructure or permanent settlement.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom reflects on being completely separated from Earth, feeling homesickness for the floating islands even during a brief absence. The cord of longing he feels seems to stretch back before his birth, emphasizing the vast distance from his home world.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Lady has no concept of stories or fiction, no understanding of multi-person conversation, and no knowledge of dwelling permanently in one place. Her social framework is entirely alien to Earth norms, with complete innocence and direct communion with Maleldil.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The conversation between Weston's body and the Lady takes place in Old Solar, a distinct interplanetary language. Ransom recognizes the voice as Weston's but notes it sounds curiously unlike itself.",
        "q6": "Manageable but risky",
        "q6_justification": "Ransom finds food on the Fixed Island (bilberries and oval nuts) but the flavour is austere compared to floating island fruit. He travels across open sea on a fish at night, which is risky but manageable. The environment sustains life but requires effort.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom and Weston are present from Earth. Ransom counts twenty-three floating islands but the only inhabitants are the Lady and the absent King. Space habitation remains extraordinarily rare.",
        "q8": "No political order / ungoverned",
        "q8_justification": "There is no political structure. The Lady and King answer only to Maleldil. The Un-man's temptation introduces the concept of independence from divine authority, but no political order exists.",
        "q9": "Drama",
        "q9_justification": "The chapter is intensely dramatic, centering on the Un-man's subtle temptation of the Lady to disobey Maleldil's command about the Fixed Land. Ransom listens in horror as the dialogue unfolds, feeling both terror and a sense of cosmic stakes.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter involves civilian characters engaged in philosophical and theological dialogue. There is no military presence, weapons, or military framework of any kind.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The narrative continues to echo frontier exploration themes. Ransom rides a fish across unknown seas to reach new islands, discovering phosphorescent sea creatures and mermaid-like beings, evoking the wonder of encountering an unexplored world.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The environment features floating islands, phosphorescent sea creatures, mermaid-like beings, giant rideable fish, and a night sky without visible heavens. Ransom's earth-trained walking habits fail on the heaving island surfaces."
    },
    {
        "chapter": "Chapter Nine",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter depicts an escalating spiritual battle. The Un-man systematically tempts the Lady to disobey Maleldil, while Ransom desperately tries to counter its arguments. The Un-man also engages in gratuitous cruelty, mutilating frogs, representing a deeper evil conflict.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "All human characters remain temporary visitors. The Lady and King live nomadically on floating islands. The Un-man's temptation to settle on Fixed Land is precisely the forbidden act, underscoring that permanent territory-holding does not exist.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom remains completely separated from Earth with no prospect of return. The Un-man references the deep gulf between worlds, claiming to have journeyed through Deep Heaven to reach Perelandra.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Lady has no concept of badness, lying, or evil. She cannot understand multi-person conversation and has never seen death or suffering. Her innocence is so complete that the Un-man must slowly construct concepts like disobedience from scratch.",
        "q5": "Distinct space language(s)",
        "q5_justification": "All dialogue occurs in Old Solar. The Lady, Ransom, and the Un-man all communicate in this interplanetary language. Ransom struggles to find words for concepts like bad or enemy that have no equivalent in her vocabulary.",
        "q6": "Manageable but risky",
        "q6_justification": "The environment remains survivable with abundant fruit and mild climate, but the discovery of mutilated frogs introduces a new element of danger. The floating islands pitch dramatically in heavy weather, and Ransom faints upon seeing the Un-man's true nature.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only three beings interact: Ransom, the Un-man in Weston's body, and the Lady. The King is absent somewhere on another floating island. Space habitation is limited to these few individuals.",
        "q8": "No political order / ungoverned",
        "q8_justification": "No political structure exists. The Un-man's temptation aims to introduce independence from divine authority, but the current state is one of direct divine governance with no political institutions.",
        "q9": "Drama",
        "q9_justification": "The chapter is deeply dramatic, featuring the horrifying discovery of mutilated frogs, Ransom's terrifying encounter with the Un-man's true nature that causes him to faint, and the intense three-way theological debate about obedience and disobedience.",
        "q10": "Entirely civilian",
        "q10_justification": "The conflict is entirely spiritual and philosophical. There are no military elements, weapons, or military organization. The struggle is between good and evil on a theological plane.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The temptation narrative parallels colonial themes of encountering indigenous peoples and the tension between preserving innocence and introducing civilization. The Un-man acts as a corrupting colonial influence on the Lady's pristine world.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The floating islands climb enormous hills of water, the weather shifts dramatically, and the Un-man's possessed body moves in ways that are subtly inhuman. Ransom had never seen anything dead or spoiled in Perelandra before the mutilated frogs."
    },
    {
        "chapter": "Chapter Ten",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The chapter depicts a sustained, multi-day strategic struggle between the Un-man and Ransom for the Lady's soul. The Un-man uses relentless psychological warfare, telling stories and teaching vanity, while Ransom fights desperately to counter each move.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The characters continue as temporary visitors on floating islands that constantly move. The Un-man tempts the Lady with the concept of keeping possessions and settling on Fixed Land, but this remains forbidden and unrealized.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom remains totally cut off from Earth. The separation is so complete that Earth customs like clothing and mirrors must be explained as foreign concepts to the Lady.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Lady has no concept of keeping possessions, wearing clothes for beauty, seeing her own reflection, or self-admiration. The Un-man must teach her concepts like vanity and fear from scratch, and she experiences fear for the first time when seeing her reflection.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Communication continues in Old Solar. The Un-man teaches the Lady new words like Creative, Intuition, and Spiritual, which have no native equivalents in her language, highlighting the linguistic distinctness of Perelandra.",
        "q6": "Manageable but risky",
        "q6_justification": "The physical environment remains survivable with fruit and water available. However, the psychological and spiritual dangers intensify enormously. Rain and storms occur but are not life-threatening.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Still only three characters interact on Perelandra. The King remains absent. The entire world has only two native inhabitants, making human presence in space exceptionally rare.",
        "q8": "No political order / ungoverned",
        "q8_justification": "No political order exists. The Un-man introduces concepts of keeping and ownership that could lead to governance, but currently there is only divine command and no political institutions.",
        "q9": "Drama",
        "q9_justification": "The chapter is intensely dramatic with the Un-man telling stories of heroic women, introducing the mirror and the concept of vanity, teaching the Lady about clothing and self-image, and slowly corrupting her innocence through theatrical self-consciousness.",
        "q10": "Entirely civilian",
        "q10_justification": "No military elements appear. The conflict is entirely psychological, spiritual, and philosophical. The Un-man uses stories, a mirror, and feathered robes as its weapons of temptation.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Un-man's introduction of mirrors, clothing, and Earth customs to the Lady parallels colonial contact narratives where indigenous peoples are introduced to foreign goods and values, gradually undermining their native way of life.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The floating islands continue to heave dramatically. The Lady experiences fear for the first time upon seeing her reflection. The environment requires no clothing, has no concept of possessions, and operates under fundamentally different physical and social laws."
    },
    {
        "chapter": "Chapter Eleven",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The spiritual and physical stakes reach their peak. Ransom realizes he must physically fight the Un-man to stop the temptation. The entire chapter is devoted to his agonizing internal struggle over whether to engage in mortal combat with the possessed body.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom remains a temporary visitor sent to Perelandra for a specific mission. The chapter emphasizes his role as a transient agent, not a settler, who was brought to this world to intervene at a critical moment.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom reflects on men fighting on Earth in wartime, underscoring his complete separation from his home world. His journey to Perelandra is described as a miracle comparable to the Un-man's arrival, crossing vast interplanetary distance.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Perelandra's social reality is so different that the distinction between truth and myth, fact and fiction, does not apply there. The Lady sleeps nearby in a state that is itself unlike Earth sleep, showing expression and readiness even in repose.",
        "q5": "Distinct space language(s)",
        "q5_justification": "Old Solar remains the medium of communication. The chapter does not focus on language but the distinct interplanetary language continues to be the mode of interaction between Ransom and the Perelandrian beings.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "While the natural environment remains physically survivable, the spiritual and psychological conditions become extremely harsh. Ransom faces sleep deprivation, exhaustion, and the prospect of fighting to the death with no weapons against a tireless supernatural enemy.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Ransom is still essentially alone as a human on Perelandra, with only the Un-man in Weston's body as another Earth-origin being. The chapter emphasizes how everything depends on this one individual's actions.",
        "q8": "No political order / ungoverned",
        "q8_justification": "No political order exists. The chapter focuses on cosmic spiritual governance by Maleldil rather than any political structure. The fate of the world depends on individual moral choices, not political institutions.",
        "q9": "Drama",
        "q9_justification": "The chapter is pure psychological and spiritual drama as Ransom wrestles with the knowledge that he must physically fight the Un-man. The Voice in the darkness presses him toward this realization with inexorable force.",
        "q10": "Entirely civilian",
        "q10_justification": "Ransom explicitly describes himself as a sedentary scholar, not a military man. His coming fight is framed not as military action but as a desperate civilian act of self-sacrifice against supernatural evil.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter evokes frontier themes with Ransom as a lone individual facing an impossible challenge in an alien wilderness, responsible for the fate of an entire world. The parallel to Eden frames Perelandra as a new frontier of creation.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The chapter emphasizes how Perelandra operates under different metaphysical laws where the distinction between myth and fact dissolves. The physical reality is intertwined with spiritual reality in ways that do not occur on Earth."
    },
    {
        "chapter": "Chapter Twelve",
        "q1": "Total war / constant conflict",
        "q1_justification": "The chapter is dominated by an extended, brutal physical fight between Ransom and the Un-man, followed by a desperate chase across the island and out to sea. The conflict is total and unrelenting, with both combatants severely wounded.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Ransom remains a temporary visitor. He reflects that he has lived in Paradise but will never return. The floating islands and the sea are transient environments with no permanent human presence or territory.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Ransom is completely cut off from Earth, reflecting he will never again wield an unmaimed body until a greater morning comes. He is alone on the high seas of an alien world with no prospect of return visible.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Maleldil has cast the entire island into a charmed sleep so no memory of violence will remain. The world operates under divine intervention that has no parallel on Earth, with animals and the Lady sleeping supernaturally.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The Un-man speaks English to Ransom during their confrontation, but also utters Aramaic from the First Century. The coexistence of Earth languages and Old Solar on an alien world underscores the distinct linguistic landscape.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Ransom engages in a brutal, prolonged physical fight where his back is torn to shreds, he loses a tooth, and he is covered in blood. He then must pursue the Un-man across the island and out to open sea while severely wounded and dehydrated.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ransom and the Un-man are active on Perelandra. The Lady and all animals are supernaturally asleep. Human presence in space remains limited to these few individuals from Earth.",
        "q8": "No political order / ungoverned",
        "q8_justification": "No political structure exists. The world is governed solely by Maleldil's direct intervention, who has put the entire island to sleep. There are no nations, institutions, or political entities.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is dominated by a violent physical fight, a desperate chase through sleeping forests, and a pursuit across open ocean. Ransom faces severe injuries, dehydration, and the constant threat of death in a survival scenario.",
        "q10": "Entirely civilian",
        "q10_justification": "Ransom is explicitly a middle-aged scholar fighting with fists and teeth, not a soldier. The combat is a desperate civilian act, not a military operation. He recalls boxing at preparatory school and quotes Anglo-Saxon poetry mid-fight.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter reads like a frontier survival narrative with Ransom pursuing his quarry through alien wilderness, past sleeping creatures, and out to sea on fish-back, evoking themes of individual struggle against nature in an unexplored world.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The entire island is supernaturally asleep. Ransom chases the Un-man through alien forests, across seas of copper-colored water, riding giant fish that follow instinctively. Long-necked birds join the pursuit in formation. The environment is fundamentally unlike anything on Earth."
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
