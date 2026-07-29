import csv

employees = []

with open("../csv/employees.csv", "r") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        employees.append(row)

# Create full names
names = [
    row[1] + " " + row[2]
    for row in employees[1:]
]

print(names)

# Keep only names containing "e"
filtered_names = [
    name
    for name in names
    if "e" in name
]

print(filtered_names)