import csv

user_input = input("Please enter CSV filename: ")
filename = user_input + '.csv'

with open(filename, 'r', newline='') as csv_file:
    row1 = csv.reader(csv_file)
    fieldnames = next(row1)
    table = csv.DictReader(csv_file, fieldnames = fieldnames)
    listoflists = []
    for row in table:
        if row['Categories'] != '':
            buff = []
            for field in fieldnames:
                buff.append(row[field])
            listoflists.append(buff)

with open(user_input + '_parsed.csv', 'w') as gen_csv:
    writer = csv.writer(gen_csv)
    writer.writerow(fieldnames)
    for item in listoflists:
        writer.writerow(item)

        