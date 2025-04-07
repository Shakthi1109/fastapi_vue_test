from fastapi import FastAPI
import os
from dotenv import load_dotenv
from services.twitch_api import search_videos_by_game
from fastapi.middleware.cors import CORSMiddleware
# from db.mongo import save_search_query
# from db.mongo import queries_collection


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")


@app.get("/")
def home():
    return {"message": "Twitch Video Search Backend is running"}


@app.get("/search")
async def search(game: str):
    # await save_search_query(game)
    return await search_videos_by_game(game)


# @app.get("/trending")
# async def get_trending_queries():
#     pipeline = [
#         {"$group": {"_id": "$query", "count": {"$sum": 1}}},
#         {"$sort": {"count": -1}},
#         {"$limit": 10}
#     ]
#     results = await queries_collection.aggregate(pipeline).to_list(length=10)
#     return [{"query": r["_id"], "count": r["count"]} for r in results]


# @app.get("/autocomplete")
# async def autocomplete(query: str):
#     results = await queries_collection.find(
#         {"query": {"$regex": f"^{query}", "$options": "i"}}
#     ).limit(5).to_list(length=5)
    
#     # Remove duplicates
#     unique = list({r["query"] for r in results})
#     return unique

