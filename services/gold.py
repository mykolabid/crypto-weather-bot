import requests


def get_gold_price():

    url = "https://api.gold-api.com/price/XAU"

    response = requests.get(url)

    data = response.json()

    return data["price"]
