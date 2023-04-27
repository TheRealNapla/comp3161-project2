from flask import Flask, request, make_response, jsonify
from passlib.hash import sha256_crypt
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/register",methods=['POST'])
def register():
    try: 
        cnx = mysql.connector.connect( 
            user="root", password="", host="localhost", database="betterourvle" 
        ) 

        cursor = cnx.cursor() 
        content = request.json 
        user_id = content['UserID'] 
        name = content['Name'] 
        email = content['Email'] 
        password = sha256_crypt.encrypt(content["Password"])
        type = content['Account_Type'] 


        cursor.execute(
            f"INSERT INTO account (`UserID`, `Name`, `Email`, `Password`, `Account_Type`) VALUES({user_id},'{name}','{email}', '{password}', '{type}')" 
        )
        cnx.commit()

        cursor.execute(
            f"INSERT INTO {type}s (`ID`, `Name`, `Email`, `Password`) VALUES({user_id}, '{name}', '{email}', '{password}')" 
        )
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({"success": "Account created"}, 201) 
    except Exception as e: 
        return make_response({"error": str(e)}, 400) 


@app.route("/courses")
#Retrieves all courses
def get_courses():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM courses')
        courses = []
        for Course_id, Coursename, Lecturer_ID, CourseLecturer, Coursegrade in cursor:
            course = {}
            course['Course_id'] = Course_id
            course['Coursename'] = Coursename
            course['Lecturer_ID'] = Lecturer_ID
            course['CourseLecturer'] = CourseLecturer
            course['Coursegrade'] = Coursegrade
            courses.append(course)
        cursor.close()
        cnx.close()
        return make_response(courses, 200)
    except:
        return make_response({'error': "An error has occurred"}, 400)

@app.route("/courses/lecturer/<lecturer_id>")
#Retrieves all courses taught by a particular lecturer
def get_lecturer_courses(lecturer_id):
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM courses WHERE Lecturer_ID='{lecturer_id}'")
        courses = []
        for Course_id, Coursename, Lecturer_ID, CourseLecturer, Coursegrade in cursor:
            course = {}
            course['Course_id'] = Course_id
            course['Coursename'] = Coursename
            course['Lecturer_ID'] = Lecturer_ID
            course['CourseLecturer'] = CourseLecturer
            course['Coursegrade'] = Coursegrade
            courses.append(course)
        cursor.close()
        cnx.close()
        return make_response(courses, 200)
    except:
        return make_response({'error': "An error has occurred"}, 400)
    
@app.route("/courses/student/<student_id>")
#Retrieves all courses taken by a particular student
def get_student_courses(student_id):
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM courses WHERE Course_id IN (SELECT Course_id FROM enrol WHERE Student_ID='{student_id}')")
        courses = []
        for Course_id, Coursename, Lecturer_ID, CourseLecturer, Coursegrade in cursor:
            course = {}
            course['Course_id'] = Course_id
            course['Coursename'] = Coursename
            course['Lecturer_ID'] = Lecturer_ID
            course['CourseLecturer'] = CourseLecturer
            course['Coursegrade'] = Coursegrade
            courses.append(course)
        cursor.close()
        cnx.close()
        return make_response(courses, 200)
    except:
        return make_response({'error': "An error has occurred"}, 400)

