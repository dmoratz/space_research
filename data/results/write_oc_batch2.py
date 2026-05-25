import json, csv, os

chapters_data = [
    {
        "chapter": "Chapter 6 - Discovery Pursuit",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The team flees to the Nippon Grand Hotel (a Chinese safe house) after North Korean agents appear. Sekiguchi discovers Shiraishi used JAXA's MDM to track them. They plan to contact NORAD and send Kazumi and Akari to Seattle while fleeing North Korean operatives.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The orbital hotel and ISS are referenced. The Wyvern orbital hotel is actively being occupied by the Smarks.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital objects are in LEO. The discussion focuses on space tethers at 350 km altitude.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Kurosaki discusses how Japanese engineers leave for China due to lack of opportunity, reflecting Earth-normal professional dynamics extending into space work.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The international team communicates in a mix of Japanese and English. Sekiguchi demonstrates fluency in Korean and Chinese. They draft an email to NORAD in English.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter focuses on Earth-based espionage and planning. Space conditions are discussed analytically but not directly experienced.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks are in orbit. All main characters are Earth-based.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Japan's IGS spy satellites, NORAD, and Chinese safe houses all represent national interests extending into orbital affairs. Shiraishi previously worked for JAXA before going to China.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The team discovers Shiraishi tracked them via JAXA's MDM system. Akari reveals Shiraishi is her uncle. The connection between Shiraishi, JAXA, and the space tethers deepens the espionage thriller.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Civilians Kazumi and Akari, JAXA officials Kurosaki and Sekiguchi, and intelligence infrastructure (Chinese safe house, North Korean agents) all feature.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The chapter revolves around mobile device management hacking, shadow-ware tracking, PGP-encrypted emails, and the team's digital operational security.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is referenced but all action takes place on Earth.",
    },
    {
        "chapter": "Chapter 7 - War",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "The team splits: Kazumi and Akari go to Seattle under NORAD protection, Kurosaki and Sekiguchi head to Tehran. The CIA monitors Freeman's movements. Shiraishi plans to bring the Rod from God within range of the orbital hotel.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Judy's blog describes the orbital hotel's water shielding, cosmic radiation (2 microsieverts in two days), and seeing cosmic rays with closed eyes. The orbital hotel is a temporary tourist facility.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All activity is at 350 km LEO. Judy describes being protected by Earth's magnetic field at that altitude.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Judy blogs casually about her age, makeup concerns, and NDA violations while in orbit. Earth social norms persist completely.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Kazumi struggles with English in Seattle. Daryl (Indonesian-American) and Kazumi communicate across language barriers. Sekiguchi speaks fluent Korean, Persian, and Chinese.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Judy describes cosmic radiation striking her retina behind closed eyes, 150x higher radiation than Earth's surface, and the absolute dependence on the thin hotel walls for survival in vacuum.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks are in orbit. Judy notes the historic nature of their commercial space journey.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The CIA reads NORAD's PGP-encrypted emails from JAXA. Freeman is dispatched to protect Japanese civilians. National intelligence apparatus drives orbital affairs.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The team flees Japan for Seattle while hunted by North Korean agents. Shiraishi plans to weaponize the Rod from God deception. Judy describes the visceral reality of cosmic radiation exposure.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Daryl (NORAD military) escorts civilians Kazumi and Akari. CIA agents Bruce and Chris monitor from the background. Judy is a civilian journalist in orbit.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is experienced through Judy's blog, data analysis, and the intelligence community's surveillance networks. The team shops at Costco for Raspberry Pis and DIY equipment to build an analysis center.",
        "q12": "Very different (human bodies/technology constantly challenged)",
        "q12_justification": "Judy describes cosmic rays physically striking her retina, radiation 150x Earth levels, the necessity of water shielding, and the razor-thin margin between life and death in the vacuum beyond one foot of wall.",
    },
    {
        "chapter": "Chapter 8 - The Team",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Chris formally establishes Team Seattle with a CIA operations center. Shiraishi reveals he has real-time video from space tethers. The team begins systematic analysis of the tethercraft hypothesis. Strategic positioning between multiple intelligence agencies intensifies.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Wyvern orbital hotel is occupied by the Smarks. Space tethers orbit as unmanned craft. No permanent settlements exist.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All activity is in LEO. The space tethers and orbital hotel are at approximately 350 km altitude.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Chris runs the operations center like a standard CIA field office. The team dynamic mirrors any multinational professional collaboration.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Kazumi's limited English is accommodated by the team. Chris coaches him on American communication styles. Akari speaks stiff but uninhibited English.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter focuses on Earth-based team building and planning. Space conditions are not directly depicted.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks are in orbit. The chapter focuses on Earth-based analysis of orbital threats.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The CIA, NORAD, and North Korean intelligence all compete over orbital affairs. National security apparatus drives the response to the space tether threat.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Chris establishes the mission framework for countering the orbital threat. Shiraishi reveals stunning real-time Earth video from 40,000 space tether cameras, showing the terrifying scope of North Korea's orbital capability.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "CIA agent Chris leads the team. NORAD's Daryl provides military expertise. Civilians Kazumi and Akari provide technical analysis. The domain is thoroughly mixed.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The operations center is built from Raspberry Pis, Wi-Fi equipment, and DIY electronics. Space tethers are analyzed through data processing. Shiraishi's Earth video is stitched from 40,000 cameras using crowdsourced code.",
        "q12": "Other / Unsure",
        "q12_justification": "Space conditions are discussed analytically but not directly experienced in this chapter.",
    },
    {
        "chapter": "Chapter 9 - Great Leap",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Ozzy joins Team Seattle after seeing Judy's defiant broadcast. The Rod from God approaches the orbital hotel. Judy delivers a powerful televised speech challenging the unknown threat. Ricky and Madu prepare for Operation Seed Pod.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Smarks occupy the orbital hotel. SAFIR 3's second stage approaches in a rendezvous orbit. The ISS is nearby. All are temporary presences.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital activity is in LEO at 350 km.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Judy gives a live TV broadcast from orbit that plays in bars across America. The cultural response is entirely Earth-normal: cheering crowds, raised glasses.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "Ozzy (Australian accent), Kazumi (limited English), Daryl (Indonesian-American), Chris and Bruce (American), and Friday (Somali) all communicate in English with varying fluency.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Judy acknowledges that beyond one foot of wall is vacuum, that the smallest hole would be fatal, and that an unknown object is approaching their fragile orbital habitat.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks and their small crew are in orbit. Judy's broadcast emphasizes the historic and rare nature of their position.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The US military prepares Operation Seed Pod. North Korea manipulates orbital objects. International audiences watch Judy's broadcast. Earth geopolitics drives orbital events.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Judy's defiant broadcast from the orbital hotel, with an unknown weapon approaching, creates high drama. Ricky and Madu prepare to fly into the stratosphere to destroy the threat. Ozzy confronts his guilt over creating the Rod from God hoax.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Judy and Ronnie are civilians under threat. Ricky and Madu are military pilots. Ozzy and Friday are civilians. Bruce and Chris are CIA. The domain is thoroughly mixed.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Ozzy's radar data drives discovery. The team connects via CIA encrypted video calls. Live television broadcast from orbit creates a networked global event.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Judy describes floating in zero gravity, the dangers of vacuum, and the psychological impact of having an unknown orbital weapon approach, but the hotel makes conditions survivable.",
    },
    {
        "chapter": "Chapter 10 - Riot",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "Team Seattle confirms 40,000 space tethers in three separate Clouds. Kazumi predicts their targets: Japanese IGS satellites, the Wyvern return craft, and the orbital hotel. Kurosaki and Sekiguchi arrive in Tehran amid student demonstrations. Shiraishi discovers he was deceived by Sekiguchi's phone trick.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The orbital hotel, ISS, and various satellites represent temporary orbital presence. No permanent space settlements exist.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital activity is in LEO. The Clouds target objects at various LEO altitudes.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Space activity is entirely driven by Earth geopolitics. The student demonstration for internet freedom in Tehran parallels the orbital struggle.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The multinational team communicates in English. Sekiguchi speaks Persian in Tehran. Kazumi occasionally slips into Japanese. Chance speaks Korean with the Cyber Front.",
        "q6": "Harsh and resource-intensive",
        "q6_justification": "Chris notes that the space tethers could rip the orbital hotel to shreds. Terminal apparatuses move many times faster than bullets and could pierce the hotel's shell.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks and ISS crew are in orbit. The vast majority of characters are Earth-based.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Japan's IGS satellites, the Chinese Tiangong-2, NORAD's defense radars, and North Korea's space tethers all represent national interests in orbit.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The revelation of 40,000 space tethers targeting multiple orbital assets creates existential threat. Kazumi's uncanny ability to predict orbital movements adds tension. Shiraishi discovers he has been outmaneuvered and plans retaliation.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "CIA, NORAD, JAXA officials, civilian engineers, North Korean intelligence, and student demonstrators in Tehran all participate in the unfolding crisis.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The team uses Raspberry Pi clusters to process Sampson-5 radar data, projecting orbital objects on a 3D globe. Internet freedom demonstrations in Tehran mirror the theme of information warfare.",
        "q12": "Moderately different (regular adaptation needed)",
        "q12_justification": "The space tethers operate in an environment where terminal apparatuses move at kilometers per second, objects follow complex orbital mechanics, and debris poses constant threat. The orbital hotel requires specialized protection.",
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

print('Done batch 2.')
