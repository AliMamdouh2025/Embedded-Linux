#include <stdio.h>
#include <string.h>

/*Try: convert negative decimal to binary and Vice-Versa !!!!!!*/

// Function to convert a decimal number to binary
void decimal_to_binary(unsigned int decimal, char *binary_str) {
    char index = 0;
    if (decimal == 0) {
        binary_str[index++] = '0';
    } else {
        while (decimal > 0) {
            binary_str[index++] = (decimal % 2) + '0';
            decimal /= 2;
        }
    }
    binary_str[index] = '\0';
    
    // Reverse the binary string
    char len = index; //Not strlen() due to previous loop
    for (char i = 0; i < len / 2; i++) {
        char temp = binary_str[i];
        binary_str[i] = binary_str[len - 1 - i];
        binary_str[len - 1 - i] = temp;
    }
}

// Function to convert a binary string to decimal
unsigned int binary_to_decimal(const char *binary_str) {
    unsigned int decimal = 0;
    char len = strlen(binary_str);
    for (char i = 0; i < len; i++) {
        if (binary_str[i] == '1') {
            decimal += (1 << (len - 1 - i));
        }
    }
    return decimal;
}

int main() {
    char choice;
    printf("Choose conversion type (d for Decimal to Binary, b for Binary to Decimal): ");
    scanf(" %c", &choice);

    if (choice == 'd') {
        unsigned int decimal_number;
        char binary_str[33];  // 32 bits + null terminator

        printf("Enter a decimal number: ");
        scanf("%u", &decimal_number);

        // Convert decimal to binary
        decimal_to_binary(decimal_number, binary_str);
        printf("Decimal: %u\n", decimal_number);
        printf("Binary: %s\n", binary_str);
    } else if (choice == 'b') {
        char binary_str[33];  // 32 bits + null terminator

        printf("Enter a binary number: ");
        scanf("%s", binary_str);

        // Convert binary to decimal
        unsigned int decimal_number = binary_to_decimal(binary_str);
        printf("Binary: %s\n", binary_str);
        printf("Decimal: %u\n", decimal_number);
    } else {
        printf("Invalid choice. Please choose 'd' or 'b'.\n");
    }

    return 0;
}
