from http import client
from pydoc import cli
import pymongo
import urllib


mongo = pymongo.MongoClient('mongodb+srv://pmalage:' + urllib.parse.quote('Pratham@1234') + '@cluster0.nwu3o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', connect=False)

db = mongo.get_database('flask_mongodb_atlas')

user_collection = pymongo.collection.Collection(db, 'user_collection')

