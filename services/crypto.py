import requests


def get_btc_price():

    url = "https://api.binance.com/api/v3/ticker/price"
    data = requests.get(url, params={"symbol": "BTCUSDT"}, timeout=5).json()

    return float(data["price"])


def get_eth_price():

    url = "https://api.binance.com/api/v3/ticker/price"
    data = requests.get(url, params={"symbol": "ETHUSDT"}, timeout=5).json()

    return float(data["price"])