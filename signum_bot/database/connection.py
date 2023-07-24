from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')  # cluster
db = client.signum_bot  # create database

# create collections
students = db['students']
teachers = db['teachers']
admins = db['admins']
