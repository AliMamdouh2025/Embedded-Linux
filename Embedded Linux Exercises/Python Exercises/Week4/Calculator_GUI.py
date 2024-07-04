import tkinter as tk

def validate_and_get_inputs():
    """
    Validate the input values to ensure they are integers.
    Returns the values as integers if valid, otherwise returns None.
    """
    op1 = entry1.get()  # Get the value from the first entry widget
    op2 = entry2.get()  # Get the value from the second entry widget

    # Check if both inputs are valid integers
    if not op1.isdigit() or not op2.isdigit():
        label_result.config(text="Please enter valid integers.")  # Update the result label with an error message
        return None, None  # Return None if inputs are invalid

    return int(op1), int(op2)  # Return the integer values of the inputs

def perform_operation(op1, op2):
    """
    Perform the selected operation (addition or subtraction) based on the radio button value.
    Returns the result as a string.
    """
    if v3.get() == 1:
        # Subtraction operation
        result = op1 - op2  # Calculate the difference between op1 and op2
        return f'The subtraction is: {op1} - {op2} = {result}'  # Return the formatted result string
    elif v3.get() == 2:
        # Addition operation
        result = op1 + op2  # Calculate the sum of op1 and op2
        return f'The sum is: {op1} + {op2} = {result}'  # Return the formatted result string

def calculate_func():
    """
    Main function to retrieve inputs, validate them, perform the selected operation,
    and update the result label with the calculated result.
    """
    op1, op2 = validate_and_get_inputs()  # Validate inputs and get the integer values
    if op1 is None or op2 is None:
        return  # Exit the function if inputs are invalid

    result_text = perform_operation(op1, op2)  # Perform the selected operation
    label_result.config(text=result_text)  # Update the result label with the calculated result

def create_widgets(root):
    """
    Function to create and place all the widgets in the main window.
    """
    # Create and place the label and entry widget for the first input value (X)
    tk.Label(root, text='Enter the value of X:').grid(row=0, column=0, padx=10, pady=5, sticky="w")
    global entry1
    entry1 = tk.Entry(root, width=20)  # Create an entry widget for the first input value
    entry1.grid(row=0, column=1, padx=10, pady=5)  # Place the entry widget in the grid

    # Create and place the label and entry widget for the second input value (Y)
    tk.Label(root, text='Enter the value of Y:').grid(row=1, column=0, padx=10, pady=5, sticky="w")
    global entry2
    entry2 = tk.Entry(root, width=20)  # Create an entry widget for the second input value
    entry2.grid(row=1, column=1, padx=10, pady=5)  # Place the entry widget in the grid

    # Create and place the radio buttons for selecting the operation (subtraction or addition)
    global v3
    v3 = tk.IntVar()  # Variable to hold the value of the selected radio button
    tk.Radiobutton(root, text='Subtraction', variable=v3, value=1).grid(row=2, column=0, padx=10, pady=5, sticky="w")
    tk.Radiobutton(root, text='Addition', variable=v3, value=2).grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Create and place the button to trigger the calculation
    tk.Button(root, text="Calculate", command=calculate_func).grid(row=3, column=0, columnspan=2, pady=10)

    # Create and place the label to display the result of the calculation
    global label_result
    label_result = tk.Label(root, text='', fg='blue')  # Initialize with an empty text and set the text color to blue
    label_result.grid(row=4, column=0, columnspan=2, pady=10)  # Place the label in the grid

def main():
    """
    Main function to initialize the tkinter application and create widgets.
    """
    root = tk.Tk()  # Create the main window
    root.geometry("400x200")  # Set the size of the window to 400x200 pixels
    root.title("Sum and Subtraction Calculator")  # Set the title of the window

    create_widgets(root)  # Create and place the widgets

    root.mainloop()  # Start the main event loop to run the tkinter application

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly
