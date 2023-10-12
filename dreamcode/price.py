og_price = int (input("what is the original price "))
p_discount= int(input ("what is the percentage discount "))

p = og_price-(og_price*(p_discount/100))

print (f"The new price for an item that use to cost {og_price} at a {p_discount} is {p}")