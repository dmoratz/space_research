import json, csv, os

# Corrected chapter data based on actual extracted text from .docx files
fixes = {
    "Book 2 - Chapter 16": {
        "q1": "No contestation",
        "q1_justification": "Servadac, Timascheff, and Procope meet cooperatively to discuss survival. Despite a secret personal rivalry between Servadac and Timascheff, they scrupulously conceal it and apply their best energies to the universal crisis. Ben Zoof contributes cheerfully.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "The 23 residents of the volcano face imminent loss of their settlement. The ships Dobryna and Hansa are destroyed when the ice pedestal collapses, and the comet itself violently splits in two, severing Ceuta and Gibraltar with the English garrisons into a separate fragment launched into space.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "Servadac states they have 51 days until the predicted recurrence of collision with Earth. The comet traveled 50 million leagues during the month and is now 78 million leagues from the sun, still meaningfully separated from Earth.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "The council proceeds with Earth-style formality: Timascheff invokes Providence, Servadac quotes the proverb about Heaven helping those who help themselves, and Procope delivers a systematic scientific briefing. Ben Zoof provides comic relief in his usual Montmartre manner.",
        "q5": "Same languages as Earth",
        "q5_justification": "All discussion between the French captain, Russian count, and their companions takes place in standard European languages. No space-specific vocabulary or translation technology is mentioned.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "Lieutenant Procope systematically describes how every collision scenario leads to death: crushed by direct impact, suffocated on a 450-mile mountain without atmosphere, roasted alive as velocity converts to millions of degrees of heat, or drowned in the Atlantic. The balloon is their only desperate hope.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only 23 people reside in the volcano, and the balloon must carry all of them. After the comet splits, 13 Englishmen are carried away on the severed fragment, leaving only this tiny community on Gallia.",
        "q8": "Single unified authority",
        "q8_justification": "Servadac presides as de facto leader, Procope proposes the balloon plan, and Timascheff pledges cooperation. The English have excluded themselves by refusing to leave their posts. Servadac later threatens Hakkabut with irons to maintain order.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Procope's chilling enumeration of lethal collision scenarios dominates the chapter: being crushed to atoms, suffocated, burnt alive at millions of degrees, or drowned. The desperate balloon plan and the violent splitting of the comet intensify the survival drama.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Military officers Servadac and Procope lead the discussion, but the plan is a civilian evacuation. Construction of the montgolfier involves all hands including Russians, Spaniards, and even little Nina sewing the casing.",
        "q11": "Like the air / airpower",
        "q11_justification": "The central solution is explicitly aerial: Procope proposes a montgolfier hot-air balloon made from the Dobryna's sails, using heated air for an hour's journey between atmospheres. The concept of launching from one atmosphere into another defines the chapter's approach to space.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The combined velocity of 21,000 miles per hour, the risk of heat generation in the millions of degrees upon impact, the possibility of being stranded 450 miles above Earth's surface, and the violent splitting of the comet demonstrate fundamentally non-Earth-like physical conditions.",
    },
    "Book 2 - Chapter 17": {
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The personal rivalry between Servadac and Timascheff resurfaces as they near Earth, driven by their old competition over Madame de L. Servadac stages a fierce argument with Rosette to trick him into revealing the collision time. Hakkabut is threatened with being left behind if he complains.",
        "q2": "Limited settlement (small colonies, hard to sustain/control)",
        "q2_justification": "The comet violently splits, its rotation period halves, and muscular power increases while gravity diminishes. The ships are already destroyed. The remaining 23 settlers must rely entirely on the untested balloon to evacuate before collision.",
        "q3": "Moderate journey (months/meaningful separation)",
        "q3_justification": "Thirteen days remain until the collision on January 1st at 2:42:35.6 AM. The comet is within 4 million miles of Earth, closing at 208,000 miles per hour. The journey is nearly over but the transit itself is extremely dangerous.",
        "q4": "Mostly Earth-like with minor adaptations",
        "q4_justification": "Christmas is celebrated solemnly, Servadac obsesses over finishing his rondo, Hakkabut frets over his 66 pounds of money, and the old romantic rivalry resurfaces. Earth social customs and personal concerns persist intact on the comet.",
        "q5": "Same languages as Earth",
        "q5_justification": "Servadac's staged argument with Rosette is conducted entirely in French, with the professor revealing the precise collision time in standard notation. All communication uses Earth languages throughout.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The comet splits apart with violent volcanic convulsions, shattering Rosette's telescope. The colony's survival depends entirely on the untested montgolfier balloon, and Procope warns that the slightest check in their progress will result in instantaneous combustion.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "After the split, 13 Englishmen are carried away on the severed fragment into unknown space. Only 23 people remain on the main comet, all of whom must fit in the balloon car for evacuation.",
        "q8": "Single unified authority",
        "q8_justification": "Servadac exercises authority as Governor-General, claiming ownership of Gallia in his staged argument. He organizes the balloon preparations, threatens Hakkabut with irons, and orders sailors to physically carry Rosette into the car against his will.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter features the clever trick to extract the collision time, the dramatic comet splitting, Christmas preparations, Hakkabut forced to abandon his money belt, Rosette bodily carried into the car, and the climactic balloon launch as Servadac insists on being the last to leave.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "Servadac uses military authority to command the operation, but the endeavor itself is a civilian evacuation: constructing a hot-air balloon from ship sails, inflating it with hay, and launching with all 23 community members including women, children, and a carrier pigeon.",
        "q11": "Like the air / airpower",
        "q11_justification": "The montgolfier balloon dominates the chapter: its construction from the Dobryna's sails, the network from rigging, the wicker car from the Hansa, inflation with hay combustion, and the dramatic launch from masts erected on the shore. Air travel is the defining concept.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The comet's rotation period halves to six-hour days after splitting, gravity diminishes noticeably, the comet travels at nearly 138,000 miles per hour while Earth approaches at 70,000, and volcanic convulsions shake the mountain. Physical conditions are in dangerous flux.",
    },
    "Book 2 - Chapter 18": {
        "q1": "No contestation",
        "q1_justification": "All passengers cooperate during the balloon transit. The only minor frictions are personal: Hakkabut reluctantly discards his money belt and Rosette gazes mournfully at his abandoned comet. Everyone else works together in silent, tense expectation.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The colonists are in pure transit in a balloon between the comet and Earth, lasting less than an hour. Their presence in space is entirely temporary, and by the chapter's end they have been deposited back on terrestrial soil.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The balloon ascent begins with Earth already within half its average moon distance. At 70 miles per second, the distance closes from 72,000 miles to zero in approximately 5 minutes. The transit is measured in minutes, not hours.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The passengers shout the names of European countries as they recognize them. Ben Zoof claims to see Montmartre. Servadac sends a message via carrier pigeon. Their entire frame of reference is Earth-based, with no space-adapted culture evident.",
        "q5": "Same languages as Earth",
        "q5_justification": "Procope, the count, and Servadac shout 'Europe! Russia! France!' in their native languages. Ben Zoof exclaims about Montmartre. All communication is in standard Earth languages.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The passengers face death from atmospheric fusion as the two atmospheres amalgamate with dense clouds, violent vibrations, and flashes of lurid flame. The montgolfier is elongated to its utmost stretch and sucked into a vortex. Everyone loses consciousness during the transfer.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Twenty-three people suspended in a balloon between a comet and Earth at 70 miles per second represent an utterly unique and unrepeatable human presence in space.",
        "q8": "Single unified authority",
        "q8_justification": "Lieutenant Procope manages the technical details and announces the countdown, while Servadac commands from the car, having insisted on being the last to board. The unified command structure persists through the final moments.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter is pure suspense: Procope counts down minutes to collision, Earth's disc swells like a vast funnel, the balloon elongates and is sucked into a vortex, clouds and lurid flame engulf them, and everyone loses consciousness. The outcome is uncertain until the final sentence.",
        "q10": "Entirely civilian",
        "q10_justification": "The balloon escape is a purely civilian operation focused on saving all 23 passengers. There is no military dimension to the transit; even the military officers act in civilian survival roles.",
        "q11": "Like the air / airpower",
        "q11_justification": "The entire chapter takes place in a montgolfier balloon at 2,500 yards altitude, with a wire-work stove maintaining air temperature. The aeronauts navigate between two atmospheres, and altitude, buoyancy, and air pressure are central concerns throughout.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Traveling at 70 miles per second, the passengers watch Earth's disc expand from a distant sphere to a vast funnel. The two atmospheres amalgamate violently with clouds, flame, and vortex forces. The physical transfer renders everyone unconscious, and the balloon is completely destroyed.",
    },
    "Book 2 - Chapter 19": {
        "q1": "No contestation",
        "q1_justification": "The return to Earth is entirely peaceful. Servadac and Timascheff discover Madame de L has married someone else, resolving their old rivalry. They shake hands and become sincere, confiding friends. The community disperses amicably.",
        "q2": "Cannot inhabit or hold territory",
        "q2_justification": "Everyone is back on Earth. The comet has passed on into space far away with no human presence, except possibly the 13 Englishmen on the severed fragment whose fate remains unknown. Space is no longer inhabited or held.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The chapter opens with everyone already back on Earth near Mostaganem, scarcely more than a mile from the town. The comet merely grazed the earth and continued on, depositing them at their exact point of departure.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Earth society continued completely unchanged during their absence. The population is perfectly calm, cattle graze, the sun rises normally, and no one noticed anything unusual. The Gallians immediately reintegrate into their old Earth lives.",
        "q5": "Same languages as Earth",
        "q5_justification": "Servadac immediately converses with his old friends at the Mascara gate in French. The colonel greets him familiarly. All communication is in standard Earth languages with no trace of any space-related language change.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The chapter takes place on a perfectly normal January morning in Algeria with dew on the pastures, cattle browsing quietly, and the sun rising in the east. Conditions are entirely benign and Earth-normal.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The comet experience was so singular that no one on Earth believes it. Rosette publishes his treatise but is ridiculed by astronomers. Servadac and Timascheff maintain rigid silence about their incredible experiences.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "National identities persist unchanged: the Dobryna's crew returns to Russia, the Spaniards are sent to their native shores, and Rosette insists 13 Englishmen remain on a fragment of Gibraltar traversing space. Earth nations extend their identity beyond the planet.",
        "q9": "Adventure / exploration",
        "q9_justification": "The chapter provides a classic adventure epilogue: heroes return home, old conflicts are resolved, children grow up and marry (Pablo weds Nina), and the mystery of the comet remains unsolved. Ben Zoof asks if it really happened at all.",
        "q10": "Entirely civilian",
        "q10_justification": "The return to Earth is entirely peaceful and civilian. The community disperses, Pablo and Nina are adopted and educated, Servadac eventually becomes a colonel through normal career progression, and life resumes its ordinary civilian course.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The epilogue mirrors the return from a frontier expedition: explorers come home to find civilization unchanged, try to reintegrate into normal life, and struggle to convince others of their experiences. Rosette's published treatise parallels an explorer's disputed account.",
        "q12": "Almost Earth-like",
        "q12_justification": "The chapter takes place entirely on Earth after the return. The physical environment is perfectly normal: an ordinary January morning in Algeria with dew, cattle, and sunrise. No trace of the comet's alien physics remains.",
    },
}

csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'France_Off_on_a_Comet.csv')
questions_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'questions.json')

with open(questions_path, 'r', encoding='utf-8-sig', errors='replace') as f:
    questions = json.load(f)

# Validate all answers against valid options
for chapter, fix in fixes.items():
    for q in questions:
        n = q['number']
        key = f'q{n}'
        answer = fix[key]
        if answer not in q['answer_options']:
            print(f"WARNING: {chapter} {key} answer '{answer}' not in valid options: {q['answer_options']}")

# Read existing CSV
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Update rows
fixed_count = 0
for row in rows:
    if row['chapter'] in fixes:
        fix = fixes[row['chapter']]
        for q in questions:
            n = q['number']
            row['q' + str(n)] = fix['q' + str(n)]
            row['q' + str(n) + '_justification'] = fix['q' + str(n) + '_justification']
        print('Fixed: ' + row['chapter'])
        fixed_count += 1

if fixed_count != 4:
    print(f'WARNING: Expected to fix 4 rows but fixed {fixed_count}')

# Write back
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f'Done fixing {fixed_count} rows.')
