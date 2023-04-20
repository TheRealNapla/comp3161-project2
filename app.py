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
def get_courses():
    return "Hello, Flask!"

@app.route("/register")
def get_calendar():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host="localhost", port=5000)