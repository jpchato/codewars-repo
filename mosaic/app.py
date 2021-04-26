import csv

students = []
marks = []
courses = []
tests = []

with open('mosaic/students.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        students.append(line)

with open('mosaic/marks.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        marks.append(line)

with open('mosaic/courses.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        courses.append(line)

with open('mosaic/tests.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        tests.append(line)

