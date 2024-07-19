#include <stdio.h>
#include <limits.h>

// Function to find the maximum number in an array
int findMax(int arr[], int n) 
{
    if (n <= 0) 
    {
        // Return a specific value or handle the error for empty array
        printf("Array is empty.\n");
        return INT_MIN; // or some error code
    }

    int maxValue = arr[0]; // Assume the first element is the maximum

    // Loop through the array
    for(int i = 1; i < n; i++) 
    {
        if(arr[i] > maxValue) 
        {
            maxValue = arr[i]; // Update maxValue if current element is greater
        }
    }

    return maxValue; // Return the maximum value
}

int main() 
{
    int arr[] = {1, 3, 7, 2, 9, 4}; // Example array
    int n = sizeof(arr) / sizeof(arr[0]); // Calculate the number of elements in the array

    int max = findMax(arr, n); // Call the function to find the maximum number
    if (max != INT_MIN) 
    {
        printf("The maximum number in the array is: %d\n", max); // Print the maximum number
    }

    return 0;
}
