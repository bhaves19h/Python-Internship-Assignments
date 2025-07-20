#c9afe899a2372d4b00cc5d051a956692

import requests

# Replace this with your actual API key from OpenWeatherMap
API_KEY = 'e642268ba29a079af176e0844f2045f3'

# Base URL for the OpenWeatherMap current weather API
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Get city name from user
city = input("Enter city name: ").strip()

# Prepare request parameters
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'  # To get temperature in Celsius
}

# Make the API request
try:
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        # Successful response
        data = response.json()

        # Extract weather description and temperature
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']

        # Display the weather info
        print(f"\nWeather in {city}: {weather_desc}")
        print(f"Temperature: {temp}°C")

    elif response.status_code == 404:
        # City not found
        print("City not found. Please check the spelling and try again.")
    else:
        # Some other error occurred
        print(f"Error fetching data. Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Handle any network-related errors (e.g., no internet)
    print("Failed to connect to the weather service.")
    print("Error:", e)
