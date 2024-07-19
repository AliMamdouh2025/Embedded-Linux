#include <stdio.h>

void deleteNumber(int arr[], int *size, int number) 
{
    int i, j;

    // Find the index of the number to be deleted
    for (i = 0; i < *size; i++) 
    {
        if (arr[i] == number) 
        {
            // Shift elements to the left to delete the number
            for (j = i; j < *size - 1; j++) 
            {
                arr[j] = arr[j + 1];
            }
            (*size)--;
        }
    }
}

int main() 
{
    int arr[] = {1, 2, 3, 4, 5, 2, 5};
    int size = 7;
    int numberToDelete = 2;
    int i;

    printf("Original array: ");
    for (i = 0; i < size; i++) 
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    deleteNumber(arr, &size, numberToDelete);

    printf("Array after deleting %d: ", numberToDelete);
    for (i = 0; i < size; i++) 
    {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
