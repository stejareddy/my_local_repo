import tkinter as tk
import random

def on_button_click(value):
    """Handles button click events and updates the entry field."""
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear_entry():
    """Clears the calculator entry field."""
    entry_var.set("")

def calculate_result():
    """Evaluates the expression in the entry field and displays the result."""
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception:
        entry_var.set("Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry field for displaying the expression/result
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Define button labels
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons and place them in the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), bg="lightblue", command=calculate_result)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: on_button_click(t))

    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Clear button
clear_button = tk.Button(root, text="C", font=("Arial", 18), bg="red", command=clear_entry)
clear_button.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Configure row and column resizing
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

# Run the Tkinter event loop
root.mainloop()
