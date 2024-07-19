#include <stdio.h>

// Function to merge two arrays
void mergeArrays(int arr1[], int size1, int arr2[], int size2, int mergedArray[]) {
    int i;

    // Copy elements from arr1 to mergedArray
    for (i = 0; i < size1; i++) {
        mergedArray[i] = arr1[i];
    }

    // Copy elements from arr2 to mergedArray
    for (i = 0; i < size2; i++) {
        mergedArray[size1 + i] = arr2[i];
    }
}

int main() {
    int arr1[] = {1, 3, 5, 7};
    int arr2[] = {2, 4, 6, 8};
    int size1 = sizeof(arr1) / sizeof(arr1[0]);
    int size2 = sizeof(arr2) / sizeof(arr2[0]);
    int mergedSize = size1 + size2;
    int mergedArray[mergedSize];
    int i;

    // Merge the two arrays
    mergeArrays(arr1, size1, arr2, size2, mergedArray);

    // Print the merged array
    printf("Merged array: ");
    for (i = 0; i < mergedSize; i++) {
        printf("%d ", mergedArray[i]);
    }
    printf("\n");

    return 0;
}
