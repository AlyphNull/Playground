import random

my_numbers=[random.randint(1,10) for _ in range(4)]

result = sum(my_numbers)

x = int(input("What is the sum of {}".format(my_numbers)))

if x==result:
   print("correct")
else: 
   print("wrong")
   