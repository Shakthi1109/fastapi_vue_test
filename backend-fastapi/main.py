from fastapi import FastAPI
import os
from dotenv import load_dotenv
from services.twitch_api import search_videos_by_game
from fastapi.middleware.cors import CORSMiddleware


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
    return await search_videos_by_game(game)

