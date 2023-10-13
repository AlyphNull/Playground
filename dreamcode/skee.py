score=int(input())
price=int(input())


def can_buy(score, price):
    tickets = score // 12
    if tickets >= price:
        return "Buy it!"
    else:
        return "Try again"

# Sample input

print(can_buy(score, price))