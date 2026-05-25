import csv, json

with open('data/questions.json', 'r', encoding='utf-8-sig', errors='replace') as f:
    questions = json.load(f)

valid_options = {}
for q in questions:
    valid_options[q['number']] = q['answer_options']

csv_path = 'data/results/France_Voyage_To_Venus.csv'
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

errors = []
for row in rows:
    chapter = row['chapter']
    for qn in range(1, 13):
        answer = row['q' + str(qn)]
        if answer not in valid_options[qn]:
            errors.append(f"  Chapter '{chapter}', q{qn}: '{answer}' NOT in valid options")

if errors:
    print('VALIDATION ERRORS:')
    for e in errors:
        print(e)
else:
    print('All answers validated successfully!')

print(f'\nTotal chapters: {len(rows)}')
print(f'Total answers checked: {len(rows) * 12}')

print('\nChapters in CSV:')
for row in rows:
    print(f"  {row['chapter']}")
