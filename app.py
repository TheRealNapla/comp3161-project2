from flask import Flask, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/register")
@requires_auth
@is_role(["admin"])
def register():
    try: 
        cnx = mysql.connector.connect( 
            user="root", password="", host="localhost", database="betterourvle" 
        ) 

        cursor = cnx.cursor() 
        content = request.json 
        user_id = content["UserID"] 
        name = content["Name"] 
        email = content["Email"] 
        password = get_password_hash(content["Password"])
        type = content["Account_Type"] 
         

        cursor.execute( 
            f"INSERT INTO account (`Name`, `Email`, `Password`, `Account_Type`) VALUES('{user_id}','{name}','{email}', '{password}', '{type}')" 
        ) 
        cnx.commit() 

        cursor.execute( 
            f"INSERT INTO {type}({role}Id) VALUES('{id}')" 
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

if __name__ == '__main__':
    app.run(host="localhost", port=5000)