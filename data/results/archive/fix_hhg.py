import csv, os

csv_path = "data/results/US_The_Hitchhikers_Guide_to_the_Galaxy_Omnibus_A_Trilogy_of_Five_Part_1_up_to_chapter_26.csv"

# Read all rows
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    fieldnames = reader.fieldnames
    rows = list(reader)

# Remove all Part 3 rows (we'll re-add them with correct options)
rows = [r for r in rows if not r['chapter'].startswith('Part 3')]

# Fix Part 2 Chapter 19 and 20 q12 (used q6 option by mistake)
for row in rows:
    if row['chapter'] == 'Part 2 Chapter 19':
        row['q12'] = 'Very different (human bodies/technology constantly challenged)'
        row['q12_justification'] = 'Frogstar World B is a hostile, alien dump. The characters face extreme environmental conditions completely unlike Earth.'
    elif row['chapter'] == 'Part 2 Chapter 20':
        row['q12'] = 'Very different (human bodies/technology constantly challenged)'
        row['q12_justification'] = 'Frogstar World C and the Haggunenon ship represent environments fundamentally challenging to human existence.'

# Rewrite CSV without Part 3 rows
with open(csv_path, 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f'Wrote {len(rows)} rows (Part 3 removed, Part 2 fixes applied)')
print('Now run batch 7 and 8 with corrected options.')
