import tkinter as tk #This imports the Tkinter module, which is used for creating GUI applications. It's aliased as tk for convenience.
from tkinter import messagebox #This imports the messagebox module from Tkinter, which is used to display message boxes (like error messages) to the user.

def create_main_window():
    """
    Create and return the main application window.
    """
    root = tk.Tk()
    root.title("Sum Calculator")
    return root

def create_label(parent, text, row, column, padx = 10, pady = 10):
    """
    Create and place a label in the specified parent widget.

    Args:
    parent: The parent widget.
    text: The text to display on the label.
    row: The row in the grid where the label should be placed.
    column: The column in the grid where the label should be placed.
    padx: Padding along the x-axis (default is 10).
    pady: Padding along the y-axis (default is 10).
    """
    label = tk.Label(parent, text = text)
    label.grid(row = row, column = column, padx = padx, pady = pady)
    return label

def create_entry(parent, row, column, padx = 10, pady = 10):
    """
    Create and place an entry widget in the specified parent widget.

    Args:
    parent: The parent widget.
    row: The row in the grid where the entry should be placed.
    column: The column in the grid where the entry should be placed.
    padx: Padding along the x-axis (default is 10).
    pady: Padding along the y-axis (default is 10).
    """
    entry = tk.Entry(parent)
    entry.grid(row = row, column = column, padx = padx, pady = pady)
    return entry

def create_button(parent, text, command, row, column, columnspan = 1, pady = 10):
    """
    Create and place a button in the specified parent widget.

    Args:
    parent: The parent widget.
    text: The text to display on the button.
    command: The function to call when the button is clicked.
    row: The row in the grid where the button should be placed.
    column: The column in the grid where the button should be placed.
    columnspan: The number of columns the button should span (default is 1).
    pady: Padding along the y-axis (default is 10).
    """
    button = tk.Button(parent, text = text, command = command)
    button.grid(row = row, column = column, columnspan = columnspan, pady = pady)
    return button

def create_result_label(parent, row, column, columnspan = 1, pady = 10):
    """
    Create and place a result label in the specified parent widget.

    Args:
    parent: The parent widget.
    row: The row in the grid where the label should be placed.
    column: The column in the grid where the label should be placed.
    columnspan: The number of columns the label should span (default is 1).
    pady: Padding along the y-axis (default is 10).
    """
    label = tk.Label(parent, text = "Sum is not entered yet ")
    label.grid(row = row, column = column, columnspan = columnspan, pady = pady)
    return label

def calculate_sum(entry1, entry2, result_label):
    """
    Calculate the sum of the integers entered in the two entry widgets and display the result.

    Args:
    entry1: The first entry widget.
    entry2: The second entry widget.
    result_label: The label to display the result.
    """
    try:
        num1 = int(entry1.get())  # Get the first integer from entry1
        num2 = int(entry2.get())  # Get the second integer from entry2
        total = num1 + num2       # Calculate the sum of num1 and num2
        result_label.config(text=f"Sum is: {total}")  # Update the result label with the sum
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integers")  # Show error if input is invalid

# Main application setup
root = create_main_window()

# Create and place widgets in the main window
label1 = create_label(root, "Enter first integer:", 0, 0)
entry1 = create_entry(root, 0, 1)

label2 = create_label(root, "Enter second integer:", 1, 0)
entry2 = create_entry(root, 1, 1)

calculate_button = create_button(root, "Calculate", lambda: calculate_sum(entry1, entry2, result_label), 2, 0, columnspan = 2)

result_label = create_result_label(root, 3, 0, columnspan = 2)

# Run the main event loop
root.mainloop()
