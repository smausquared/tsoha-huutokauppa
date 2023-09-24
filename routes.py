from app import app
import auctions
from flask import render_template, redirect

@app.route("/")
def index():
    item = auctions.get_auction()
    return render_template("index.html",item=item)

@app.route("/login")
def login():
    pass
