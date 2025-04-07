import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = AsyncIOMotorClient(MONGO_URI)
db = client["twitch_app"]    


videos_collection = db["videos"]
queries_collection = db["search_queries"]


# async def save_search_query(query: str):
#     await queries_collection.insert_one({
#         "query": query,
#         "timestamp": datetime.utcnow()
#     })