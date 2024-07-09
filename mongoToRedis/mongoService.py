from pymongo import MongoClient, errors
import logging
import os

class MongoService:
    def __init__(self):
        try:
            mongo_link = os.getenv('MONGO_LINK')
            mongo_db = os.getenv('MONGO_DB_NAME')
            mongo_collection_name = os.getenv('MONGO_COLLECTION_NAME')

            self.client = MongoClient(mongo_link)
            self.db = self.client[mongo_db]
            self.collection = self.db[mongo_collection_name]
        except errors.ConnectionError as e:
            logger.error(f"Error connecting to MongoDB: {e}")
            raise
            self.query = {"timestamp": {"$gt": max_date_event}}
    
    def get_filtered_collection(self, max_date_event):
        query = {"timestamp": {"$gt": max_date_event}}
        return self.collection.find(query)
    