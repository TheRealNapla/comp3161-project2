import csv
import os
import random

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

courses = []
studentid=[]

openFile2 = open( "Courses.csv", "r")
csvreader = csv.reader(openFile2)

openFile3 = open( "Students.csv", "r")
csvreader1 = csv.reader(openFile3)

first = True
for row in csvreader:
    if first == True:
        first = False
        continue
    courses.append(row[0].strip())

first = True
for row in csvreader1:
    if first == True:
        first = False
        continue
    studentid.append(row[0].strip())

with open('Enrol.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Student_ID", "Course_ID","Grade"])
    for student in studentid:
        num_courses = random.randint(3,6)
        choices = random.sample(range(0, len(courses)), num_courses)
        course_choices = []
        for choice in choices:
            writer.writerow([student, courses[choice],random.randint(0,100)])