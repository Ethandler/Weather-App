import requests

API_KEY = "your_api_key_here"   # Replace "your_api_key_here" with your actual OpenWeatherMap API key
WEATHER_URL = "https://api.openweathermap.org/data/3.0/onecall"
GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"

def get_lat_lon(city_name):
    """Fetch latitude and longitude for a given city name."""
    try:
        params = {
            "q": city_name,
            "limit": 1,
            "appid": API_KEY
        }
        response = requests.get(GEOCODING_URL, params=params)
        response.raise_for_status()

        data = response.json()
        if not data:
            raise ValueError("City not found. Please check the name and try again.")

        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except Exception as e:
        print(f"Error: {e}")
        return None, None

def get_weather(lat, lon):
    """Fetch weather data using latitude and longitude."""
    try:
        units = input("Choose temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()
        units_param = "imperial" if units == "F" else "metric"

        # Build request URL
        params = {
            "lat": lat,
            "lon": lon,
            "appid": API_KEY,
            "units": units_param,
            "exclude": "minutely,hourly,alerts",  # Optional: exclude unneeded data
        }
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()
        current = data.get("current", {})
        temp = current.get("temp")
        humidity = current.get("humidity")
        description = current.get("weather", [{}])[0].get("description", "No description available")

        if temp is None or humidity is None:
            raise ValueError("Incomplete data received from API.")

        # Display weather information
        unit_label = "°F" if units == "F" else "°C"
        print(f"Weather at latitude {lat}, longitude {lon}:")
        print(f"Temperature: {temp}{unit_label}")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except ValueError as val_err:
        print(f"Error: {val_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    city = input("Enter the name of a city: ").strip()
    lat, lon = get_lat_lon(city)
    if lat is not None and lon is not None:
        get_weather(lat, lon)
