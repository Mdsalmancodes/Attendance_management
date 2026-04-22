from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("Home1.html")

@app.route("/about")
def about():
    return render_template("About1.html")

@app.route("/signup")
def signup():
    return render_template("Signup1.html")

@app.route("/login")
def login():
    return render_template("Login1.html")


if __name__ == "__main__":
      app.run(debug=True,host="0.0.0.0",port=5000)