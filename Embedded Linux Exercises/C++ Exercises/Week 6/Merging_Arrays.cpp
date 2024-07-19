#include <iostream>
#include <vector>
#include <algorithm>

/**
 * @brief Merges two vectors into one.
 * 
 * This function takes two vectors of integers and merges them into a single vector.
 * The elements of the second vector are appended to the elements of the first vector.
 * 
 * @param vec1 Reference to the first vector of integers.
 * @param vec2 Reference to the second vector of integers.
 * @return A new vector containing all elements of vec1 followed by all elements of vec2.
 */
std::vector<int> mergeVectors(const std::vector<int>& vec1, const std::vector<int>& vec2) 
{
    // Create a new vector to hold the merged result
    std::vector<int> mergedVec;
    
    // Reserve space in the merged vector to improve performance by reducing reallocations
    mergedVec.reserve(vec1.size() + vec2.size());
    
    // Insert elements of the first vector into the merged vector
    mergedVec.insert(mergedVec.end(), vec1.begin(), vec1.end());
    
    // Insert elements of the second vector into the merged vector
    mergedVec.insert(mergedVec.end(), vec2.begin(), vec2.end());
    
    // Return the merged vector
    return mergedVec;
}

int main() 
{
    // Example usage of the mergeVectors function
    std::vector<int> vec1 = {1, 2, 3, 4};
    std::vector<int> vec2 = {5, 6, 7, 8};

    // Merge vec1 and vec2
    std::vector<int> mergedVec = mergeVectors(vec1, vec2);

    // Print the merged vector
    std::cout << "Merged vector: ";
    for (int num : mergedVec) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
