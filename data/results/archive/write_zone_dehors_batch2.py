import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter IX",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Volte escalates dramatically during Clastre month with the 'Disjonc-télés' TV pirating operation, hijacking broadcasts with subversive content. The government responds with a 1-million bounty on the Bosquet and a 'Wanted' campaign. Capt discovers surveillance cameras in his apartment, and the Volte develops body-language codes to evade electronic monitoring. The conflict has become a strategic struggle between organized resistance and state repression.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "Cerclon remains a fully governed permanent settlement. The chapter describes rooftop commando operations across the city, TV broadcast infrastructure, secret meeting locations like Cuve 13, and the government's comprehensive surveillance apparatus. The settlement's infrastructure supports both state control and resistance operations.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information is provided. The setting remains on Cerclon orbiting Saturn, maintaining the established major separation from Earth. The chapter's focus on internal political conflict reinforces the characters' distance from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The Clastre month rituals, the TV pirating operation using rooftop emitters, the subliminal 'A' image broadcast, the fake circuit voice takeover, and the body-language code system (zipper/hands/pockets) developed at Cuve 13 all represent cultural practices unique to this enclosed space society. The 'intellectueur' media concept is a distinctly Cerclonnien phenomenon.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Characters continue speaking French with Cerclon-specific terminology. The chapter introduces terms like 'Disjonc-télés,' 'cloisonnement,' 'clameurs,' and the Volte's coded body language. Media broadcasts use standard French adapted with political and technological neologisms of Cerclon.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter focuses on interior Cerclon operations. Slift's rooftop commando involves physical risk from climbing and evading detection, but the environment itself is controlled. The dangers are political and operational rather than environmental.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The TV pirating operation reaches the entire population of Cerclon. The growing popular support for the Volte, the media polarization, and the government's mass communication response all confirm a large, established space population for whom space habitation is entirely normal.",
        "q8": "Single unified authority",
        "q8_justification": "The government responds as a unified entity: issuing the Wanted announcement, coordinating media response, and deploying surveillance. The Bosquet operates as a clandestine opposition to this single authority. No competing state entities exist.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter centers on political escalation: the TV pirating as political media warfare, the government's propaganda response, the 'intellectueur' interview debating the Volte's legitimacy, and the Bosquet's strategic planning at Cuve 13. The narrative is fundamentally about political struggle and media manipulation.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The domain remains primarily civilian, but the escalation introduces more forceful elements: Slift's rooftop commando operates with military-style coordination, the government's Wanted campaign resembles a military manhunt, and the Volte develops covert operational security (cloisonnement, body codes). The civilian-military boundary begins to blur.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The TV pirating operation is the ultimate expression of networked warfare: hijacking broadcast frequencies, inserting subliminal images, and taking over the circuit voice. The government's response through media control and surveillance cameras in Capt's apartment reinforces the characterization of space governance as operating through information networks.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter takes place entirely inside Cerclon where conditions are artificially controlled. Rooftop operations expose characters to the exterior environment briefly, but the focus is on the urban interior where environmental differences from Earth are managed."
    },
    {
        "chapter": "Chapter X",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The Volte intensifies its campaign with Kamio's provocative public speeches in centres de rencontres and Capt's illegal placement of clameurs (sound pastilles) throughout the city despite government decrees. Capt threatens a woman who confronts him, showing the escalating personal toll. The conflict has become a sustained strategic struggle over public consciousness.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The chapter describes centres de rencontres, public spaces, and city streets where Kamio delivers speeches and Capt places clameurs. The governed urban infrastructure of Cerclon is the battleground for the Volte's campaign of public agitation.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information. The setting remains Cerclon orbiting Saturn, with the established major separation from Earth continuing as background context for the political events.",
        "q4": "Distinct space culture",
        "q4_justification": "The clameurs invention is a uniquely Cerclonnien cultural artifact: small sound pastilles placed around the city that play 10-second philosophical recordings when people pass. Kamio's concept of 'l'orœil' and body politics ('organismés') represent philosophical ideas shaped by the experience of living in an enclosed, surveilled space habitat.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Kamio's speeches use French with distinctive Cerclon philosophical vocabulary: 'organismés,' 'l'orœil,' 'clameurs,' 'capsulateurs.' The language remains recognizably French but heavily adapted with neologisms born from space-society experience.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter is set entirely inside Cerclon's controlled urban environment. The risks are political and interpersonal rather than environmental. Capt's threatening encounter with Gncsr demonstrates social danger, not physical environmental hazard.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "Kamio addresses packed centres de rencontres and Capt places clameurs throughout the city for the general population to encounter. The chapter depicts a fully populated urban society where space habitation is the unremarkable norm.",
        "q8": "Single unified authority",
        "q8_justification": "The government issues decrees against clameurs and maintains surveillance. The single unified authority continues to govern Cerclon while the Volte operates as an underground opposition.",
        "q9": "Political / diplomatic",
        "q9_justification": "Kamio's speeches directly confront citizens about their complicity in the Clastre system, challenging them to revolt against self-surveillance and body control. Capt's clameurs are a form of political art activism. The entire chapter is political agitation and philosophical provocation.",
        "q10": "Entirely civilian",
        "q10_justification": "Kamio's speeches are civilian political harangues in public meeting spaces. Capt's clameur placement is civilian activism. The government response consists of civilian decrees and policing. No military elements appear in this chapter.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The clameurs create a distributed network of subversive messages embedded in the city's physical infrastructure, functioning like a physical internet of resistance. Kamio's speeches about how bodies are 'organismés' by networked control systems reinforce the cyberspace characterization of the domain.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter takes place entirely in Cerclon's interior urban spaces where conditions are artificially maintained. The environment is functionally Earth-like, with differences managed by the habitat's infrastructure."
    },
    {
        "chapter": "Chapter XI",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The lake electrification at the fête du Clastre is the most violent action yet: Blusq ionizes the water, causing electrical torture to approximately 300,000 capsulateurs, resulting in 540 comas, 1,496 wounded, 2,753 hospitalizations, and 17 deaths. P is forced to resign, the new P raises the bounty to 5 million, and mass interrogations begin. This is open strategic struggle.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The fête du Clastre at Parc bleu with 500,000 attendees demonstrates the scale of the permanent settlement. The government's ability to conduct mass interrogations and establish Camps d'Éducation Civique shows comprehensive territorial governance.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information. The setting remains Cerclon orbiting Saturn with established major separation from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The fête du Clastre celebration, the elaborate technogreffe/capsule culture (biogiciels like Narcisse, Sexe, Sensual, Attraction), and the Camp d'Éducation Civique (virtual reality brainwashing facility) are all uniquely Cerclonnien cultural phenomena with no Earth equivalent. The capsulateur subculture represents a distinct space-born identity.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The chapter uses French with extensive Cerclon terminology: 'capsulateurs,' 'technogreffés,' 'biogiciels,' 'Camp d'Éducation Civique,' and the Volte's message transmitted through water ('le Bosquet, c'est 110 Voltes'). The base language remains French with heavy technological and cultural adaptation.",
        "q6": "Manageable but risky",
        "q6_justification": "The physical environment of Cerclon remains controlled, but the lake electrification demonstrates that the managed environment can be weaponized. The festival takes place in a park with an artificial lake, showing conditions that are normally benign but vulnerable to sabotage.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The fête du Clastre draws 500,000 attendees, and the lake electrification affects roughly 300,000 people. The mass scale of both the celebration and the casualties confirms that space habitation is entirely common and normalized.",
        "q8": "Single unified authority",
        "q8_justification": "The government responds as a unified entity: P resigns, a new P is appointed, the bounty is raised, mass interrogations are conducted, and Camps d'Éducation Civique are deployed. The political structure remains a single centralized authority.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The lake electrification scene is depicted with horror-like intensity: 300,000 people convulsing in electrified water, the 'panache' message transmitted through pain, 17 deaths, and hundreds of comas. The Camp d'Éducation Civique's virtual reality brainwashing adds a dystopian horror dimension. This chapter shifts from political narrative to thriller territory.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The fête du Clastre is a civilian event, but the government's response escalates to quasi-military levels: mass interrogations, forced re-education camps, and a massive bounty. The Volte's lake electrification operation resembles a military strike in its planning and casualties. Slift kills Brihx's cat suspecting it is a cyborchat surveillance device.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The lake electrification exploits the technological infrastructure of the technogreffe culture, turning people's own implants against them. The Camp d'Éducation Civique uses virtual reality to reprogram citizens. The domain continues to be characterized by networked technological control.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter is set inside Cerclon where conditions are controlled. The Parc bleu with its artificial lake represents managed environmental conditions. The physical environment remains artificially Earth-like."
    },
    {
        "chapter": "Chapter XII",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The TV tower assault is a full-scale military-style operation with multiple perspectives (Brihx, Kamio, Capt, Slift, Obffs, Boule). The battle includes Slift climbing the 83-meter tower, commando neutralizing guards, a firefight with escadre 7 (cyborg-like elite police), Slift's cavalry charge of glisseur knights, Austral Le Sec's legendary laser boomerang cutting a helicopter rotor, and Capt's capture. This is open warfare.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The TV tower is a major piece of broadcast infrastructure within the governed settlement. The assault and defense of this strategic asset demonstrate that Cerclon's territory is actively held and contested. The governmental cube where Capt is transported further shows established governance infrastructure.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information. The setting remains Cerclon orbiting Saturn with major separation from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The multi-perspective battle narration reveals a uniquely Cerclonnien conflict: glisseur knights charging on floating vehicles, laser boomerangs, escadre 7 cyborg police, and Slift surfing on a metal plate via cable escape. The weapons, tactics, and technology all reflect a culture evolved in the space-station environment.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "Battle communications and narration use French with Cerclon military and technological vocabulary: 'glisseurs,' 'escadre 7,' 'canonras,' 'cyborchat.' The combat terminology is adapted from French military language with space-specific innovations.",
        "q6": "Manageable but risky",
        "q6_justification": "The physical environment remains the controlled interior of Cerclon. The risks are entirely from the combat situation rather than natural conditions. The tower's height and the rooftop operations involve standard physical dangers within a managed environment.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The large-scale battle involves multiple commando units, police squadrons, helicopters, and civilian observers. The scale of forces on both sides confirms a densely populated settlement where space habitation is normal.",
        "q8": "Single unified authority",
        "q8_justification": "The government deploys escadre 7 elite police, helicopters, and coordinates a defensive response through a single command structure. Kohtp's betrayal (blocking Capt's elevator) comes from within the government's unified intelligence apparatus.",
        "q9": "Military / war",
        "q9_justification": "The chapter is a real-time multi-perspective battle narrative: commando assault, tower climbing, guard neutralization, firefight with elite police, cavalry charge, helicopter destruction, capture, and escape. This is military/war genre writing.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "The TV tower assault crosses fully into military territory: the Volte operates as a paramilitary force with organized commandos, cavalry units, and coordinated tactical operations. The government deploys escadre 7 (elite paramilitary police) and helicopters. Both sides operate with military-grade weaponry and tactics.",
        "q11": "Like the air / airpower",
        "q11_justification": "The battle is characterized by verticality and aerial combat: Slift climbing the 83-meter tower, glisseurs functioning as aerial cavalry, a helicopter engagement, Austral's laser boomerang cutting the helicopter rotor, and Slift's aerial cable escape. The spatial domain of the battle is defined by altitude, flight, and three-dimensional movement.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The battle takes place inside Cerclon's controlled environment. The tower's height and the aerial combat occur within the enclosed habitat space. Environmental conditions remain artificially managed."
    },
    {
        "chapter": "Chapter XIII",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Capt is interrogated by P with laser-targeted canonras while Ksa reads his comprehensive surveillance file including intimate details. P shows a fabricated murder video to frame Capt. The extended philosophical dialogue between Capt and President A reveals the full scope of the strategic struggle: A openly describes democracy as 'optimal alienation under the appearance of total freedom' and the machinery of control through media, education, and polling (Sondophage).",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The governmental cube where Capt is held demonstrates the highest level of governance infrastructure. A's office and the interrogation chambers represent the physical center of power in a fully governed permanent settlement.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information. The setting remains within Cerclon's governmental core, orbiting Saturn at great distance from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "A's philosophical revelations expose the deep structure of Cerclon's distinct culture: the Clastre as social control technology, Sondophage (fabricated polling that creates self-fulfilling prophecies), the education system as formatting tool, and the 'affecting' (manipulation of primary emotions). These governance technologies constitute a uniquely space-born political culture.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The philosophical dialogue between Capt and A uses sophisticated French with Cerclon political concepts: 'Sondophage,' 'l'affecting,' 'clastré,' and institutional terminology specific to Cerclon's governance. The language is intellectually rich French adapted with space-society political vocabulary.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter is set inside the governmental cube. The physical environment is entirely controlled and comfortable. The dangers are political (interrogation, fabricated charges, potential execution) rather than environmental.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "A's description of the governance machinery implies control over the entire population of millions. The Sondophage system, media manipulation, and education formatting all operate at population scale, confirming mass space habitation.",
        "q8": "Single unified authority",
        "q8_justification": "A is the apex of a single unified authority. His candid description of how power operates through the Clastre, media, education, and polling reveals a comprehensive, centralized governance system controlling all aspects of Cerclon society.",
        "q9": "Political / diplomatic",
        "q9_justification": "The chapter is dominated by the philosophical dialogue between Capt and A about the nature of power, democracy, and control. A's revelations about the Sondophage, the affecting, and the education system constitute the most explicitly political content in the novel. This is political theory embedded in narrative.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The interrogation by P involves laser-targeted canonras (weapons), and escadre-level security surrounds the governmental cube. However, the core narrative is a civilian political dialogue between a philosopher-dissident and a president. Slift's dramatic escape sequences intercut with the dialogue add paramilitary action elements.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "A's revelations describe governance as operating through networked information systems: Sondophage fabricates public opinion through data manipulation, media controls narrative, the education system formats minds, and the Clastre processes identity through databases. The domain is fundamentally defined by information control rather than physical force.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter is set in the interior of the governmental cube where conditions are fully controlled. No environmental differences from Earth are relevant to this chapter's events."
    },
    {
        "chapter": "Chapter XIV",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Capt faces the ultimate personal stakes of the strategic struggle: accept A's offer to become Minister of Education (betraying the Volte) or refuse and face death via fabricated murder charges. His 30-minute deliberation weighs survival against principles. The cendrier scene where Capt forces A into a ritualized game of chance represents the conflict distilled to its purest form. Capt refuses, choosing death over collaboration.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The chapter takes place in A's office within the governmental cube, the physical center of governance. A's ability to offer a ministerial position or order execution demonstrates total governmental control over the settlement.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "No new journey information. The setting remains within the governmental cube on Cerclon, orbiting Saturn far from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The offer of Minister of Education within the Clastre system, the fabricated video technology, and A's whispered 'gâchis' (waste) all reflect a political culture unique to Cerclon. Capt's discovery that Boule's image on the monitor is fabricated (missing bouton de fièvre) shows the depth of technological deception in this space society.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The dialogue between Capt and A uses French with political terminology specific to Cerclon's governance: 'Minister E,' 'Clastre,' and institutional vocabulary. The base language remains recognizably French.",
        "q6": "Manageable but risky",
        "q6_justification": "The chapter is set in A's controlled office environment. Physical conditions are entirely managed. The mortal danger Capt faces is political (execution via fabricated charges), not environmental.",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The ministerial position offered to Capt would involve overseeing education for the entire population, confirming the large scale of the settled space community.",
        "q8": "Single unified authority",
        "q8_justification": "A exercises singular authority to offer a ministerial position or order death. P is summoned with a call. The entire political apparatus is at A's command, demonstrating absolute unified authority.",
        "q9": "Drama",
        "q9_justification": "The chapter is a dramatic tour de force: Capt's agonizing 30-minute deliberation, the discovery of the fabricated Boule image, the cendrier game with A (forcing the president to participate in a ritualized chance decision), and the final refusal. The emotional and philosophical weight is dramatic rather than political or military.",
        "q10": "Entirely civilian",
        "q10_justification": "The chapter involves only civilian actors: a president, a dissident, and a minister. The offer is for a civilian government position. No military forces or operations appear. The drama is entirely within the civilian political sphere.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Capt's discovery that Boule's monitor image is fabricated (missing the bouton de fièvre) reveals the government's ability to create convincing false realities through networked media technology. The entire chapter's tension revolves around the power of information manipulation and fabricated evidence.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter is set entirely in the governmental cube's interior where conditions are fully controlled and Earth-like. No environmental differences are relevant."
    },
    {
        "chapter": "Chapter XV",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The government broadcasts the fabricated murder video ('L'Événement') to destroy the Volte's public support. The Volte remnants hide in their cache while Capt is imprisoned. The government manipulates polls via Sondophage (pushing approval from 52% to 60%) and calls a referendum on the death penalty. Slift leads an escape raid after 15 days. The strategic struggle reaches its most desperate phase.",
        "q2": "Habitable and governable (permanent settlements can hold territory)",
        "q2_justification": "The chapter depicts multiple layers of governed space: Capt's padded prison cell with inescapable TV, the Volte's hidden cache, and the government's ability to conduct population-wide referendums and media campaigns. The settlement's governance infrastructure encompasses even its prisons and underground spaces.",
        "q3": "Long-distance journey (years, major separation from Earth)",
        "q3_justification": "A reveals the Terminor's secret: a disconnector exists in the Zone du Dehors at coordinates 990-990-996, planted by the CSI as a fail-safe. This critical device's location in the hostile exterior reinforces the isolation of the settlement and its distance from Earth.",
        "q4": "Distinct space culture",
        "q4_justification": "The virtual reality game 'Capturez Captp' where Capt plays as guard Lnpor and discovers he can pass through TV screens represents a uniquely Cerclonnien cultural artifact. The Sondophage self-fulfilling prophecy polling system and the referendum on death penalty within the Clastre framework are distinctly space-society phenomena.",
        "q5": "Mostly same, with dialect/slang differences",
        "q5_justification": "The chapter uses French with Cerclon vocabulary: 'Sondophage,' 'Terminor,' 'L'Événement,' 'disconnecteur,' 'Zone du Dehors.' The VR game's dialogue and the media broadcasts use standard French adapted with space-society political and technological terms.",
        "q6": "Manageable but risky",
        "q6_justification": "Capt's prison cell is a controlled environment. The chapter references the Zone du Dehors where the disconnector is located, implying hostile exterior conditions. Inside Cerclon, conditions remain managed but psychologically oppressive (padded cell, forced TV viewing).",
        "q7": "Common (many people live/work there)",
        "q7_justification": "The Sondophage manipulates population-wide polling, and the referendum on death penalty involves the entire citizenry. The media broadcast of 'L'Événement' reaches the whole population. Space habitation remains entirely normalized at mass scale.",
        "q8": "Single unified authority",
        "q8_justification": "The government exercises unified control through media broadcasts, fabricated polling, referendums, and imprisonment. A personally visits Capt in prison and reveals state secrets. The single authority's reach extends from mass media to individual prisoners.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Capt's imprisonment in a padded cell with inescapable TV, his disturbing identification with his violent double in the fabricated video, and the extended VR game sequence where he plays as a guard and discovers he can pass through screens create a psychological thriller atmosphere. The moral guidance system in the game that tries to shape his behavior adds a horror dimension of thought control.",
        "q10": "Mostly civilian with some military presence",
        "q10_justification": "The chapter is primarily civilian: media broadcasts, polling, referendums, and prison. However, Slift's escape raid after 15 days of confinement introduces paramilitary action. The government's comprehensive control apparatus blurs the line between civilian governance and authoritarian force.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The VR game 'Capturez Captp' epitomizes the cyberspace characterization: Capt discovers he can pass through TV screens because the system cannot distinguish real from represented. The Sondophage creates self-fulfilling prophecies through data manipulation. The entire chapter explores the boundary between reality and networked simulation.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "The chapter is set inside Cerclon (prison cell, Volte cache). The Zone du Dehors is referenced but not entered. Interior conditions remain artificially controlled and Earth-like."
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

print('Done with batch 2.')
