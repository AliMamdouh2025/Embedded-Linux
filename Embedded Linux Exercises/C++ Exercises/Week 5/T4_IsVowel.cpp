#include <iostream>  // Include iostream for input and output
#include <string>    // Include string for string operations
#include <cctype>    // Include cctype for character handling functions

// Function to check if a character is a vowel
bool isVowel(char ch, const std::string& vowels) 
{
    // Convert the character to lowercase to make the check case-insensitive
    ch = std::tolower(static_cast<unsigned char>(ch));
    // Check if the character is found in the vowels string
    return (vowels.find(ch) != std::string::npos); //Return True or False based on that comparison.
}

// Function to get a character input from the user
char getInput() 
{
    char letter;
    std::cout << "Enter a character: "; // Prompt the user to enter a character
    std::cin >> letter; // Read the input character
    return letter;
}

// Function to print whether the character is a vowel or not
void printResult(char letter, bool is_vowel) 
{
    if (is_vowel) 
    {
        std::cout << letter << " is a vowel" << std::endl; // Output if the character is a vowel
    } else 
    {
        std::cout << letter << " is not a vowel" << std::endl; // Output if the character is not a vowel
    }
}

int main() 
{
    const std::string vowels = "aeiou"; // String containing all vowel characters

    char letter = getInput(); // Get input from the user
    bool is_vowel = isVowel(letter, vowels); // Check if the input character is a vowel
    printResult(letter, is_vowel); // Print the result

    return 0; // Return 0 to indicate successful program execution
}
