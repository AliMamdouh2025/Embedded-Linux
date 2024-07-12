#include <iostream>
#include <iomanip> // Needed for setw()

int main() 
{
    int tableSize;

    // Prompt the user to enter the size of the table
    std::cout << "Enter the size of the multiplication table: ";
    std::cin >> tableSize;

    // Validate input
    if (tableSize <= 0) 
    {
        std::cerr << "Error: Table size must be a positive integer." << std::endl;
        return 1; // Exit with error code 1
    }

    // Print the header of the multiplication table
    std::cout << "\nMultiplication Table up to " << tableSize << "x" << tableSize << ":\n";
    std::cout << "---------------------------------------------------------\n";

    // Print the top header row (column headers)
    std::cout << std::setw(11) << " "; // Empty space for alignment
    for (int i = 1; i <= tableSize; ++i) 
    {
        std::cout << i << std::setw(4); // Column numbers with width of 4
    }
    std::cout << "\n";

    // Print separator line
    std::cout << "---------------------------------------------------------\n";

    // Print each row of the multiplication table
    for (int i = 1; i <= tableSize; ++i) 
    {
        std::cout << i << std::setw(7) << " "; // Row header
        for (int j = 1; j <= tableSize; ++j) 
        {
            std::cout << std::setw(4) << i * j; // Multiplication result with width of 4
        }
        std::cout << "\n";
    }

    return 0;
}