@app.route("/calendar/<course_id>")
#Retrieves all calendar events for a particular course
def get_calendar(course_id):
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM calendarevents WHERE Course_ID='{course_id}'")
        events = []
        for Event_no, Event_name, Event_date, Course_ID in cursor:
            event = {}
            event['Event_no'] = Event_no
            event['Event_name'] = Event_name
            event['Event_date'] = Event_date
            event['Course_ID'] = Course_ID
            events.append(event)
        cursor.close()
        cnx.close()
        return make_response(events, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route("/calendar/student/<student_id>")
#Retrieves all calendar events for a particular course
def get_calendar_student(student_id):
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM calendarevents WHERE Course_ID IN (SELECT Course_id FROM enrol WHERE Student_ID='{student_id}')")
        events = []
        for Event_no, Event_name, Event_date, Course_ID in cursor:
            event = {}
            event['Event_no'] = Event_no
            event['Event_name'] = Event_name
            event['Event_date'] = Event_date
            event['Course_ID'] = Course_ID
            events.append(event)
        cursor.close()
        cnx.close()
        return make_response(events, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)
    
#Create Course
#Retrive Members
#Register for course
def getcolumn():
    cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
    col = cnx.cursor()
    #col = mysql.connection.cursor()
    col.execute("DESCRIBE students")
    names = [c[0] for c in col.fetchall()]
    col.close()
    print(names)
    return names
    
 #a
@app.route('/students',methods=['GET'])
def customer():
    cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
    cust = cnx.cursor()
    cust.execute("SELECT * FROM students")
    custlist = cust.fetchall()
    headers= getcolumn() 
    result = []
    for r in custlist:
        result.append(dict(zip(headers,r)))
    return result

@app.route('/courses',methods=['GET'])
def courses():
    cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
    cust = cnx.cursor()
    cust.execute("SELECT * FROM courses")
    custlist = cust.fetchall()
    result = []
    return custlist

#create course
#remember to add login required
@app.route('/create_course',methods=['POST'])
def create_course():
    try:
        print("here")
        cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
        cust = cnx.cursor()
        data=request.get_json()
        Course_id = data['Course_id']
        Coursename = data['Coursename']
        CourseLecturer = data['CourseLecturer']
        Coursegrade = data['Coursegrade']
        cust.execute(f"SELECT * FROM courses WHERE Coursename = %s",(Coursename,))
        coursetlist = cust.fetchall()
        print(coursetlist)
        print(coursetlist)
        if len(coursetlist) == 0:
            cust.execute(f"INSERT INTO courses VALUES('{Course_id}','{Coursename}','{CourseLecturer}','{Coursegrade}');")
            cnx.commit()
            cnx.close()
            return {"success":"Course Created"}
        else:
            return {"error":"Course name already Exists"}

        
    except Exception as e:
        print(e)
        return {"error":"Course Not Created"}
    
#Retrive Members. have to add students
@app.route('/get_members/<string:Course_id>',methods=['GET'])
def members(Course_id):
    cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
    cust = cnx.cursor()
    cust.execute("SELECT CourseLecturer FROM courses WHERE Course_id  = %s",(Course_id,))
    lecturers = cust.fetchone()

    cust.execute("SELECT students.name FROM students Join enrol ON students.ID = enrol.Student_ID WHERE enrol.Course_ID  = %s",(Course_id,))
    students = cust.fetchall()
    print(students)
    print(lecturers)
    members =[]
    if len(lecturers) ==0 :
        return {"error":"Course Not Found or no lecturer assigned"}
    else:
        members.append({"Name":lecturers[0],
                "Role": "Lecturer"})
        for student in students:
            members.append({"Name":student[0],
                "Role": "Student"})
        return members


#Register for Course
@app.route('/course_registration',methods=['POST'])
def course_registration():
    cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
    cust = cnx.cursor()
    data=request.get_json()
    Course_ID = data['Course_ID']
    Student_ID = data['Student_ID']    
    cust.execute(f"SELECT COUNT(Student_ID) FROM enrol WHERE Student_ID = %s",(Student_ID,))
    count= int(cust.fetchone()[0])
    cust.execute(f"SELECT * FROM courses WHERE  Course_id  = %s",(Course_ID,))
    course = cust.fetchone()
    cust.execute(f"SELECT * FROM students WHERE  ID  = %s",(Student_ID,))
    student = cust.fetchone()
    print(count)
    if count < 6 and course is not None and student is not None:
        cust.execute(f"INSERT INTO enrol (Student_ID, Course_ID)VALUES('{Student_ID}','{Course_ID}');")
        cnx.commit()
        cnx.close()
        return {"success":"Course Registration Successful"}
    elif count >= 6:
        return {"error":"You cant register for this course, you can register for a max of 6 courses "}
    elif course is None:
        return {"error": "Course ID incorrect"}
    else:
        return{"error":"Student not found check the student ID"}

@app.route('/assign_course_lecturer',methods=['POST'])
def assignlecturer():
    cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
    cust = cnx.cursor()
    data=request.get_json()
    Course_id = data['Course_id']
    CourseLecturer = data['CourseLecturer'] 
    cust.execute(f"SELECT * FROM courses WHERE  Course_id  = %s",(Course_id,))
    course = cust.fetchone()
    cust.execute(f"SELECT COUNT(CourseLecturer) FROM courses WHERE CourseLecturer = %s",(CourseLecturer,))
    count= int(cust.fetchone()[0])
    cust.execute(f"SELECT * FROM lecturers WHERE Name  = %s",(CourseLecturer,))
    lecturer = cust.fetchone()
    if course is not None and count<5 and lecturer is not None:
        cust.execute(f"UPDATE courses set CourseLecturer = %s WHERE Course_id = %s",(CourseLecturer,Course_id))
        cnx.commit()
        cnx.close()
        return {"success":"Course Lecturer Assigned"}
    elif course is None:
        return {"error": "Course Not found"}
    elif lecturer is None:
        return {"error": "Lecturer Not found"}
    else:
        return{"error":"Lecturer already teaches 5 courses"}

        

if __name__ == '__main__':
    app.run(host="localhost", port=5000)





