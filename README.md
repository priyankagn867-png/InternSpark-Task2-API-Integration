# Task 2 — API Integration

Uses Python `requests` to call the public CoinGecko market API, parse JSON, and provide search/filter support.

No API key is required for the included demonstration endpoint.

Run:

```bash
pip install requests
python crypto_api.py
```

Example interaction:

```text
Search coin (blank = all): bitcoin
Minimum price in USD (blank = 0): 100
```

Because this is a live API, exact prices and output values change over time.
