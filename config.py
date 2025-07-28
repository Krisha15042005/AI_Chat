from dotenv import load_dotenv
import os

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")