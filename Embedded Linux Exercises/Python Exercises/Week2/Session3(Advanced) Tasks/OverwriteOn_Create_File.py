def write_list_to_file(file_path, data_list):
    """
    This function writes a list of strings to a specified text file.

    Parameters:
    file_path (str): The path to the text file.
    data_list (list): The list of strings to write to the file.
    """
    try:
        # Join the list into a single string with newline characters separating elements
        # This will convert ['Moatssem', 'Embedded', 'Linux'] into 'Moatssem\nEmbedded\nLinux'
        data_str = '\n'.join(data_list)
        
        # Open the file in write mode. If the file does not exist, it will be created.
        # If the file exists, its content will be overwritten.
        with open(file_path, 'w') as file:
            # Write the joined string to the file
            file.write(data_str)
        
        # Print a success message indicating the file has been written
        print(f"List successfully written to {file_path}")
    except Exception as e:
        # Catch any exception that occurs and print an error message
        print(f"An error occurred: {e}")

def read_file(file_path):
    """
    This function reads the content of a specified text file.

    Parameters:
    file_path (str): The path to the text file.

    Returns:
    str: The content of the file.
    """
    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the entire content of the file into a string
            content = file.read()
        # Return the content read from the file
        return content
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"The file at {file_path} was not found.")
        return ""
    except Exception as e:
        # Catch any other exception that occurs and print an error message
        print(f"An error occurred: {e}")
        return ""

# Example usage:
file_path = 'E:\Moatssem Embedded Linux\Ali_Mamdouh.txt'  # Specify the path to the output file
data_list = ['Moatssem', 'Embedded', 'Linux']  # List of strings to write to the file

# Write the list to the specified file
write_list_to_file(file_path, data_list)

# Read and print the content of the file to verify the write operation
file_content = read_file(file_path)
print(f"Content of the file:\n{file_content}")
