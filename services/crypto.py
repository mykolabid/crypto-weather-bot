import requests


def get_crypto_prices():

    url = "https://api.coingecko.com/api/v3/simple/price"

    params = {
        "ids": "bitcoin,ethereum",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    response = requests.get(url, params=params)

    data = response.json()

    btc = data["bitcoin"]
    eth = data["ethereum"]

    return btc,eth