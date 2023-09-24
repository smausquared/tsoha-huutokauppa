from db import db
from sqlalchemy.sql import text
from random import randint

def get_auction():
    sql = "SELECT (id, name, starting_price) FROM items"
    result = db.session.execute(text(sql))
    return result.fetchone()

def get_item_count():
    result = db.session.execute(text("SELECT COUNT(*) FROM items"))
    return result.fetchone()

def new_auction(id):
    # id = randint(1,row[0])
    
    result = db.session.execute(text("SELECT COUNT(*) FROM auction_history"))
    row = result.fetchone()
    if row[0] > 0:
        result = db.session.execute(text("SELECT id, name, starting_price FROM items WHERE id = :id"))
        row = result.fetchone()
        db.session.execute(text("INSERT INTO auction_history(item_id, winner_id, price, time) VALUES (:id, NULL, row[starting_price])"))
