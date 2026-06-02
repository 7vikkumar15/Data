import tkinter as tk

# Function to check password strength
def check_password():
    password = entry.get()

    strength = 0

    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(not char.isalnum() for char in password):
        strength += 1

    # Result
    if strength <= 2:
        result = "Weak Password"
    elif strength <= 4:
        result = "Medium Password"
    else:
        result = "Strong Password"

    result_label.config(text=result)

# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x250")

title = tk.Label(root, text="Password Strength Checker",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

label = tk.Label(root, text="Enter Password:",
                 font=("Arial", 12))
label.pack()

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

check_btn = tk.Button(root, text="Check Strength",
                      command=check_password)
check_btn.pack(pady=10)

result_label = tk.Label(root, text="",
                        font=("Arial", 14, "bold"))
result_label.pack(pady=10)

root.mainloop()