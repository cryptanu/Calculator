import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

# Global variables
current_input = ""
stored_num = None
current_operation = None

# Function to update the display
def update_display():
    display_var.set(current_input)

# Function to handle number button clicks
def number_click(number):
    global current_input
    current_input += str(number)
    update_display()

# Function to handle operation button clicks
def operation_click(operation):
    global current_input, stored_num, current_operation
    if current_input:
        if stored_num is None:
            stored_num = float(current_input)
        else:
            if current_operation:
                result = perform_operation(stored_num, float(current_input), current_operation)
                stored_num = result
                current_input = str(result)
                update_display()
        current_operation = operation
        current_input = ""
    else:
        current_operation = operation

# Function to perform the selected operation
def perform_operation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
            return None
        return num1 / num2
    elif operation == "%":
        if num2 == 0:
            messagebox.showerror("Error", "Modulus by zero is not allowed.")
            return None
        return num1 % num2
    elif operation == "√":
        if num1 < 0:
            messagebox.showerror("Error", "Square root of a negative number is not allowed.")
            return None
        return math.sqrt(num1)

# Function to handle the equal button click
def equal_click():
    global current_input, stored_num, current_operation
    if current_input and stored_num is not None and current_operation:
        result = perform_operation(stored_num, float(current_input), current_operation)
        if result is not None:
            current_input = str(result)
            stored_num = None
            current_operation = None
            update_display()

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a display pane
display_var = tk.StringVar()
display = ttk.Label(root, textvariable=display_var, font=("Arial", 18), anchor="e")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Create number and operation buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "√", "+",
    "="
]

row_val = 1
col_val = 0
for button_text in buttons:
    ttk.Button(root, text=button_text, command=lambda b=button_text: number_click(b) if b.isdigit() or b == "." else operation_click(b) if b in ("+", "-", "*", "/", "%", "√") else equal_click()).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Set row and column weights for resizing
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Run the Tkinter main loop
root.mainloop()

