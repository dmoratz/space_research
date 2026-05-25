import json, csv, os

chapters_data = [
    {
        "chapter": "Part 7 Chapter 2",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Yukikaze discovers that dead men in the Systems Corps retraining unit are JAM duplicates. The SAF debates whether to attack the ghost unit or take a more measured approach.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Faery base is a permanent installation with full command infrastructure.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Events on Faery, accessed through the Passageway far from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The SAF's unique culture of human-computer partnership and its distinct approach to the JAM threat set it apart from Earth society.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "International military personnel communicate in shared language. Yukikaze communicates through display text.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "JAM infiltration makes the base environment dangerous. The ongoing war demands constant resource expenditure.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Faery base and the wider FAF have large numbers of personnel.",
        "q8": "Single unified authority",
        "q8_justification": "The FAF governs Faery as a single authority, though JAM infiltration threatens its integrity.",
        "q9": "Political / diplomatic",
        "q9_justification": "Strategic debate about how to handle the JAM duplicates in the retraining unit. The SAF weighs attacking versus gathering intelligence, balancing military action against diplomatic considerations.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are SAF military personnel in a command center discussing tactical options.",
        "q11": "Like the air / airpower",
        "q11_justification": "The SAF is an air force unit; its fighter AIs provide the intelligence driving the discussion.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Faery requires adaptation but supports human habitation at military bases.",
    },
    {
        "chapter": "Part 7 Chapter 3",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Deep philosophical debate about JAM nature, with discussions of quantum uncertainty and the impossibility of truly perceiving the enemy. Cooley reveals her personal motivation for fighting.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Faery base continues as a permanent military installation with full infrastructure.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Events on Faery, far from Earth through the Passageway.",
        "q4": "Distinct space culture",
        "q4_justification": "The discussion of JAM as quantum beings and Cooley's existential philosophy about declaring her existence to an incomprehensible alien enemy reflects a culture unique to Faery.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "International SAF personnel from various backgrounds engage in complex philosophical discussion in a shared language.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The imminent JAM threat and the need for constant vigilance make Faery a harsh environment.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Large FAF personnel presence on Faery across multiple bases.",
        "q8": "Single unified authority",
        "q8_justification": "The FAF remains the single governing authority on Faery.",
        "q9": "Drama",
        "q9_justification": "Deep character-driven chapter with philosophical debates about quantum theory, JAM nature, and Cooley's personal existential motivations. The quantum uncertainty discussion and Cooley's rage against being ignored by the JAM are deeply dramatic.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are military personnel: Booker, Foss, Pivot, Katsuragi, Eco, Rei, and General Cooley.",
        "q11": "Like the air / airpower",
        "q11_justification": "The SAF is an air force unit; discussions reference fighter operations and aerial combat.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Faery supports human habitation but has alien features requiring adaptation.",
    },
    {
        "chapter": "Part 7 Chapter 4",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Intensive strategic planning in the SAF command center. Rei proposes seizing Banshee III as a mobile base. Booker plans cyberwar against FAF computers. Cooley delegates strategy to Booker.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Faery base and Banshee III (a flying aircraft carrier) represent permanent military infrastructure. Multiple bases discussed across Faery.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Discussion of fleeing to Earth through the Passageway is rejected as impractical, emphasizing the separation. Katsuragi proposes flying through the Passageway to Australia.",
        "q4": "Distinct space culture",
        "q4_justification": "The SAF operates with a unique culture of human-machine partnership. Banshee III, a flying carrier built in space that has never landed, represents distinctly non-Earth technology and culture.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "International personnel discuss complex strategy. Rei, Booker, Foss, Katsuragi, Pivot, and Eco communicate seamlessly despite diverse origins.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The discussion of limited options for evacuation and the need for fuel and bases highlights how resource-intensive survival on Faery is.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Multiple bases, Banshee III with its crew, and the broader FAF all represent large populations on Faery.",
        "q8": "Single unified authority",
        "q8_justification": "The FAF governs Faery, though the SAF plans to act independently within that structure.",
        "q9": "Political / diplomatic",
        "q9_justification": "Strategic planning session where the SAF debates survival options: fleeing to Earth, seizing Banshee III, or waging cyberwar against FAF computers. The chapter is dominated by tactical and political considerations.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are military personnel planning combat operations and survival strategies.",
        "q11": "Like the air / airpower",
        "q11_justification": "Fighter operations, aerial bases (Banshee III flying carrier), and air combat strategy dominate the planning.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Faery has alien features but supports conventional flight and military operations.",
    },
    {
        "chapter": "Part 7 Chapter 5",
        "q1": "Total war / constant conflict",
        "q1_justification": "Colonel Rombert's coup begins. Burgadish shoots and kills Lieutenant Mayle. Rombert executes Burgadish. The ghost unit seizes Systems Corps, activates BAX-4 powered armor. Rombert escapes when the JAM make him invisible to the duplicates.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The action takes place within Faery base's underground complex, a permanent military installation.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Events on Faery, far from Earth. Rombert mentions his desire to go home to his fireless fireplace on Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The JAM duplicates, Rombert's ambition to control the JAM, and the ghost unit represent a war culture entirely alien to Earth norms.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Personnel from various backgrounds communicate in shared language during the coup.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Armed conflict within the base itself, with JAM duplicates, powered armor, and gunfire making survival precarious.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Large numbers of personnel serve at Faery base across multiple corps.",
        "q8": "Single unified authority",
        "q8_justification": "The FAF is the single authority, though Rombert's coup attempts to subvert it using the Intelligence Forces.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Murder, betrayal, and a violent coup unfold. Burgadish kills Mayle in cold blood. Rombert executes Burgadish. The ghost unit activates powered armor. Rombert escapes when the JAM make him invisible — a deeply unsettling scene.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are military personnel or JAM military duplicates engaged in armed conflict.",
        "q11": "Like the air / airpower",
        "q11_justification": "The broader context is an air force at war; the coup targets air base command infrastructure.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The underground base environment is Earth-like, but JAM presence and their ability to manipulate perception make it alien.",
    },
    {
        "chapter": "Part 7 Chapter 6",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Major General Linneberg negotiates with the SAF in the command center. Tense discussions about Rombert's role as potential JAM communicator. Katsuragi is transferred to Intelligence Forces. Strategic positioning between SAF and Intelligence Forces.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "SAF command center at Faery base, a permanent installation.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Events on Faery. Linneberg describes the 30-year war as something spanning generations, emphasizing the distance from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The FAF's institutional culture with its intelligence services, SAF autonomy, and computer consciousness represents a civilization distinct from Earth.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "International personnel including German-named Linneberg communicate in shared language with the SAF team.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The imminent JAM attack and internal FAF conflicts make Faery extremely dangerous.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Large FAF personnel presence. Linneberg describes the diversity of people serving on Faery.",
        "q8": "Single unified authority",
        "q8_justification": "The FAF governs Faery, with the Intelligence Forces operating as a semi-independent organ within it.",
        "q9": "Political / diplomatic",
        "q9_justification": "Intense negotiations between Linneberg and Cooley over intelligence cooperation, Rombert's status, and Katsuragi's transfer. Linneberg reveals the Intelligence Forces' long-term strategy of using Rombert as a JAM communicator.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are military: generals, majors, captains, and lieutenants in a command center.",
        "q11": "Like the air / airpower",
        "q11_justification": "The SAF is an air force unit. Discussions reference fighter operations and the FAF's air combat computer networks.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Faery supports human habitation but its alien war context requires constant adaptation.",
    },
    {
        "chapter": "Part 7 Chapter 7",
        "q1": "Total war / constant conflict",
        "q1_justification": "Full-scale war erupts. Cooley declares war on the JAM. All SAF fighters launch. Banshee III explodes. FAF planes attack each other due to JAM manipulation. Massive JAM offensive from all directions. Rei and Yukikaze sortie into the chaos.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Faery base is under attack but remains operational. Banshee III is destroyed. Multiple bases mentioned.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The battle takes place on Faery, completely cut off from Earth. No possibility of reinforcement or evacuation.",
        "q4": "Distinct space culture",
        "q4_justification": "The SAF's composite human-machine culture, Foss's discussion of love between Rei and Yukikaze, and the strategic computer's self-preservation instinct represent a radically distinct culture.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "International pilots communicate via radio. SAF computers communicate via text. Foss and Rei have a deeply personal conversation in shared language.",
        "q6": "Extremely hostile (constant survival pressure)",
        "q6_justification": "Total war across all of Faery. JAM attacking from every direction. FAF planes shooting each other. Banshee III destroyed. Survival is in doubt for everyone.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Thousands of FAF personnel across multiple bases are caught in the conflict.",
        "q8": "Single unified authority",
        "q8_justification": "The FAF is the single authority, though its computer systems are in chaos and its planes are attacking each other.",
        "q9": "Military / war",
        "q9_justification": "Full-scale aerial warfare with multiple fighter engagements, Banshee III's destruction, FAF fratricide, and a massive JAM offensive. The climactic battle of the novel.",
        "q10": "Entirely military / war-focused",
        "q10_justification": "All characters are military: pilots, commanders, generals, and maintenance crews in combat.",
        "q11": "Like the air / airpower",
        "q11_justification": "The entire chapter is aerial warfare: fighter launches, dogfights, a flying carrier's destruction, and air patrols. Yukikaze takes off for the final sortie.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Bloody Road glows on the alien horizon, Faery's twin suns rise, and the JAM manipulate FAF systems in ways impossible on Earth. The environment is fundamentally alien during this climactic battle.",
    },
]

country = 'Japan'
book_title = "good luck yukikaze"
csv_path = "data/results/Japan_good_luck_yukikaze.csv"
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

print('Done batch 4.')
