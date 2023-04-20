from flask import Flask, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/register")
def register_user():
    return "Hello, Flask!"

@app.route("/courses")
#Retrieves all courses
def get_courses():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute('SELECT * FROM courses')
        courses = []
        for Course_id, Coursename, CourseLecturer, Coursegrade in cursor:
            course = {}
            course['Course_id'] = Course_id
            course['Coursename'] = Coursename
            course['CourseLecturer'] = CourseLecturer
            course['Coursegrade'] = Coursegrade
            courses.append(course)
        cursor.close()
        cnx.close()
        return make_response(courses, 200)
    except:
        return make_response({'error': "An error has occurred"}, 400)

@app.route("/calendar/<course_id>")
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

if __name__ == '__main__':
    app.run(host="localhost", port=5000)