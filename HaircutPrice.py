 Prices and Cuts:
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]
print ("Prices: " + str(prices))
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for x in prices:
  total_price +=x
average_price = total_price / len(prices)
print("Average Haircut Price: " + str(average_price))

new_prices = [ price - 5 for price in prices]
print("New prices: " + str(new_prices))

#Revenue:
total_revenue = 0
for i in range(len(hairstyles)):
   total_revenue += prices[i] * last_week[i]

print("Total Revenue for old prices: "+ str(total_revenue))

average_daily_revenue = total_revenue/7
print("Average daily revenue: " + str(average_daily_revenue))

# Find cuts with new prices under 30
cuts_under_30 = [price for price in new_prices if price < 30]
print(cuts_under_30)
