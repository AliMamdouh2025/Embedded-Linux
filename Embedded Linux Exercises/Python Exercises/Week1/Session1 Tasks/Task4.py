import math

def compute_area(radius):
    """
    Compute the area of a circle given its radius.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    return math.pi * (radius ** 2)

def get_radius_from_user():
    """
    Prompt the user to enter the radius of the circle.

    Returns:
        float: The radius entered by the user.
    """
    while True:
        try: #To catch ValueError when converting user input to float. This prevents the program from crashing if the user enters invalid input (like a string instead of a number).
            radius = float(input("Enter the radius of the circle: "))
            if radius <= 0:
                raise ValueError("Radius must be a positive number.") #Assign message of ValueError as the user enter a valid float(When user Assigns non-float like char ValueError have automacally an error message)
            return radius
        except ValueError as e: #If any ValueError occurs within the try block (either due to invalid input or non-positive radius), Python jumps to the except block. It assigns it to the variable, "e" (for easier reference).
            print(f"Error: {e}. Please enter a valid positive number.")

if __name__ == "__main__": # To ensure that it only runs if the script is executed directly. This prevents the script from executing when imported as a module(Just for try).

    radius = get_radius_from_user()
    area = compute_area(radius)
    print(f"The area of the circle with radius {radius} is: {area}")
