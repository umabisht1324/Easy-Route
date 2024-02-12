from flask import Flask,request
from flask import render_template
app=Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        conPass = request.form["conPass"]

        print("Username:", username)
        print("Password:", password)
        print("Con Pass:", conPass)

        if username.isalnum() and password == conPass:
            print("Passwords match")
            return render_template('distance.html')
        else:
            print("Passwords do not match")

    return render_template("login.html")



@app.route("/signup")
def signup():
    return render_template('signup.html')



@app.route("/distance")
def distance():
    return render_template('distance.html')

if __name__ == "__main__":
    app.run()
