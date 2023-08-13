from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')  # cluster
db = client.signum_bot  # create database
