from app import app
from random import randint
import auctions
import atexit
from flask import render_template, redirect, session, request, flash
from werkzeug.security import check_password_hash, generate_password_hash
from apscheduler.schedulers.background import BackgroundScheduler

TIMER = 119

def every_two_min():
    with app.app_context():
        itemcount = auctions.get_item_count()[0]
    id = randint(1,itemcount)
    with app.app_context():
        auctions.new_auction(id)

def timer_tracker():
    global TIMER
    if TIMER > 0:
        TIMER -= 1
    else:
        TIMER = 119

with app.app_context():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=timer_tracker,trigger="interval", seconds = 1)
    scheduler.add_job(func=every_two_min, trigger="interval", minutes = 2)
    scheduler.start()

@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if session["id"]:
            isadmin = auctions.is_admin(session["id"])
            item = auctions.get_auction()
            if item[2]:
                winner = auctions.find_user(item[2])[0]
            else:
                winner = ""
            return render_template("index.html",item=item, session=session, winner=winner, timer=TIMER, isadmin=isadmin)
    except:
        return redirect("/register")

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register_form.html", session=session)

@app.route("/register_result", methods=["GET", "POST"])
def register_result():
    username = request.form["username"]
    password = request.form["password"]
    if len(password) > 0 and len(username) > 0:
        hash = generate_password_hash(password)
        auctions.create_user(username, hash, 0)
        flash("User created!")
        return redirect("/login")
    return render_template("error.html", error="Username and password can't be empty!")

@app.route("/login", methods=["GET","POST"])
def login():
    try:
        if session["id"]:
            return redirect("/")
    except:
        return render_template("login_form.html")

@app.route("/login_result", methods=["GET","POST"])
def login_result():
    try:
        username = request.form["username"]
        password = request.form["password"]
        serverword = auctions.get_hash(username)[0]
        if check_password_hash(serverword, password):
            user_id = auctions.find_id(username)[0]
            session["username"] = username
            session["id"] = user_id
            flash("Logged in successfully!")
            return redirect("/")
        else:
            flash("Wrong password!")
            return redirect("/login")
    except:
        flash("User not found!")
        return redirect("/login")

@app.route("/bid_result", methods=["GET","POST"])
def bid_result():
    try:
        current_auction = auctions.get_auction()
        current_price = int(current_auction[3])
        auction_id = current_auction[0]
        increment = int(request.form["bid"])
        if current_price + increment <= current_price:
            return render_template("error.html", error="Invalid bid")
        auctions.bid(auction_id, session["id"], current_price + increment)
        return redirect("/")
    except:
        return render_template("error.html", error="Invalid bid")

@app.route("/feedback_result", methods=["GET","POST"])
def feedback_result():
    try:
        title = request.form["title"]
        message = request.form["message"]
        id = session["id"]
        if len(title) > 0 and len(message) > 0:
            auctions.send_feedback(id, title, message)
            flash("Message sent successfully!")
            return redirect("/")
    except:
        return render_template("error.html", error="Something went wrong! lol")

@app.route("/logout")
def logout():
    try:
        del session["username"]
        del session["id"]
    except:
        pass
    return redirect("/")

@app.route("/secretpage") # kept for testing
def secret():
    auctions.new_auction(1)
    return redirect("/")

@app.route("/mypage", methods=["GET", "POST"])
def mypage():
    try:
        my_id = session["id"]
        my_username = session["username"]
        item_list = auctions.get_won_auctions(my_id)
        print(item_list)
        return render_template("won_items.html", items=item_list, username=my_username)
    except:
        return render_template("error.html", error="Hey! Log in!")
atexit.register(lambda:scheduler.shutdown())

@app.route("/admin", methods=["GET", "POST"])
def admin():
    try:
        isadmin = auctions.is_admin(session["id"])
        if isadmin:
            feedback = auctions.get_feedback()
            return render_template("admin.html", isadmin=isadmin, feedback=feedback)
        else:
            return render_template("error.html", error="You do not have the right")
    except:
        return render_template("error.html", error="Log in!")
