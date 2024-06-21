def count_words_in_file(file_path):
    """
    This function counts the number of words in the specified text file.

    Parameters:
    file_path (str): The path to the text file.

    Returns:
    int: The number of words in the file.
    """
    # Initialize the word count to zero
    word_count = 0

    try:
        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Enumerate over each line in the file, with line numbers starting from 1
            for line_number, line in enumerate(file, start=1):
                # Split the line into words using whitespace as the delimiter
                words = line.split()
                # Add the number of words in the current line to the total word count
                word_count += len(words)
    except FileNotFoundError:
        # Handle the case where the file is not found
        print(f"The file at {file_path} was not found.")
        return 0
    except Exception as e:
        # Handle any other exceptions that might occur
        print(f"An error occurred: {e}")
        return 0

    # Return the total word count
    return word_count

# Example usage:
file_path = 'E:\Moatssem Embedded Linux\Ali_Mamdouh.txt'
total_words = count_words_in_file(file_path)
print(f"The number of words in the file is: {total_words}")
