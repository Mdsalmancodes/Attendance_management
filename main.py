from flask import Flask, render_template, request, session, redirect, url_for
from models import User, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your-secret-key-change-this'

db.init_app(app)

with app.app_context():
    db.create_all()


@app.context_processor
def inject_user():
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    return dict(user=user)


@app.route("/")
def hello_world():
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user=User.query.filter_by(email=email,password=password).first()
        if user:
            session["user_id"]=user.id
            return redirect(url_for('hello_world'))
        else:
            return render_template("login.html")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        db_user = User.query.filter_by(email=email).first()
        if db_user:
            return render_template("signup.html", error="Email already exists.")
        db_user = User.query.filter_by(name=name).first()
        if db_user:
            return render_template("signup.html", error="Username already exists.") 
        user = User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        return render_template("login.html")

    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('hello_world'))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)