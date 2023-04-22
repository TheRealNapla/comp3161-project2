from flask import Flask, request, make_response
import mysql.connector
from flask import Flask,jsonify,request
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"


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
    elif count > 6:
        return {"error":"You cant register for this coruse, you can register for a max of 6 courses "}
    elif course is None:
        return {"error": "Course ID incorect"}
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

        



