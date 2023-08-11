import csv

with open('sample_csv.csv', 'r') as file:
    read_file = csv.reader(file)
    conversion = list(read_file)
    print(conversion)

for i, rows in enumerate(conversion):
    # print(rows[0])
    if "abhishek" in rows:
        print('yes')