#include <iostream>
#include <vector>
#include <algorithm>

/**
 * @brief Removes all occurrences of a specified number from a vector of integers.
 * 
 * This function uses the erase-remove idiom to efficiently remove all instances of
 * the specified number from the vector. The vector is modified in place.
 * 
 * @param arr Reference to the vector of integers to be modified.
 * @param numberToDelete The integer value to be removed from the vector.
 */
void deleteNumber(std::vector<int>& arr, int numberToDelete) 
{
    // Use std::remove to move all elements not equal to numberToDelete to the front of the vector.
    // The return value is an iterator to the new end of the range of elements to keep.
    auto new_end = std::remove(arr.begin(), arr.end(), numberToDelete);
    
    // Use std::vector::erase to remove elements from the new end to the actual end of the vector,
    // effectively resizing the vector and removing all occurrences of numberToDelete.
    arr.erase(new_end, arr.end());
}

int main() 
{
    // Example usage of the deleteNumber function
    std::vector<int> arr = {1, 2, 3, 4, 2, 5, 2};

    std::cout << "Original array: ";
    for (int num : arr) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    int numberToDelete = 2;
    deleteNumber(arr, numberToDelete);

    std::cout << "Array after deleting " << numberToDelete << ": ";
    for (int num : arr) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
