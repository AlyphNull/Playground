from datetime import datetime

# Function to get weather based on the month
def get_weather(month):
    if month in range(5, 10):
        return "Sunny"
    elif month == 10:
        return "Rainy"
    elif month in range(11, 2) or month == 2:
        return "Snowy"
    else:
        return "Chill"

# Function to get celebrity birthdays based on the provided date
def get_celebrities_birthdays(date):
    # Implement logic to fetch celebrity data from an API or database
    # For simplicity, let's return a hardcoded list of celebrities
    celebrities = ["Your Mama"]
    return celebrities

# Function to handle input and display result
def get_birthday_info():
    date_input = input("Enter your birthdate (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(date_input, "%Y-%m-%d")
        day_of_week = birth_date.strftime("%A")
        month = birth_date.month
        weather = get_weather(month)
        celebrities = get_celebrities_birthdays(birth_date)
        
        print(f"Day of the Week: {day_of_week}")
        print(f"Weather: {weather}")
        print(f"Celebrities: {', '.join(celebrities)}")
    except ValueError:
        print("Invalid date format! Please enter date in YYYY-MM-DD format.")

# Call the function to get input and display result
get_birthday_info()
