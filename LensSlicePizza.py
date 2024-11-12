# the kinds of pizzas to sell
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# each kind of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

# Count pizza with the same price $2
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# count kinds of pizza
num_pizzas = len(toppings)
print("We sell " + str(num_pizzas) + " different kinds of pizza!")

# create two-dimensional list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7,"anchovies"], [2, "mushrooms"]]

# Sort pizza_and_prices so that the pizzas are in the order of increasing price (ascending)
pizza_and_prices.sort()
print(pizza_and_prices)

# cheapest and priciest pizza
cheapest_pizza = pizza_and_prices[1]
print("The cheapest pizza: " + str(cheapest_pizza))
priciest_pizza = pizza_and_prices[-1]
print("The priciest pizza: " + str(priciest_pizza))

# remove priciest pizza
pizza_and_prices.remove(pizza_and_prices[-1])
print(pizza_and_prices)

# add the new pizza
pizza_and_prices.insert(4,[2.5, "peppers"])
print(pizza_and_prices)

# select three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print("The three cheapest pizzas: " + str(three_cheapest))
