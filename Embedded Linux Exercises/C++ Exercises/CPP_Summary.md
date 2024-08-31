# C++ Study Summary for Embedded Linux
- This document provides an overview of C++ features with practical examples relevant to embedded Linux programming.


# C++ Input & Output
- C++ provides a streamlined way to handle input and output operations through the standard library.

### Basic Example:

```cpp
#include <iostream>

int main()
{
    int x;
    std::cout << "Enter a number: ";
    std::cin >> x;
    std::cout << "You entered: " << x << "\n";
    return 0;
}
```

### Practical Example for Embedded Linux:

Consider a scenario where your embedded Linux device is interfacing with a UART (serial) port to receive data from a sensor and send it back:

```cpp
#include <iostream>   // Include the I/O stream library for standard input and output operations
#include <fcntl.h>    // Include the file control options for opening the UART device
#include <unistd.h>   // Include the POSIX constants and types for system calls
#include <termios.h>  // Include the terminal I/O library for configuring the UART

int main()
{
    /** Open the UART device at /dev/ttyS0 with read/write access, no controlling terminal, and non-blocking mode
     *
     * The open function is used to open a file or device.
     * 
     *
     * /dev/ttyS0 This is the device file corresponding to the first serial port (UART0) on a Linux system.
     * Serial ports are represented as device files in the /dev directory.
     *
     * O_RDWR: This flag specifies that the device should be opened for both reading and writing. In the context of a UART device, it means you can both send and receive data through this serial        *  port.
     *
     * O_NOCTTY: This flag prevents the terminal from becoming the controlling terminal for the process. If this flag is not set, the device could potentially become the controlling terminal for        * the process, which is generally not desired for a serial communication application.
     *
     * O_NDELAY: This flag opens the device in non-blocking mode. In non-blocking mode, operations on the device will return immediately rather than blocking if no data is available or if the           * device is not ready. For example, reading from the UART device will return immediately with an error code if no data is available, rather than waiting for data to arrive.
     */
    int uart0_filestream = open("/dev/ttyS0", O_RDWR | O_NOCTTY | O_NDELAY);

    
    // Check if the UART device was successfully opened
    if (uart0_filestream == -1)
    {
        std::cerr << "Error - Unable to open UART." << std::endl;  // Output error message if failed to open
        return -1;  // Return an error code
    }

    // Configure UART settings
    tcgetattr(uart0_filestream, &options);  // Retrieve the current settings of the UART device
    struct termios options;  // Create a termios structure to hold the configuration options  
    options.c_cflag = B9600 | CS8 | CLOCAL | CREAD; // Set UART options: baud rate of 9600, 8 data bits, Disables control of the terminal by the modem., 1 stop bit, and enable receiver
    options.c_iflag = IGNPAR;  // Ignore parity errors
    options.c_oflag = 0;       // No special output processing
    options.c_lflag = 0;       // No special input processing
    tcflush(uart0_filestream, TCIFLUSH);  // Flush the input buffer to discard any old data
    tcsetattr(uart0_filestream, TCSANOW, &options);  // Apply the new settings immediately

    // Write a message to the UART device
    const char* message = "Hello, UART!";  // Message to be sent via UART
    int count = write(uart0_filestream, message, strlen(message));  // Write the message to UART
    if (count < 0)
    {
        std::cerr << "UART TX error" << std::endl;  // Output error message if writing failed
    }

    // Read data from the UART device
    unsigned char rx_buffer[256];  // Buffer to store incoming data
    int rx_length = read(uart0_filestream, (void*)rx_buffer, 255);  // Read data from UART into buffer
    if (rx_length < 0)
    {
        std::cerr << "UART RX error" << std::endl;  // Output error message if reading failed
    } else if (rx_length == 0)
    {
        std::cout << "No data received" << std::endl;  // Notify if no data was received
    } else
    {
        rx_buffer[rx_length] = '\0';  // Null-terminate the buffer to make it a valid string
        std::cout << "Received: " << rx_buffer << std::endl;  // Output the received data
    }

    close(uart0_filestream);  // Close the UART device
    return 0;  // Return success code
}
```

# C++ Manipulators

Manipulators in C++ are used to modify the formatting of the input/output streams. This is particularly useful when dealing with different data representations, such as hexadecimal or binary, which are common in embedded programming.

### Example:

```cpp
#include <iostream>
#include <iomanip>

int main()
{
    int num = 255;
    
    std::cout << "Hexadecimal: " << std::hex << num << std::endl; // Outputs in hexadecimal
    std::cout << "Decimal: " << std::dec << num << std::endl;     // Outputs in decimal
    
    // Reset manipulator after use
    std::cout << std::dec;
    
    return 0;
}
```

### Practical Example for Embedded Linux:

Suppose you are working with memory-mapped registers where you need to read and display register values in hexadecimal format:

