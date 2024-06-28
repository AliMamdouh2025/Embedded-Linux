def get_ascii_value(character: str) -> int:
    """
    Get the ASCII value of a character.

    Args:
        character (str): The character for which ASCII value is to be obtained.
                         It should be a single character string.

    Returns:
        int: The ASCII value of the character.

    Raises:
        ValueError: If the input is not a single character.
    """
    if len(character) != 1:
        raise ValueError("Input should be a single character.")
    return ord(character)

if __name__ == "__main__":
    try:
        character = input("Enter a character: ")
        ascii_value = get_ascii_value(character)
        print(f"The ASCII value of '{character}' is {ascii_value}.")
    except ValueError as e:
        print(e)
