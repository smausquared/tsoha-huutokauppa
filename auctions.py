from db import db
from sqlalchemy.sql import text
from random import randint

# the way the app is going to function, or useful notes for me and you
#
# so for the front page we want to be able to see the previous auction,
# the current auction and the next auction. We can do this by
# so:
# the current auction is always going to be the second latest item in the
# auction history: that is, the auction with the second biggest id. when the auction ends,
# a new auction gets added to the auction_history table: the new auction is the
# next auction, and the old one now doesn't have the highest id in the table,
# making it the current auction.
#
# first though, we need a login function. I think we're going to do it
# the easy way and make it so that you can't see the main page if you're not
# logged in!
# i think it's also possible to make bot users in 
# flask, so that's another thing to develop once
# the page is functioning, so you're not bidding alone.

def create_user(username, password):
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":password})
    db.session.commit()

def get_hash(username):
    sql = text("SELECT password FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()

def get_auction():
    sql = "SELECT (id, name, starting_price) FROM items ORDER BY id DESC LIMIT 1 OFFSET 1"
    result = db.session.execute(text(sql))
    return result.fetchone()

def get_item_count():
    result = db.session.execute(text("SELECT COUNT(*) FROM items"))
    return result.fetchone()

def get_item_count(username):
    result = db.session.execute(text("SELECT password FROM users WHERE name = :username"), {"username":username})
    return result.fetchone()

def new_auction(id):
    result1 = db.session.execute(text("SELECT COUNT(*) FROM auction_history"))
    row1 = result1.fetchone()
    itemcount = get_item_count()

    result = db.session.execute(text("SELECT id, name, starting_price FROM items WHERE id = :id"), {"id":id})
    row = result.fetchone()
    db.session.execute(text("INSERT INTO auction_history(item_id, winner_id, price, time) VALUES (:id, NULL, :starting_price, NOW())", {"id":id, "starting_price":row[2]}))
    db.session.commit()
    # the app needs there to be at least two items in the auction history. 
    # we'll add another automatically if the history is empty
    if row1[0] < 1:
        id2 = randint(1,itemcount)
        result = db.session.execute(text("SELECT id, name, starting_price FROM items WHERE id = :id"), {"id":id2})
        row = result.fetchone()
        db.session.execute(text("INSERT INTO auction_history(item_id, winner_id, price, time) VALUES (:id, NULL, :starting_price, NOW())", {"id":id2, "starting_price":row[2]}))
        db.session.commit()
