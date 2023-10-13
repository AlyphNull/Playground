order = input()


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
    
    # Calculate
result = subtotal*0.07

print (result)
