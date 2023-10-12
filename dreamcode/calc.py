import random

for _ in range(10):
    r1, r2 = random.randint(0, 100), random.randint(1, 100)

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b != 0 and a%b==0:
            return a//b
        else:
            return "Division by zero is not allowed."

    # Create a list of functions
    function_list = [add, subtract, multiply, divide]

    # Randomly select a function from the list
    selected_function = random.choice(function_list)

    user_answer = int(input(f"What is {r1} {selected_function.__name__} {r2}? "))

    # Call the selected function to calculate the correct answer
    correct_answer = selected_function(r1, r2)

    if user_answer == correct_answer:
        print("Correct")
    else:
        print(f"Incorrect, the correct answer is {correct_answer}")

