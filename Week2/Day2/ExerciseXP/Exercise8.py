
toppings = []

while True:
    
    topping = input("Enter a topping to add to your pizza (or 'quit' to finish): ")
    
    
    if topping.lower() == 'quit':
        break
    
    
    toppings.append(topping)
    

    print("Adding", topping, "to your pizza.")

total_price = 10 + len(toppings) * 2.5

print("\nYour pizza toppings:")
for topping in toppings:
    print("-", topping)
print("\nTotal price of your pizza:", total_price)