```cpp
#include <iostream>   // For standard input and output operations
#include <iomanip>    // For input/output manipulators like std::hex
#include <fcntl.h>    // For file control options (e.g., open flags)
#include <unistd.h>   // For POSIX constants and functions (e.g., close, read, write)
#include <sys/mman.h> // For memory management declarations (e.g., mmap, munmap)

// Define the base address for a peripheral register.
// This address should correspond to the specific hardware peripheral you want to interact with.
#define BASE_ADDR        0x3F200000  // Example base address for a peripheral register

int main()
{
   
    // Open /dev/mem for read/write access with synchronization.
    // /dev/mem provides access to physical memory, which is useful for low-level hardware interactions.
    int mem_fd = open("/dev/mem", O_RDWR | O_SYNC);

    if (mem_fd == -1)
    {
        // Print an error message and exit if opening /dev/mem fails.
        std::cerr << "Error opening /dev/mem" << std::endl;
        return -1; // Return with an error code
    }

    // Map a memory region to the process's address space.
    // The size of the region is 4096 bytes (1 page), and the region is mapped with read and write permissions.
    // MAP_SHARED allows changes to the memory to be visible to other processes mapping the same region.
    volatile unsigned int* reg = (unsigned int*)mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, BASE_ADDR);

    if (reg == MAP_FAILED)
    {
        // Print an error message and close the file descriptor if memory mapping fails.
        std::cerr << "Memory mapping failed" << std::endl;
        close(mem_fd); // Close the file descriptor as the memory mapping was not successful
        return -1; // Return with an error code
    }

    // Output the value of the register to the console.
    // std::hex sets the output format to hexadecimal.
    std::cout << "Register value: 0x" << std::hex << *reg << std::endl;

    // Unmap the memory region to release the resources.
    // munmap should be called to clean up after you are done using the mapped memory region.
    munmap((void*)reg, 4096);

    // Close the file descriptor for /dev/mem.
    close(mem_fd);

    return 0; // Return 0 to indicate successful execution
}
```


# C++ Operators

C++ operators are largely the same as in C, including arithmetic, logical, and bitwise operators. However, C++ introduces additional operators, like the scope resolution operator (`::`), which is essential in object-oriented programming.

### Practical Example for Embedded Linux:

Let's say you need to toggle specific bits in a hardware register for controlling an LED or configuring a peripheral:

```cpp
#include <iostream>  // Include the I/O stream library for input and output operations
#include <fcntl.h>   // Include the file control library for file operations
#include <unistd.h>  // Include the POSIX constants and types for system calls

#define BASE_ADDR 0x3F200000  // Define the base address for the peripheral register you want to access
#define LED_BIT 18            // Define the bit position for controlling the LED (example bit position)

int main()
{
    // Open the /dev/mem device file to access physical memory
    // O_RDWR: Open the file descriptor for read and write access
    // O_SYNC: Ensure data is synchronized with the underlying hardware
    int mem_fd = open("/dev/mem", O_RDWR | O_SYNC);

    // Check if the file descriptor was successfully opened
    if (mem_fd == -1)
    {  
        std::cerr << "Error opening /dev/mem" << std::endl;  // Print error message if opening failed
        return -1;  // Return with error code
    }

    // Map the physical memory region to the process's virtual address space
    // NULL: Let the system choose the address where the memory will be mapped
    // 4096: Size of the memory region to map (1 page)
    // PROT_READ | PROT_WRITE: Allow both read and write operations
    // MAP_SHARED: Changes to the memory are visible to other processes mapping the same region
    // mem_fd: File descriptor for /dev/mem
    // BASE_ADDR: Offset into the physical memory to start the mapping
    volatile unsigned int* reg = (unsigned int*)mmap(NULL, 4096, PROT_READ | PROT_WRITE, MAP_SHARED, mem_fd, BASE_ADDR);

    // Check if memory mapping was successful
    if (reg == MAP_FAILED)
    {  
        std::cerr << "Memory mapping failed" << std::endl;  // Print error message if mapping failed
        close(mem_fd);  // Close the file descriptor before exiting
        return -1;  // Return with error code
    }

    // Toggle the LED bit by XORing with 1 << LED_BIT
    // XOR operation will flip the bit at the position defined by LED_BIT
    *reg ^= (1 << LED_BIT);  // Modify the register to toggle the LED state

    // Print the register value after the toggle operation
    // std::hex: Output in hexadecimal format
    std::cout << "Register value after toggle: 0x" << std::hex << *reg << std::endl;

    // Unmap the memory region and release resources
    // (void*)reg: Cast the register pointer to void* for munmap
    munmap((void*)reg, 4096);  // Unmap the memory region

    // Close the file descriptor for /dev/mem
    close(mem_fd);  // Release the file descriptor and associated resources

    return 0;  // Return with success code
}
```



# C++ Loops

