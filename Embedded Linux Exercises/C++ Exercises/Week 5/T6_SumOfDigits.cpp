#include <stdio.h>

int main() {
    int num, sum = 0;

    printf("Enter an integer: ");
    scanf("%d", &num);

    // Calculate sum of digits
    while (num != 0) 
    {
        sum += num % 10;
        num /= 10;
    }

    printf("Sum of digits: %d\n", sum);

    return 0;
}
