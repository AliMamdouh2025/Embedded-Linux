def count_occurrences_of_four(numbers_list):
    """
    Counts the number of occurrences of the number 4 in a given list.

    Args:
        numbers_list (list): A list of integers.

    Returns:
        int: The number of times the integer 4 appears in the list.
    """
    return numbers_list.count(4)

# Example usage
example_numbers = [1, 4, 6, 4, 7, 4, 9]
print(f"Number of 4's in the list: {count_occurrences_of_four(example_numbers)}")
