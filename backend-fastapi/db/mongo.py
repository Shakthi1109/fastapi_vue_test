from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pymongo import ReturnDocument

load_dotenv()

mongo_uri = os.getenv('MONGO_URI')
client = AsyncIOMotorClient(mongo_uri)

# Define your database and collection
db = client['twitch_app1']
search_history_collection = db['search_history']

async def test_mongo_connection():
    try:
        await client.server_info()  # To check if the MongoDB server is accessible
        print("MongoDB connection is successful!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

async def db_write_search_history(game_name: str):
    """
    Increments frequency count for existing game_name,
    or inserts it with frequency 1 if it doesn't exist.
    """
    try:
        result = await search_history_collection.find_one_and_update(
            {"game_name": game_name},
            {"$inc": {"frequency": 1}},
            upsert=True,
            return_document=ReturnDocument.AFTER
        )
        print(f"Search history updated: {result}")
    except Exception as e:
        print(f"Error inserting/updating search history: {e}")
        raise

async def get_trending_searches(limit: int = 10):
    """
    Returns the top trending game names based on frequency.
    """
    try:
        trending = search_history_collection.find().sort("frequency", -1).limit(limit)
        return await trending.to_list(length=limit)
    except Exception as e:
        print(f"Error fetching trending searches: {e}")
        return []
