from faker import Faker
import csv
import random
import secrets
import string

#Student (Student_ID, name, email, password)
#Course Maintainer/Lecturer (UserID, name, email, password, course_ID)


fake = Faker()
ids = set()
while len(ids) < 100001:
    id = random.randint(100000,999999) 
    id1 = "1" + str(id)
    ids.add(int(id1))
ids1 = list(ids)

cids = set()
while len(cids) <= 100:
    cid = random.randint(100000,999999) 
    cid1 = "7" + str(cid)
    cids.add(int(cid1))
cids1 = list(cids)

with open("Students.csv", "w", newline='') as data:
    writer = csv.writer(data)
    writer.writerow(["ID","Name","Email","Password"])
    for i in range(100001):
        name = fake.first_name() + ' ' + fake.last_name()
        domain= fake.domain_name()
        email = name.lower().replace(' ','.') + '@' + domain
        pchars= string.ascii_letters + string.digits
        password = ''.join(secrets.choice(pchars) for i in range(10))
        writer.writerow([int(ids1[i]),name,email,password])
    print(" Student File Created")
    
with open("Lecturer.csv", "w", newline='') as data:
    writer = csv.writer(data)
    writer.writerow(["ID","Name","Email","Password"])
    for j in range(100):
        name = fake.first_name() + ' ' + fake.last_name()
        domain= fake.domain_name()
        email = name.lower().replace(' ','.') + '@' + domain
        pchars= string.ascii_letters + string.digits
        password = ''.join(secrets.choice(pchars) for i in range(10))
        writer.writerow([int(cids1[j]),name,email,password])
    print("Lecturer File Created")

#Course (Course_id, Coursename, CourseLecturer, Coursegrade)
with open("Courses.csv", "w", newline='') as data:
    courselist = []
    coursenamelst = set()
    coursecodelst = set()
    writer = csv.writer(data)
    writer.writerow(["Course_id","Coursename","CourseLecturer","Coursegrade"])
    for i in range(130):
        # Generate a random course code
        code = ['COMP', 'INFO','SWEN']
        course_code = ''.join(random.choice(code)) + ''.join(random.choices(string.digits, k=3))

        # Generate a random course name
        prefixes = ['Introduction to', 'Advanced', 'Fundamentals of', 'Principles of', 'Applied', 'Exploring']
        topics = ['Data Science', 'Artificial Intelligence', 'Web Development', 'Cybersecurity', 'Cloud Computing', 'Robotics']
        suffixes = ['with Python', 'using Java', 'in C++', 'for Beginners', 'for Professionals', 'and Machine Learning']
        course_name = f"{random.choice(prefixes)} {random.choice(topics)} {random.choice(suffixes)}"
        if course_code not in coursecodelst and course_name not in coursenamelst:
            coursecodelst.add(course_code)
            coursenamelst.add(course_name)
            writer.writerow([course_code,course_name,"",0])

    for i in range(110):
    # Generate a random course code
        code1 = ['SOCI', 'GOVT','SOWK']
        course_code1 = ''.join(random.choice(code1)) + ''.join(random.choices(string.digits, k=3))

        # Generate a random course name
        prefixes1 = ['Introduction to', 'Foundations of', 'Key Concepts in', 'Theories of', 'Research Methods in', 'Comparative Studies of']
        topics1 = ['Sociology', 'Psychology', 'Anthropology', 'Political Science', 'Economics', 'Geography']
        suffixes1 = ['for Beginners', 'for Advanced Students', 'for Professionals', 'in Contemporary Society', 'in Global Perspective']
        course_name1 = f"{random.choice(prefixes1)} {random.choice(topics1)} {random.choice(suffixes1)}"
        if course_code1 not in coursecodelst and course_name1 not in coursenamelst:
            coursecodelst.add(course_code1)
            coursenamelst.add(course_name1)
            writer.writerow([course_code1,course_name1,"",0])
    print("Course File Created")


    
