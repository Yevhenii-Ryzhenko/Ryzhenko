import csv

unique_rows = set()
header = None

with open('random.csv', newline='') as f1:
    reader1 = csv.reader(f1, delimiter=';')
    header = next(reader1)
    for row in reader1:
        unique_rows.add(tuple(row))

with open('random-michaels.csv', newline='') as f2:
    reader2 = csv.reader(f2, delimiter=';')
    next(reader2)
    for row in reader2:
        unique_rows.add(tuple(row))

with open('ryzhenko.csv', 'w', newline='', encoding='utf-8') as f_out:
    writer = csv.writer(f_out, delimiter=';')
    writer.writerow(header)
    for row in sorted(unique_rows):
        writer.writerow(row)
