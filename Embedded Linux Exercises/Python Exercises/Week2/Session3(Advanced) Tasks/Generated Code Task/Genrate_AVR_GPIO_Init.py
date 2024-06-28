def generate_init_code():
    """
    This function prompts the user to configure the mode ('in' or 'out') for each bit (0 to 7)
    of a PORTA on an AVR microcontroller. It then generates and writes the corresponding
    initialization code to set the port direction register (DDRA) based on the user input.
    """

    # Prompt user to enter mode for each bit from 0 to 7
    modes = []
    for i in range(8):
        # Prompt the user to enter mode for the current bit (in/out)
        mode = input(f"Please enter Bit {i} mode (in/out): ").strip().lower()
        
        # Validate the input to ensure it is either 'in' or 'out'
        while mode not in ['in', 'out']:
            print("Invalid mode. Please enter 'in' or 'out'.")
            mode = input(f"Please enter Bit {i} mode (in/out): ").strip().lower()
        
        # Add the validated mode to the list of modes to allow iteration on mode
        modes.append(mode)
    
    # Generate the initialization function code based on user input
    init_code = "void Init_PORTA_DIR (void)\n"  # Function signature
    init_code += "{\n"  # Begin function body
    init_code += "    DDRA = 0b"  # Start setting DDRA register value
    
    # Convert each mode ('in' or 'out') to '0' or '1' and append to init_code
    for mode in modes:
        if mode == 'in':
            init_code += '0'  # '0' sets pin direction to input
        elif mode == 'out':
            init_code += '1'  # '1' sets pin direction to output
    
    init_code += ";\n"  # End DDRA register value setting with a semicolon
    init_code += "}\n"  # End function body with a closing curly brace
    
    # Write the generated code to Init_AVR_GPIO.c file
    with open('Init_AVR_GPIO.c', 'w') as file:
        file.write(init_code)
    
    print("Generated Init_AVR_GPIO.c file successfully.")

# Call the function to generate and write the code
generate_init_code()

