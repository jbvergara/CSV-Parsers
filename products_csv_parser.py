import csv
import requests

url = input("Please enter the URL of the CSV file: ")
filename = url.split('/')[-1]
filename = filename.split('.')[0]
r = requests.get(url)
open(filename, 'wb').write(r.content)

with open(filename, 'r') as csv_file:
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

with open(filename + '_parsed.csv', 'w') as gen_csv:
    writer = csv.writer(gen_csv)
    writer.writerow(fieldnames)
    for item in listoflists:
        writer.writerow(item)

        