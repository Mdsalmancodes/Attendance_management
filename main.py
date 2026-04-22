from flask import Flask, render_template 
from flask import Flask,render_template
from models import User,db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup",methods=["POST","GET"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        user=User(name=name,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        return render_template("Login.html")

        
    return render_template("Signup.html")


if __name__ == "__main__":
      app.run(debug=True,host="0.0.0.0",port=5000)