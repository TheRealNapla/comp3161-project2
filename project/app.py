from flask import Flask, request, make_response, jsonify
from passlib.hash import sha256_crypt
import mysql.connector


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

#return all the forums from a particular course
@app.route('/particularforumreport/<Course_ID>', methods=['GET'])
def particularforumreport(Course_ID):
    try:
        connection = mysql.connector.connect(user='root',password='', host='localhost', database='BetterOurvle')
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT Active, Course_ID,Date_Posted, Discussion_Name,Forum_ID FROM discussionforum WHERE Course_ID = %s",(Course_ID,))
        info = cursor.fetchone()
        foruml = []
        if info is not None:
            Active, Course_ID,Date_Posted, Discussion_Name,Forum_ID  = info 
            forum = {}
            forum["Course_ID"] = Course_ID
            forum["Forum_ID"] = Forum_ID
            forum["Discussion_Name"] = Discussion_Name
            forum["Date_Posted"] = Date_Posted
            forum["Active"] =Active
            cursor.close()
            connection.close()
            return make_response(forum,200)
        else:
            return make_response({'error': 'An error has occurred, could not return all the forums from a particular course'}, 400)
    except:
        return make_response({'error': 'An error has occured'}, 400)

# create forum for a particular course
@app.route('/addforum', methods=['POST'])
def addforum():
    try:
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='BetterOurvle')
        cursor = connection.cursor()
        forum_content = request.json
        Course_ID = forum_content['Course_ID']
        Forum_ID = forum_content['Forum_ID']
        Discussion_Name = forum_content['Discussion_Name']
        Date_Posted = forum_content['Date_Posted']
        Active = forum_content['Active']
        cursor.execute(f"INSERT INTO discussionforum VALUES('{Course_ID}','{Forum_ID}','{Discussion_Name}','{Date_Posted}','{Active}')")
        connection.commit()
        cursor.close()
        connection.close()
        return make_response({"success" : "The forum has been added"}, 201)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

#return all courses that  have  50 or more students
@app.route('/coursereport', methods=['GET'])
def coursereport():
    try:
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='BetterOurvle')
        cursor = connection.cursor(buffered=True)
        cursor.execute('SELECT Courses.Course_ID, Courses.Coursename, COUNT(Enrol.Student_ID) AS student_count FROM Courses JOIN enrol ON  Courses.Course_ID = Enrol.Course_ID GROUP BY Courses.Course_ID, Courses.Coursename HAVING COUNT(Enrol.Student_ID) >= 50')
        courselist = []
        for Course_ID, Coursename, student_count in cursor:
            course = {}
            course["Course_ID"] = Course_ID
            course["Coursename"] = Coursename
            course["student_count"] = student_count
            
            courselist.append(course)
        cursor.close()
        connection.close()
        return make_response({'courselist': courselist}, 200)
    except Exception as e:
        return make_response({'error':'An error has occured, could not return all courses that  have  50 or more students'}, 400)

# return all students that do 5 or more courses 
# return all students that do 5 or more courses 
@app.route('/studentreport', methods=['GET'])
def studentreport():
    try:
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='BetterOurvle')
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT students.ID, students.Name, COUNT(enrol.Course_ID) AS course_count FROM students JOIN enrol ON Students.ID = enrol.Student_ID  GROUP BY students.ID, students.Name HAVING COUNT(enrol.Course_ID) >= 5;")
        studentlist = []
        for ID, Name, course_count in cursor:
            student = {}
            student["ID"] = ID
            student["Name"] = Name
            student["course_count"] = course_count
            
            studentlist.append(student)
        cursor.close()
        connection.close()
        return make_response({'studentlist': studentlist}, 200)
    except Exception as e:
        return make_response({'error':'An error has occured, could not return all courses that  have  50 or more students'},400)

# return the lectures that teach 3 or more courses 
@app.route('/lecturerreport', methods=['GET'])
def lecturerreport():
    try:
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='BetterOurvle')
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT Lecturers.ID, Lecturers.Name, COUNT(Courses.Course_id) AS course_count FROM Lecturers  JOIN Courses  ON Lecturers.Name = Courses.CourseLecturer GROUP BY Lecturers.Name HAVING COUNT(Courses.Course_ID) >= 3")
        lecturerlist = []
        for ID, Name, course_count in cursor:
            lecturer = {}
            lecturer["ID"] = ID
            lecturer["Name"] = Name
            lecturer["course_count"] = course_count
            
            lecturerlist.append(lecturer)
        cursor.close()
        connection.close()
        return make_response({'lecturerlist': lecturerlist}, 200)
    except Exception as e:
        return make_response({'error':'An error has occured, could not return the lectures that teach 3 or more courses'}, 400)

