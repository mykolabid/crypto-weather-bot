import requests

def get_usd_uah():

    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)

    data = response.json()

    rate = data["rates"]["UAH"]

    return rate