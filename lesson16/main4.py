import tkinter as tk
import random

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")

# Game logic
def play(player_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    result = ""

    # Determine the result
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "You Lose!"

    # Update the labels
    player_choice_label.config(text=f"Your Choice: {player_choice}")
    computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")

# Labels to display choices and results
player_choice_label = tk.Label(root, text="Your Choice: ", font=("Arial", 14))
player_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 14))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16), fg="blue")
result_label.pack(pady=10)

# Buttons for user input
rock_button = tk.Button(root, text="Rock", font=("Arial", 12), command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", font=("Arial", 12), command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", font=("Arial", 12), command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Run the GUI application
root.mainloop()