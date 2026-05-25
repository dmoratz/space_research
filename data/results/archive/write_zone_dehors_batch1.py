import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter I",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "There is no military or inter-state conflict over space. The contestation is purely internal and political: Capt and Boule evade surveillance drones and cameras to reach the Zone du Dehors, a forbidden-but-not-illegal area outside the city. The conflict is between citizens seeking freedom and a soft surveillance state, not a struggle over territory.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon is a permanent, fully governed settlement on an asteroid orbiting Saturn, housing seven million people. It has its own infrastructure, government (the Clastre ranking system), industry, and agriculture. The city is a self-sustaining colony with artificial gravity and oxygen turbines.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The chapter does not detail journey length directly, but Capt recalls his childhood on Earth and arriving on Cerclon at age thirteen, suggesting a significant journey. The setting orbits Saturn, which represents a major separation from Earth in both distance and lived experience.",
        "q4": "Distinct space culture",
        "q4_justification": "Cerclon has developed its own unique social system: the Clastre replaces names with alphanumeric codes based on rankings, citizens are surveilled by drones and cameras, and the Zone du Dehors represents a culturally significant forbidden wilderness. These elements have no Earth analog and constitute a distinctly space-born culture.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The characters speak French with distinctive slang and neologisms specific to Cerclon life, such as 'clastré,' 'radieux,' 'sinueuse,' and 'codebarré.' The language is recognizably Earth-derived (French) but adapted with terms unique to the space-station environment.",
        "q6": "Manageable but risky",
        "q6_justification": "The Zone du Dehors outside Cerclon has low gravity, toxic Nox vapors, and ammonia in the atmosphere requiring oxygen masks with limited supply. However, Capt and Boule survive their outing with proper equipment. The environment is dangerous but navigable with precautions, while inside Cerclon conditions are entirely controlled.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Cerclon houses seven million inhabitants who live and work permanently on the asteroid. Space habitation is the normal condition for these people, not an exceptional feat. However, it is not yet universal for humanity since Earth refugees emigrated to the Cerclons.",
        "q8": "Single unified authority",
        "q8_justification": "Cerclon I is governed by a single unified authority with a President (A) and ministers designated by letters. The government controls the Clastre ranking system, the Terminor surveillance network, and all public infrastructure. There is no mention of competing political entities in space.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter establishes the core political tension of the novel: the Volte resistance movement versus the soft-totalitarian Clastre system. Capt's philosophical text on identity and control, the surveillance evasion, and the description of how the state uses the Ligne du Dehors as a filter for potential delinquents all frame the narrative as fundamentally political.",
        "q10": "Entirely civilian",
        "q10_justification": "There is no military presence described. The surveillance apparatus consists of civilian drones, cameras, and vigiles (security guards), not soldiers. The conflict is between citizens and a civilian government's security apparatus. No military forces, ranks, or warfare are mentioned.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space in this chapter is not characterized as ocean, air, or frontier. Instead, the dominant characterization is of a networked surveillance domain: cameras, drones, codebars, the Terminor database, and identification software define the relationship between people and space. Control is exercised through information networks rather than physical force.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The Zone du Dehors features one-tenth Earth gravity, toxic Nox vapors, ammonia atmosphere, and unpredictable weather. Inside Cerclon, gravity is artificially maintained and oxygen is pumped by turbines. Regular adaptation is needed: oxygen masks, gravity pills, and specialized equipment for excursions outside the city walls."
    },
    {
        "chapter": "Chapter II",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The chapter continues the cat-and-mouse dynamic between Capt/Boule and the surveillance system. The vigiles at the Ligne du Dehors track traces and try to identify the passers, and Capt shoots down a sinueuse drone. The conflict remains low-level, individual evasion rather than open warfare.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon continues to be depicted as a fully functioning permanent settlement with seven million residents, complete governance systems, and controlled environments. The vigiles' surveillance of the boundary demonstrates active territorial governance.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information is provided, but the setting remains Saturn orbit. The chapter's references to Earth are nostalgic and distant, reinforcing the sense of major separation from the home planet.",
        "q4": "Distinct space culture",
        "q4_justification": "The chapter deepens the portrayal of Cerclon's unique culture: the vigiles use the Terminor identification system and Clastre rankings as currency for social advancement, citizens have alphanumeric names, and the Dehors represents a philosophical and cultural concept of freedom unique to this space society.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters continue speaking French with space-specific slang. The vigiles use terms like 'banquer,' 'codebarrer,' 'paramétrer par le visage,' reflecting a shared language with technical and social jargon specific to Cerclon.",
        "q6": "Manageable but risky",
        "q6_justification": "Capt and Boule explore the stone river, climb a 150-meter cliff with reduced gravity, and navigate toxic atmospheric conditions. The environment is risky but manageable with equipment and experience. Boule's near-death experience from removing her helmet shows the danger is real but survivable with intervention.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The chapter references seven million pairs of eyes in the Terminor database, confirming the large permanent population of Cerclon. Space habitation is the norm for this society.",
        "q8": "Single unified authority",
        "q8_justification": "The government is referenced through its surveillance apparatus and the minister P. The vigiles work within a single hierarchical system that controls the Ligne du Dehors and the Terminor identification database.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter interweaves Capt's philosophical reflections on surveillance, freedom, and the Dehors as political concept. His meditation on how the state uses the Ligne as a filter for 'potential delinquents' and the vigiles' surveillance work frame the narrative as political resistance literature.",
        "q10": "Entirely civilian",
        "q10_justification": "All security personnel described are civilian vigiles and surveillance operators, not military. The drones and cameras are civilian policing tools. The conflict involves no military apparatus.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The chapter emphasizes the networked nature of control: the Terminor identification system processes morphometric data, the vigiles operate through screens and databases, and identification is achieved through image recognition algorithms comparing hand shapes against seven million records.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The stone river of meteorites, the low gravity enabling cliff climbing, the toxic atmosphere, and the meteorite lake all demonstrate an environment that requires constant adaptation. Gravity pills, oxygen masks, and specialized knowledge are necessary for survival outside Cerclon."
    },
    {
        "chapter": "Chapter III",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The chapter depicts the internal political schism within the Volte movement. A vote splits the movement between moderates (Molte) and radicals (Volte), with Slift advocating for placing blades on security doors. The level of contestation escalates from low-level evasion to organized political action and internal factional struggle.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon is described as a fully governed settlement with sectors, industrial zones, and a crashed spaceship repurposed as the Volte's secret meeting hall. The political infrastructure of governance, including media and security, is firmly established.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "The chapter references Earth's destruction by chemical warfare, with Europeans emigrating to Africa. Cerclon is described as a destination that required significant travel, reinforcing the major separation from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The Volte resistance movement, the Clastre ranking system, the crashed-vaisseau meeting hall, and the sociopolitical dynamics of the seven sectors all represent a culture that has evolved distinctly from any Earth society. The debate over revolutionary tactics is shaped by the unique conditions of enclosed space habitation.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak French with Cerclon-specific vocabulary: 'molteux,' 'volté,' 'robotag,' 'radrock,' 'clastré,' and political neologisms like 'Volution.' The base language is recognizable but heavily adapted.",
        "q6": "Manageable but risky",
        "q6_justification": "This chapter focuses on the interior of Cerclon rather than the Dehors. The physical environment inside is entirely controlled and benign. The risks described are political and social rather than environmental.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The Volte has four thousand activists among seven million Cerclonniens. The chapter describes a full society with workers, students, artists, and political movements, confirming that space habitation is common and normalized for this population.",
        "q8": "Single unified authority",
        "q8_justification": "The government is described as a unified structure with ministers designated by letters, media channels, and a comprehensive surveillance system. The Volte opposes this single authority; there are no competing state entities.",
        "q9": "Political / diplomatic",
        "q9_justification": "The entire chapter revolves around the political dynamics of the Volte: the assembly debate, the schism between moderates and radicals, the vote, and the planning of direct action against the security-door system. It is fundamentally a political narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "All actors are civilians: the Volte members are workers, students, and artists. The opposition consists of civilian police and surveillance systems. No military presence is mentioned.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The chapter describes how the Volte uses a buried spaceship as headquarters, accessed through tunnels, and how the government controls population through networked systems of access control, surveillance, and the Clastre database. Space as a domain is defined by information and control networks.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "This chapter takes place entirely inside Cerclon where conditions are controlled. The environmental differences from Earth are present but managed: artificial gravity, manufactured oxygen, and engineered climate. The setting feels urban and enclosed rather than physically alien."
    },
    {
        "chapter": "Chapter IV",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Volte's blade action has injured a young girl, escalating the conflict. The government and media respond with accusations of terrorism, while the Volte is internally torn by guilt and political calculation. The contestation has moved from philosophical opposition to actual physical confrontation with consequences.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Cube, an enormous structure serving as both waste dump and death-sentence prison, demonstrates the scale of permanent infrastructure. The chapter describes the Cube's industrial and political functions within the governed territory of Cerclon.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new information on journey length, but the setting remains orbiting Saturn. The Cube receives waste from three Cerclons and orbital stations, suggesting an established interplanetary infrastructure that implies long-distance separation from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The Cube as combined waste repository and execution site, the media's treatment of the Volte's action, and Capt's philosophical processing of violence all reflect a culture shaped by unique space-station conditions. The mythology around Zorlk surviving inside the Cube is a distinctly Cerclonnien cultural element.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The media broadcasts and Capt's internal monologue continue in French with Cerclon-specific terminology. Terms like 'incubé,' 'pyracides,' 'repousseurs magnétiques' reflect technological adaptations of the base language.",
        "q6": "Manageable but risky",
        "q6_justification": "This chapter is mostly interior to Cerclon. The Cube is described as extremely dangerous internally but poses no threat to the general population from outside. The physical environment of the city remains controlled and safe.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The chapter references seven million citizens, media broadcasts reaching the entire population, and the Cube serving three Cerclons plus orbital stations. Space habitation is fully normalized.",
        "q8": "Single unified authority",
        "q8_justification": "The government's media response and political apparatus function as a unified authority. The President and ministers respond collectively to the Volte's action. No competing political entities are mentioned.",
        "q9": "Political / diplomatic",
        "q9_justification": "The entire chapter examines the political aftermath of the blade action: Capt's moral crisis, the media's framing of the event, and the political calculus of how the government and Volte will each exploit the situation. It is deeply political narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "All actors remain civilian. The media, government, and Volte are all civilian entities. The security apparatus consists of civilian police and surveillance technology, not military forces.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The media network's treatment of the event dominates the chapter. Control is exercised through information manipulation: the media's framing, the government's messaging, and the Volte's inability to control the narrative all characterize space governance as a domain of networked information control.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter takes place inside Cerclon where environmental conditions are controlled. The Cube's extreme internal conditions (radiation, heat, toxic gases) are referenced but isolated from the general population. The city environment is Earth-like but artificial."
    },
    {
        "chapter": "Chapter V",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The aftermath of the blade action continues with ongoing tension between the Volte and the state. Capt reflects on the political implications while cycling through the city, encounters public opinion, and prepares for the evening meeting. The contestation is political and ongoing.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The chapter provides the most detailed description of Cerclon's urban geography: seven sectors organized by distance from the Cube, with distinct social classes, parks, agriculture zones, and a central government district. This is a fully permanent, governed settlement.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Capt recalls arriving from Earth at age thirteen after a year-and-a-half journey, fleeing a Europe devastated by war. This explicitly confirms a long-distance journey with major separation from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The panoptic towers, the artificial trees with cellophane leaves, the radzone culture, the seven-sector social hierarchy, and the incitateurs (paid conversational advertisers) all depict a culture radically different from Earth. The nostalgia Capt feels for real trees underscores how distinct this space culture is.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Capt's philosophical monologues and conversations are in French with heavy use of Cerclon-specific terms: 'radieux,' 'incitatrice,' 'terminora,' 'parleur,' 'vocoréac.' The language is recognizably French but laden with space-society neologisms.",
        "q6": "Manageable but risky",
        "q6_justification": "The radzone is described as radioactive and dangerous, with toxic puddles and irradiated debris. Young pillards risk their lives dismantling radioactive reactor cores. However, inside the main sectors of Cerclon, conditions are entirely managed and safe.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Seven million people live across Cerclon's seven sectors. The chapter describes a complete urban society with agriculture, industry, commerce, and culture. Eight more Cerclons are under construction for 150 million total people, confirming that space habitation is becoming widespread.",
        "q8": "Single unified authority",
        "q8_justification": "The chapter describes the government cube at the geometric center of the city, housing 26 ministers, the Terminor below, and the astroport above. This is a single, centralized authority governing all of Cerclon.",
        "q9": "Political / diplomatic",
        "q9_justification": "Capt's extended philosophical reflections on panoptic towers, surveillance, self-control, dévitalization of bodies, and technogreffes make this chapter predominantly political and philosophical. His spoken recordings critique the democratic surveillance state.",
        "q10": "Entirely civilian",
        "q10_justification": "The surveillance system is civilian: panoptic towers with public observation boxes, civilian voyeurs, and anonymous denunciation forms. The police operate through covert surveillance, not military force. Meanwhile, police agents secretly install cameras in Capt's apartment using civilian espionage techniques.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The panoptic towers epitomize the networked surveillance domain: observation boxes with advanced optics, anonymous denunciation systems, and the principle that self-surveillance replaces direct policing. The chapter's description of how power operates through information networks rather than physical force strongly characterizes space as a cyberspace-like domain.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Inside Cerclon, conditions are artificially Earth-like: constant temperature, humidity, gravity, and oxygen. The artificial trees and climate generators create a managed simulation of Earth conditions. The radzone is more physically different but remains peripheral to main habitation."
    },
    {
        "chapter": "Chapter VI",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Volte's internal debate over the blade action intensifies. Slift advocates killing if necessary, Kamio demands ethical limits, and the group struggles to define their approach. The government responds with denunciation campaigns and heightened surveillance. The contestation is sustained and multi-dimensional.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The chapter describes the Cubilingus cafe, the radzone, the tube transport system, and the Volte's buried vaisseau headquarters. All demonstrate the fully established, governed infrastructure of a permanent settlement.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Capt references Earth being three-quarters uninhabitable, with only Africa remaining. Eight more Cerclons are under construction, including super-Cerclons for 150 million people. The Cerclons are presented as humanity's primary settlements far from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The Volte's internal political dynamics, the media's manipulation of the blade incident, the Cubilingus cafe where advertisers get kicked, and the radzone culture of scavengers all represent a distinct space culture with no direct Earth equivalent.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The Bosquet's debate features French with extensive Cerclon slang: 'traqueurs,' 'encubée,' 'claste,' 'sociopathe,' 'volutionnaire.' Slift's distinctive working-class dialect adds further linguistic variation within the same base language.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter focuses on interior Cerclon environments. The radzone bicycle journey involves mud and radiation exposure but is manageable. The primary risks are political (surveillance, denunciation) rather than environmental.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "References to seven million citizens, eight additional Cerclons under construction, and 150 million people to be housed confirm that space habitation is common and expanding significantly.",
        "q8": "Single unified authority",
        "q8_justification": "The government's response to the blade action is coordinated through a single hierarchy: P pressures subordinates, who pressure the surveillance operatives. The political structure is unified and hierarchical.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is dominated by the Bosquet's political debate: whether to continue violent action, how to respond to media framing, whether to publish a communique, and the ethical boundaries of resistance. Capt's speech about carcevisceral technologies and the future of control is deeply political.",
        "q10": "Entirely civilian",
        "q10_justification": "All actors are civilian. The Volte members are workers, artists, and students. The opposition consists of media organizations, civilian government, and police surveillance. No military presence is described.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The chapter's focus on media manipulation, information control, and the networked surveillance response to the blade action reinforces the characterization of space governance as operating through information networks. The media's ability to reframe events and the government's denunciation campaigns are exercises in networked power.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter is set inside Cerclon where conditions are controlled. Capt's bicycle ride through the radzone involves mud and radioactive materials, but the main city sectors remain environmentally Earth-like."
    },
    {
        "chapter": "Chapter VII",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Volte holds its post-action meeting under heightened security, with armed sentinels and password-protected access. Traqueurs (government trackers) are actively searching the radzone. The Volte adopts a new electronic sabotage strategy to invert the access-control system, representing an escalation in the ongoing rivalry.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The chapter describes the radzone's established community of scavengers, the Volte's underground headquarters, and Blusq's insider access to Defordre's network systems. The governance infrastructure is comprehensive enough that a single programmer can potentially subvert the entire access system.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "Capt's mother is described as having left Earth specifically to see Saturn's storms. The detailed description of Saturn, its rings, and its moons from the asteroid's surface reinforces the vast distance from Earth. The frozen, cratered landscape beyond the Nakkarst emphasizes cosmic isolation.",
        "q4": "Distinct space culture",
        "q4_justification": "The Volte's underground assembly, the coded passwords, the electronic sabotage strategy, and the four declared values (unconditional freedom, creation, multiplicity, vitality) all represent a counter-culture unique to Cerclon's space society. The distinction between 'revoltes' and 'voltes' is a cultural innovation.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters speak French with Cerclon vocabulary. The Volte's new terminology includes 'carcevisceral technologies,' 'revoltes' vs 'voltes,' and technical hacking jargon specific to the Defordre system. The base language remains French with significant space-society adaptation.",
        "q6": "Manageable but risky",
        "q6_justification": "The radzone at night is described as eerie and deserted due to traqueur activity. The ride through toxic puddles, radioactive zones, and cosmic wind is risky but manageable. The methane clouds from Saturn add atmospheric danger. Inside Cerclon proper, conditions remain controlled.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The assembly gathers roughly a hundred people from a movement of thousands, within a city of seven million. The Volte's organizing reflects a full civil society in space. Space habitation is entirely normalized.",
        "q8": "Single unified authority",
        "q8_justification": "The government's unified response includes traqueurs searching the radzone, denunciation campaigns with escalating rewards, and coordinated media control. The single authority's apparatus is comprehensive.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on the Volte's political reorganization: adopting a communique, defining values, debating ethics, and choosing the electronic sabotage strategy over physical violence. The Blusq proposal to invert the access system is a political action designed to expose inequality.",
        "q10": "Entirely civilian",
        "q10_justification": "All actors remain civilian. The Volte sentinels carry paralysis guns, not military weapons. The traqueurs are civilian police investigators. The electronic sabotage targets a civilian access-control system.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The Blusq sabotage plan is the ultimate expression of space-as-cyberspace: hacking the Defordre electronic access network to invert its logic, turning a tool of exclusion against the wealthy. The chapter's resolution through electronic subversion rather than physical violence characterizes the domain as fundamentally networked.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The nighttime ride through the radzone features methane clouds, cosmic wind, ammonia filets, and Saturn's immense presence overhead. The description of Saturn's storms, metallic hydrogen core, and the frozen landscape beyond the Nakkarst emphasizes a physically alien environment requiring regular adaptation."
    },
    {
        "chapter": "Chapter VIII",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "The Clastre system dominates the chapter as a tool of social control. The surveillance apparatus actively investigates Capt: his apartment has been bugged, his hand is being tracked, and vigiles are recommending full surveillance. The political contestation between the Volte and the state continues through institutional mechanisms.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The Clastre system itself is the ultimate expression of governance: every two years, seven million citizens are evaluated, ranked, renamed, and reassigned within the social hierarchy. This comprehensive administrative control demonstrates a fully governed permanent settlement.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information is provided. The setting remains Saturn orbit. The chapter's focus on internal Cerclon politics rather than interplanetary matters reinforces that the characters are firmly established far from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The Clastre system is the most distinctly non-Earth cultural element: a biennial ranking system that renames all seven million citizens, turning people into alphanumeric codes based on composite evaluations. Capt's university lecture on how the Clastre fragments and reconstructs identity is a cultural analysis unique to this space society.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The academic lecture uses French philosophical vocabulary mixed with Cerclon-specific terms: 'dividuel,' 'collexiqueur,' 'claustrologie,' 'mirécran.' The radio broadcasts use standard French media language with Cerclon political terminology.",
        "q6": "Manageable but risky",
        "q6_justification": "This chapter is entirely set inside Cerclon where conditions are controlled. The risks are political and social, not environmental. The physical environment is comfortable and safe.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The Clastre evaluates all seven million citizens, from President A to the last-ranked Qzaac at position 7,054,423. The system's comprehensive scope confirms a large, established space population.",
        "q8": "Single unified authority",
        "q8_justification": "The Clastre is administered by a single centralized government through the Terminor system. The surveillance hierarchy flows from P through subordinate ministers to field operatives. The entire political apparatus is unified.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is dominated by Capt's university lecture deconstructing the Clastre as a political technology of control, using Foucault's framework of power, knowledge, and subjectivation. The radio broadcasts of the Volte's communique and the government's response further the political narrative.",
        "q10": "Entirely civilian",
        "q10_justification": "The Clastre is a civilian evaluation system. The surveillance operatives installing cameras and listening devices in Capt's apartment are civilian intelligence agents, not military. The university setting and media landscape are entirely civilian.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The Clastre is the ultimate networked control system: it collects data from medical exams, psychological evaluations, peer ratings, and performance reviews, processes them through the Terminor, and outputs a comprehensive identity assignment. Capt's lecture on 'dividuels' describes space governance as fundamentally operating through data networks and information processing.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter takes place entirely inside Cerclon where conditions are artificially Earth-like. The constant temperature, gravity, humidity, and oxygen levels described in previous chapters continue. The environment is managed to minimize physical differences from Earth."
    }
]

country = 'France'
book_title = 'La Zone du Dehors'
csv_path = 'data/results/France_La_Zone_du_Dehors.csv'

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

print('Done with batch 1.')
