import json
import csv
import os

# Load questions
questions_path = os.path.join(os.path.dirname(__file__), '..', 'questions.json')
with open(questions_path, encoding='utf-8-sig', errors='replace') as f:
    questions = json.load(f)

country = "China"
book_title = "Vagabonds"
csv_path = os.path.join(os.path.dirname(__file__), 'China_Vagabonds.csv')

# Build fieldnames
fieldnames = ["country", "book", "chapter"]
for q in questions:
    fieldnames.append(f"q{q['number']}")
for q in questions:
    fieldnames.append(f"q{q['number']}_justification")

# Check existing chapters
existing_chapters = set()
if os.path.exists(csv_path) and os.path.getsize(csv_path) > 0:
    with open(csv_path, encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_chapters.add(row['chapter'])

# Chapter data for Part 2
chapters = [
    {
        "chapter": "Part 2 - Prologue",
        "answers": {
            "q1": "Other / Unsure",
            "q2": "Other / Unsure",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Other / Unsure",
            "q7": "Other / Unsure",
            "q8": "Other / Unsure",
            "q9": "Drama",
            "q10": "Other / Unsure",
            "q11": "Other / Unsure",
            "q12": "Other / Unsure",
        },
        "justifications": {
            "q1_justification": "Abstract philosophical dialogue with no specific conflict depicted; the chapter poses questions about freedom without showing any active contestation.",
            "q2_justification": "No habitation is depicted in this abstract prologue; the dialogue exists outside any concrete spatial setting.",
            "q3_justification": "The dialogue implies meaningful separation between worlds, suggesting a moderate journey distance between Earth and Mars.",
            "q4_justification": "Mars is described as 'a way of life' rather than a nation, marking it as a distinctly non-Earth cultural identity.",
            "q5_justification": "The dialogue proceeds without any language barriers; both speakers share the same tongue and rhetorical framework.",
            "q6_justification": "No environment is depicted in this abstract philosophical exchange.",
            "q7_justification": "No specifics about habitation frequency are provided in this abstract prologue.",
            "q8_justification": "No political order is directly depicted; the chapter is purely philosophical.",
            "q9_justification": "The chapter is philosophical and melancholic in tone, exploring abstract questions of freedom through spare, allusive dialogue.",
            "q10_justification": "No domain activity is depicted; the chapter is abstract dialogue with no operational context.",
            "q11_justification": "The abstract framing provides no analogy to any earthly domain.",
            "q12_justification": "No physical environment is described in this abstract prologue.",
        },
    },
    {
        "chapter": "Part 2 - Book",
        "answers": {
            "q1": "Moderate contestation (ongoing rivalry/disputes)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Drama",
            "q10": "Entirely civilian",
            "q11": "Like the frontier / colonial expansion",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "Luoying was told on Earth that her grandfather is a dictator; she wrestles with dual and contradictory perspectives on Mars, reflecting ongoing ideological rivalry between Earth and Mars narratives.",
            "q2_justification": "Mars City is described as humanity's greatest architectural achievement, built from iron, glass, and silicon, constituting a permanent, governable settlement.",
            "q3_justification": "Mars viewed from Earth is described as 'a cartoonish ball of dust,' implying a meaningful distance and separation between the two worlds.",
            "q4_justification": "Martians are described as intimately connected to their sky; the city was built from Martian sand and founders created an entirely new civilization from the void, distinct from Earth's traditions.",
            "q5_justification": "No language barriers exist; Terrans and Martians use the same words but assign them different meanings, showing shared language with divergent conceptual frameworks.",
            "q6_justification": "The city is built from sand, iron, and glass and requires sustained engineering to sustain life; Martian sunsets are described as simple (white sun, dark sky, no clouds), conveying a resource-intensive built environment.",
            "q7_justification": "Mars has a full civilization with a Boule, an archon system, a Registry, and a Security System, indicating a large, established population.",
            "q8_justification": "Mars is governed by a Boule, a consul, nine systems, and three justices, constituting a single unified political authority.",
            "q9_justification": "The chapter is intellectual, philosophical, and meditative, richly allusive and focused on historiography and personal reflection rather than action.",
            "q10_justification": "The chapter is entirely devoted to historical and philosophical reflection with no military presence or activity.",
            "q11_justification": "Mars is framed as a civilization built from scratch in hostile territory, with a founding narrative that closely parallels frontier settlement and colonial expansion.",
            "q12_justification": "Martian sunsets are white with a dark sky (no atmospheric scattering), mountains exceed Earth's in grandeur, and the night sky is always present, marking constant physical difference from Earth.",
        },
    },
    {
        "chapter": "Part 2 - Crystal",
        "answers": {
            "q1": "Moderate contestation (ongoing rivalry/disputes)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Political / diplomatic",
            "q10": "Mostly civilian with some military presence",
            "q11": "Like the frontier / colonial expansion",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "Intense political debate divides the Boule between Climbers (migrate to a terraformed crater) and Waders (stay in the glass city), reflecting an ongoing internal rivalry over Mars's future.",
            "q2_justification": "The chapter debates expanding habitable territory from the enclosed city to an open crater, presupposing that Mars is already a permanent, governable settlement.",
            "q3_justification": "Ceres is repositioned into Mars orbit as a source of water, a feat of interplanetary engineering that underscores meaningful separation between celestial bodies.",
            "q4_justification": "Mars operates as a 'planned democracy' where the consul ensures process fairness and every proposal is publicly archived and debated, constituting a governance culture distinct from Earth's.",
            "q5_justification": "The chapter is an internal Martian political discussion conducted without translation or language barriers.",
            "q6_justification": "Maintaining an open atmosphere in a crater is described as 'a million times harder' than an enclosed city, and Mars's low escape velocity makes atmospheric retention inherently difficult.",
            "q7_justification": "A full civilization is depicted debating large-scale infrastructure expansion, indicating a substantial and established population.",
            "q8_justification": "The consul chooses voting formats and the Boule conducts legislative debate, indicating a single unified governing authority over Mars.",
            "q9_justification": "The chapter centers on a political debate about Mars's future direction, with Hans navigating legislative strategy and factional maneuvering.",
            "q10_justification": "Hans was a wartime pilot but now operates entirely in a civilian role; the chapter is primarily civilian political deliberation.",
            "q11_justification": "The terraforming debate is literally about expanding the frontier of habitable territory, mirroring colonial expansion logic.",
            "q12_justification": "The enclosed glass city functions as a fragile biosphere; temperatures outside fall far below freezing and rivers would freeze, marking constant physical challenge.",
        },
    },
    {
        "chapter": "Part 2 - Messages",
        "answers": {
            "q1": "Moderate contestation (ongoing rivalry/disputes)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Political / diplomatic",
            "q10": "Entirely civilian",
            "q11": "Like cyberspace / networked or abstract domain",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "The Mercury Group is politically split; Chania calls for revolution and Runge accuses the group of having been used as political hostages, reflecting ongoing internal contestation.",
            "q2_justification": "The hospital and Mars City infrastructure are operational, and the Maearth ship is heading back to Earth, confirming Mars as a permanent, governable settlement.",
            "q3_justification": "The Maearth is 80+ days from Earth, and Luoying struggles to explain Mars across a conceptual and spatial distance that is meaningfully separating.",
            "q4_justification": "Mars has no financial sector, no service industry, and no banking; stipends are distributed by age; ateliers compete for state budget; motivation comes from recognition rather than money, creating a radically distinct economic culture.",
            "q5_justification": "Luoying and Eko use the same words but Eko cannot understand non-monetary incentives, showing shared language but incompatible conceptual frameworks.",
            "q6_justification": "Ceres is visible overhead; the nightscape outside the glass is described as desolate; a recorded Earth thunderstorm is played as an alien novelty, underscoring the harshness of the Martian environment.",
            "q7_justification": "A full economic system with ateliers, budget allocations, and production schedules is in operation, indicating a large, functioning population.",
            "q8_justification": "The state allocates budgets to ateliers and manages unified economic planning, indicating a single centralized authority.",
            "q9_justification": "The chapter is structured as an epistolary political debate, with characters exchanging messages about revolutionary strategy and the nature of Martian society.",
            "q10_justification": "The chapter is entirely devoted to economic, political, and personal correspondence with no military activity.",
            "q11_justification": "The central archive serves as the communication medium across space, and messages traverse interplanetary distances as the primary mode of interaction, aligning with a networked or abstract domain.",
            "q12_justification": "Ceres is visible as a disk overhead, there are no moons, the exterior landscape is desolate, and rainfall is described as an alien sensation to Martians, marking stark physical difference from Earth.",
        },
    },
    {
        "chapter": "Part 2 - Medal",
        "answers": {
            "q1": "High contestation (frequent conflict or strategic struggle)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Nearly uninhabitable / lethal without major intervention",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Drama",
            "q10": "Mixed civilian-military domain",
            "q11": "Like the air / airpower",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "The origin of the interplanetary war is traced to a fatal corporate IP dispute; Richard Sloan's violent act sparked a rebellion, and Hans's suppression of protests reveals ongoing high-stakes strategic struggle.",
            "q2_justification": "Mars City, the Registry of Files, and historical surface bases all demonstrate permanent, governable settlement capable of holding territory.",
            "q3_justification": "The distance between Earth and Mars proved fatal when rescue ships could not launch in time due to a corporate IP dispute, underscoring meaningful physical separation.",
            "q4_justification": "The Registry preserves an equal file for every citizen regardless of rank; the founding rebellion was explicitly against corporate Earth, establishing a distinct cultural and political identity.",
            "q5_justification": "Historical accounts are shared between characters without any translation, indicating the same language is used across worlds.",
            "q6_justification": "A dust storm in a canyon killed Hanna when rescue was denied; atmospheric pressure is 1% of Earth's; aircraft need 6x airspeed for lift, making Mars nearly uninhabitable without major technical intervention.",
            "q7_justification": "Mars has a full military with squadrons, aircraft, and assigned fighters, indicating a substantial established population.",
            "q8_justification": "Mars operates as a republic with a centralized Registry governing records and rights for all citizens.",
            "q9_justification": "The chapter delivers a historical revelation about Luoying's family origins and the founding of the rebellion, rendered with emotional intensity.",
            "q10_justification": "Anka is a military pilot grounded by her commander; the Flight System assigns fighters; military authorization is required for flights, while civilian life continues alongside.",
            "q11_justification": "Detailed discussion of flight physics on Mars (atmospheric pressure 1% of Earth's) and the dominance of pilots, squadrons, and fighter craft aligns this domain with airpower.",
            "q12_justification": "Mars's atmosphere is 1% of Earth's; dust storms are lethal; aircraft require fundamentally different design to achieve lift, marking profound physical difference.",
        },
    },
    {
        "chapter": "Part 2 - Membrane",
        "answers": {
            "q1": "Low contestation (minor competition, little open conflict)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Drama",
            "q10": "Mostly civilian with some military presence",
            "q11": "Like the frontier / colonial expansion",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "Conflict is personal—Rudy's sabotage of Luoying's dance costume—with no political or military dimension; contestation is minor and interpersonal.",
            "q2_justification": "Glass houses are described as self-contained ecological units that produce energy, air, and water, constituting permanent and governable habitation.",
            "q3_justification": "Mercury Group members sustained injuries from trying to meet Earth performance standards, implying a meaningful separation between the physical demands of the two worlds.",
            "q4_justification": "The city began as a single dwelling that expanded by cellular division; membrane technology underlies the entire city's infrastructure, reflecting an entirely Martian architectural and cultural logic.",
            "q5_justification": "Chania's outburst about human limitations is delivered and understood without any translation or language barrier.",
            "q6_justification": "Glass houses must produce energy, regenerate air, circulate water, cultivate organisms, and break down waste—a constant, resource-intensive life-support burden.",
            "q7_justification": "A full residential and industrial infrastructure is described, indicating a large and established population.",
            "q8_justification": "The city was built from a single unified architectural vision and continues to operate as a unified system.",
            "q9_justification": "The chapter focuses on a personal confrontation about systemic pressure alongside an architectural-philosophical history of the city, both rendered in dramatic register.",
            "q10_justification": "Rudy appears in military uniform, but the chapter is otherwise entirely civilian in focus.",
            "q11_justification": "Space construction begins from zero using only local materials; buildings are described like plants adapted to niches, paralleling the logic of frontier colonial settlement.",
            "q12_justification": "Glass houses function as self-contained ecosystems with membrane technology and magnetic fields in walls, representing a built environment fundamentally unlike anything on Earth.",
        },
    },
    {
        "chapter": "Part 2 - Rock",
        "answers": {
            "q1": "Moderate contestation (ongoing rivalry/disputes)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Drama",
            "q10": "Mostly civilian with some military presence",
            "q11": "Like the frontier / colonial expansion",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "Reini was scapegoated to protect a project leader; the Mercury Group's satirical play makes a hostage accusation publicly; systemic injustice reflects ongoing institutional contestation.",
            "q2_justification": "The Creativity Fair, ateliers, and rehearsal spaces function within a fully operational Mars City, confirming permanent and governable settlement.",
            "q3_justification": "The Mercury Group's hostage timeline was tied to an Earth-Mars cargo shipment, indicating that interplanetary distance is a meaningful operational factor.",
            "q4_justification": "The Creativity Fair is the highest cultural institution on Mars; the punishment system prioritizes institutional credibility over individual justice, reflecting a distinctly Martian social logic.",
            "q5_justification": "The satirical play simultaneously targets both Mars and Earth systems, proceeding without any language barrier between the two worlds' cultures.",
            "q6_justification": "Mining machines based on insect biomimetics are described as essential for survival, indicating that resource extraction is a critical and technically demanding activity.",
            "q7_justification": "A full cultural and industrial infrastructure including the Creativity Fair and ateliers indicates a large, established population.",
            "q8_justification": "The accountability system requires punishment after every accident, enforced by a centralized authority that governs institutional behavior.",
            "q9_justification": "The chapter combines an intimate personal revelation (Reini's backstory) with theatrical satire at the Creativity Fair, rendered in a dramatic register.",
            "q10_justification": "Anka circumvents her military commander by using the Creativity Fair, indicating a civilian space that nonetheless intersects with military authority.",
            "q11_justification": "Mining is described as an essential frontier activity; survival depends on resource extraction from the Martian terrain, paralleling colonial frontier logic.",
            "q12_justification": "Biomimetic mining machines engineered specifically for Martian conditions represent a physical environment that demands constant technological adaptation unlike Earth.",
        },
    },
    {
        "chapter": "Part 2 - Ship",
        "answers": {
            "q1": "High contestation (frequent conflict or strategic struggle)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Adventure / exploration",
            "q10": "Mixed civilian-military domain",
            "q11": "Like the air / airpower",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "The group's unauthorized departure from the city, Juan's illegal surveillance system, and four warships visible on the Boule screen indicate high-stakes strategic contestation beneath the civilian surface.",
            "q2_justification": "Mars City with its gates requiring permits and old mining ships for surface travel constitutes a permanent, governable settlement capable of controlling movement and territory.",
            "q3_justification": "The group travels across the Martian surface in a mining ship while interplanetary tensions continue, indicating meaningful spatial and political separation from Earth.",
            "q4_justification": "The Creativity Fair motto 'To create is the highest of honors!' and mining ships as multi-day wilderness vehicles reflect a distinctly Martian cultural order.",
            "q5_justification": "The group's satirical play targets both worlds simultaneously without any language barrier; internal communication is seamless.",
            "q6_justification": "The mining ship has thick castle-like walls; gate exit requires permits; surface travel demands survival equipment, marking a harsh and resource-intensive environment.",
            "q7_justification": "A full civilization with fairs, gate systems, surveillance infrastructure, and military assets indicates a large, established population.",
            "q8_justification": "Juan's extralegal surveillance capability suggests an authoritarian potential within a unified governing system; permits are required for exit, indicating centralized control.",
            "q9_justification": "The group's clandestine departure in a mining ship for an unauthorized wilderness expedition has a festive, rebellious, and adventurous character.",
            "q10_justification": "Juan inspects new fighter aircraft; illegal surveillance operates; four warships appear on screen; civilian life at the Creativity Fair continues alongside these military elements.",
            "q11_justification": "Juan is at an airfield inspecting new fighters; warships appear on screen; fighter aircraft production frames the military dimension in terms of airpower.",
            "q12_justification": "Mining ships are required for surface travel; a gate system separates the city from the hostile exterior, marking a physical environment that demands specialized technology.",
        },
    },
    {
        "chapter": "Part 2 - Wings",
        "answers": {
            "q1": "Low contestation (minor competition, little open conflict)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Nearly uninhabitable / lethal without major intervention",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Adventure / exploration",
            "q10": "Mostly civilian with some military presence",
            "q11": "Like the air / airpower",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "A historical debate about the purpose of the revolution (practical vs ideological) is discussed, but there is no active conflict in the chapter; contestation is minor and retrospective.",
            "q2_justification": "Pre-war caves and the current glass city both attest to permanent habitation; the dance school and labs indicate a governable, functioning settlement.",
            "q3_justification": "Pre-war settlers were dependent on supplies from Earth, and Garcia's diplomatic mission implies ongoing meaningful separation between the worlds.",
            "q4_justification": "The central archive is described as a founding philosophy separating the production of goods from the production of ideas, unprecedented in human history and distinctly Martian.",
            "q5_justification": "Luoying reflects that each world believed the other would eventually evolve toward it, implying mutual comprehension in a shared language.",
            "q6_justification": "Mars's atmosphere is too thin for conventional flight; pre-war settlers lived in crude caves and depended on Earth supplies; early settlement was survival-level existence.",
            "q7_justification": "A full civilization with dance schools, laboratories, and workshops indicates a large, established population.",
            "q8_justification": "The central archive serves as the foundational institution of Martian governance; Garcia's diplomatic mission operates within this unified framework.",
            "q9_justification": "The chapter combines engineering problem-solving (large insect-like wings with photoelectric membranes) with historical revelation about pre-war settlement, creating an exploratory and inventive register.",
            "q10_justification": "Anka's squadron training boundaries are mentioned, but the chapter is otherwise focused on civilian engineering and historical reflection.",
            "q11_justification": "The entire chapter concerns the physics of flight on Mars, wing design, and insect biomimetics for air travel, firmly aligning with an airpower domain analogy.",
            "q12_justification": "Mars's atmosphere is 1% of Earth's; winds are strong and predictable; temperatures swing from low teens to below -100°C, marking a physical environment that constantly challenges human bodies and technology.",
        },
    },
    {
        "chapter": "Part 2 - Sand",
        "answers": {
            "q1": "Moderate contestation (ongoing rivalry/disputes)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Nearly uninhabitable / lethal without major intervention",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Adventure / exploration",
            "q10": "Mixed civilian-military domain",
            "q11": "Like the air / airpower",
            "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        },
        "justifications": {
            "q1_justification": "A military vehicle scouts the crater, a secret military installation with a flame insignia is discovered, and the group hides from patrols, indicating ongoing strategic surveillance and contestation.",
            "q2_justification": "Outside Mars City, ancient crater habitations and a secret military installation both demonstrate that territory beyond the city can be occupied and held.",
            "q3_justification": "The group travels deep into Martian wilderness far outside the city, operating in a remote landscape that implies meaningful distance from both Mars City and Earth.",
            "q4_justification": "A pre-war rebel camp archaeological site and a Martian military with its own flame insignia reflect a cultural order uniquely shaped by Martian history.",
            "q5_justification": "Communication requires headsets because the atmosphere is too thin to transmit voice, but the language used is the same as Earth's.",
            "q6_justification": "Survival suits are mandatory; oxygen supplies are limited; communication range is under 100 meters; a dust storm traps characters; temperature swings are extreme, making the surface nearly lethal without intervention.",
            "q7_justification": "A military outpost exists in the wilderness while a full civilization operates nearby, indicating substantial population and infrastructure.",
            "q8_justification": "Juan's military operates within the unified Martian system but maintains hidden installations, reflecting a single authority with covert capabilities.",
            "q9_justification": "Wing flight experiments, the archaeological discovery of a pre-war rebel camp, and a dust storm crisis combine to give the chapter a strongly adventurous and exploratory character.",
            "q10_justification": "A military vehicle patrols and a secret base is discovered, while the Mercury Group are civilian explorers hiding from military detection.",
            "q11_justification": "Wing flight is the central activity; military ground-effect vehicles patrol; air is the primary operational domain for both the group and the military.",
            "q12_justification": "The atmosphere is too thin to transmit voice; extreme temperature swings occur; dust storms exert lethal force; survival suits are mandatory—physics and environment are fundamentally unlike Earth.",
        },
    },
    {
        "chapter": "Part 2 - Wind",
        "answers": {
            "q1": "Moderate contestation (ongoing rivalry/disputes)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Political / diplomatic",
            "q10": "Entirely civilian",
            "q11": "Like the frontier / colonial expansion",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "A heated ideological debate divides the group between revolutionary and reformist factions, reflecting ongoing political contestation within Martian society.",
            "q2_justification": "The mining ship interior and the approaching crater terrain presuppose Mars as permanently inhabited and governable territory.",
            "q3_justification": "The surface journey takes the group far from the city across vast Martian geography, indicating meaningful distance and separation.",
            "q4_justification": "The debate about Martian systemic hypocrisy versus founders' ideals shows that neither faction wants Earth's model; both are arguing from within a distinctly Martian political culture.",
            "q5_justification": "The internal Martian political debate is conducted in a shared language without any translation barriers.",
            "q6_justification": "Canyon walls are too tall to see their peaks; the ship travels through extreme terrain that demands sustained engineering and navigation.",
            "q7_justification": "The mining ship itself is described as infrastructure for wilderness travel, indicating an established population that supports such operational capability.",
            "q8_justification": "The debate is about reforming or demolishing the unified system, presupposing that a single unified authority currently governs Mars.",
            "q9_justification": "Political debate dominates the chapter, with warm camaraderie contrasting cold confrontation, giving it a strongly political-diplomatic character.",
            "q10_justification": "The chapter consists entirely of youth political discussion on a civilian mining ship with no military presence.",
            "q11_justification": "Traveling into Martian wilderness and debating the future direction of civilization parallels the logic of frontier colonial expansion.",
            "q12_justification": "Fire-red canyon walls, massive craters, Olympus Mons (3x Everest), and Valles Marineris (5x Grand Canyon) mark a physical landscape constantly challenging human scale and perception.",
        },
    },
    {
        "chapter": "Part 2 - Morning",
        "answers": {
            "q1": "Moderate contestation (ongoing rivalry/disputes)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Nearly uninhabitable / lethal without major intervention",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Adventure / exploration",
            "q10": "Mixed civilian-military domain",
            "q11": "Like the air / airpower",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "Hans issues a public apology for using Mercury Group as hostages; Reini is punished; four warships are visible; political accountability is enacted under ongoing contestation.",
            "q2_justification": "The Boule Chamber governs Mars City, visible from the plains as glass domes, confirming permanent and governable settlement.",
            "q3_justification": "The surface expedition is far from the city; return requires a ship and kite-flight system, underscoring meaningful physical distance.",
            "q4_justification": "The consul publicly apologizes and applies rule of law even to his granddaughter; punishment is deployed as political calculation, reflecting a distinctly Martian governance culture.",
            "q5_justification": "Luoying recites Saint-Exupéry in French on a Martian cliff, demonstrating shared literary heritage with Earth and no language barrier.",
            "q6_justification": "Characters are rescued by an improvised cable-tow kite system; oxygen supplies are limited; dawn temperatures are below zero, making survival dependent on constant technical intervention.",
            "q7_justification": "A full civilization with a Boule, warships, and mining infrastructure indicates a large, established population.",
            "q8_justification": "The Boule session with the consul's authority over punishment terms demonstrates a single unified political authority governing Mars.",
            "q9_justification": "The dawn revelation of Hans's shadow-painting, canyon flying, and the Boule confrontation combine to give the chapter a strongly adventurous and exploratory arc.",
            "q10_justification": "Four warships appear on screen and a military base is present, while the Boule proceedings and the group's expedition are civilian in nature.",
            "q11_justification": "Kite-flight through canyons, military fighter aircraft, and air as the primary operational domain all align with an airpower analogy.",
            "q12_justification": "Dawn on Mars has no clouds; a gentle breeze is unfelt through a suit; temperatures are below zero; Mars City appears as glass domes over a sand ocean—a physical world constantly unlike Earth.",
        },
    },
    {
        "chapter": "Part 2 - Stars",
        "answers": {
            "q1": "Low contestation (minor competition, little open conflict)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Nearly uninhabitable / lethal without major intervention",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Drama",
            "q10": "Entirely civilian",
            "q11": "Like the frontier / colonial expansion",
            "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        },
        "justifications": {
            "q1_justification": "The chapter is a philosophical debate between two people stranded overnight; there is no active political or military conflict.",
            "q2_justification": "The ancient cave retains pre-war insulation and radiation shielding, indicating past permanent habitation; current Mars City operates nearby.",
            "q3_justification": "The colony ship Cerealia is mentioned as leaving the Solar System; Anka and Luoying are far from the city, underscoring meaningful separation at multiple scales.",
            "q4_justification": "The founders' vision separated creativity from economic survival through the central archive as a protector of freedom of conscience, an unprecedented and distinctly Martian cultural framework.",
            "q5_justification": "Luoying quotes Camus in French, and the two share literary and philosophical references from Earth's heritage without any language barrier.",
            "q6_justification": "Temperatures fall below zero; survival suits are required; oxygen is limited until noon; the cave provides radiation shielding; improvised heating from wing materials is needed for survival.",
            "q7_justification": "Evidence of past habitation in the cave and a functioning civilization nearby indicate established and common human presence on Mars.",
            "q8_justification": "The discussion of Mars's founding philosophy centers on the republic's unified authority and its central archive as a governing institution.",
            "q9_justification": "The chapter is an intimate philosophical conversation between two young people under stars, tender and hopeful in register, entirely dramatic in character.",
            "q10_justification": "Two young people discuss ideas in a cave; there is no military activity in the chapter.",
            "q11_justification": "The ancient frontier cave habitation and the founders' philosophical frontier of human knowledge both invoke the logic of colonial expansion.",
            "q12_justification": "Stars do not twinkle; the Milky Way is visible without atmospheric interference; Luoying cannot find Earth among the stars; cosmic radiation requires shielding—the physical environment is fundamentally unlike Earth.",
        },
    },
    {
        "chapter": "Part 2 - A Beginning Serving as an End",
        "answers": {
            "q1": "Low contestation (minor competition, little open conflict)",
            "q2": "Habitable and governable (permanent settlements can hold territory)",
            "q3": "Moderate journey (months/meaningful separation)",
            "q4": "Distinct space culture",
            "q5": "Same languages as Earth",
            "q6": "Harsh and resource-intensive",
            "q7": "Common (many people live/work there)",
            "q8": "Single unified authority",
            "q9": "Drama",
            "q10": "Entirely civilian",
            "q11": "Like the frontier / colonial expansion",
            "q12": "Very different (human bodies/technology constantly challenged)",
        },
        "justifications": {
            "q1_justification": "Reini accepts his punishment calmly and the mystery of the military base remains unresolved; there is no active conflict, only a quiet lingering tension.",
            "q2_justification": "The hospital and Mars City awakening in morning light confirm a permanent and governable settlement in full operation.",
            "q3_justification": "The Mercury Group's shared experience of wandering between worlds implies a meaningful journey distance between Earth and Mars.",
            "q4_justification": "Reini is reassigned to the Registry under Mars's system of managed consequences, reflecting a distinctly Martian institutional and cultural logic.",
            "q5_justification": "The internal Martian conversation between Luoying and Reini proceeds without any language barrier.",
            "q6_justification": "The glass-walled hospital and vast Martian landscape visible outside underscore the resource-intensive character of maintaining life within the built environment.",
            "q7_justification": "A hospital, a registry, and full city infrastructure indicate a large and established population.",
            "q8_justification": "Hans's authority over personnel assignments demonstrates the continuing operation of a single unified authority governing Mars.",
            "q9_justification": "The chapter is a quiet, bittersweet epilogue—a farewell on the skydeck rendered in a reflective and emotional dramatic register.",
            "q10_justification": "The chapter takes place in a hospital and involves only personal reflection; there is no military activity.",
            "q11_justification": "The vast Martian landscape framing the human story invokes the frontier colonial sense of small human figures against an immense, not-yet-tamed terrain.",
            "q12_justification": "A vast, silent Martian landscape with cliffs and mountains is separated from the characters by a glass dome, marking the physical environment as constantly and fundamentally different from Earth.",
        },
    },
]

# Write rows
analyzed = 0
skipped = 0

for ch in chapters:
    chapter_label = ch["chapter"]
    if chapter_label in existing_chapters:
        print(f"Skipping (already exists): {chapter_label}")
        skipped += 1
        continue

    row = {"country": country, "book": book_title, "chapter": chapter_label}
    for q in questions:
        qkey = f"q{q['number']}"
        row[qkey] = ch["answers"][qkey]
    for q in questions:
        jkey = f"q{q['number']}_justification"
        row[jkey] = ch["justifications"][jkey]

    file_exists = os.path.exists(csv_path) and os.path.getsize(csv_path) > 0
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

    print(f"Written: {chapter_label}")
    analyzed += 1

print(f"\nSummary: {analyzed} chapters analyzed, {skipped} skipped.")
print("Done with batch 2.")
