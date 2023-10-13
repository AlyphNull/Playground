order = input("What do you want?")

def total_cost(order):
    # Menu with prices
    menu = {
        "Pizza": 6.00,
        "Nachos": 6.00,
        "Cheeseburger": 10.00,
        "Water": 4.00,
        "Coke": 5.00
    }
    
    # Calculate the total before tax
    subtotal = sum([menu[item] if item in menu else menu["Coke"] for item in order.split()])
    
    # Calculate the total cost including tax
    total = subtotal * 1.07  # 7% tax (1.07 is 100% + 7% tax)
    
    return total  # Return the total cost

# Call the function and store the result
result = total_cost(order)

# Print the result
print(round(result,2))


