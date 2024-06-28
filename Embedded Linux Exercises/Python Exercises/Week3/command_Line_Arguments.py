import sys

def main():
    # Print the name of the script
    print("Script name:", sys.argv[0])

    # Check if any arguments were passed
    if len(sys.argv) > 1:
        # Print the arguments passed to the script
        print("Arguments:")
        
        # Loop through the arguments starting from the first one, Execluding Script name
        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")
    else:
        # No arguments were passed
        print("No arguments were passed.")

if __name__ == "__main__":
    main()
