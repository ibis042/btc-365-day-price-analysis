import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r"C:\Users\Javad\Desktop\for vs code\Data analys\Crypto_Project\btc_365_days.csv")

print(df.isnull().sum())    
print(f"Max Price of BTC {df["price_usd"].max()}")
print(f"Min Price of BTC {df['price_usd'].min()}")
print(f"Median price of BTC {df['price_usd'].mean()}")
first_price = df["price_usd"].iloc[0]
last_price = df["price_usd"].iloc[-1]
print(f"Difference between first-last day: {abs(first_price - last_price)}")


df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(10, 4))
plt.plot(df["date"], df["price_usd"], label="BTC Price (USD)")
plt.grid(True, alpha=0.3)
plt.title("Bitcoin Price Over the Last 365 Days")
plt.xlabel("Date")
plt.ylabel("Price (USD)")

plt.legend()
plt.tight_layout()
plt.show()