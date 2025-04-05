from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Twitch Video Search Backend is running"}