C++ supports all the traditional loops from C (`for`, `while`, `do-while`) but adds a range-based `for` loop that simplifies iteration over collections like arrays or vectors.

### Range-Based Loop Example:

```cpp
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> numbers = {1, 2, 3, 4, 535};

    for (int num : numbers)
    {
        std::cout << num << "\n";
    }

    return 0;
}
```





# C++ Functions

Functions in C++ work similarly to C. Here’s a deeper look into C++ functions, with practical examples that might be useful for embedded systems programming.

## **Basic Function Declaration and Definition**
In C++, functions are declared and defined much like in C. However, C++ allows for default parameters, which can simplify function calls and reduce redundancy in code.

**Basic Function Example:**
```cpp
#include <iostream>

// Function with a default parameter
void printMessage(std::string message = "Hello, World!") {
    std::cout << message << std::endl;
}

int main() {
    printMessage();            // Prints: Hello, World! (default message)
    printMessage("Hi there!"); // Prints: Hi there! (custom message)
    return 0;
}
```
**Explanation:**
- The function `printMessage` can be called with or without an argument. If no argument is provided, it uses the default value `"Hello, World!"`.
- This feature is particularly useful in embedded systems where you might want to have default configurations or debug messages that can be overridden as needed.

## **Handling Default Parameters**
One important rule when using default parameters in C++ is that once a default parameter is specified, all subsequent parameters must also have default values.

**Incorrect Code:**
```cpp
#include <iostream>

// Incorrect function declaration: Missing default value for y
void fun(int x = 2, int y);

void fun(int x, int y)
{
    std::cout << x << " " << y << std::endl;
}

int main()
{
    fun(2);  // Error: Function call is ambiguous
    return 0;
}
```
**Why It Fails:**
- The above code will result in a compilation error because `y` is not given a default value, making it impossible to call the function with just one argument.

**Correct Code:**
```cpp
#include <iostream>

// Correct function declaration with default value for x
void fun(int y, int x = 2);

void fun(int y, int x)
{
    std::cout << x << " " << y << std::endl;
}

int main()
{
    fun(3);  // Outputs: 2 3
    return 0;
}
```
**Explanation:**
- Here, the function `fun` can be called with just one argument (`y`), and `x` will default to `2`. This avoids ambiguity and ensures that the function works as intended.

### **Practical Embedded Linux Examples**
When working with embedded systems, functions with default parameters can be quite powerful. They allow for more readable code and can help in managing hardware configurations.

**Example: Configurable GPIO Setup**
Imagine you’re working with GPIO pins on an embedded Linux device. You might have a function to configure a pin with default settings but allow customization if needed.

```cpp
#include <iostream>
#include <string>

// Function to configure a GPIO pin with default direction and value
void configureGPIO(int pinNumber, std::string direction = "out", int value = 0)
{
    std::cout << "Configuring GPIO Pin: " << pinNumber 
              << " Direction: " << direction 
              << " Value: " << value << std::endl;
}

int main()
{
    configureGPIO(17);                      // Default: Output, Low
    configureGPIO(18, "in");                // Custom: Input, no value needed
    configureGPIO(22, "out", 1);            // Custom: Output, High
    return 0;
}
```
**Explanation:**
- `configureGPIO` can be called with just a pin number, and it will use default values (`direction = "out"` and `value = 0`).
- This flexibility allows you to easily manage GPIO configurations without repeatedly specifying common settings.

## **Default Parameters and Overloading**
Default parameters can also be combined with function overloading to create even more flexible and powerful interfaces.

**Example: Overloaded GPIO Setup**
```cpp
#include <iostream>
#include <string>

// Overloaded function to configure a GPIO pin
void configureGPIO(int pinNumber, std::string direction, int value)
{
    std::cout << "Configuring GPIO Pin: " << pinNumber 
              << " Direction: " << direction 
              << " Value: " << value << std::endl;
}

// Overloaded version for input pins without a value parameter
void configureGPIO(int pinNumber, std::string direction = "in")
{
    std::cout << "Configuring GPIO Pin: " << pinNumber 
              << " Direction: " << direction << std::endl;
}

int main()
{
    configureGPIO(17, "out", 1);            // Output, High
    configureGPIO(18);                      // Input, default direction
    configureGPIO(22, "out");               // Output, default low value
    return 0;
}
```
**Explanation:**
- First Call: configureGPIO(17, "out", 1);

This call uses the first overloaded function, passing all three arguments (pinNumber, direction, 
and value). It configures GPIO pin 17 as an output and sets it to high (1).

- Second Call: configureGPIO(18);

This call uses the second overloaded function. It only passes pinNumber, relying on the default value of "in" for direction. It configures GPIO pin 18 as an input.

- Third Call: configureGPIO(22, "out");

This call uses the second overloaded function, passing pinNumber and direction ("out"). Since no value is provided, this assumes a default operation (which could be low or as configured elsewhere in a real system).


