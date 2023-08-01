from pymongo import MongoClient
from pymongo.collection import Collection


_client = MongoClient('mongodb://localhost:27017/')  # cluster
_db = _client.signum_bot  # create database

# create collections
users: Collection = _db['students']
teams: Collection = _db['teams']
requests: Collection = _db['requests']
