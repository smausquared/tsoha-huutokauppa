from app import app
import auctions
from flask import render_template, redirect, session, request
from werkzeug.security import check_password_hash, generate_password_hash

@app.route("/", methods=["GET", "POST"])
def index():
    if session:
        item = auctions.get_auction()
        return render_template("index.html",item=item, session = session)
    return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register_form.html", session = session)

@app.route("/register_result", methods=["GET", "POST"])
def register_result():
    username = request.form["username"]
    password = request.form["password"]
    if len(password) > 0 and len(username) > 0:
        hash = generate_password_hash(password)
        auctions.create_user(username, hash)
        return redirect("/login")
    else:
        return redirect("/register")

@app.route("/login", methods=["GET","POST"])
def login():
    if session:
        return redirect("/")
    return render_template("login_form.html")

@app.route("/login_result", methods=["GET","POST"])
def login_result():
    username = request.form["username"]
    password = request.form["password"]
    serverword = auctions.get_hash(username)[0]
    print(serverword)
    if check_password_hash(serverword, password):
        session["username"] = username
        return redirect("/")
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
