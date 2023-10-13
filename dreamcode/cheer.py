yrds = int(input())

def chr(yrds):
    if 1 <= yrds <= 10:
        p="Ra!"
        x = p*yrds
    elif yrds > 10:
        x = "High Five"
    elif yrds < 1:
        x = "shh"
    return x

result = chr(yrds)

print(result)

