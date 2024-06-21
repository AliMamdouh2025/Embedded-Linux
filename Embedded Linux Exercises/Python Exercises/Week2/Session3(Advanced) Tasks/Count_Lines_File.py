def count_lines_in_file(file_path):
    """
    This function counts the number of lines in the specified text file.

    Parameters:
    file_path (str): The path to the text file.

    Returns:
    int: The number of lines in the file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return len(lines)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Example usage:
file_path = 'E:\Moatssem Embedded Linux\Ali_Mamdouh.txt'  # My txt file needed to be read
line_count = count_lines_in_file(file_path)
print(f"The number of lines in the file is: {line_count}")
