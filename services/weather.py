import requests


def get_weather():

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 51.1079,
        "longitude": 17.0385,
        "current_weather": True
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data["current_weather"]["temperature"]