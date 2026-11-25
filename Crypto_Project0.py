import pandas as pd
import matplotlib.pyplot as plt
import requests



url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    "vs_currency": "usd",
    "days": "365",
}

response = requests.get(url, params=params, timeout=15)
data = response.json()


df = pd.DataFrame(data["prices"], columns=["timestamp", "price_usd"])
df["date"] = pd.to_datetime(df["timestamp"], unit="ms")
df = df[["date", "price_usd"]]

df.to_csv("btc_365_days.csv", index=False)
print("Hazırdır! İlk 5 sətir:")
print(df.head())