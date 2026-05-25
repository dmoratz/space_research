import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 11 - Unity",
        "q1": "Total war / constant conflict",
        "q1_justification": "Shiraishi destroys Japanese IGS satellites using space tethers. The Cyber Front ransacks JAXA's IT systems. Shiraishi plans an LEO massacre to destroy all 2,000 satellites in low orbit. Chance demands Shiraishi's JAXA accounts to attack their servers.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The orbital hotel, ISS, Tiangong-2, and IGS satellites all represent temporary orbital infrastructure now under direct attack.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital activity is in LEO. The IGS satellites are in sun-synchronous orbits. The space tethers operate at 350 km altitude.",
        "q4": "Basically Earth society in space",
        "q4_justification": "JAXA's bureaucratic dysfunction, the minister berating Hashimoto, and the politics of spy satellite budgets are entirely Earth-normal institutional dynamics extending to space.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Team Seattle conducts a videoconference with Jamshed in Tehran, communicating in English across multiple accents and fluency levels. Akari and Kazumi occasionally speak Japanese. Sekiguchi uses multiple languages.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Space tether impacts at 500 m/s destroy IGS satellites like a metal bat striking them. The Wyvern's return craft is punctured. The entire orbital infrastructure is revealed as fragile and under existential threat.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks and ISS/Tiangong crews are in orbit. The vast battle over orbital assets is conducted entirely from Earth.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Japan's spy satellites, China's Tiangong-2, NORAD's defense systems, and North Korea's space tethers all represent national interests competing in orbit.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Shiraishi systematically destroys satellites while planning a complete LEO massacre. JAXA's systems are devastated by cyberattack. Hashimoto is berated by an ignorant minister. Shiraishi declares he will make himself the scapegoat to destroy all orbital infrastructure.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "JAXA civilians, military satellites, CIA and NORAD personnel, North Korean intelligence, civilian Jamshed, and intelligence operative Shiraishi all operate in the same domain.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Shiraishi controls 40,000 spacecraft via a web application. The Cyber Front ransacks JAXA's servers. Space tether base stations are D-Fi USB cables in millions of computers worldwide. The entire conflict is mediated through networks.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Orbital mechanics govern all movements. Satellites are vulnerable to impacts at orbital velocities. The space tethers exploit the unique physics of LEO: magnetic fields, tidal forces, and the Lorentz force.",
    },
    {
        "chapter": "Chapter 12 - Seed Pod",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Operation Seed Pod is briefed at Peterson AFB. Lintz realizes the space tethers make the operation potentially pointless. Team Seattle discovers that D-Fi USB cables are the worldwide base station network for controlling space tethers. Ricky prepares for his stratosphere mission.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The orbital hotel houses the Smarks. SAFIR 3 approaches it. The ASM-140 targets objects in LEO. All represent temporary orbital presence.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The ASM-140 targets a satellite at 390 km. Ricky will fly to 70,000 feet (stratosphere). All activity is near-Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The military briefing, pilot bravado, and industrial espionage (D-Fi cables) are all standard Earth institutional behaviors driving orbital events.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The multinational team communicates in English. Military personnel use formal military English. Akari's technical English contrasts with Bruce's colloquial style.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "The ASM-140 must reach Mach 23 to intercept. Depleted uranium rounds are needed to penetrate orbital shielding. The stratosphere requires a pressure suit. Space is portrayed as an extremely hostile combat environment.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks are in orbit. Ricky will reach the stratosphere but not orbit. The ASM-140 operates autonomously.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The US military conducts Operation Seed Pod. The D-Fi cable network spans multiple nations. COPUOS debris guidelines constrain military action.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Lintz realizes with horror that the ASM-140 warhead must pass through 20,000 space tethers. The D-Fi cable revelation shows the enemy's base stations are embedded in a million consumer products worldwide. Ricky paints 'Shooting Star' on his F-15.",
        "q10": "Mostly military",
        "q10_justification": "The chapter is dominated by military briefings (Lintz, Waabboy, Fernandez, Ricky, Madu, Gehner) and military operations. The D-Fi discovery scene includes CIA and civilian team members.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The D-Fi cables reveal that the space tether control network is embedded in consumer electronics worldwide. Space is controlled through software drivers, USB cables, and distributed computing. The Trojan horse is a consumer audio product.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The stratosphere requires pressure suits. Orbital intercept requires Mach 23 speeds. Whipple bumpers and composite armor govern space survivability. The environment demands specialized technology.",
    },
    {
        "chapter": "Chapter 13 - Pier 37",
        "q1": "Total war / constant conflict",
        "q1_justification": "Akari rides to Shiraishi's warehouse. Chance shoots and kills coast guard sailor Nash. Bruce and the coast guard assault the warehouse. Chance sets the warehouse on fire with gasoline sprinklers. Shiraishi is cornered inside.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The orbital hotel and space tethers are referenced but the chapter's action is entirely Earth-based. The Clouds continue operating in orbit during the ground confrontation.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital references are to LEO objects.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The confrontation at the warehouse is a standard ground-level espionage operation, even though it concerns control of orbital assets.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Akari calls out in Japanese to her uncle. Kazumi speaks Japanese with Shiraishi. Chance and Bruce communicate in English. Kurosaki and Sekiguchi join via video call mixing Japanese and English.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter is entirely Earth-based. Space conditions are not depicted.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "The chapter focuses entirely on Earth-based characters. Only the Smarks remain in orbit.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The ground confrontation involves US coast guard, CIA, NORAD, Japanese civilians, and a North Korean operative, all fighting over control of orbital weapons.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Chance cold-bloodedly kills Nash using a concealed shot. She uses his body as a shooting rest. The warehouse is rigged with gasoline sprinklers. Akari faces gunfire. The confrontation is lethal and desperate.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "CIA agent Bruce, coast guard sailor Nash, NORAD's Daryl, civilians Kazumi and Akari, and North Korean operative Chance all converge on the warehouse.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Even during the physical confrontation, the battle is ultimately about control of 40,000 networked spacecraft. Shiraishi's blueprint case contains plans for the Great Leap. The arson is triggered via a smartphone app.",
        "q12": "Other / Unsure",
        "q12_justification": "The chapter's action is entirely Earth-based.",
    },
    {
        "chapter": "Chapter 14 - Team Seattle",
        "q1": "Total war / constant conflict",
        "q1_justification": "Jamshed takes control of all 40,000 space tethers and targets the orbital hotel, Tiangong-2, Hubble, and KH-12. Sekiguchi is revealed as a Chinese spy. He threatens Jamshed with a gun and accidentally shoots himself. Kurosaki drugs Sekiguchi. Professor Ryu delivers North Korea's message.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The orbital hotel, Tiangong-2, Hubble telescope, and KH-12 spy satellite are all targets of the Cloud. All represent temporary orbital infrastructure.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All targets are in LEO. The Cloud must change orbits between targets at LEO altitudes.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The conflict over orbital assets is driven entirely by Earth geopolitics: North Korea's Great Leap ambition, China's intelligence operations, US-Iran tensions.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The expanded team communicates via videoconference in English. Sekiguchi speaks Persian with Alef, Korean knowledge is implied. Kazumi sometimes speaks Japanese. Jamshed uses stiff English.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Terminal apparatuses moving at 10 km/s will tear apart the orbital hotel. The Cloud forms a flattened spheroid 50 km wide to engulf targets. The orbital environment is lethal for unprotected assets.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks and space station crews are in orbit, and they face destruction from the Cloud.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The US (CIA, NORAD, NASA), China (Sekiguchi's handlers, Tiangong-2), North Korea (Ryu, the Great Leap), Iran (Jamshed), and Japan (JAXA) all compete over orbital control.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Jamshed commandeers the Cloud to destroy orbital infrastructure. Sekiguchi pulls a gun and accidentally shoots himself. Kurosaki drugs Sekiguchi with his own medication. Kazumi predicts orbital movements with uncanny precision. The crisis escalates to existential proportions.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "NASA, CIA, NORAD military, civilian Kazumi, scientist Jamshed, Chinese spy Sekiguchi, and North Korean envoy Ryu all participate in the crisis.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Kazumi predicts orbital movements through mental visualization. Space tethers are controlled via phone connections and base station networks. The NORAD team verifies predictions through orbital calculation software. Lintz uses a presidential hotline.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "Orbital mechanics govern the Cloud's approach. Objects at 10 km/s relative velocity destroy anything they touch. The team must understand orbital periods, inclinations, and rendezvous timing to counter the threat.",
    },
    {
        "chapter": "Chapter 15 - Meteors",
        "q1": "Total war / constant conflict",
        "q1_justification": "Kazumi proposes burning through space tethers using radio waves from Ozzy's Sampson-5 radar. Lintz calls the US president on NORAD's nuclear hotline to request control of global infrastructure. The team races against a 3-hour deadline before the Cloud reaches the orbital hotel.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The orbital hotel, Tiangong-2, Hubble, and KH-12 are all threatened. The Smarks have no return vehicle. All are temporary orbital assets.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The Cloud operates in LEO. The Sampson-5 radar on Desnoeufs Island must wait for the Cloud to pass overhead. All activity is near-Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The countermeasure relies entirely on Earth-based infrastructure: a radar on a Seychelles island, presidential authority, global communications networks.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The expanded multinational team (US military, CIA, NASA, Japanese civilians, Iranian scientist, Chinese spy) communicates primarily in English via videoconference. Akari mutters technical observations in Japanese.",
        "q6": "Nearly uninhabitable / lethal without major intervention",
        "q6_justification": "The Cloud's terminal apparatuses at 10 km/s will destroy anything in their path. The Smarks have no escape vehicle. The orbital hotel cannot maneuver to evade. Without intervention, everyone in LEO is dead.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks and space station crews face the threat in orbit. The entire defense is mounted from Earth.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The US president is called via NORAD's nuclear hotline to authorize use of global infrastructure. China is warned about Tiangong-2 through diplomatic channels. National authority governs the orbital response.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "A 3-hour countdown to the destruction of the orbital hotel drives desperate innovation. Kazumi's radio wave countermeasure depends on the ionosphere, presidential authorization, and precise timing. Kurosaki drugs Sekiguchi to prevent further violence in Tehran.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "NORAD's Lintz calls the president. Civilian Kazumi devises the countermeasure. CIA coordinates. Ozzy's civilian radar is the key weapon. NASA observes. The response spans every sector.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The countermeasure treats space tethers as antennas to be burned through with radio waves at specific frequencies. The solution depends on understanding wavelengths, ionospheric physics, and phased array radar technology.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The orbital environment demands understanding of the ionosphere, radio wave propagation, orbital velocity physics, and the Lorentz force. Human survival depends on technology operating at the edge of capability.",
    },
    {
        "chapter": "Epilogue",
        "q1": "No contestation",
        "q1_justification": "Set two years later at the Great Leap project unveiling. The crisis is resolved. Ageha probes are launched peacefully. The space tether technology is being used for exploration, not warfare.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "10,000 space tethers orbit Earth for imaging and probe launch. The Ageha probes are sent toward Jupiter and the Sun. The Loki 10 launch facility is operational. These represent temporary but growing presence.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "The space tethers orbit at 500 km. The Ageha probes are launched toward Jupiter and the Sun, but this is just beginning. Current activity remains near-Earth.",
        "q4": "Basically Earth society in space",
        "q4_justification": "The Great Leap unveiling is a gala event at the Western Days Hotel with champagne toasts and PR presentations, exactly like an Earth tech launch event.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The international audience at the unveiling communicates in English. Kazumi and Akari speak Japanese to each other. Ronnie presents in English.",
        "q6": "Manageable but risky",
        "q6_justification": "Space tethers orbit indefinitely using the Lorentz force. The 70 km tether connecting the Ageha probes is the largest moving device ever made. Space is harsh but increasingly manageable with tether technology.",
        "q7": "Uncommon (small specialist population)",
        "q7_justification": "10,000 space tethers orbit Earth. The Ageha probes are launched. Space activity has grown from the crisis but remains specialized.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The Great Leap is a multinational venture. Sekiguchi is in witness protection. Jamshed is under house arrest in Pyongyang. National interests still govern space activity.",
        "q9": "Adventure / exploration",
        "q9_justification": "The Ageha probes are launched toward Jupiter and the Sun. Ronnie presents a vision of helium-3 extraction, space lighthouses, and interplanetary rapid transit. The tone is optimistic and exploratory.",
        "q10": "Entirely civilian",
        "q10_justification": "The Great Leap unveiling is a civilian event. Ronnie Smark presents. Kazumi and Akari attend as executives. No military presence is noted.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The Great Leap vision frames space as a new frontier: extracting resources from Jupiter, establishing space lighthouses as navigation beacons, creating interplanetary transit systems. Shiraishi's dream of space development for the rest of the world echoes colonial expansion themes.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "The Ageha probes must navigate Jupiter's magnetic field 20,000 times stronger than Earth's, descend into Jupiter's atmosphere for helium-3 extraction, and traverse interplanetary distances using space tether propulsion. The environment is fundamentally unlike Earth.",
    },
]

country = 'Japan'
book_title = "Orbital Cloud"
csv_path = "data/results/Japan_Orbital_Cloud.csv"
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
