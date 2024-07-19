#include <iostream>
#include <vector>
#include <limits.h> // for INT_MIN

int findMax(const std::vector<int>& arr) {
    int maxVal = INT_MIN; // Initialize to the minimum possible integer value
    for (int num : arr) {
        if (num > maxVal) {
            maxVal = num;
        }
    }
    return maxVal;
}

int main() {
    std::vector<int> arr = {3, 5, 7, 2, 8, -1, 4, 10, 12};
    int maxNumber = findMax(arr);
    std::cout << "The maximum number in the array is: " << maxNumber << std::endl;
    return 0;
}
