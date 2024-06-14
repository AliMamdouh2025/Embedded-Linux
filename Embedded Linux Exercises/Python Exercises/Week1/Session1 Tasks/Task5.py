import calendar

def get_year():
    """
    Prompt the user to enter a valid year.

    Returns:
        int: The valid year entered by the user.
    """
    while True:
        try:
            year = int(input("Enter the year: ")) 
            if year < 0:
                raise ValueError("Year must be a positive number.")
            return year
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid year.")

def get_month():
    """
    Prompt the user to enter a valid month (1-12).

    Returns:
        int: The valid month entered by the user.
    """
    while True:
        try: #To catch ValueError when converting user input to int. This prevents the program from bugs if the user enters invalid input (like a float instead of int).
            month = int(input("Enter the month (1-12): ")) 
            if month < 1 or month > 12: 
                raise ValueError("Month must be between 1 and 12.") #Assign message of ValueError as the user enter a invalid int range(When user Assigns non-int like char ValueError have automacally an error message)
            return month
        except ValueError as e:  #If any ValueError occurs within the try block (either due to invalid input or out of range month), Python jumps to the except block. It assigns it to the variable, "e" (for easier reference).
            print(f"Error: {e}. Please enter a valid month (1-12).")

if __name__ == "__main__": # To ensure that it only runs if the script is executed directly. This prevents the script from executing when imported as a module(Just for try).
    year = get_year()
    month = get_month()
    print(calendar.month(year, month))
