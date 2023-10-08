from flask import Flask
from os import getenv
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

import routes
scheduler = BackgroundScheduler()

# job = scheduler.add_job(auctions.new_auction, 'interval',minutes=5)
# this is eventually going to make a new auction every five minutes!

# also, apparently we need to move the scheduler to a different file...
# maybe auctions?
# i'd also like to make it so that when the five minutes is up, the page
# automatically refreshes so that the user can't keep bidding on the
# finished auction.
