import tkinter as tk

# Function to convert length
def convert():
    meters = float(entry.get())

    centimeters = meters * 100
    kilometers = meters / 1000

    result_label.config(
        text=f"{meters} m = {centimeters} cm\n{meters} m = {kilometers} km"
    )

# Main Window
root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x250")

title = tk.Label(root, text="Length Converter",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

label = tk.Label(root, text="Enter Length in Meters:",
                 font=("Arial", 12))
label.pack()

entry = tk.Entry(root, width=25)
entry.pack(pady=10)

button = tk.Button(root, text="Convert",
                   command=convert)
button.pack(pady=10)

result_label = tk.Label(root, text="",
                        font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()