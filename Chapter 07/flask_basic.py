from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"

# PS D:\workspace\PythonPractice\Chapter 07> set FLASK_APP=flask_basic.py
# PS D:\workspace\PythonPractice\Chapter 07> $env:FLASK_APP = "flask_basic.py"
# PS D:\workspace\PythonPractice\Chapter 07> flask run