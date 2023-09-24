from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

import routes
scheduler = BackgroundScheduler()
# job = scheduler.add_job(auctions.new_auction, 'interval',minutes=5)
# this is eventually going to make a new auction every five minutes!
