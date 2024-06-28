import csv  # Import the csv module for handling CSV file operations
import logging  # Import the logging module for logging information and errors
from typing import List, Optional, Dict, Any  # Import typing helpers to specify the type of elements, which helps in improving readability and early detection of type-related errors during development.
from abc import ABC, abstractmethod  # Import ABC and abstractmethod for creating abstract base classes
#Example to understand role of abstractmethod:
"""
from abc import ABC, abstractmethod

class Shape(ABC):  # Abstract base class
    @abstractmethod
    def area(self):  # Abstract method
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# Usage
# shape = Shape()  # This will raise TypeError: Can't instantiate abstract class Shape with abstract methods area
square = Square(5)
print("Square Area:", square.area())  # Output: Square Area: 25
circle = Circle(3)
print("Circle Area:", circle.area())  # Output: Circle Area: 28.26
"""




# Configuration constants
CONFIG = {
    'DATABASE_PATH': 'employees_database.csv',  # Path to the CSV file for storing employee data
    'LOG_FILE': 'employee_management.log',  # Path to the log file for logging
    'INITIAL_EMPLOYEE_DATA': [  # Initial data to populate the database
        ["ID", "Name", "Job Title", "Salary"],  # Header row
        [1, "Ali Mamdouh", "Embedded Linux Engineer", "60000"],  # Example employee data
        [2, "Ahmed Ashraf", "Analog Designer", "40000"],  # Example employee data
        [3, "Omar Abduelkreem", "Digital Designer", "30000"],  # Example employee data
    ]
}






# Initializes the logging system for the application.
logging.basicConfig(
    filename = CONFIG['LOG_FILE'],  # Specifies the path to the log file where logs will be written.
    level = logging.INFO,  # Sets the logging level to INFO, This ensures that only important messages are logged.
    # Only log messages of level INFO and higher (e.g., WARNING, ERROR, CRITICAL) will be recorded in the log file.
    # Levels below INFO (like DEBUG) won't be logged.

    format = '%(asctime)s - %(levelname)s - %(message)s'  # Defines the format of each log message.
    # %(asctime)s: The timestamp of when the log message was created.
    # %(levelname)s: The level of the log message (e.g., INFO, ERROR).
    # %(message)s: The actual content of the log message.
)






# Class for handling database operations
class DatabaseManager:
    def __init__(self, database_path: str):
        """
        Initialize the DatabaseManager with the path to the database file.
        
        Parameters:
        database_path: Path to the database file.
        """
        self.database_path = database_path

    def read_all(self) -> List[List[str]]: #  Indicates that the function returns a list of lists of strings
        """
        Read all rows from the database file.
    
        Returns:
        List of rows from the database.
        """
        try:
            with open(self.database_path, 'r') as file:
                # Open the database file in read mode using a context manager (with statement),
                # ensuring it is properly closed even if an error occurs.
                return list(csv.reader(file))
                # Read all rows from the CSV file (`file`) and convert them into a list of lists of strings.
                # Each inner list corresponds to a row in the CSV file, where each element is a string.
        except IOError as e:
            # Catch IOError exceptions, which occur when there's an issue reading the file (e.g., file not found, permissions issue).
            logging.error(f"Error reading database: {e}")
            # Log the specific IOError (`e`) encountered while reading the database.
            return []
            # Return an empty list if an error occurs during file reading.

    def write_all(self, data: List[List[Any]]) -> None:
        """
        Write a list of rows to the database file.
        
        Parameters:
        data: List of rows to write to the database. Which is expected to be a list of lists where each inner list contains elements of any type (Any). 
        """
        try:
            with open(self.database_path, 'w', newline = '') as file:  # Open the database file in write mode(so we can overwrite over it)
            #We specify newline = '' in the open() function, to instruct Python to handle the newline character explicitly, For Example:
            # Linux Systems: It ensures that Python does not translate \n to \r\n.
            # Windows: It prevents Python from inserting an extra \r before each \n.
                csv.writer(file).writerows(data)  # Write all rows to the file,
                # Where it creates a CSV writer object csv.writer(file) for file, and uses its writerows() method to write all rows from data into the CSV file.
                  
        except IOError as e:  # Catch IOError exceptions, which occur when there's an issue reading the file (e.g., file not found, permissions issue).
            logging.error(f"Error writing to database: {e}")  # Log the error

    def append_row(self, row: List[Any]) -> None:
        """
        Append a single row to the database file.
        
        Parameters:
        row: The row to append to the database.
        """
        try:
            with open(self.database_path, 'a', newline = '') as file:  # Open the database file in append mode
                csv.writer(file).writerow(row)  # Append the row to the file.
                # Using the csv.writer object created from the file, the writerow() method appends the row list as a new row at the end of the CSV file.
        except IOError as e:  # Catch IOError exceptions, which occur when there's an issue reading the file (e.g., file not found, permissions issue).
            logging.error(f"Error appending to database: {e}")  # Log the error