#  return the top 10 most enrolled courses

@app.route('/mostenrolledreport', methods=['GET'])
def mostenrolledreport():
    try:
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='BetterOurvle')
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT Courses.Course_ID, Courses.Coursename, COUNT(Enrol.Student_ID) AS enrollment_count FROM Courses JOIN Enrol ON Courses.Course_ID = Enrol.Course_ID GROUP BY Courses.Course_ID ORDER BY enrollment_count DESC LIMIT 10")
        courselist = []
        for Course_ID, Coursename, enrollment_count in cursor:
            course = {}
            course["Course_ID"] = Course_ID
            course["Coursename"] = Coursename
            course["enrollment_count"] = enrollment_count
            
            courselist.append(course)
        cursor.close()
        connection.close()
        return make_response({'courselist': courselist}, 200)
    except Exception as e:
        return make_response({'error':'An error has occured, could not return the top 10 most enrolled courses'}, 400)



# return the top 10 students with the highest overall averages
@app.route('/topstudentsreport', methods=['GET'])
def topstudentsreport():
    try:
        connection = mysql.connector.connect(user='root', password='', host='localhost', database='BetterOurvle')
        cursor = connection.cursor(buffered=True)
        cursor.execute("SELECT Students.ID, Students.Name, AVG(Enrol.Grade) AS average_grade FROM Students JOIN Enrol ON Students.ID = Enrol.Student_ID GROUP BY Students.ID, Students.Name ORDER BY average_grade DESC LIMIT 10")
        studentlist = []
        for ID, Name, average_grade in cursor:
            student = {}
            student["ID"] = ID
            student["Name"] = Name
            student["average_grade"] = average_grade
            
            studentlist.append(student)
        cursor.close()
        connection.close()
        return make_response({'studentlist': studentlist}, 200)
    except Exception as e:
        return make_response({'error': 'An error has occurred, could not return the top 10 students with the highest overall averages'}, 400)

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


@app.route("/courses",methods=['GET'])
#Retrieves all courses
def get_courses():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='BetterOurvle')
        cursor = cnx.cursor()
        cursor.execute("SELECT * FROM Courses")
        courses = []
        for Course_id, Coursename,Lecturer_ID, CourseLecturer, Coursegrade in cursor:
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
    
#Create Course
#Retrive Members
#Register for course


 

#Create Calendar Event 
@app.route('/create_calendar_event',methods=['POST'])
def create_cevent():
    try:
        print("here")
        cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
        cust = cnx.cursor()
        data=request.get_json()
        Event_no = data['Event_no']
        Event_name = data['Event_name']
        Event_date = data['Event_date']
        Course_ID = data['Course_ID']
        cust.execute(f"INSERT INTO calendarevents VALUES('{Event_no}','{Event_name}','{Event_date}','{Course_ID}');")
        cnx.commit()
        cnx.close()
        return {"success":"Calendar Event Created"}
    except Exception as e:
        print(e)
        return {"error":e}




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
        Lecturer_ID= data["Lecturer_ID"]
        CourseLecturer = data['CourseLecturer']
        Coursegrade = data['Coursegrade']
        cust.execute(f"SELECT COUNT(CourseLecturer) FROM courses WHERE CourseLecturer = %s",(CourseLecturer,))
        count= int(cust.fetchone()[0])
        cust.execute(f"SELECT * FROM courses WHERE Coursename = %s",(Coursename,))
        coursetlist = cust.fetchall()
        print(coursetlist)
        print(coursetlist)
        if len(coursetlist) == 0 and count <=5:
            cust.execute(f"INSERT INTO courses VALUES('{Course_id}','{Coursename}','{Lecturer_ID}','{CourseLecturer}','{Coursegrade}');")
            cnx.commit()
            cnx.close()
            return {"success":"Course Created"}
        elif count >5:
            return {"error":"Lecturer at course courselimit"}
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

