#include <iostream>

int main() {
    int rows;

    // Prompt the user to enter the number of rows for the triangle
    std::cout << "Enter the number of rows for the right-angle triangle: ";
    std::cin >> rows;

    // Input validation
    if (rows <= 0)
    {
        std::cerr << "Error!!\nNumber of rows should be a positive integer." << std::endl;
        return -1;
    }

    // Loop to print the right-angle triangle
    for (char i = 1; i <= rows; ++i) 
    {
        for (char j = 1; j <= i; ++j) 
        {
            std::cout << "* ";
        }
        std::cout << std::endl;
    }

    return 0;
}
