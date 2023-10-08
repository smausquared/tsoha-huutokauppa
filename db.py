from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

# Tables: users, auction_history, items
# i have the problem of the structure being too
# efficient: I seem to not need more than 3 tables.
# maybe more functionality eventually, like
# messages between users
