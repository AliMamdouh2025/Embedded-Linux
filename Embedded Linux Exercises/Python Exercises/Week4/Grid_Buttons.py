import tkinter as tk

def create_buttons(root):
    """
    Function to create and place buttons in the root window.
    """
    # Create and place button1 at row 0, column 1
    button1 = tk.Button(root, text="Button 1")
    button1.grid(row=0, column=1)

    # Create and place button2 at row 1, column 0
    button2 = tk.Button(root, text="Button 2")
    button2.grid(row=1, column=0)

    # Create and place button3 at row 1, column 3
    button3 = tk.Button(root, text="Button 3")
    button3.grid(row=1, column=3)

    # Create and place button4 at row 2, column 1
    button4 = tk.Button(root, text="Button 4")
    button4.grid(row=2, column=1)

def main():
    """
    Main function to set up the root window and create buttons.
    """
    # Create the main window
    root = tk.Tk()
    root.geometry("500x500")  # Set the size of the window to 500x500 pixels
    root.title("Grid Layout Example")  # Set the title of the window

    # Create buttons in the root window
    create_buttons(root)

    # Start the main event loop to run the tkinter application
    root.mainloop()

if __name__ == "__main__":
    main()  # Execute the main function if this script is run directly
