import csv
studentfile = "Students.csv"
sqlfile = "studentsinsertvalues.sql"

lecturerfile = "Lecturer.csv"
sqlfile1 = "lecturersinsertvalues.sql"

coursesfile = "Courses.csv"
sqlfile2 = "coursesinsertvalues.sql"

enrolfile = "Enrol.csv"
sqlfile3 = "enrolinsertvalues.sql"

calendarfile = "fakeEventsData.csv"
sqlfile4 = "calendarinsertvalues.sql"

with open(calendarfile,"r") as calendarfile:
    custreader = csv.reader(calendarfile)
    titles = next(custreader)
    fields = ", ".join(titles)
    #print(fields)
    values = []
    for value in custreader:
        values.append("("+",".join("'"+str(cell).replace("'","''")+"'" for cell in value)+")")
    
    createdatabase = f"USE BetterOurvle;\nCREATE TABLE CalendarEvents (Event_no int,Event_name varchar(255) CHARACTER SET utf8, Event_date DATETIME,Course_ID VARCHAR(7) CHARACTER SET utf8); \nINSERT INTO CalendarEvents ({fields}) VALUES\n{','.join(values)};"

    with open(sqlfile4,"w") as sql_file:
        sql_file.write(createdatabase)
print("SQL commands have been wirtten to Calendar")

with open(enrolfile,"r") as enrolfile:
    custreader = csv.reader(enrolfile)
    titles = next(custreader)
    fields = ", ".join(titles)
    #print(fields)
    values = []
    for value in custreader:
        values.append("("+",".join("'"+str(cell).replace("'","''")+"'" for cell in value)+")")
    
    createdatabase = f"USE BetterOurvle;\nCREATE TABLE Enrol (Student_ID int, Course_ID varchar(255), Grade int); \nINSERT INTO Enrol ({fields}) VALUES\n{','.join(values)};"

    with open(sqlfile3,"w") as sql_file:
        sql_file.write(createdatabase)
print("SQL commands have been wirtten to Enrol")
with open(studentfile,"r") as studentfile:
    custreader = csv.reader(studentfile)
    titles = next(custreader)
    fields = ", ".join(titles)
    #print(fields)
    values = []
    for value in custreader:
        values.append("("+",".join("'"+str(cell).replace("'","''")+"'" for cell in value)+")")
    
    createdatabase = f"USE BetterOurvle;\nCREATE TABLE Students (ID int, Name varchar(255), Email varchar(125),Password varchar(255), PRIMARY KEY (ID)); \nINSERT INTO Students ({fields}) VALUES\n{','.join(values)};"

    with open(sqlfile,"w") as sql_file:
        sql_file.write(createdatabase)
print("SQL commands have been wirtten to Students")

with open(lecturerfile,"r") as lecturerfile:
    custreader1 = csv.reader(lecturerfile)
    titles1 = next(custreader1)
    fields1 = ", ".join(titles1)
    #print(fields1)
    values1 = []
    for value1 in custreader1:
        values1.append("("+",".join("'"+str(cell).replace("'","''")+"'" for cell in value1)+")")
    
    createdatabase1 = f"USE BetterOurvle;\nCREATE TABLE Lecturers (ID int, Name varchar(255), Email varchar(125),Password varchar(255), PRIMARY KEY (ID)); \n INSERT INTO Lecturers ({fields1}) VALUES\n{','.join(values1)};"

    with open(sqlfile1,"w") as sql_file1:
        sql_file1.write(createdatabase1)
print("SQL commands have been wirtten to Lecturer")

with open(coursesfile ,"r") as coursesfile :
    custreader2 = csv.reader(coursesfile )
    titles2 = next(custreader2)
    fields2 = ", ".join(titles2)
    #print(fields2)
    values2 = []
    for value2 in custreader2:
        values2.append("("+",".join("'"+str(cell).replace("'","''")+"'" for cell in value2)+")")
    
    createdatabase2 = f"USE BetterOurvle;\nCREATE TABLE Courses (Course_id varchar(255),Coursename varchar(255), CourseLecturer varchar(255),Coursegrade int, PRIMARYKEY(Course_id));\nINSERT INTO Courses ({fields2}) VALUES\n{','.join(values2)};"

    with open(sqlfile2,"w") as sql_file2:
        sql_file2.write(createdatabase2)
print("SQL commands have been wirtten to courses")
