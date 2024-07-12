#include <iostream>       // Includes the standard input-output stream library for handling input and output operations.
#include <bitset>         // Includes the bitset library for working with binary representations.
#include <string>         // Includes the string library for working with strings.

#define BIT_REPRESENTATION_SIZE 32 // Defines a constant for the size of the bitset, set to 32 to represent any unsigned int.

// Function to convert a decimal number to binary representation
std::bitset<BIT_REPRESENTATION_SIZE> decimalToBinary(unsigned int number) 
{
    // Initializes a bitset of size BIT_REPRESENTATION_SIZE with the value of the decimal number.
    std::bitset<BIT_REPRESENTATION_SIZE> binary(number);
    // Returns the binary representation.
    return binary;
}

// Function to convert a binary string to decimal representation
unsigned long binaryToDecimal(const std::string& binaryString) //string & not string to avoid any unnecessary redundant data in memory 
{
    // Checks if the length of the input binary string exceeds the defined bitset size.
    if (binaryString.length() > BIT_REPRESENTATION_SIZE) 
    {
        // Prints an error message if the binary string is too long.
        std::cerr << "Error: Binary number is too long." << std::endl;
        // Returns 0 as an error value.
        return -1;
    }
    // Iterates over each character in the binary string.
    for (char c : binaryString) 
    {
        // Checks if the character is not '0' or '1'.
        if (c != '0' && c != '1') 
        {
            // Prints an error message if the binary string contains invalid characters.
            std::cerr << "Error: Invalid binary number." << std::endl;
            // Returns 0 as an error value.
            return -1;
        }
    }

    // Initializes a bitset of size BIT_REPRESENTATION_SIZE with the value of the binary string.
    std::bitset<BIT_REPRESENTATION_SIZE> binary(binaryString);
    // Converts the bitset to an unsigned long value.
    unsigned long decimalNumber = binary.to_ulong();
    // Returns the decimal representation.
    return decimalNumber;
}

int main() 
{
    int choice; // Variable to store the user's choice, It can't be char to get correct input using 'cin'.
    // Prints the menu for conversion type selection.
    std::cout << "Choose conversion type:\n";
    std::cout << "1. Decimal to Binary\n";
    std::cout << "2. Binary to Decimal\n";
    std::cout << "Enter your choice (1 or 2): ";
    // Reads the user's choice.
    std::cin >> choice;

    // Checks if the user's choice is 1 (Decimal to Binary).
    if (choice == 1) 
    {
        unsigned int decimalNumber; // Variable to store the decimal number input by the user.
        // Prompts the user to enter a decimal number.
        std::cout << "Enter a decimal number: ";
        // Reads the decimal number input by the user.
        std::cin >> decimalNumber;
        // Prints the binary representation of the entered decimal number.
        std::cout << "Binary representation: " << decimalToBinary(decimalNumber) << std::endl;
    } 
    // Checks if the user's choice is 2 (Binary to Decimal).
    else if (choice == 2)
    {
        std::string binaryString; // Variable to store the binary string input by the user.
        // Prompts the user to enter a binary number.
        std::cout << "Enter a binary number: ";
        // Reads the binary string input by the user.
        std::cin >> binaryString;
        // Converts the binary string to a decimal number.
        unsigned long decimalNumber = binaryToDecimal(binaryString);
        // Checks if the conversion was successful.
        if (decimalNumber != -1) 
        {
            // Prints the decimal representation of the entered binary number.
            std::cout << "Decimal representation: " << decimalNumber << std::endl;
        }
    } 
    // If the user's choice is invalid.
    else 
    {
        // Prints an error message for an invalid choice.
        std::cerr << "Invalid choice" << std::endl;
    }

    return 0; // Returns 0 to indicate successful program termination.
}
