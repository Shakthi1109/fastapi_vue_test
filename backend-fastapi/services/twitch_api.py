import os
import httpx
from dotenv import load_dotenv

# Getting credentials from environment file
load_dotenv()

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

async def get_twitch_token():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "grant_type": "client_credentials"
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(url, params=params)
        data = response.json()
        return data["access_token"]
    
    
async def get_game_id(game_name: str, twitch_access_token: str):
    url = "https://api.twitch.tv/helix/games"
    headers = {
        "Authorization": f"Bearer {twitch_access_token}",
        "Client-ID": CLIENT_ID
    }
    params = {
        "name": game_name
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)
        data = response.json()
        
        if "data" in data and len(data["data"]) > 0:
            return data["data"][0]["id"]
        else:
            print("Error: No valid data found in the response.")
            return None
    
