from pymongo import MongoClient
from config import MONGODB_LINK, MONGO_DB

mdb = MongoClient(MONGO_DB)[MONGO_DB]