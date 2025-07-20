import requests

# Got this key from OpenWeatherMap — hope it's still valid
API_KEY = 'e642268ba29a079af176e0844f2045f3'

# Standard URL for getting current weather
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Ask the user to enter the city name
city = input("Enter city name: ").strip()  # just trimming extra spaces

# Putting together the stuff we need to send to the API
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'  # Celsius — no one wants Kelvin...
}

# Trying to make the request — fingers crossed
try:
    response = requests.get(BASE_URL, params=params)

    # If everything went fine
    if response.status_code == 200:
        data = response.json()

        # Getting weather and temperature info
        weather = data['weather'][0]['description']
        temp = data['main']['temp']

        print(f"\nWeather in {city}: {weather.capitalize()}")
        print(f"Temperature: {temp}°C")

    elif response.status_code == 404:
        # So probably the city name is wrong
        print("Oops... couldn't find that city. Maybe check the spelling?")

    else:
        # No idea what went wrong but it wasn't good
        print(f"Something went wrong! Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Most likely no internet or some server issue
    print("Could not connect to the weather service.")
    print("Details:", e)
