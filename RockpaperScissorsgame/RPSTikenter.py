import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Function to handle user choice and update the result
def play(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Creating the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Adding buttons for user choices
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: play('rock'))
paper_button = tk.Button(root, text="Paper", width=15, command=lambda: play('paper'))
scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: play('scissors'))

rock_button.grid(row=0, column=0, padx=10, pady=10)
paper_button.grid(row=0, column=1, padx=10, pady=10)
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Label to display the result
result_label = tk.Label(root, text="Make your choice!", font=('Helvetica', 16))
result_label.grid(row=1, column=0, columnspan=3, pady=20)

# Running the main event loop
root.mainloop()
