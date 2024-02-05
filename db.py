from pymongo import MongoClient
from flask_pymongo import pymongo

uri = "mongodb+srv://samyabeshv:X7VAt8ZcYHSQT6qW@cluster0.vszxved.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client.get_database('snapchat_scrape')
user_profile_collection = pymongo.collection.Collection(db, 'snapchat_profiles')

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
