import requests


def get_prices():

    url = "https://api.binance.com/api/v3/ticker/price"

    symbols = "BTCUSDT,ETHUSDT"

    try:
        r = requests.get(url, params={"symbols": '["BTCUSDT","ETHUSDT"]'}, timeout=5)
        data = r.json()

        prices = {
            item["symbol"]: float(item["price"])
            for item in data
        }

        return {
            "btc": prices["BTCUSDT"],
            "eth": prices["ETHUSDT"]
        }

    except Exception as e:
        print("API error:", e)
        return None