@app.route("/get_discussion_thread/<Forum_ID>", methods = ['GET'])
def get_discussion_thread(Forum_ID):
    try:
        cnx = mysql.connector.connect(user ='root', password='', host='localhost',database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT * FROM discussionthreads WHERE Forum_ID = {Forum_ID}")
        threads = []
          # initialize discuss_thread to None
        for  Thread_ID, Forum_ID, Thread_Name, Thread_Replies, Reply_No, Reply_Content in cursor:
            discuss_thread = {}
            discuss_thread['Thread_ID'] = Thread_ID
            discuss_thread['Forum_ID'] = Forum_ID
            discuss_thread['Thread_Name'] = Thread_Name
            discuss_thread['Thread_Replies'] = Thread_Replies
            discuss_thread['Reply_No'] = Reply_No
            discuss_thread['Reply_Content'] = Reply_Content
            threads.append(discuss_thread)
        cursor.close()
        cnx.close()
        return make_response(threads, 200)
        
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route("/add_discussion_thread", methods = ['POST'])
def add_discussion_thread():
    try:
        
        cnx = mysql.connector.connect(user='root',password='',host='localhost',database='betterourvle')
        cursor = cnx.cursor()
        data = request.get_json()
        Thread_ID = data['Thread_ID']  
        Forum_ID = data['Forum_ID']
        Thread_Name = data['Thread_Name']
        Thread_Replies = data['Thread_Replies']
        Reply_No = data['Reply_No']
        Reply_Content = data['Reply_Content']
        cursor.execute(f"INSERT INTO discussionthreads VALUES('{Thread_ID}','{Forum_ID}','{Thread_Name}','{Thread_Replies}','{Reply_No}','{Reply_Content}');") 
        cnx.commit()
        cnx.close()   
        return make_response({'message': 'Thread added successfully'}, 201)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/post_grade', methods = ['POST'])
def post_grade():
    try:
        cnx = mysql.connector.connect(user='root',password='',host='localhost',database='BetterOurvle')
        cursor = cnx.cursor()
        data=request.get_json()
        Student_ID = data['Student_ID']
        Grade = data['Grade']
        Course_ID = data['Course_ID']
        cursor.execute(f"UPDATE enrol set Grade = %s WHERE Course_ID = %s and Student_ID = %s",(Grade,Course_ID,Student_ID))
        
        cnx.commit()
        cursor.close()
        cnx.close()
        return make_response({'message': 'Grade  added successfully!'}, 201)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/add_course_content', methods = ['POST'])
def add_course_content():
    try:
        data = request.get_json()
        cnx = mysql.connector.connect(user='root',password='',host='localhost',database='betterourvle')
        cursor = cnx.cursor()
        section_query = {}
        SectionID = data['SectionID']  
        Section_Name = data['Section_Name']
        Active = data['Active']
        Course_id = data['Course_id']
        cursor.execute(f"INSERT INTO section VALUES('{SectionID}','{Section_Name}','{Active}','{Course_id}');") 
        cnx.commit()
        cursor.close()
        cnx.close()   
        return make_response({'message': 'New Course Content added successfully'}, 201)
    except Exception as e:
        return make_response({'error': str(e)}, 400)  

@app.route('/retrieve_course_content/<Course_id>', methods=['GET'])
def retrieve_course_content(Course_id):
    try:
        cnx = mysql.connector.connect(user='root', password='', host='localhost', database='betterourvle')
        cursor = cnx.cursor()
        cursor.execute(f"SELECT SectionID, Section_Name FROM section WHERE Course_id = %s",(Course_id,))
        coursecontent = cursor.fetchall()
        cursor.close()
        cnx.commit()
        cnx.close()
        return make_response(coursecontent, 200)
    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/average_final', methods=['GET'])
def average_final():
    try:
        cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='BetterOurvle')
        cursor = cnx.cursor(dictionary=True)
        query = ("""
            SELECT Student_ID, AVG(Grade) AS AvgGrade
            FROM enrol
            GROUP BY Student_ID
        """)

        cursor.execute(query)
        result = cursor.fetchall()

        cursor.close()
        cnx.close()

        if len(result) == 0:
            return make_response({'message': 'No results found.'}, 404)

        return jsonify(result), 200

    except Exception as e:
        return make_response({'error': str(e)}, 400)

@app.route('/login', methods=['POST'])
def login():
    try:
        cnx = mysql.connector.connect(user='root', password='',host='localhost',database='BetterOurvle')
        cursor = cnx.cursor()
        content = request.get_json()    
        InputtedPassword  = sha256_crypt.encrypt(content["Password"]) 
        InputtedUser_ID = content['UserID'] 
        cursor.execute(f"SELECT * from Account WHERE UserID = {InputtedUser_ID}")
        row = cursor.fetchone()
        account = {}
        cnx.commit()
        cursor.close()
        cnx.close()
        if row is not None:
            UserID, Password, Name, Email, Account_Type = row
            account = {}
            account['UserID'] = UserID
            account['Password'] = Password
            account['Name'] = Name
            account['Email'] = Email
            account['Account_Type'] = Account_Type
            if InputtedPassword == Password:
                return make_response({"success" : "Login successful"}, 201)
            else:
                return make_response({'error': 'Invalid password. Please try again.'}, 400)
        else:
            return make_response({'error': 'Invalid username. Please try again.'}, 400)
    except Exception as e:
        print(e)
        return make_response({'error': str(e)}, 400)

        

if __name__ == '__main__':
    app.run(host="localhost", port=5000)