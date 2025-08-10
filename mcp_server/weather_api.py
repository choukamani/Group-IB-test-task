import httpx

USER_AGENT = "WeatherAgent/1.0 (your_email@example.com)"

async def fetch_coordinates(city: str):
    response = httpx.get(
        "https://nominatim.openstreetmap.org/search",
        params={"q": city, "format": "json"},
        headers={"User-Agent": USER_AGENT}
    )
    data = response.json()
    if data:
        return float(data[0]["lat"]), float(data[0]["lon"])
    raise ValueError("City not found")

async def fetch_weather(lat: float, lon: float, date=None, forecast=False):
    params = {"latitude": lat, "longitude": lon, "current_weather": not forecast}
    if date:
        params.update({"start_date": date, "end_date": date})
    response = httpx.get(
        "https://api.open-meteo.com/v1/forecast",
        params=params,
        headers={"User-Agent": USER_AGENT}
    )
    return response.json()

def get_coordinates(city: str):
    return httpx.run(lambda: fetch_coordinates(city))

def get_weather(lat: float, lon: float, date: str = None, forecast: bool = False):
    return httpx.run(lambda: fetch_weather(lat, lon, date, forecast))
