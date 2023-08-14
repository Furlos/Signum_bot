from pymongo.collection import Collection
from signum_bot.database.db import db


users: Collection = db['users']
teams: Collection = db['teams']
requests: Collection = db['requests']

users.create_index('role')
