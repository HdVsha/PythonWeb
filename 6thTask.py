import csv

#In my table.csv i used commas because it is a CSV file, so i didn't explicitly use "delimiter ;"

with open('table.csv', 'r') as csvfile:
    data = list(csv.reader(csvfile))

data.insert(2, [-200, -200, -200, -200])
with open("middle_row.csv", 'w') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerow(line)

