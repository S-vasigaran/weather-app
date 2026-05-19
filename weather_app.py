import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY", "your_api_key_here")
BASE_URL = "https://api.openweathermap.org/data/2.5"


def get_current_weather(city: str) -> dict:
    """Fetch current weather data for a given city."""
    url = f"{BASE_URL}/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_5day_forecast(city: str) -> dict:
    """Fetch 5-day / 3-hour forecast for a given city."""
    url = f"{BASE_URL}/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def display_current_weather(data: dict) -> None:
    """Display current weather information."""
    city        = data["name"]
    country     = data["sys"]["country"]
    temp        = data["main"]["temp"]
    feels_like  = data["main"]["feels_like"]
    humidity    = data["main"]["humidity"]
    description = data["weather"][0]["description"].capitalize()
    wind_speed  = data["wind"]["speed"]
    visibility  = data.get("visibility", 0) // 1000  # convert to km

    print("\n" + "=" * 45)
    print(f"  📍 Weather in {city}, {country}")
    print("=" * 45)
    print(f"  🌡  Temperature  : {temp:.1f}°C  (Feels like {feels_like:.1f}°C)")
    print(f"  🌤  Condition    : {description}")
    print(f"  💧 Humidity     : {humidity}%")
    print(f"  💨 Wind Speed   : {wind_speed} m/s")
    print(f"  👁  Visibility   : {visibility} km")
    print("=" * 45)


def display_5day_forecast(data: dict) -> None:
    """Display a daily summary of the 5-day forecast."""
    print("\n  📅  5-Day Forecast")
    print("-" * 45)

    seen_dates = {}
    for entry in data["list"]:
        date_str = entry["dt_txt"].split(" ")[0]
        hour     = int(entry["dt_txt"].split(" ")[1].split(":")[0])

        # Pick the midday reading (12:00) as the daily representative
        if date_str not in seen_dates and hour == 12:
            seen_dates[date_str] = entry

    # Fallback: if no 12:00 slot found for a date, use first available
    for entry in data["list"]:
        date_str = entry["dt_txt"].split(" ")[0]
        if date_str not in seen_dates:
            seen_dates[date_str] = entry

    for date_str, entry in sorted(seen_dates.items()):
        date_obj    = datetime.strptime(date_str, "%Y-%m-%d")
        day_label   = date_obj.strftime("%A, %d %b")
        temp        = entry["main"]["temp"]
        description = entry["weather"][0]["description"].capitalize()
        humidity    = entry["main"]["humidity"]
        print(f"  {day_label:<20} {temp:>5.1f}°C  {description:<25} 💧{humidity}%")

    print("-" * 45)


def main():
    print("\n╔══════════════════════════════════════════╗")
    print("║        🌦  Python Weather App  🌦        ║")
    print("╚══════════════════════════════════════════╝")

    while True:
        city = input("\n  Enter city name (or 'quit' to exit): ").strip()

        if city.lower() in ("quit", "exit", "q"):
            print("\n  Goodbye! Stay weather-aware. 👋\n")
            break

        if not city:
            print("  ⚠  Please enter a valid city name.")
            continue

        try:
            print(f"\n  Fetching weather data for '{city}'...")

            current_data  = get_current_weather(city)
            forecast_data = get_5day_forecast(city)

            display_current_weather(current_data)
            display_5day_forecast(forecast_data)

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"  ❌ City '{city}' not found. Please check the spelling.")
            elif e.response.status_code == 401:
                print("  ❌ Invalid API key. Please check your .env file.")
            else:
                print(f"  ❌ HTTP Error: {e}")
        except requests.exceptions.ConnectionError:
            print("  ❌ Connection error. Please check your internet connection.")
        except requests.exceptions.Timeout:
            print("  ❌ Request timed out. Please try again.")
        except Exception as e:
            print(f"  ❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
