import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import requests

# Function to get weather based on the month
def get_weather(month):
    if month in range(5, 10):
        return "Sunny"
    elif month == 10:
        return "Rainy"
    elif month in range(11, 2):
        return "Snowy"
    else:
        return "Chill"

# Function to get celebrity birthdays based on the provided date
def get_celebrities_birthdays(date):
    # You can implement logic to fetch celebrity data from an API or a database here
    # For simplicity, let's return a hardcoded list of celebrities
    celebrities = ["John Doe", "Jane Smith", "Alice Johnson"]
    return celebrities

# Function to handle button click
def on_submit():
    try:
        birth_date = datetime.strptime(date_entry.get(), "%Y-%m-%d")
        day_of_week = birth_date.strftime("%A")
        month = birth_date.month
        weather = get_weather(month)
        celebrities = get_celebrities_birthdays(birth_date)
        
        result_label.config(text=f"Day of the Week: {day_of_week}\nWeather: {weather}\nCelebrities: {', '.join(celebrities)}")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format! Please enter date in YYYY-MM-DD format.")

# Create main window
root = tk.Tk()
root.title("Birthday Information")
root.geometry("300x200")
root.configure(bg='blue')

# Date entry
date_label = tk.Label(root, text="Enter your birthdate (YYYY-MM-DD):", bg='blue', fg='white')
date_label.pack()
date_entry = tk.Entry(root)
date_entry.pack()

# Submit button
submit_button = tk.Button(root, text="Submit", command=on_submit, bg='white', fg='blue')
submit_button.pack()

# Result label
result_label = tk.Label(root, text="", bg='blue', fg='white')
result_label.pack()

# Run the tkinter main loop
root.mainloop()
