#include <iostream>
#include <iomanip> // For setw()

int main()
{
    std::cout << "+-----------+\n";
    std::cout << "| ASCII Table|\n";
    std::cout << "+-----------+\n";
    std::cout << "| Char  | ASCII |\n";
    std::cout << "+-----------+\n";

    for (char i = 0; i < 128; ++i) 
    {
        std::cout << "| " << std::setw(5) << i << " | " << std::setw(5) << static_cast<int>(i) << " |\n";
    }

    std::cout << "+-----------+\n";

    return 0;
}
