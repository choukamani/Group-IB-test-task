from fastapi import FastAPI
from weather_api import get_coordinates, get_weather

app = FastAPI()

@app.get("/coordinates")
def coordinates(city: str):
    return get_coordinates(city)

@app.get("/weather")
def weather(lat: float, lon: float, date: str = None, forecast: bool = False):
    return get_weather(lat, lon, date=date, forecast=forecast)
