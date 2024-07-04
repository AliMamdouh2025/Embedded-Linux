import tkinter as tk
from tkinter import messagebox

def calculate_factorial():
    """Calculates factorial of the number entered by the user."""
    try:
        # Retrieve the integer input from the entry widget
        n = int(entry.get())
        
        # Validate input: Factorial is not defined for negative numbers
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        
        # Calculate factorial
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        
        # Display factorial result in a message box
        messagebox.showinfo("Factorial", f"The factorial of {n} is {factorial}")
    
    except ValueError:
        # Handle ValueError if input is not a valid integer
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create the main window
root = tk.Tk()
root.title("Factorial Calculator")  # Set window title

# Create widgets
label = tk.Label(root, text="Enter an integer:")  # Create label widget
label.pack(pady=10)  # Pack label widget with vertical padding

entry = tk.Entry(root, width=20)  # Create entry widget
entry.pack()  # Pack entry widget

calculate_button = tk.Button(root, text="Calculate Factorial", command=calculate_factorial)
# Create button widget with command to calculate factorial
calculate_button.pack(pady=10)  # Pack button widget with vertical padding

# Run the main loop
root.mainloop()  # Start tkinter event loop to display window and handle user interactions
