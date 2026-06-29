import requests


def get_crypto_prices():

    btc_url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
    eth_url = "https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT"

    btc_data = requests.get(btc_url, timeout=5).json()
    eth_data = requests.get(eth_url, timeout=5).json()

    btc = {
        "usd": float(btc_data["lastPrice"]),
        "change": float(btc_data["priceChangePercent"])
    }

    eth = {
        "usd": float(eth_data["lastPrice"]),
        "change": float(eth_data["priceChangePercent"])
    }

    return btc, eth