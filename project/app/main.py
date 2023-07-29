from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()


# Define an endpoint that returns a JSON response with a "ping" key and a "pong!" value.
# The endpoint also includes the environment and testing settings from the app's configuration.
@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    Endpoint that returns a JSON response with a "ping" key and a "pong!" value.
    """
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
