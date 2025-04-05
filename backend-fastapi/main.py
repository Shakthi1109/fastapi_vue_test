from fastapi import FastAPI
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

TWITCH_CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")


@app.get("/")
def home():
    return {"message": "Twitch Video Search Backend is running"}




