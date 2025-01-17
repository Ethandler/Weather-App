# Weather Lookup Script

This Python script retrieves weather data for a given city using the OpenWeatherMap API. It converts city names into latitude and longitude using the Geocoding API and fetches weather details with the One Call API.

## Features
- Fetches weather by city name
- Supports Fahrenheit and Celsius
- Simple command-line interface

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Ethandler/Weather-App.git

2. Install Dependencies
pip install -r requirements.txt

3.Replace the API_KEY placeholder with your OpenWeatherMap API key in the script.

4.Run the script:
python weather_lookup.py
Example
Enter the name of a city: Prescott
Choose temperature unit (C for Celsius, F for Fahrenheit): F
Weather at latitude 34.54, longitude -112.47:
Temperature: 72°F
Humidity: 35%
Description: Clear sky
License
See LICENSE.md for details.