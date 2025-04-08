from fastapi import FastAPI
from dotenv import load_dotenv
from services.twitch_api import search_videos_by_game
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from db.mongo import get_trending_searches


load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Twitch Video Search Backend is running"}


@app.get("/search")
async def search(game: str):
    # await save_search_query(game)
    return await search_videos_by_game(game)

@app.get("/trending-searches")
async def trending_searches():
    trending = await get_trending_searches(limit=5)
    return [
        {
            "game_name": item["game_name"],
            "frequency": item["frequency"]
        }
        for item in trending
    ]