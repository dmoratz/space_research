import json, csv, os

chapters_data = [
    {
        "chapter": "The Eleventh Letter",
        "q1": "No contestation",
        "q1_justification": "The narrator visits the prince's palace freely with no guards or conflict. The prince himself is a forgotten, powerless figure whose authority has dissolved without any struggle or contestation.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator is a foreigner visiting Tainaron temporarily. The prince's palace is open but abandoned, and the narrator's presence is that of a transient visitor rather than a settler holding territory.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator appears completely separated from their place of origin with no mention of return. Tainaron feels like a self-contained world entirely removed from Earth, with communication only through letters.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Tainaron's prince sits alone in a dusty tower with no attendants, no guards, and no protocol. The complete indifference of citizens to their ruler and the insect-like physical features of the prince represent a social order utterly unlike Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator converses directly with the prince and Longhorn without any translation difficulties. Communication happens in the same language, though cultural meanings and customs differ.",
        "q6": "Manageable but risky",
        "q6_justification": "The narrator moves freely through the palace and city without physical danger, but there are subtle risks hinted at by the prince's warning about exile and bayonets. Survival is not a constant struggle but uncertainty exists.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator appears to be the only human foreigner in Tainaron. The dusty footprints in the prince's chamber confirm the narrator is the sole visitor, making human presence exceptionally rare.",
        "q8": "Single unified authority",
        "q8_justification": "Tainaron is governed by a prince from his palace, representing a single political authority. Though his power has waned and he may no longer truly rule, the city has one nominal governing structure.",
        "q9": "Drama",
        "q9_justification": "The chapter is a melancholic dramatic encounter between the narrator and an aging, forgotten prince. Themes of loss, loneliness, and fading power dominate the emotional tone.",
        "q10": "Entirely civilian",
        "q10_justification": "The prince's palace has no guards, no military presence, and the audience is entirely civilian in nature. The only mention of military is the prince's hypothetical fear of bayonets from a national guard.",
        "q11": "Other / Unsure",
        "q11_justification": "Tainaron is not characterized as any recognizable military domain. The city is an allegorical, fantastical place that does not map onto naval, air, frontier, or cyber analogies.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The prince has forelimbs with downy pincers and a fluffy blue collar, indicating insect-like physiology radically different from humans. The narrator's human body is conspicuously out of place in this environment of non-human beings."
    },
    {
        "chapter": "The Twelfth Letter",
        "q1": "No contestation",
        "q1_justification": "The chapter describes a personal emotional crisis and melancholy rather than any form of conflict or contestation. The narrator walks through the city observing decay and aging without encountering disputes.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator remains a visitor in Tainaron, sitting at cafe windows and walking streets. There is no sense of territorial ownership, only temporary habitation in a city that feels increasingly alien.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator writes letters with no expectation of return mail, suggesting complete separation from home. The distance feels one-way and effectively unreachable.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The narrator reflects that Tainaron rests on nothing but a crust as insubstantial as one night's ice. The city's nature is fundamentally alien, with inhabitants whose eyes crowd streets seeking lost pupils in windows.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator reads books, visits cafes, and interacts with friends in Tainaron using shared language. A friend speaks to the narrator directly, and a woman on the tramcar complains audibly in understandable speech.",
        "q6": "Manageable but risky",
        "q6_justification": "The narrator describes Tainaron as built on an insubstantial crust, suggesting underlying physical fragility. Daily life is manageable but the ground itself may give way, creating latent environmental risk.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator is a solitary foreign visitor writing letters home. No other human visitors or settlers are mentioned, making human presence exceptionally rare in Tainaron.",
        "q8": "Single unified authority",
        "q8_justification": "Tainaron continues to function as a single city with shared infrastructure including tramcars, department stores, and cafes. No competing political factions or alternative governance structures are mentioned.",
        "q9": "Drama",
        "q9_justification": "The chapter is deeply introspective and melancholic, meditating on aging, loss, and the passage of time. The narrator mourns the youth of the world and contemplates mortality, placing it firmly in the drama genre.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter depicts entirely civilian scenes: cafes, tramcars, department stores, streets, and personal reflection. There is no military presence or reference whatsoever.",
        "q11": "Other / Unsure",
        "q11_justification": "Tainaron is not characterized as any military domain. The chapter is a personal meditation on aging and loss with no military analogies or domain characterizations.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The narrator describes inhabitants with eyes that crowd streets and physical characteristics unlike humans. The ground of Tainaron itself is described as an insubstantial crust, fundamentally different from solid Earth ground."
    },
    {
        "chapter": "The Thirteenth Letter",
        "q1": "No contestation",
        "q1_justification": "The chapter is a deeply personal meditation on love, identity, and self-reflection. There is no conflict, competition, or contestation of any kind in Tainaron during this letter.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator continues as a temporary visitor in Tainaron, shopping at department stores and walking streets. The opening dream of escape reinforces the sense of transience and impermanence.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator recalls memories from a distant past with the letter's recipient, separated by what feels like an unbridgeable distance. Communication is only through one-way letters with no expectation of reply.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The narrator walks among Tainaron's inhabitants and shops at its department stores, but the dream opening featuring a pursuer and the surreal shadow-trees growing from the narrator's legs suggest a reality fundamentally unlike Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator recalls past conversations with the letter's recipient and plans to shop at department stores, all conducted in shared language. No communication barriers are mentioned.",
        "q6": "Manageable but risky",
        "q6_justification": "The narrator dreams of a threatening pursuer but daily life in Tainaron itself appears manageable. The city has department stores and streets to walk, though the dream suggests underlying dangers.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator remains the sole human visitor mentioned in Tainaron. The letter is addressed to a distant recipient who is not present in the city.",
        "q8": "Single unified authority",
        "q8_justification": "Tainaron continues to operate as a unified city with department stores and civic infrastructure. No competing authorities or political fragmentation is mentioned.",
        "q9": "Drama",
        "q9_justification": "The chapter is a lyrical, emotional reflection on love, memory, and identity. The narrator meditates on past words spoken by a loved one and the overwhelming feeling of having something wider than a prairie to give.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter contains only personal reflection, dreams, and civilian activities like shopping. There is no military presence or reference.",
        "q11": "Other / Unsure",
        "q11_justification": "No military domain characterization is present in this deeply personal and philosophical chapter. Tainaron is portrayed as an allegorical city, not analogous to any military domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The narrator's shadow splits into two shadow-trees growing from their legs, and the dream features metamorphosis and surreal physical phenomena. The physical reality of Tainaron operates by different rules than Earth."
    },
    {
        "chapter": "The Fourteenth Letter",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Longhorn warns the narrator to stay away from the eastern parts of the city as it is not safe. The narrator encounters a threatening creature in a sand pit, suggesting minor dangers and territorial boundaries, though no open conflict occurs.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator explores Tainaron as a visitor, venturing into unfamiliar eastern districts. The narrator has no territorial claim and is merely passing through dangerous areas as a temporary presence.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator is completely immersed in Tainaron with no means of return mentioned. The city feels like a self-contained world where the narrator compares sand dunes to snowfields at home, emphasizing vast separation.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The narrator discovers two Tainarons: one with architecture and culture, and another primitive area of earth-colored clay dwellings, caves, and mounds for the most insignificant beings. This stratified insect society is entirely unlike Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator communicates with Longhorn and navigates the city without language barriers. Conversations happen naturally, though the narrator does not fully understand the culture.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The eastern outskirts are dangerous, with unpaved roads, sand that infiltrates shoes and mouth, and a predatory creature lurking in sand pits. The narrator barely escapes the ant-lion-like trap, making survival resource-intensive in these parts.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator explores alone and encounters only small dragonfly-like creatures in the dangerous eastern district. No other human presence exists in Tainaron.",
        "q8": "Single unified authority",
        "q8_justification": "Tainaron is presented as one city, though with vastly different districts. The central city has architecture and culture while the eastern parts are primitive, but all fall under one civic entity.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The narrator narrowly escapes a predatory creature hidden in a sand pit that nearly swallows them. The chapter builds suspense as the narrator ventures into increasingly desolate and threatening terrain, culminating in a terrifying encounter.",
        "q10": "Entirely civilian",
        "q10_justification": "The narrator's exploration is entirely civilian. The dangers encountered are natural predators in the landscape, not military forces. There is no military presence in the chapter.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The narrator's journey into the primitive eastern outskirts of Tainaron resembles frontier exploration, moving from civilized center to wild, dangerous periphery with increasingly primitive dwellings and hidden predators.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "The eastern outskirts feature dwellings made of clay that merge into sand, ant-lion traps with creatures lurking in conical pits, and an environment where the boundary between habitation and wilderness dissolves completely. The physical landscape is fundamentally unlike Earth."
    },
    {
        "chapter": "The Fifteenth Letter",
        "q1": "No contestation",
        "q1_justification": "The chapter is a deeply personal reminiscence about listening to radio white noise as a child. There is no conflict or contestation in Tainaron or anywhere else in the narrative.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator walks through Tainaron's streets amid a confusion of voices but remains a visitor. Most of the chapter is spent in childhood memories rather than engaging with Tainaron's territory.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator recalls hearing a name called from a place so far off they could never have reached it. Tainaron and the narrator's homeland feel separated by an unbridgeable, almost metaphysical distance.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The streets of Tainaron are filled with alien sounds: croaking, drumming, snapping, bellowing, and shrill cries that the narrator compares to bird screams and fish silence. This cacophony represents a social order incomprehensible to the human narrator.",
        "q5": "Distinct space language(s)",
        "q5_justification": "The narrator explicitly states being surrounded by voices they understand as little as the screaming of birds or the silence of fish. The Tainaronians communicate through croaking, drumming, and snapping sounds that constitute distinct non-human languages.",
        "q6": "Manageable but risky",
        "q6_justification": "The narrator walks through Tainaron's streets experiencing confusion but not physical danger. The environment is disorienting with alien sounds and communication barriers but ultimately manageable for daily survival.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator is a solitary human amid Tainaron's alien inhabitants. The confusion of incomprehensible voices underscores the narrator's singular, isolated human presence in the city.",
        "q8": "Single unified authority",
        "q8_justification": "Tainaron continues to function as a single city with streets and civic life. No alternative governance structures or competing authorities are introduced in this chapter.",
        "q9": "Drama",
        "q9_justification": "The chapter is a lyrical, introspective meditation on childhood wonder, the mystery of white noise, and the yearning to find meaning in formless sound. It is emotionally contemplative rather than action-driven.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter describes civilian street life in Tainaron and childhood memories of listening to radio. There is no military presence or reference.",
        "q11": "Other / Unsure",
        "q11_justification": "The chapter does not characterize Tainaron as any military domain. The radio white noise metaphor evokes something cosmic and formless, not comparable to naval, air, or frontier domains.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The soundscape of Tainaron is composed of alien vocalizations incomprehensible to the human narrator. The city's inhabitants produce croaking, drumming, and snapping sounds, creating a physical sensory environment very different from Earth."
    },
    {
        "chapter": "The Sixteenth Letter",
        "q1": "No contestation",
        "q1_justification": "The chapter describes a peaceful afternoon on the narrator's balcony watching the Mimic change forms. There is no conflict, rivalry, or contestation of any kind.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator has a balcony and lives in a building, but remains a visitor. The narrator's impulsive statement about staying forever is met with Longhorn's darkened voice, suggesting permanence is not truly possible.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator notes that for the letter's recipient it is autumn while in Tainaron it is still high summer, suggesting the two places exist in completely different temporal and spatial realities.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Mimic is a creature who has no fixed identity, becoming stone, grass, or tree at will. Longhorn questions whether the Mimic can even have a personality, representing a social reality where identity and continuity are not assumed.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator and Longhorn converse freely and directly, debating philosophical questions about identity and continuity. Language is shared, though cultural concepts differ significantly.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The narrator sits comfortably on a balcony basking in summer sunshine. The courtyard, tree, and peaceful atmosphere present no survival challenges whatsoever in this chapter.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator is the sole human in Tainaron, interacting only with Longhorn and observing the Mimic from the balcony. No other human visitors are present.",
        "q8": "Single unified authority",
        "q8_justification": "Tainaron functions as a single city where Longhorn and the narrator live. No competing political entities or authorities are mentioned.",
        "q9": "Drama",
        "q9_justification": "The chapter explores philosophical themes of identity, transformation, and permanence through the encounter with the shape-shifting Mimic. The emotional tone is contemplative and dramatic.",
        "q10": "Entirely civilian",
        "q10_justification": "The scene is entirely domestic and civilian: a balcony, a courtyard, a philosophical conversation between the narrator and Longhorn about identity. No military elements appear.",
        "q11": "Other / Unsure",
        "q11_justification": "Tainaron is not characterized as any military domain in this chapter. The focus is on identity and transformation in a civilian, philosophical context.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Mimic can transform into stone, grass, or a tree, representing physical laws fundamentally different from Earth. Longhorn's jaw withdraws to the side of his face in a smile, and his forelimb rests on the narrator's shoulder, showing alien physicality."
    },
    {
        "chapter": "The Seventeenth Letter",
        "q1": "No contestation",
        "q1_justification": "The chapter is an introspective childhood memory about a toy shop window and the realization of mortality. There is no conflict or contestation in Tainaron or elsewhere.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The chapter is primarily set in a childhood memory outside Tainaron. The narrator's presence in any place is that of a temporary observer, standing before a shop window as a metaphor for experiencing life.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator describes standing in a strange street in a strange city after the realization of mortality, feeling completely displaced. The separation from both childhood and the letter's recipient is absolute.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Though the chapter revisits an Earth memory, the experience of reality shifting between meaning and void represents the narrator's perception of existence as fundamentally unstable, consistent with Tainaron's alien nature.",
        "q5": "Other / Unsure",
        "q5_justification": "The chapter is set entirely in a childhood memory with no interaction with Tainaron's inhabitants. Language and communication are not addressed.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter describes no physical danger but conveys existential risk through the realization of mortality. The narrator's world shifts between meaning and void, a psychological rather than physical hazard.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator remains a solitary figure, standing alone before a shop window both in childhood memory and metaphorically in Tainaron. No other humans inhabit the alien city.",
        "q8": "Other / Unsure",
        "q8_justification": "The chapter focuses entirely on a personal childhood memory and philosophical reflection. No political structures or governance of Tainaron are discussed.",
        "q9": "Drama",
        "q9_justification": "The chapter is a profound meditation on mortality, meaning, and perception, triggered by a childhood memory of a marble in a toy shop. The emotional depth and philosophical weight make it clearly dramatic.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter describes a child looking at a toy shop window and contemplating mortality. There is no military element of any kind.",
        "q11": "Other / Unsure",
        "q11_justification": "No domain characterization is applicable to this deeply personal philosophical chapter. Tainaron is not discussed in terms of any military or strategic analogy.",
        "q12": "Other / Unsure",
        "q12_justification": "The chapter is set in a childhood memory on Earth rather than in Tainaron. The physical environment described is an Earth city street, making the question about physical differences not directly applicable."
    },
    {
        "chapter": "The Eighteenth Letter",
        "q1": "No contestation",
        "q1_justification": "The narrator peacefully observes the City Surveyor at work and converses with him on a park bench. There is no conflict or contestation in the chapter.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator walks through the city, sits on a bench in the park, and observes. The narrator remains a visitor in Tainaron with no territorial claim or permanent settlement.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator is fully immersed in Tainaron's daily life, watching city officials and sitting alone in parks. The complete absence of any reference to returning home suggests an effectively unreachable separation.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The City Surveyor measures streets using his own long green body as the sole measuring device, a hereditary role passed through generations. This represents a social order where bodily identity literally defines civic function, radically unlike Earth society.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator converses directly with the Surveyor, asking about his work and receiving detailed answers. Communication is in a shared language without barriers, though cultural concepts differ.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The narrator walks through the park, sits on a bench, and shops at stores. The environment is calm and unthreatening, with bells ringing from the cathedral and children playing in the playground.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator sits alone on the bench after the Surveyor departs, the sole human in a city of non-human beings. No other human visitors are mentioned.",
        "q8": "Single unified authority",
        "q8_justification": "The City Surveyor wears a white cap of city officials and measures for the city's archives. Tainaron operates under a single civic authority with officials, a cathedral, and city arms on rubbish bins.",
        "q9": "Drama",
        "q9_justification": "The chapter is a contemplative encounter with the Surveyor, exploring themes of measurement, generational change, and the relativity of time. The falling autumn leaf marks the passage of seasons in a dramatic, reflective tone.",
        "q10": "Entirely civilian",
        "q10_justification": "The City Surveyor is a civilian official measuring streets. The chapter features parks, playgrounds, shops, and a cathedral. There is no military presence.",
        "q11": "Other / Unsure",
        "q11_justification": "Tainaron is portrayed as a civilian city with bureaucratic structures like city surveyors and archives. It does not resemble any military domain.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Surveyor has a long green body he uses as a measuring device, climbing vertical walls without vertigo. His flat face and many rows of teeth represent a physical reality very different from human experience."
    },
    {
        "chapter": "The Nineteenth Letter",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "A massive silent procession of grub-like creatures marches through Tainaron, creating an atmosphere of fear and tension among citizens. A small weevil is nearly consumed by the procession, suggesting latent threat, though no open conflict erupts.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator stands on a kerbstone watching the procession as a spectator, acknowledging being a stranger in Tainaron. The narrator's presence remains that of a temporary visitor observing events they cannot fully understand.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator asks the letter's recipient if they have encountered anything comparable in their travels, suggesting they exist in completely separate, unreachable worlds. Communication is only through one-way letters.",
        "q4": "Radically different / alien social order",
        "q4_justification": "A procession of millions of grub-like creatures covered in a transparent membrane marches silently through the city, with citizens watching in silent awe. This collective insect behavior and civic ritual is utterly unlike any Earth social phenomenon.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator communicates with a gleaming black diver-like figure who answers curtly in shared language. Despite cultural gaps, basic verbal communication functions between the narrator and Tainaronians.",
        "q6": "Manageable but risky",
        "q6_justification": "The massive procession creates an atmosphere of fear and a weevil is nearly swallowed by the living snake of creatures. The narrator manages to observe safely from the kerbstone but the environment carries real risk.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator stands alone on the kerbstone after the crowds disperse, the sole human among the citizens of Tainaron. The narrator acknowledges being a stranger in the city.",
        "q8": "Single unified authority",
        "q8_justification": "The narrator speculates whether the prince might appear for a parade, and Tainaron has a national flag with a spiral or nautilus. The city operates under a single civic authority despite the mysterious procession.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter builds suspense as an eerie silent procession of millions of grub-like creatures marches through the city. The terrified weevil nearly consumed by the living serpent and the crowd's fearful silence create a horror-tinged atmosphere.",
        "q10": "Entirely civilian",
        "q10_justification": "The narrator uses military terms like battalions and divisions but explicitly states not knowing whether the procession was military. The event appears to be a mysterious civic phenomenon rather than a military one.",
        "q11": "Other / Unsure",
        "q11_justification": "The procession is described with military vocabulary (battalions, divisions, regiments) but its nature is unknown and mysterious. It does not clearly map to any recognized military domain.",
        "q12": "Radically non-Earth-like (physics/environment fundamentally unlike Earth experience)",
        "q12_justification": "Millions of grub-like creatures form a living snake covered in transparent membrane, with individuals carrying each other in rotating layers. This biological phenomenon and the slimy trail left on the boulevard represent a physical reality fundamentally unlike Earth."
    },
    {
        "chapter": "The Twentieth Letter",
        "q1": "No contestation",
        "q1_justification": "The narrator visits an ancient neighbor in a sack on a park bench and strolls to the harbour. There is no conflict, rivalry, or contestation of any kind in the chapter.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The narrator remains a visitor in Tainaron, sitting beside the old man on a park bench and strolling to the harbour. The sight of the white ship that brought the narrator to Tainaron reinforces their status as a visitor.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The narrator sees the ship that brought them to Tainaron but cannot remember why they came. The old man in the sack is over 150 years old, and the narrator's separation from home feels absolute and one-way.",
        "q4": "Radically different / alien social order",
        "q4_justification": "An ancient being over 150 years old is carried in a sack to a park bench daily by a servant or descendant. He has shrunk to resemble a bunch of straw with thin limbs, representing a life cycle and social arrangement utterly unlike Earth.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The narrator converses with the ancient being in the sack, who asks where the narrator is from. Communication happens in shared language, though the being's voice is weak and hoarse.",
        "q6": "Benign / easily survivable",
        "q6_justification": "The narrator sits on a park bench in sunshine and strolls to the harbour. The environment is calm and peaceful with no survival challenges present in this chapter.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The narrator is the sole human visitor in Tainaron. The old man in the sack confirms he was not born in Tainaron either, but the narrator is the only identifiably human foreigner.",
        "q8": "Single unified authority",
        "q8_justification": "Tainaron continues to function as a single city with a harbour, parks, and civic life. No competing authorities or political structures are introduced.",
        "q9": "Drama",
        "q9_justification": "The chapter meditates on aging, identity, and the question of whether a person remains the same throughout life. King Milinda's philosophical question about birth and death gives the chapter a deeply dramatic and contemplative tone.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter describes parks, a harbour, and an encounter with an elderly neighbor. There is no military presence or reference of any kind.",
        "q11": "Other / Unsure",
        "q11_justification": "Tainaron is not characterized as any military domain. The chapter focuses on aging, identity, and philosophical questions in a civilian setting.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The ancient neighbor has shrunk to fit in a sack, resembling a bunch of straw with thin limbs, having lived over 150 years. This extreme aging process and insect-like physicality represent a very different physical reality from Earth."
    }
]

country = 'Finland'
book_title = 'Tainaron: Mail from Another City'
csv_path = 'data/results/Finland_Tainaron__mail_from_another_city.csv'

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

print('Done with batch 2.')
