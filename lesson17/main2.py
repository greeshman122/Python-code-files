import tkinter as tk
import random

# Possible choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play the game
def play_game():
    user_choice = user_entry.get().capitalize()
    if user_choice not in choices:
        result_label.config(text="Invalid choice! Please enter Rock, Paper, or Scissors.")
        return
    
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"Computer: {computer_choice}\n{result}")

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "Rock" and computer == "Scissors") or (user == "Paper" and computer == "Rock") or (user == "Scissors" and computer == "Paper"):
        return "You win!"
    else:
        return "You lose!"

# Create GUI window
root = tk.Tk()
root.title("Rock Paper Scissors Game")

# Input field and play button
tk.Label(root, text="Enter Rock, Paper, or Scissors:").pack()
user_entry = tk.Entry(root)
user_entry.pack()
tk.Button(root, text="Play", command=play_game).pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the Tkinter event loop
root.mainloop()
