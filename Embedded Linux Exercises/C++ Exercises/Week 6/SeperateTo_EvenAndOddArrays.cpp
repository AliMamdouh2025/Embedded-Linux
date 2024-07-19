#include <iostream>
#include <vector>

/**
 * @brief Separates even and odd numbers from a given vector.
 * 
 * This function takes a vector of integers and divides it into two separate vectors:
 * one containing all the even numbers and one containing all the odd numbers.
 * 
 * @param inputVec The input vector of integers to be separated.
 * @param evenVec A reference to a vector that will be filled with the even numbers.
 * @param oddVec A reference to a vector that will be filled with the odd numbers.
 */
void separateEvenOdd(const std::vector<int>& inputVec, std::vector<int>& evenVec, std::vector<int>& oddVec) {
    // Clear the output vectors to ensure they are empty before adding new elements
    evenVec.clear();
    oddVec.clear();
    
    // Iterate over each element in the input vector
    for (int num : inputVec) 
    {
        if (num % 2 == 0) 
        {
            // If the number is even, add it to the evenVec
            evenVec.push_back(num);
        } else 
        {
            // If the number is odd, add it to the oddVec
            oddVec.push_back(num);
        }
    }
}

int main() 
{
    // Example usage of the separateEvenOdd function
    std::vector<int> inputVec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    std::vector<int> evenVec;
    std::vector<int> oddVec;
    
    // Call the function to separate even and odd numbers
    separateEvenOdd(inputVec, evenVec, oddVec);
    
    // Print the even numbers
    std::cout << "Even numbers: ";
    for (int num : evenVec) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;
    
    // Print the odd numbers
    std::cout << "Odd numbers: ";
    for (int num : oddVec) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
