import pandas as pd

def find_good_deals(asking_prices, fair_prices):
    asking_series = pd.Series(asking_prices)
    fair_series = pd.Series(fair_prices)
    good_deals = asking_series[asking_series < fair_series].index.tolist()
    return good_deals

# Taking user input
n = int(input("Enter the number of cars: "))
asking_prices = []
fair_prices = []

for i in range(n):
    asking_price = float(input(f"Enter asking price for car {i}: "))
    fair_price = float(input(f"Enter fair price for car {i}: "))
    asking_prices.append(asking_price)
    fair_prices.append(fair_price)

# Finding good deals
good_deal_indices = find_good_deals(asking_prices, fair_prices)
print("Good deals are at indices:", good_deal_indices)
