#include <iostream>
#include <vector>
#include <algorithm>

// Function to sort a vector of integers in ascending and descending order using lambda functions
std::pair< std::vector<int>, std::vector<int> > sortArray(const std::vector<int>& arr) 
{
    // Copy the original array to maintain the original data
    std::vector<int> ascending(arr);
    std::vector<int> descending(arr);

    // Sort in ascending order
    std::sort(ascending.begin(), ascending.end(), [](int a, int b) {
        return a < b;
    });

    // Sort in descending order
    std::sort(descending.begin(), descending.end(), [](int a, int b) {
        return a > b;
    });

    return {ascending, descending};
}

int main() 
{
    // Example usage
    std::vector<int> arr = {5, 3, 8, 1, 9, 2};

    // Get the sorted arrays
    auto [ascending, descending] = sortArray(arr);

    // Print the sorted arrays
    std::cout << "Ascending: ";
    for (int num : ascending) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    std::cout << "Descending: ";
    for (int num : descending) 
    {
        std::cout << num << " ";
    }
    std::cout << std::endl;

    return 0;
}
