#include <stdio.h>
#include <ctype.h>

int main() {
    char ch;

    // Ask the user to enter a character
    printf("Enter a character: ");
    scanf("%c", &ch);

    // Convert the character to lowercase to make the check case-insensitive
    ch = tolower(ch);

    // Check if the character is a vowel
    if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u') 
    {
        printf("%c is a vowel.\n", ch);
    } else 
    {
        printf("%c is not a vowel.\n", ch);
    }

    return 0;
}
