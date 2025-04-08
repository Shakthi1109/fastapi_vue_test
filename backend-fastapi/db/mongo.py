from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

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
    """Writes search history to MongoDB asynchronously."""
    try:
        result = await search_history_collection.insert_one({"game_name": game_name})
        print(f"Search history for '{game_name}' inserted successfully with _id: {result.inserted_id}")
    except Exception as e:
        print(f"Error inserting search history: {e}")
        raise
