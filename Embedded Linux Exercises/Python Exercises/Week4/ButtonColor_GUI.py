import tkinter as tk  # Import the tkinter library for GUI development

class LEDIndicator:
    def __init__(self, root):
        self.root = root
        self.root.title("LED Indicator")  # Set the title of the window
        
        # Set up the canvas with a white background
        self.canvas = tk.Canvas(self.root, width=200, height=250, bg='white')
        self.canvas.pack()  # Add the canvas to the window
        
        # Create the circle for the LED indicator on the canvas
        # The circle is defined by the bounding box with top-left corner (50, 50)
        # and bottom-right corner (150, 150). Initially, it is filled with gray color.
        self.led_circle = self.canvas.create_oval(50, 50, 150, 150, fill='gray')
        
        # Create the label for displaying the LED status
        # Initially, the text is "Led OFF" and it has a white background
        self.status_label = tk.Label(self.root, text="Led OFF", bg='white')
        self.status_label.pack(pady=10)  # Add the label to the window with some padding
        
        # Create the "Led ON" button
        # When clicked, it calls the led_on method
        self.led_on_button = tk.Button(self.root, text="Led ON", command=self.led_on)
        self.led_on_button.pack(pady=5)  # Add the button to the window with some padding
        
        # Create the "Led OFF" button
        # When clicked, it calls the led_off method
        self.led_off_button = tk.Button(self.root, text="Led OFF", command=self.led_off)
        self.led_off_button.pack(pady=5)  # Add the button to the window with some padding
    
    def led_on(self):
        # Change the LED circle color to green
        # Update the status label text to "Led ON"
        self.canvas.itemconfig(self.led_circle, fill='green')
        self.status_label.config(text="Led ON")
    
    def led_off(self):
        # Change the LED circle color to red
        # Update the status label text to "Led OFF"
        self.canvas.itemconfig(self.led_circle, fill='red')
        self.status_label.config(text="Led OFF")

# Main block to run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    app = LEDIndicator(root)  # Create an instance of the LEDIndicator class
    root.mainloop()  # Start the Tkinter event loop
