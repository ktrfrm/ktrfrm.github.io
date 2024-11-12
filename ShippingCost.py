weight = 41.5
flat_charge = 20
flat_charge_premium = 125
if weight <= 2:
  ground_shipping_price = 1.5
  drone_shipping_price = 4.5
elif weight <= 6:
  ground_shipping_price = 3
  drone_shipping_price = 9
elif weight <= 10:
  ground_shipping_price = 4
  drone_shipping_price = 12
elif weight > 10:
  ground_shipping_price = 4.75
  drone_shipping_price = 14.25
else:
  print("Error")
  
# Ground Shipping
ground_shipping_cost = weight * ground_shipping_price + flat_charge
print("Ground Shipping: $ " + str(ground_shipping_cost))

# Premium Ground Shipping
ground_shipping_cost_premium = flat_charge_premium
print("Ground Shipping Premium: $ " + str(ground_shipping_cost_premium))

# Drone Shipping
drone_shipping_cost = weight * drone_shipping_price
print("Drone Shipping: $ " + str(drone_shipping_cost))
