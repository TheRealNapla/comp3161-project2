from flask import Flask, request, make_response
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host="localhost", port=5000)