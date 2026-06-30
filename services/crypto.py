import requests


def get_price(asset: str):

    url = f"https://api.coincap.io/v2/assets/{asset}"

    try:
        r = requests.get(url, timeout=5)
        data = r.json()

        price = data["data"]["priceUsd"]

        return float(price)

    except Exception as e:
        print("Crypto API error:", e)
        return None
