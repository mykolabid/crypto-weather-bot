import requests


def get_price(symbol: str):

    url = "https://api.binance.com/api/v3/ticker/24hr"

    try:
        r = requests.get(url, params={"symbol": symbol}, timeout=5)
        data = r.json()

        return {
            "price": float(data["lastPrice"]),
            "change": float(data["priceChangePercent"])
        }

    except Exception as e:
        print("API error:", e)
        return None