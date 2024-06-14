def check_if_vowel(character):
    """
    Determines whether a given character is a vowel.

    Args:
        character (str): A single character to be checked.

    Returns:
        bool: True if the character is a vowel, False otherwise.
    """
    vowels = 'aeiouAEIOU'
    return character in vowels

# Example usage
example_character_1 = 'a'
print(f"Is '{example_character_1}' a vowel? {check_if_vowel(example_character_1)}")

example_character_2 = 'b'
print(f"Is '{example_character_2}' a vowel? {check_if_vowel(example_character_2)}")
