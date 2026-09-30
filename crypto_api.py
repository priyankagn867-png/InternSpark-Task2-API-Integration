import requests

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

def fetch_crypto_data(vs_currency="usd", per_page=20):
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": per_page,
        "page": 1,
        "sparkline": "false",
    }

    response = requests.get(API_URL, params=params, timeout=15)
    response.raise_for_status()
    return response.json()

def search_and_filter(data, keyword="", min_price=0):
    keyword = keyword.strip().lower()
    results = []

    for coin in data:
        name = str(coin.get("name", ""))
        symbol = str(coin.get("symbol", ""))

        if keyword and keyword not in name.lower() and keyword not in symbol.lower():
            continue

        price = coin.get("current_price")
        if price is None or price < min_price:
            continue

        results.append(coin)

    return results

def display(data):
    if not data:
        print("No matching coins found.")
        return

    print("\nID / NAME / SYMBOL / CURRENT PRICE / 24H CHANGE")
    print("-" * 72)
    for coin in data:
        print(
            f"{coin.get('id','-'):<18} "
            f"{coin.get('name','-'):<18} "
            f"{coin.get('symbol','-').upper():<7} "
            f"${coin.get('current_price', 0):>12,.4f} "
            f"{coin.get('price_change_percentage_24h') or 0:>8.2f}%"
        )

def main():
    print("=== InternSpark API Integration: Crypto Market Explorer ===")

    keyword = input("Search coin (blank = all): ").strip()
    min_price_text = input("Minimum price in USD (blank = 0): ").strip()

    try:
        min_price = float(min_price_text) if min_price_text else 0.0
        if min_price < 0:
            raise ValueError
    except ValueError:
        print("Invalid minimum price. Using 0.")
        min_price = 0.0

    try:
        data = fetch_crypto_data()
        filtered = search_and_filter(data, keyword, min_price)
        display(filtered)
    except requests.exceptions.RequestException as exc:
        print(f"API request failed: {exc}")
    except ValueError as exc:
        print(f"Unexpected response format: {exc}")

if __name__ == "__main__":
    main()