# Class representing an employee
class Employee:
    def __init__(self, id: int, name: str, job_title: str, salary: int):
        """
        Initialize an Employee with the given attributes.
        
        Parameters:
        id: Employee ID.
        name: Employee name.
        job_title: Employee job title.
        salary: Employee salary.
        """
        self.id = id  # Assign the employee ID
        self.name = name  # Assign the employee name
        self.job_title = job_title  # Assign the employee job title
        self.salary = salary  # Assign the employee salary

    def to_list(self) -> List[Any]:
        """
        Convert the Employee object to a list.

        Returns:
        List representation of the employee.
        """
        return [self.id, self.name, self.job_title, self.salary]  # Return the employee attributes as a list
        #we return it as a list, so that we can make operations such as storing or serializing Employee objects into formats like CSV.

    @classmethod # For situations where we need to create a new instance but don't have an existing instance to call a method on.
    def from_list(cls, data: List[str]) -> 'Employee':
        """
        Create an Employee object from a list.
        
        This method is useful for converting data read from CSV files or other text-based sources into structured Employee objects,
        facilitating further manipulation and usage within the application.

        When you use cls in a class method, it refers to the class that calls the method, not necessarily the class where the method is defined.
        This allows for more flexible and dynamic object creation, especially when dealing with inheritance and subclasses.

        Parameters:
        data: List of employee attributes.
        
        Returns:
        An Employee object.
        """
        return cls(int(data[0]), data[1], data[2], int(data[3]))  # Create and return an Employee object






