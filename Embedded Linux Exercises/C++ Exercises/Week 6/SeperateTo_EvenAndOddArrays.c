#include <stdio.h>

// Function to separate even and odd numbers from the input array
void findEvenAndOdd(int arr[], int size, int evenArr[], int *evenSize, int oddArr[], int *oddSize) {
    int i;
    *evenSize = 0;
    *oddSize = 0;

    for (i = 0; i < size; i++) {
        if (arr[i] % 2 == 0) {
            evenArr[*evenSize] = arr[i];
            (*evenSize)++;
        } else {
            oddArr[*oddSize] = arr[i];
            (*oddSize)++;
        }
    }
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(arr[0]);
    int evenArr[size]; // Maximum possible size
    int oddArr[size];  // Maximum possible size
    int evenSize, oddSize;
    int i;

    // Find even and odd numbers
    findEvenAndOdd(arr, size, evenArr, &evenSize, oddArr, &oddSize);

    // Print even numbers
    printf("Even numbers: ");
    for (i = 0; i < evenSize; i++) {
        printf("%d ", evenArr[i]);
    }
    printf("\n");

    // Print odd numbers
    printf("Odd numbers: ");
    for (i = 0; i < oddSize; i++) {
        printf("%d ", oddArr[i]);
    }
    printf("\n");

    return 0;
}
