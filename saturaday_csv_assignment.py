import csv

with open('file.csv', 'r') as saturday_csv_assignment:
    read_file = csv.reader(saturday_csv_assignment)
    conversion = list(read_file)

checking_word = input('type your answer : ')
for i, rows in enumerate(conversion):
    if checking_word not in rows:
        print(conversion)
