import requests


def get_btc_price():

    url = "https://api.binance.com/api/v3/ticker/price"

    r = requests.get(url, params={"symbol": "BTCUSDT"}, timeout=5)
    data = r.json()

    return float(data.get("price", 0))


def get_eth_price():

    url = "https://api.binance.com/api/v3/ticker/price"

    r = requests.get(url, params={"symbol": "ETHUSDT"}, timeout=5)
    data = r.json()

    return float(data.get("price", 0))