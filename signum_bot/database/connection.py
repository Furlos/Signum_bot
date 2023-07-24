from pymongo import MongoClient
from pymongo.collection import Collection


client = MongoClient('mongodb://localhost:27017/')  # cluster
db = client.signum_bot  # create database

# create collections
students: Collection = db['students']
teachers: Collection = db['teachers']
admins: Collection = db['admins']
