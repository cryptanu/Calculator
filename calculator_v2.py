import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        elif operation == "Modulus":
            if num2 == 0:
                messagebox.showerror("Error", "Modulus by zero is not allowed.")
                return
            result = num1 % num2
        elif operation == "Square Root":
            if num1 < 0:
                messagebox.showerror("Error", "Square root of a negative number is not allowed.")
                return
            result = math.sqrt(num1)

        result_label.config(text=f"Result: {result:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create labels and entry fields
label_num1 = ttk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_num1 = ttk.Entry(root)
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = ttk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_num2 = ttk.Entry(root)
entry_num2.grid(row=1, column=1, padx=10, pady=5)

# Create buttons with text labels for each operation
operation_var = tk.StringVar()
operation_var.set("Addition")

addition_button = ttk.Button(root, text="Addition", command=lambda: operation_var.set("Addition"))
subtraction_button = ttk.Button(root, text="Subtraction", command=lambda: operation_var.set("Subtraction"))
multiplication_button = ttk.Button(root, text="Multiplication", command=lambda: operation_var.set("Multiplication"))
division_button = ttk.Button(root, text="Division", command=lambda: operation_var.set("Division"))
modulus_button = ttk.Button(root, text="Modulus", command=lambda: operation_var.set("Modulus"))
square_root_button = ttk.Button(root, text="Square Root", command=lambda: operation_var.set("Square Root"))

addition_button.grid(row=2, column=0, padx=10, pady=5)
subtraction_button.grid(row=2, column=1, padx=10, pady=5)
multiplication_button.grid(row=3, column=0, padx=10, pady=5)
division_button.grid(row=3, column=1, padx=10, pady=5)
modulus_button.grid(row=4, column=0, padx=10, pady=5)
square_root_button.grid(row=4, column=1, padx=10, pady=5)

# Create a button to perform the calculation
calculate_button = ttk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=5, columnspan=2, padx=10, pady=15)

# Create a label to display the result
result_label = ttk.Label(root, text="Result:")
result_label.grid(row=6, columnspan=2, padx=10, pady=5)

# Run the Tkinter main loop
root.mainloop()

