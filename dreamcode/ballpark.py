o = input()

def price(o):
    items = o.split()
    a, b, c, d = items

    e = 6
    f = 10
    g = 4
    h = 5

    if a == "Nachos" or b == "Nachos" or c == "Nachos" or d == "Nachos" or a == "Pizza" or b == "Pizza" or c == "Pizza" or d == "Pizza":
        a, b, c, d = e, e, e, e
    elif a == "Cheeseburger" or b == "Cheeseburger" or c == "Cheeseburger" or d == "Cheeseburger":
        a, b, c, d = f, f, f, f
    elif a == "Water" or b == "Water" or c == "Water" or d == "Water":
        a, b, c, d = g, g, g, g
    elif a == "Coke" or b == "Coke" or c == "Coke" or d == "Coke":
        a, b, c, d = h, h, h, h
    else:
        a, b, c, d = h, h, h, h

    return a, b, c, d

result_a, result_b, result_c, result_d = price(o)

total_price = result_a + result_b + result_c + result_d

result = total_price + (total_price*0.07)

print(result)
