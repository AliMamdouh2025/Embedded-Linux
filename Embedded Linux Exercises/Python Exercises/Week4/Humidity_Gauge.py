# Import necessary modules from tkinter library and math for mathematical operations
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

class GaugeApp:
    def __init__(self, master):
        """Initialize the application with the main window."""
        # Initialize the main window
        self.master = master
        self.master.geometry("300x380")  # Set window size
        self.master.title("Humidity Gauge")  # Set window title

        self.value = tk.DoubleVar()  # Variable to store user input

        # Setup the user interface
        self.setup_ui()

    def setup_ui(self):
        """Setup the user interface elements."""
        # Canvas for drawing the gauge
        self.canvas = tk.Canvas(self.master, bg="white", height=280, width=300)
        self.canvas.pack()  # Pack canvas into the window

        # Create arcs representing different humidity levels
        self.create_gauge_arcs()

        # Create labels for the gauge
        self.create_gauge_labels()

        # Create tick marks around the gauge
        self.create_gauge_ticks()

        # Text displaying current humidity value
        self.value_text = self.canvas.create_text(150, 180, font=("Times", 12, "bold"), text="0%")

        # Line representing the gauge needle
        self.gauge_line = self.canvas.create_line(150, 180, 150, 30, fill="black", width=3)

        # Entry field for user input
        self.entry = ttk.Entry(self.master, width=10, textvariable=self.value)
        self.entry.pack(pady=10)  # Pack entry widget into the window with padding

        # Button to update the gauge
        self.update_button = ttk.Button(self.master, text="Update Gauge", command=self.update_gauge)
        self.update_button.pack(pady=5)  # Pack button into the window with padding

    def create_gauge_arcs(self):
        """Create arcs representing different humidity levels."""
        # Create text (not visible in current implementation)
        self.canvas.create_text(150, 30, font=("Times", 16, "bold"), text="")
        # Create green arc for low humidity
        self.canvas.create_arc(10, 40, 290, 320, start=30, extent=120, outline="green", style="arc", width=40)
        # Create yellow arc for medium humidity
        self.canvas.create_arc(10, 40, 290, 320, start=30, extent=45, outline="yellow", style="arc", width=40)
        # Create red arc for high humidity
        self.canvas.create_arc(10, 40, 290, 320, start=30, extent=30, outline="red", style="arc", width=40)

    def create_gauge_labels(self):
        """Create labels around the gauge."""
        # Create label "0%" on the left side of the gauge
        self.canvas.create_text(40, 230, font=("Times", 12, "bold"), text="0%")
        # Create label "100%" on the right side of the gauge
        self.canvas.create_text(260, 230, font=("Times", 12, "bold"), text="100%")

    def create_gauge_ticks(self):
        """Create tick marks around the gauge."""
        for i in range(11):
            angle = math.radians(30 + (120 * i / 10))  # Calculate angle for tick mark position
            # Calculate coordinates for inner tick mark
            x1 = 150 - 120 * math.cos(angle)
            y1 = 180 - 120 * math.sin(angle)
            # Calculate coordinates for outer tick mark
            x2 = 150 - 140 * math.cos(angle)
            y2 = 180 - 140 * math.sin(angle)
            # Create a line for the tick mark
            self.canvas.create_line(x1, y1, x2, y2, fill="black", width=1)

    def update_gauge(self):
        """Update the gauge based on user input."""
        try:
            value = float(self.value.get())  # Get value from entry and convert to float
            if 0 <= value <= 100:  # Check if value is within range
                # Update the text displaying the current value
                self.canvas.delete(self.value_text)
                self.value_text = self.canvas.create_text(150, 180, font=("Times", 12, "bold"), text=f"{value:.1f}%")

                # Calculate the position for the gauge needle
                angle = math.radians(30 + (120 * value / 100))
                x = 150 - 140 * math.cos(angle)
                y = 180 - 140 * math.sin(angle)

                # Update the gauge needle position
                self.canvas.delete(self.gauge_line)
                self.gauge_line = self.canvas.create_line(150, 180, x, y, fill="black", width=3)
            else:
                # Show error message if value is out of range
                messagebox.showerror("Error", "Please enter a value between 0 and 100.")
        except ValueError:
            # Show error message if input is not a valid number
            messagebox.showerror("Error", "Please enter a valid number.")

# Main program starts here
if __name__ == "__main__":
    root = tk.Tk()  # Create main window
    app = GaugeApp(root)  # Create an instance of GaugeApp
    root.mainloop()  # Start the tkinter event loop
