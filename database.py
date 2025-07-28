from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["ai_agent_db"]
collection = db["chat_history"]

def save_message(chat_id, prompt, response):
    collection.insert_one({
        "chat_id": chat_id,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.now()
    })

def get_history(chat_id):
    return list(collection.find({"chat_id": chat_id}, {"_id": 0}))

def clear_history(chat_id):
    collection.delete_many({"chat_id": chat_id})

def init_db():
    pass
