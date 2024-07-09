from pymongo import MongoClient
import os
class MongodbService:
    def __init__(self):
            mongo_link = os.getenv('MONGO_LINK')
            mongo_db = os.getenv('MONGO_DB_NAME')
            mongo_collection_name = os.getenv('MONGO_COLLECTION_NAME')

            self.client = MongoClient(mongo_link)
            self.db = self.client[mongo_db]
            self.collection = self.db[mongo_collection_name]
        
