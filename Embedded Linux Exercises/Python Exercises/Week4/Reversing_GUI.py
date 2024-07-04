import tkinter as tk

def Reverse_func(entry_widget, result_label):
    """
    Function to reverse the input string and display the result.
    """
    input_text = entry_widget.get()  # Get the input string from the entry widget
    reversed_text = input_text[::-1]  # Reverse the input string
    result_label.config(text=f'The reversed string is: {reversed_text}')  # Update the result label with the reversed string

def main():
    """
    Main function to set up the tkinter application.
    """
    root = tk.Tk()  # Create the main window
    root.geometry("300x300")  # Set window size to 300x300 pixels
    root.title("Reverse String")  # Set window title

    # Create and place the label for input
    tk.Label(root, text='Enter a String').grid(row=0, column=0, padx=10, pady=10)

    # Create a StringVar to store the input text
    v1 = tk.StringVar()

    # Create and place the entry widget for input
    entry1 = tk.Entry(root, width=20, textvariable=v1)
    entry1.grid(row=0, column=1, padx=10, pady=10)

    # Create and place the button to trigger the calculation
    tk.Button(root, text="Reverse", command=lambda: Reverse_func(entry1, result_label)).grid(row=1, column=1, padx=10, pady=10)

    # Create a label to display the result
    global result_label
    result_label = tk.Label(root, text='Enter String Please', fg='blue')
    result_label.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()  # Start the main event loop

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly
