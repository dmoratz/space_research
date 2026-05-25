import json, csv, os

chapters_data = [
    {
        "chapter": "Prologue",
        "q1": "No contestation",
        "q1_justification": "Jamshed Jahanshah conducts a peaceful balloon experiment in a Tehran suburb to test his space tether propulsion system. No conflict or strategic struggle is depicted.",
        "q2": "Other / Unsure",
        "q2_justification": "The chapter is entirely Earth-based. Jamshed launches balloons from Tehran; no orbital or space territory is depicted.",
        "q3": "Other / Unsure",
        "q3_justification": "No space journey occurs. The action takes place on the ground in Iran.",
        "q4": "Other / Unsure",
        "q4_justification": "No space society is depicted. The chapter portrays everyday life in Tehran.",
        "q5": "Same languages as Earth",
        "q5_justification": "Jamshed speaks Persian and reads English-language scientific literature. Standard Earth languages are used throughout.",
        "q6": "Other / Unsure",
        "q6_justification": "No space environment is depicted. The setting is a Tehran suburb.",
        "q7": "Other / Unsure",
        "q7_justification": "No space habitation is depicted.",
        "q8": "Other / Unsure",
        "q8_justification": "No space governance is depicted.",
        "q9": "Adventure / exploration",
        "q9_justification": "Jamshed's solo balloon experiment to prove his revolutionary propulsion concept is framed as a moment of scientific discovery and personal triumph.",
        "q10": "Entirely civilian",
        "q10_justification": "Jamshed is a civilian scientist conducting research independently. No military presence.",
        "q11": "Other / Unsure",
        "q11_justification": "No space domain is portrayed.",
        "q12": "Other / Unsure",
        "q12_justification": "The setting is entirely Earth-based.",
    },
    {
        "chapter": "Chapter 1 - Erratic Debris",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "SAFIR 3's anomalous orbit is detected by multiple parties. NORAD monitors it, Ozzy publishes the Rod from God theory, and North Korean agents Chance and Shiraishi observe from Seattle. Tensions are building but no open conflict has erupted.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Space is populated only by the ISS and the Wyvern spacecraft preparing for its orbital hotel mission. SAFIR 3 is an empty rocket body. No permanent settlements exist.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital activity occurs in low Earth orbit at 250-500 km altitude. Loki 9 is about to launch to LEO.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Space tourism is just beginning with the Smarks' Wyvern project. Judy Smark blogs as any journalist would. Earth culture is unchanged by space activity.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Japanese (Kazumi), English (Lintz, Ozzy), Korean (Chance), and Persian. No space-specific language variations exist.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter is primarily Earth-based. Space conditions are not directly depicted beyond orbital tracking data.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the ISS crew and the Smarks are in or heading to space. The vast majority of activity is Earth-based.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The US (NORAD), North Korea (SAFIR 3), and private ventures (Smark's Wyvern) all operate in orbit under their respective national frameworks.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The chapter builds suspense through multiple converging plotlines: SAFIR 3's mysterious acceleration, the Rod from God theory, North Korean spies operating in Seattle, and Shiraishi's hidden Cloud operation.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Kazumi is a civilian web developer, Lintz and Freeman are NORAD military, Ozzy is a civilian billionaire, and Chance/Shiraishi are intelligence operatives.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is experienced through data: orbital tracking screens, radar observations, web analytics. Kazumi discovers the anomaly through shooting star forecast data.",
        "q12": "Other / Unsure",
        "q12_justification": "Space conditions are not directly experienced by characters in this chapter; orbital activity is observed remotely from Earth.",
    },
    {
        "chapter": "Chapter 2 - A Proclamation",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "North Korea's Cyber Front corrupts translation engines to make their leader's speech sound threatening. Shiraishi and Chance conduct espionage from Seattle. The CIA shows interest in SAFIR 3. Multiple intelligence operations are underway.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "SAFIR 3 and the upcoming Wyvern orbital hotel represent temporary orbital presence. No permanent space settlements exist.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All referenced orbital activity is in LEO.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Space activity is an extension of Earth geopolitics. The North Korean speech and its translation are purely Earth political affairs.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters use Japanese, English, Korean, and Persian. The chapter's central plot involves mistranslation between Korean and English by corrupted machine translation.",
        "q6": "Other / Unsure",
        "q6_justification": "Space environment is not directly depicted. The chapter focuses on Earth-based espionage and investigation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "No one is shown in space. The Smarks are preparing to launch.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "North Korea operates SAFIR 3, the US monitors through NORAD, and private ventures prepare orbital tourism.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "Shiraishi's spy tradecraft in Seattle, North Korea's sophisticated corpus contamination attack, and Jamshed's desperate attempt to contact Kazumi before Iran cuts internet access create escalating tension.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "JAXA officials Kurosaki and Sekiguchi, CIA agents, civilian Kazumi and Akari, intelligence operatives Shiraishi and Chance, and scientist Jamshed all intersect.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The chapter centers on cyber warfare: translation corpus contamination, web scraping, ad revenue analysis, and internet censorship in Iran.",
        "q12": "Other / Unsure",
        "q12_justification": "Space is referenced but not directly experienced. All action occurs on Earth.",
    },
    {
        "chapter": "Chapter 3 - The Launch",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Akari discovers 10,000+ space tethers around SAFIR 3. CIA contacts Ozzy and visits NORAD. Shiraishi and Chance discuss their Cloud operation. Jamshed tries to reach Kazumi before Iran's internet is cut.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "Loki 9 launches successfully, carrying the Smarks to orbit. The orbital hotel is being prepared. Only temporary visits and stations exist in space.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "Loki 9 reaches LEO at 350 km. All orbital activity is in low Earth orbit.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Judy blogs from the Wyvern exactly as she would from Earth. Space tourism replicates Earth hospitality. No distinct space culture exists.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters communicate in their native languages. Jamshed's video call to Kazumi is in awkward English. No space-specific language.",
        "q6": "Manageable but risky",
        "q6_justification": "Judy's blog describes orbital conditions: free fall, 80% gravity, the thin blue line of atmosphere. The Wyvern's orbital hotel uses water shielding against debris and radiation.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only Ronnie and Judy Smark plus a small crew are in orbit aboard the Wyvern. The ISS crew is the only other human presence.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "Multiple nations operate in orbit: US (NORAD, Smark's private venture), North Korea (space tethers), Iran (Jamshed's research).",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The discovery of 10,000 unknown spacecraft in orbit, CIA and intelligence agency maneuvering, Jamshed's race against Iran's internet shutdown, and the Loki 9 launch create interlocking thriller narratives.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Civilians (Kazumi, Akari, Ozzy, Smarks), military (NORAD), intelligence (CIA, North Korean agents), and scientists (Jamshed) all feature prominently.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is experienced through 150GB of radar data processed into a planetarium visualization, orbital tracking, and internet-mediated communication.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Judy describes free fall, the thin atmosphere visible from orbit, and the need for Miura-folded structures and water shielding, portraying space as different but manageable with technology.",
    },
    {
        "chapter": "Chapter 4 - Standby",
        "q1": "Moderate contestation (ongoing rivalry/disputes)",
        "q1_justification": "Freeman briefs CIA on ASM-140 antisatellite weapon capabilities. Shiraishi and Chance investigate Kazumi and plan disinformation. Kazumi builds a space tether model and contacts JAXA. The UN resolution to eliminate the Rod from God is discussed.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Wyvern orbital hotel is being set up in orbit. Judy blogs about unfolding the hotel structure, checking in, and testing the engine for ISS rendezvous.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital activity is at 350 km LEO. The orbital hotel prepares to rendezvous with the ISS.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Judy's blog describes the orbital hotel as a hospitality experience. Ronnie sets up a wireless router. Earth social norms persist in orbit.",
        "q5": "Same languages as Earth",
        "q5_justification": "Characters speak Japanese, English, and Korean. No space-specific language has developed.",
        "q6": "Manageable but risky",
        "q6_justification": "Judy describes the orbital hotel's triple-layer protection (gold foil, Kevlar, water) against debris and cosmic radiation, and the 150x higher radiation exposure in orbit.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks and their small crew occupy the orbital hotel. Judy describes the hotel check-in as a historic first.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "The US plans Operation Seed Pod through NORAD. Multiple nations' military satellites monitor North America. Space treaties and COPUOS guidelines govern behavior.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "The CIA and NORAD plan to destroy what they believe is an orbital weapon. Shiraishi's intelligence operation investigates Kazumi. The deployment of depleted uranium rounds adds moral tension.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Kazumi and Akari are civilians, Freeman and Lintz are military, Bruce and Chris are CIA, Shiraishi and Chance are intelligence operatives, JAXA officials are bureaucrats.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "Space is analyzed through electromagnetic theory (Lorentz force), data processing, and web analytics. Akari discovers executable code hidden in web advertisements.",
        "q12": "Somewhat different (manageable environmental differences)",
        "q12_justification": "Judy describes zero gravity, radiation exposure, and the need for Whipple bumpers and water shielding, but the orbital hotel makes space comfortable enough for tourism.",
    },
    {
        "chapter": "Chapter 5 - Evasion",
        "q1": "High contestation (frequent conflict or strategic struggle)",
        "q1_justification": "North Korean agents attempt to photograph the team at Fool's Launchpad. Sekiguchi detects the spy and speaks Korean to confirm. The team discovers shadow-ware tracking anyone researching the space tethers. They flee to the Nippon Grand Hotel.",
        "q2": "Visiting / Temporary presence only (stations, missions, outposts)",
        "q2_justification": "The Wyvern orbital hotel and ISS are discussed. Judy's blog describes the hotel's soft-shell spacecraft and water shielding.",
        "q3": "Near-Earth / very short journey",
        "q3_justification": "All orbital objects discussed are in LEO at 350 km.",
        "q4": "Basically Earth society in space",
        "q4_justification": "Space tourism replicates Earth luxury. Judy's blog reads like a travel blog with scientific footnotes.",
        "q5": "Shared lingua franca plus local variation",
        "q5_justification": "The international team (Japanese Kazumi, Korean-speaking Sekiguchi, JAXA's Kurosaki) communicates in a mix of Japanese and English. Sekiguchi speaks Korean to the spy, Akari uses technical English for the translation corpus analysis.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter focuses on Earth-based espionage. Orbital conditions are discussed analytically but not directly experienced.",
        "q7": "Exceptionally rare (few astronauts/explorers)",
        "q7_justification": "Only the Smarks are in orbit. The chapter focuses entirely on Earth-based characters.",
        "q8": "Earth nation-states extend into space",
        "q8_justification": "North Korean cyber operations target space-related information. Japan's IGS spy satellites, NORAD, and the Wyvern all represent national extensions into orbit.",
        "q9": "Thriller / Horror / Survival",
        "q9_justification": "A North Korean spy infiltrates their meeting at Fool's Launchpad. Sekiguchi intercepts the agent's Korean, Akari uncovers the shadow-ware surveillance system, and the team must flee to a Chinese safe house hotel.",
        "q10": "Mixed civilian-military domain",
        "q10_justification": "Civilians Kazumi and Akari work alongside JAXA officials. North Korean intelligence agents, Chinese safe houses, and government bureaucrats all feature.",
        "q11": "Like cyberspace / networked or abstract domain",
        "q11_justification": "The chapter centers on cyber warfare: translation corpus contamination, shadow-ware hidden in advertisements, cross-site scripting vulnerabilities exploited across 300,000 websites.",
        "q12": "Other / Unsure",
        "q12_justification": "Space conditions are mentioned analytically but the chapter's action is entirely Earth-based.",
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

print('Done batch 1.')