# Class for managing employee data and operations
class EmployeeManagementSystem:
    def __init__(self, database_manager: DatabaseManager):
        """
        Initialize the EmployeeManagementSystem with a DatabaseManager.
        
        Parameters:
        database_manager: Instance of DatabaseManager for database operations.
        """
        self.database_manager = database_manager  # Assign the database manager

    def _generate_next_employee_id(self) -> int: # The method name starts with an underscore (_) indicating it is intended for internal use within the class.
        """
        Generate the next employee ID based on the current number of employees.
        
        Returns:
        The next employee ID.
        """
        employees = self.database_manager.read_all()  # Read all employees from the database
        return len(employees)  # The length of the list corresponds to the number of rows (employees) in the database. The next employee ID is set to this length.

    def add_employee(self, name: str, job_title: str, salary: int) -> None:
        """
        Add a new employee to the database.
        
        Parameters:
        name: Name of the employee.
        job_title: Job title of the employee.
        salary: Salary of the employee.
        """
        employee_id = self._generate_next_employee_id()  # Generate the next employee ID
        new_employee = Employee(employee_id, name, job_title, salary)  # Create a new Employee object
        self.database_manager.append_row(new_employee.to_list())  # Append the new employee to the database
        logging.info(f"Added employee: {new_employee.to_list()}")  # Log the addition of the new employee
        print("Employee added successfully.")  # Print a success message
        self.display_employee_data(employee_id)  # Display the newly added employee's data

    def display_employee_data(self, employee_id: int) -> None:
        """
        Display the data of an employee with the given ID.
        
        Parameters:
        employee_id: ID of the employee.
        """
        employees = self.database_manager.read_all()  # Read all employees from the database
        for employee in employees[1:]:  # Skip header row and iterate through employees
            if int(employee[0]) == employee_id:  # Check if the employee ID matches
                print(f"ID: {employee[0]}")  # Print employee ID
                print(f"Name: {employee[1]}")  # Print employee name
                print(f"Job Title: {employee[2]}")  # Print employee job title
                print(f"Salary: {employee[3]}")  # Print employee salary
                return
        print(f"Employee with ID {employee_id} not found.")  # Print a message if the employee is not found

    def delete_employee(self, employee_id: int) -> None:
        """
        Delete an employee from the database based on the provided ID.
        
        Parameters:
        employee_id: ID of the employee to delete.
        """
        employees = self.database_manager.read_all()  # Read all employees from the database
        updated_employees = [employees[0]]  # Keep the header row
        deleted = False  # Flag to check if an employee was deleted
        for employee in employees[1:]:  # Iterate through employees
            if int(employee[0]) != employee_id:  # If employee ID does not match, keep the employee
                updated_employees.append(employee)
            else:
                deleted = True  # Set deleted flag to True if the employee is found and deleted
        
        if deleted:
            # Update IDs to be sequential
            for i, employee in enumerate(updated_employees[1:], start=1):  # Reassign sequential IDs starting from 1
                employee[0] = i
            self.database_manager.write_all(updated_employees)  # Write the updated employee list to the database
            logging.info(f"Deleted employee with ID: {employee_id}")  # Log the deletion
            print(f"Employee with ID {employee_id} has been deleted successfully.")  # Print a success message
        else:
            print(f"Employee with ID {employee_id} not found.")  # Print a message if the employee is not found

    def update_employee(self, employee_id: int, new_job_title: Optional[str] = None, new_salary: Optional[int] = None) -> None:
        """
        Update the job title and/or salary of an existing employee.
        
        Parameters:
        employee_id: ID of the employee to update.
        new_job_title: New job title of the employee (optional).
        new_salary: New salary of the employee (optional).
        """
        employees = self.database_manager.read_all()  # Read all employees from the database
        for employee in employees[1:]:  # Iterate through employees (skip header row)
            if int(employee[0]) == employee_id:  # Check if the employee ID matches
                if new_job_title:
                    employee[2] = new_job_title  # Update the job title if provided
                if new_salary is not None:
                    employee[3] = str(new_salary)  # Update the salary if provided
                self.database_manager.write_all(employees)  # Write the updated employee list to the database
                logging.info(f"Updated employee: {employee}")  # Log the update
                print(f"Employee with ID {employee_id} has been updated successfully.")  # Print a success message
                self.display_employee_data(employee_id)  # Display the updated employee data
                return
        print(f"Employee with ID {employee_id} not found.")  # Print a message if the employee is not found






# Abstract base class for commands, We use it yo make our code more maintanable, So we can add more features to it more easily.
class Command(ABC): # This line defines a new class called Command that inherits from ABC, Abstract classes cannot be instantiated directly and must be subclassed.s
    @abstractmethod #Means that this method is declared but contains no implementation, Any subclass of Command must provide an implementation for this method.
    def execute(self, ems: EmployeeManagementSystem) -> None:
        """
        Execute the command on the EmployeeManagementSystem.
        
        Parameters:
        ems: Instance of EmployeeManagementSystem.
        """
        pass

# Command for adding a new employee
class AddEmployeeCommand(Command):
    def execute(self, ems: EmployeeManagementSystem) -> None:
        """
        Execute the add employee command.
        
        Parameters:
        ems: Instance of EmployeeManagementSystem.
        """
        name = input("Enter the employee name: ")  # Prompt for employee name
        job_title = input("Enter the employee job title: ")  # Prompt for employee job title
        salary = int(input("Enter the employee salary: "))  # Prompt for employee salary
        ems.add_employee(name, job_title, salary)  # Add the new employee

