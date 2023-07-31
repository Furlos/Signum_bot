from pymongo import MongoClient
from pymongo.collection import Collection


_client = MongoClient('mongodb://localhost:27017/')  # cluster
_db = _client.signum_bot  # create database

# create collections
students: Collection = _db['students']
teachers: Collection = _db['teachers']
teams: Collection = _db['teams']
admins: Collection = _db['admins']
