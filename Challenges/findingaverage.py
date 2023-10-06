import random

# Generate 4 random integers between 1 and 100 (inclusive)
my_numbers = [random.randint(1, 100) for _ in range(4)]

# Calculate the average of the generated numbers
result = sum(my_numbers) / 4

# Ask user for input and compare it with the calculated average
x = int(input("What is the average of {}? ".format(my_numbers)))

# Check if the input matches the calculated average
if x == result:
    print("True")
else:
    print("False")
