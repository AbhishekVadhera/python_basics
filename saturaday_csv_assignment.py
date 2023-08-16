import csv

with open('file.csv', 'r') as file:
    read_file = csv.reader(file)
    data_list = list(read_file)
print(data_list)

words = input('type your words : ')
words = words.split(',')
for rows in data_list:
    if words[0] == rows[0] and words[1] == rows[1]:
        rows[2] = words[2]
        print('csv updated with input value')
        break
else:
    data_list.append(words)
    print('input value doesn exist ,added as new value ')

with open('file.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    for rows in data_list:
        writer.writerow(rows)
