import json, csv, os

chapters_data = [
    {
        "chapter": "Part 2 Chapter 25",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Arthur despairs at the Golgafrinchans ruining prehistoric Earth. Ford discovers the cavemen's Scrabble tiles may spell out the Ultimate Question. The conflicts are philosophical.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Golgafrinchan colonization of Earth continues. The broader galactic civilization persists in the background.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Arthur and Ford remain stranded two million years in the past. Their separation from their own time is permanent.",
        "q4": "Radically different / alien social order",
        "q4_justification": "The Golgafrinchans have displaced the native cavemen and are ruining Earth's intended program as a computer. Alien colonists have overwritten Earth's purpose.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication between Arthur, Ford, and the Golgafrinchans continues via Babel fish.",
        "q6": "Manageable but risky",
        "q6_justification": "Prehistoric Earth is habitable but primitive. Arthur and Ford must adapt to life without technology.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Golgafrinchan colonization is a casual byproduct of normal galactic migration. Interstellar colonization is routine.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Golgafrinchan colonists, cavemen, and the broader galactic civilization represent distinct groups.",
        "q9": "Comedy / satire",
        "q9_justification": "The Ultimate Question may be 'What do you get if you multiply six by nine?' which doesn't equal 42. The revelation that the Golgafrinchans corrupted Earth's program is darkly satirical.",
        "q10": "Entirely civilian",
        "q10_justification": "Colonists and stranded travelers on prehistoric Earth. No military elements.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter depicts the consequences of colonial expansion: indigenous programs overwritten, original purposes lost.",
        "q12": "Almost Earth-like",
        "q12_justification": "The setting is prehistoric Earth. The environment is Earth by definition."
    },
    {
        "chapter": "Part 2 Chapter 26",
        "q1": "No contestation",
        "q1_justification": "Ford and Arthur are alone on prehistoric Earth. Ford spots a spaceship in the sky, signaling a possible rescue. The chapter is contemplative and hopeful.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "A spaceship passing over prehistoric Earth implies the galaxy continues to be populated and traveled. Galactic civilization persists above.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Arthur and Ford are marooned two million years in the past. The passing spaceship represents their only link to galactic civilization.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Arthur has adapted to primitive life on prehistoric Earth while retaining memories of galactic civilization. His culture is a hybrid of Earthman and galactic hitchhiker.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Arthur and Ford communicate freely. The Babel fish continues to function.",
        "q6": "Manageable but risky",
        "q6_justification": "Life on prehistoric Earth is primitive but survivable. Arthur and Ford have adapted to basic conditions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "A spaceship casually passing over prehistoric Earth demonstrates that galactic travel is routine even above uncontacted worlds.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The passing spaceship represents galactic civilization. Arthur and Ford represent displaced individuals from that civilization.",
        "q9": "Comedy / satire",
        "q9_justification": "Arthur has made friends with a caveman. Ford is desperate to leave. The contrast between cosmic adventure and primitive life is comedic.",
        "q10": "Entirely civilian",
        "q10_justification": "Two stranded civilians on prehistoric Earth. No military elements.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Arthur and Ford are castaways on an uncontacted world, mirroring frontier isolation narratives.",
        "q12": "Almost Earth-like",
        "q12_justification": "The setting is prehistoric Earth. The environment is Earth."
    },
    {
        "chapter": "Part 2 Chapter 27",
        "q1": "No contestation",
        "q1_justification": "An interlude chapter describing the Guide entry on the planet Golgafrincham and the fate of those who stayed behind. No active conflict.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Golgafrincham is described as a settled world with a full civilization that sent three ark fleet ships into space.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The ark fleet ships traveled vast interstellar distances. Golgafrincham is far from Earth across the galaxy.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Golgafrincham divided its population into thirds and sent the 'useless' third away. The remaining population then died from a disease contracted from a dirty telephone.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The Guide entry describes Golgafrinchan civilization without language barriers.",
        "q6": "Other / Unsure",
        "q6_justification": "The chapter is a Guide entry. No direct environmental conditions are experienced by characters.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Ark fleet ships carrying millions of colonists are described as routine technology. Mass interstellar migration is normal.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Golgafrincham's three fleet divisions represent distinct social/political groupings.",
        "q9": "Comedy / satire",
        "q9_justification": "Golgafrincham's remaining population died from a disease contracted from a dirty telephone, after sending away all their telephone sanitizers. The irony is devastating satire.",
        "q10": "Entirely civilian",
        "q10_justification": "The Guide entry describes civilian society and migration. No military elements.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Ark fleet ships colonizing new worlds is explicitly colonial expansion on an interstellar scale.",
        "q12": "Other / Unsure",
        "q12_justification": "The chapter is a Guide entry without direct environmental description."
    },
    {
        "chapter": "Part 2 Chapter 28",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "The Golgafrinchans continue their dysfunctional colonization. They hold committee meetings about reinventing fire and the wheel. Arthur observes with despair.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The Golgafrinchans occupy prehistoric Earth. Their origins from a galaxy-spanning civilization imply extensive territorial occupation.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "The colonists are permanently settled two million years in the past. Return to their origin world is impossible.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Alien colonists hold committee meetings about fire while surrounded by a forest they could burn. Their bureaucratic social order persists despite the primitive setting.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication between species continues seamlessly via Babel fish.",
        "q6": "Manageable but risky",
        "q6_justification": "Prehistoric Earth is habitable but the Golgafrinchans' incompetence makes basic survival unnecessarily difficult.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The Golgafrinchans treat their colonial situation as normal, applying familiar bureaucratic processes to primitive conditions.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The Golgafrinchan colony and the native cavemen represent distinct populations.",
        "q9": "Comedy / satire",
        "q9_justification": "Committee meetings about fire and the wheel satirize corporate culture. The Golgafrinchans cannot accomplish basic tasks because they keep forming subcommittees.",
        "q10": "Entirely civilian",
        "q10_justification": "Civilian colonists holding meetings. No military elements.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Failed colonial expansion: colonists unable to adapt to frontier conditions despite advanced origins.",
        "q12": "Almost Earth-like",
        "q12_justification": "Prehistoric Earth. The environment is literally Earth."
    },
    {
        "chapter": "Part 2 Chapter 29",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Arthur tries to help the Golgafrinchans but gives up. Ford experiments with Scrabble tiles and cavemen. The conflicts are minor and social.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The colonial situation on prehistoric Earth continues. The broader galactic context persists in memory.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Arthur and Ford remain stranded two million years in Earth's past with no means of escape.",
        "q4": "Radically different / alien social order",
        "q4_justification": "Ford uses Scrabble tiles to try to extract the Ultimate Question from cavemen's brains, treating human consciousness as a readout device for a cosmic computer.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication between Arthur, Ford, and the various groups continues via Babel fish.",
        "q6": "Manageable but risky",
        "q6_justification": "Prehistoric Earth is habitable. The challenges are social and existential rather than environmental.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Even stranded in prehistory, the characters retain knowledge of galactic civilization as normal background.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "Golgafrinchan colonists, cavemen, and the memory of galactic civilization represent distinct groups.",
        "q9": "Comedy / satire",
        "q9_justification": "Ford's attempt to extract the Ultimate Question using Scrabble tiles yields results like 'WHAT DO YOU GET IF YOU MULTIPLY SIX BY NINE.' The mathematical error is deliberately satirical.",
        "q10": "Entirely civilian",
        "q10_justification": "Stranded civilians and primitive humans. No military elements.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "The chapter continues the frontier theme: civilized beings adapting (or failing to adapt) to primitive conditions.",
        "q12": "Almost Earth-like",
        "q12_justification": "Prehistoric Earth. The environment is Earth."
    },
    {
        "chapter": "Part 2 Chapter 30",
        "q1": "No contestation",
        "q1_justification": "Arthur has adapted to life on prehistoric Earth. He makes sandwiches and lives peacefully. Ford spots something in the sky. The chapter is contemplative.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Ford's attention to the sky suggests spaceships and galactic civilization continue above prehistoric Earth.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Arthur and Ford have been stranded for an extended period. The separation from their time and civilization is seemingly permanent.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Arthur combines Earth cooking skills with prehistoric ingredients. His culture is a practical hybrid of modern knowledge and primitive resources.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Arthur and Ford communicate normally. The Babel fish persists.",
        "q6": "Manageable but risky",
        "q6_justification": "Arthur has adapted to prehistoric life. He can make food and survive, though conditions are primitive.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Ford's expectation of spotting spaceships implies that galactic traffic near Earth is routine.",
        "q8": "Other / Unsure",
        "q8_justification": "On prehistoric Earth, political structures are irrelevant to the characters' immediate situation.",
        "q9": "Comedy / satire",
        "q9_justification": "Arthur's greatest achievement in prehistory is inventing the sandwich. The mundanity of his adaptation is comedic.",
        "q10": "Entirely civilian",
        "q10_justification": "Two stranded civilians living peacefully on prehistoric Earth.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Arthur's adaptation to frontier life, making do with primitive resources, mirrors frontier survival narratives.",
        "q12": "Almost Earth-like",
        "q12_justification": "Prehistoric Earth. The environment is Earth."
    },
    {
        "chapter": "Part 2 Chapter 31",
        "q1": "No contestation",
        "q1_justification": "Arthur lives peacefully on prehistoric Earth. The chapter describes his simple daily life and philosophical reflections on his situation.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The broader galactic context persists in Arthur's memories and in Ford's continued attention to the sky.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Arthur remains stranded in deep prehistory, permanently separated from galactic civilization.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Arthur lives as a primitive but retains his modern sensibilities. His culture blends English gentility with prehistoric conditions.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Communication continues via Babel fish between Arthur, Ford, and any beings they encounter.",
        "q6": "Manageable but risky",
        "q6_justification": "Prehistoric Earth is habitable. Arthur has adapted to basic living conditions.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The knowledge that galactic civilization exists and is routine remains part of the characters' worldview.",
        "q8": "Other / Unsure",
        "q8_justification": "Political structures are irrelevant to the characters' isolated situation.",
        "q9": "Comedy / satire",
        "q9_justification": "Arthur's peaceful acceptance of prehistoric life is both touching and absurd. His domestic concerns in the Stone Age are comedic.",
        "q10": "Entirely civilian",
        "q10_justification": "Peaceful civilian existence on prehistoric Earth.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Arthur living on the frontier of civilization, adapting to primitive conditions with modern knowledge.",
        "q12": "Almost Earth-like",
        "q12_justification": "Prehistoric Earth. Literally Earth."
    },
    {
        "chapter": "Part 2 Chapter 32",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Ford convinces Arthur they need to leave prehistoric Earth. Ford has spotted a way to escape. Minor disagreements about leaving.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Ford's plan to escape implies the galaxy remains full of settled worlds and travel opportunities.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Escaping prehistoric Earth requires bridging two million years of temporal distance and unknown spatial distances.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Arthur reluctantly leaves his adapted prehistoric life to rejoin galactic civilization. The transition between cultures is jarring.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Arthur and Ford communicate freely as they plan their escape.",
        "q6": "Manageable but risky",
        "q6_justification": "The escape plan involves risk and uncertainty, but the immediate conditions are not life-threatening.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Ford's confidence that they can rejoin galactic civilization reflects how normalized space travel is.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The galactic civilization Ford aims to rejoin comprises multiple distinct polities.",
        "q9": "Comedy / satire",
        "q9_justification": "Arthur's reluctance to leave prehistoric Earth for the dangers of space travel is comedically perverse. Ford's eagerness contrasts with Arthur's contentment.",
        "q10": "Entirely civilian",
        "q10_justification": "Two civilians planning escape from prehistoric Earth. No military elements.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Leaving a frontier settlement to return to civilization mirrors reverse colonial narratives.",
        "q12": "Almost Earth-like",
        "q12_justification": "Still on prehistoric Earth. The environment is Earth."
    },
    {
        "chapter": "Part 2 Chapter 33",
        "q1": "Low contestation (minor competition, little open conflict)",
        "q1_justification": "Arthur and Ford prepare to leave prehistoric Earth. They say goodbye to their cave and possessions. The mood is bittersweet rather than confrontational.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "The coming departure implies returning to a galaxy full of settled worlds.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "They are about to leave prehistoric Earth to travel across time and space. The journey represents extreme distances.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Arthur has become a hybrid: a modern Englishman adapted to prehistoric cave life, about to rejoin galactic civilization.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "Arthur and Ford communicate normally as they prepare to depart.",
        "q6": "Manageable but risky",
        "q6_justification": "Leaving prehistoric Earth involves the uncertainty of space travel, but the immediate conditions are safe.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "The expectation of catching a spaceship or finding a way off the planet reflects normalized galactic travel.",
        "q8": "Other / Unsure",
        "q8_justification": "Political structures are not discussed in this transitional chapter.",
        "q9": "Comedy / satire",
        "q9_justification": "Arthur's sentimental attachment to his cave and his prehistoric sandwich-making skills is comedic. The absurdity of leaving Earth voluntarily after it was destroyed is darkly funny.",
        "q10": "Entirely civilian",
        "q10_justification": "Two civilians leaving their temporary home. No military elements.",
        "q11": "Like the frontier / colonial expansion",
        "q11_justification": "Departing a frontier settlement for the wider galaxy mirrors reverse frontier narratives.",
        "q12": "Almost Earth-like",
        "q12_justification": "Still on prehistoric Earth. The environment is Earth."
    },
    {
        "chapter": "Part 2 Chapter 34",
        "q1": "No contestation",
        "q1_justification": "Arthur and Ford depart prehistoric Earth. The chapter concludes Part 2 with their escape and sets up their next adventure. No active conflict.",
        "q2": "Extensive territorial occupation (many settled worlds/regions held like states or empires)",
        "q2_justification": "Their departure back into the galaxy implies returning to a universe of extensive settlement and civilization.",
        "q3": "Extreme / effectively unreachable (generational, completely separate, or one-way-feeling distance)",
        "q3_justification": "Leaving prehistoric Earth involves crossing two million years of time and unknown spatial distances to rejoin galactic civilization.",
        "q4": "Mixed / hybrid culture",
        "q4_justification": "Arthur transitions from prehistoric life back to galactic hitchhiking. His cultural identity is now permanently hybrid.",
        "q5": "Translation-mediated communication (universal translator / communication tech makes language difference irrelevant)",
        "q5_justification": "The Babel fish continues to function as they depart for new encounters.",
        "q6": "Manageable but risky",
        "q6_justification": "The departure involves uncertainty about where they'll end up, but no immediate survival threat.",
        "q7": "Normalized / widespread (space habitation is ordinary for humanity)",
        "q7_justification": "Returning to galactic civilization from a marooned situation is treated as a matter of catching the right ride.",
        "q8": "Multiple distinct space polities",
        "q8_justification": "The galaxy they are returning to contains many distinct civilizations and political entities.",
        "q9": "Comedy / satire",
        "q9_justification": "The conclusion of Part 2 maintains the comedic tone: Arthur's adventures continue from one absurd situation to the next.",
        "q10": "Entirely civilian",
        "q10_justification": "Two civilian hitchhikers departing on a new journey. No military elements.",
        "q11": "Totally unique domain",
        "q11_justification": "Hitchhiking through time and space from prehistoric Earth characterizes the domain as uniquely absurd.",
        "q12": "Other / Unsure",
        "q12_justification": "The chapter is transitional. No specific space environment is depicted beyond the departure from Earth."
    }
]

country = 'US'
book_title = "The Hitchhiker's Guide to the Galaxy Omnibus_ A Trilogy of Five (Part 1 up to chapter 26)"
csv_path = "data/results/US_The_Hitchhikers_Guide_to_the_Galaxy_Omnibus_A_Trilogy_of_Five_Part_1_up_to_chapter_26.csv"
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

print('Done batch 6.')
