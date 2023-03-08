from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def first_flask():
    return "This is my First Flask Program"

@app.route("/app2")
def second_flask():
    return "Shiva Harshil"

@app.route("/app3",methods = ["GET"])
def third_flask():
    num1 = request.form.get("num1")
    return "num1"

app.run(debug=True)
