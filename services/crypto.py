import requests


def get_btc():
    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=BTCUSDT"
    data = requests.get(url, timeout=5).json()

    return{
        "price": float(data["lastPrice"]),
        "change": float(data["priceChangePercent"]),
    }

def get_eth():

    url = "https://api.binance.com/api/v3/ticker/24hr?symbol=ETHUSDT"
    data = requests.get(url, timeout=5).json()

    return{
        "price": float(data["lastPrice"]),
        "change": float(data["priceChange"]),
    }