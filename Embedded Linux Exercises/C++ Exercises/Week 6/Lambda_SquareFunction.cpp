#include <iostream>

int main() {
    // Define a lambda function to calculate the square of a number
    auto square = [](int x) -> int {
        return x * x;
    };

    // Example usage of the lambda function
    int number = 5;
    int result = square(number);

    // Print the result
    std::cout << "The square of " << number << " is " << result << std::endl;

    return 0;
}
