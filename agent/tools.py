import httpx
from langchain.tools import Tool
import os

MCP_URL = os.getenv("MCP_SERVER_URL", "http://localhost:8000")

def tool_coordinates(city: str):
    res = httpx.get(f"{MCP_URL}/coordinates", params={"city": city})
    data = res.json()
    if "lat" in data:
        return f"{data['lat']},{data['lon']}"
    return "Coordinates not found."

def tool_weather(coords: str):
    lat, lon = coords.split(",")
    res = httpx.get(f"{MCP_URL}/weather", params={"lat": lat, "lon": lon})
    return res.json()

tools = [
    Tool(name="get_coordinates", func=tool_coordinates, description="Get latitude and longitude from a city name."),
    Tool(name="get_weather", func=tool_weather, description="Get weather data (current, forecast, or historical) from coordinates.")
]