# Command for displaying employee data
class DisplayEmployeeCommand(Command):
    def execute(self, ems: EmployeeManagementSystem) -> None:
        """
        Execute the display employee data command.
        
        Parameters:
        ems: Instance of EmployeeManagementSystem.
        """
        employee_id = int(input("Enter the employee ID: "))  # Prompt for employee ID
        ems.display_employee_data(employee_id)  # Display the employee data

# Command for deleting an employee
class DeleteEmployeeCommand(Command):
    def execute(self, ems: EmployeeManagementSystem) -> None:
        """
        Execute the delete employee command.
        
        Parameters:
        ems: Instance of EmployeeManagementSystem.
        """
        employee_id = int(input("Enter the employee ID to delete: "))  # Prompt for employee ID to delete
        ems.delete_employee(employee_id)  # Delete the employee

# Command for updating an employee
class UpdateEmployeeCommand(Command):
    def execute(self, ems: EmployeeManagementSystem) -> None:
        """
        Execute the update employee command.
        
        Parameters:
        ems: Instance of EmployeeManagementSystem.
        """
        employee_id = int(input("Enter the employee ID to update: "))  # Prompt for employee ID to update
        new_job_title = input("Enter the new job title (Press 'Enter' to unchange job title): ")  # Prompt for new job title
        new_salary = input("Enter the new salary (Press 'Enter' to unchange salary): ")  # Prompt for new salary
        new_salary = int(new_salary) if new_salary else None  # Convert new salary to int if provided
        ems.update_employee(employee_id, new_job_title or None, new_salary)  # Update the employee

# Command for exiting the program
class ExitCommand(Command):
    def execute(self, ems: EmployeeManagementSystem) -> None:
        """
        Execute the exit command.
        
        Parameters:
        ems: Instance of EmployeeManagementSystem.
        """
        print("Exiting program.")  # Print exit message
        exit()  # Exit the program






# Function to display the menu and execute user commands
def display_menu(ems: EmployeeManagementSystem) -> None:
    """
    Display the employee management menu and execute user commands.
    
    Parameters:
    ems: Instance of EmployeeManagementSystem.
    """
    commands: Dict[str, Command] = {  # Map user choices to command classes
        '1': AddEmployeeCommand(),
        '2': DisplayEmployeeCommand(),
        '3': DeleteEmployeeCommand(),
        '4': UpdateEmployeeCommand(),
        '5': ExitCommand()
    }

    while True:
        # Display the menu options
        print("\n===== Employee Management Menu =====")
        print("1. Add New Employee")
        print("2. Display Employee Data")
        print("3. Delete Employee")
        print("4. Update Employee")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")  # Prompt for user choice
        
        if choice in commands:
            commands[choice].execute(ems)  # Execute the corresponding command
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")  # Print error message for invalid choice






# Function to initialize the database with initial data
def initialize_database() -> None:
    """
    Initialize the database with initial data.
    """
    try:
        with open(CONFIG['DATABASE_PATH'], 'w', newline = '') as file:  # Open the database file in write mode
            csv.writer(file).writerows(CONFIG['INITIAL_EMPLOYEE_DATA'])  # Write the initial data to the database
        logging.info("Database initialized with initial data")  # Log the initialization
    except IOError as e:  # Catch any IOError that occurs
        logging.error(f"Error initializing database: {e}")  # Log the error






# Main function to run the program
def main() -> None:
    """
    Main function to run the Employee Management System program.
    """
    initialize_database()  # Initialize the database
    database_manager = DatabaseManager(CONFIG['DATABASE_PATH'])  # Create a DatabaseManager instance
    ems = EmployeeManagementSystem(database_manager)  # Create an EmployeeManagementSystem instance
    display_menu(ems)  # Display the menu and start accepting user commands

# Entry point for the program
if __name__ == "__main__":
    main()  # Run the main function
