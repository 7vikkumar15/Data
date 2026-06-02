import tkinter as tk
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play game
def play(user_choice):
    computer_choice = random.choice(choices)

    user_label.config(text="You chose: " + user_choice)
    computer_label.config(text="Computer chose: " + computer_choice)

    # Decide winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(text=result)

# Main window
root = tk.Tk()
root.title("Rock Paper Scissors App")
root.geometry("400x300")

title = tk.Label(root, text="Rock Paper Scissors Game",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

user_label = tk.Label(root, text="You chose: ",
                      font=("Arial", 12))
user_label.pack()

computer_label = tk.Label(root, text="Computer chose: ",
                          font=("Arial", 12))
computer_label.pack()

result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"))
result_label.pack(pady=20)

# Buttons
rock_btn = tk.Button(root, text="Rock",
                     width=12,
                     command=lambda: play("Rock"))
rock_btn.pack(pady=5)

paper_btn = tk.Button(root, text="Paper",
                      width=12,
                      command=lambda: play("Paper"))
paper_btn.pack(pady=5)

scissor_btn = tk.Button(root, text="Scissors",
                        width=12,
                        command=lambda: play("Scissors"))
scissor_btn.pack(pady=5)

root.mainloop()