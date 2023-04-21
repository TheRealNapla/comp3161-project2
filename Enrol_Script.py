import csv
import os
import random

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

courses = []


openFile2 = open( "Course.csv", "r")
csvreader = csv.reader(openFile2)

first = True
for row in csvreader:
    if first == True:
        first = False
        continue
    courses.append(row[0].strip())

with open('Enrol.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["StudentID", "CourseID"])
    for studentid in range(100000):

        num_courses = random.randint(3,6)
        choices = random.sample(range(0, len(courses)), num_courses)
        course_choices = []
        for choice in choices:
            writer.writerow([studentid, courses[choice]])
