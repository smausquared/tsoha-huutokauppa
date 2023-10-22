from db import db
from sqlalchemy.sql import text
from random import randint

def create_user(username, password, role):
    sql = text("INSERT INTO users (username, password, role) VALUES (:username, :password, :role)")
    db.session.execute(sql, {"username":username, "password":password, "role":role})
    db.session.commit()

def find_user(id):
    sql = text("SELECT username FROM users WHERE id = :id")
    result = db.session.execute(sql,{"id":id})
    return result.fetchone()

def find_id(username):
    sql = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql,{"username":username})
    return result.fetchone()

def get_hash(username):
    sql = text("SELECT password FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username":username})
    return result.fetchone()

def bid(auction_id, leader_id, increment):
    sql = text("UPDATE auction_history SET winner_id = :leader_id, price = :increment WHERE id = :auction_id")
    db.session.execute(sql, {"leader_id":leader_id, "increment":increment,"auction_id":auction_id})    
    db.session.commit()

def get_auction(): # made obsolete on the main page but kept for other functions
    sql = "SELECT A.id, A.item_id, A.winner_id, A.price, A.time, I.name \
    FROM auction_history A LEFT JOIN items I ON A.item_id = I.id ORDER BY A.id DESC LIMIT 1 OFFSET 1"
    result = db.session.execute(text(sql))
    return result.fetchone()

def get_auctions():
    sql = "SELECT A.id, A.item_id, A.winner_id, A.price, A.time, I.name \
    FROM auction_history A LEFT JOIN items I ON A.item_id = I.id ORDER BY A.id DESC LIMIT 3"
    result = db.session.execute(text(sql))
    return result.fetchall()

def get_next_auction():
    sql = "SELECT A.id, A.item_id, A.winner_id, A.price, A.time, I.name \
    FROM auction_history A LEFT JOIN items I ON A.item_id = I.id ORDER BY A.id DESC LIMIT 1"
    result = db.session.execute(text(sql))
    return result.fetchone()

def get_won_auctions(id):
    sql = "SELECT A.item_id, I.name, A.price, A.time FROM (SELECT * FROM auction_history ORDER BY id DESC OFFSET 2)\
    A LEFT JOIN items I ON A.item_id = I.id WHERE A.winner_id = :id ORDER BY A.id DESC"
    result = db.session.execute(text(sql),{"id":id})
    return result.fetchall()

def get_item_count():
    result = db.session.execute(text("SELECT COUNT(*) FROM items"))
    return result.fetchone()

def new_auction(id):
    result = db.session.execute(text("SELECT id, name, starting_price FROM items WHERE id = :id"), {"id":id})
    row = result.fetchone()
    db.session.execute(text("INSERT INTO auction_history (item_id, winner_id, price, time) \
                            VALUES (:id, NULL, :starting_price, NOW())"), {"id":id, "starting_price":row[2]})
    db.session.commit()

def send_feedback(id, title, content):
    sql = text("INSERT INTO feedback (user_id, title, content) VALUES (:id, :title, :content)")
    db.session.execute(sql, {"id":id,"title":title, "content":content})
    db.session.commit()

def is_admin(id):
    sql = text("SELECT role FROM users WHERE id = :id")
    result = db.session.execute(sql, {"id":id})
    if int(result.fetchone()[0]) == 1:
        return True
    return False

def get_feedback():
    sql = text("SELECT U.username, F.title, F.content, F.time FROM feedback F LEFT JOIN users U ON F.user_id = U.id ORDER BY F.id DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def new_item(name, price):
    sql = text("INSERT INTO items (name, starting_price) VALUES (:name, :price)")
    db.session.execute(sql, {"name":name, "price":price})
    db.session.commit()

def abort_auction():
    auction_id = get_auction()[0]
    sql = text("UPDATE auction_history SET winner_id = NULL WHERE id = :auction_id")
    db.session.execute(sql, {"auction_id":auction_id})
    itemcount = get_item_count()[0]
    new_auction(randint(1,itemcount))
    db.session.commit()

def get_bot_bid(id):
    sql = text("SELECT bid_amount FROM bots WHERE user_id = :id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()
