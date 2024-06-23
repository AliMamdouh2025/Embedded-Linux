import pyautogui
from time import sleep

# Function to open Visual Studio Code
def open_vscode():
    """
    Simulates the actions needed to open Visual Studio Code.
    
    1. Presses the Windows key to open the Start menu.
    2. Types "visual studio" to search for Visual Studio Code.
    3. Presses Enter to open Visual Studio Code.
    4. Waits for the application to launch.
    """
    pyautogui.hotkey('win')  # Open the Start menu by pressing the Windows key
    sleep(1)  # Wait for the Start menu to open
    pyautogui.typewrite("visual studio")  # Type "visual studio" to search for Visual Studio Code
    sleep(1)  # Wait for the search results to appear
    pyautogui.press("enter")  # Press Enter to open Visual Studio Code
    sleep(3)  # Wait for Visual Studio Code to fully launch

# Function to open the Extensions view in Visual Studio Code
def open_extensions_view():
    """
    Simulates the actions needed to open the Extensions view in Visual Studio Code.
    
    1. Presses Ctrl+Shift+X to open the Extensions view.
    2. Waits for the Extensions view to open.
    """
    pyautogui.hotkey('ctrl', 'shift', 'x')  # Open the Extensions view by pressing Ctrl+Shift+X
    sleep(1)  # Wait for the Extensions view to open

# Function to install an extension by name
def install_extension(extension):
    """
    Simulates the actions needed to install an extension in Visual Studio Code.
    
    1. Types the extension name into the search box.
    2. Waits for the search results to appear.
    3. Double-clicks on the install icon to install the extension.
    4. Waits for the installation to complete.
    5. Clears the search box for the next extension.
    
    Parameters:
    extension (str): The name of the extension to install.
    """
    pyautogui.typewrite(extension)  # Type the extension name into the search box
    sleep(3)  # Wait for the search results to appear
    pyautogui.doubleClick(335, 240)  # Double-click on the install icon (adjust coordinates as needed)
    sleep(10)  # Wait for the extension to install
    clear_extension_search()  # Clear the search box for the next extension

# Function to clear the search box in the Extensions view
def clear_extension_search():
    """
    Simulates the actions needed to clear the search box in the Extensions view.
    
    1. Double-clicks on the extension search box to select its content.
    2. Waits for the selection to be made.
    3. Presses the delete key multiple times to clear the search box.
    4. Waits for the search box to clear.
    """
    pyautogui.doubleClick(153, 159) # Double-click on the extension search box to select its content (adjust coordinates as needed)
    sleep(3)  # Wait for the selection to be made
    pyautogui.press('delete', presses=19)  # Press the delete key 19 times to clear the search box
    sleep(6)  # Wait for the search box to clear

# Main function to automate the installation of multiple extensions
def main():
    """
    Main function to automate the process of opening Visual Studio Code,
    navigating to the Extensions view, and installing a list of extensions.
    
    1. Opens Visual Studio Code.
    2. Opens the Extensions view.
    3. Moves the mouse cursor to a starting position.
    4. Iterates over a list of extensions and installs each one.
    5. Breaks the loop after installing the last extension in the list.
    """
    open_vscode()  # Call the function to open Visual Studio Code
    open_extensions_view()  # Call the function to open the Extensions view
    sleep(2)  # Wait for the Extensions view to fully load
    pyautogui.moveTo(130, 140)  # Move to a starting position (adjust as needed)
    sleep(2)  # Wait for the cursor to move

    # List of extensions to install
    extensions = ["c++ testmate", "clangd", "c++ helper", "cmake", "cmake tool"]
    for extension in extensions:  # Iterate over each extension in the list
        install_extension(extension)  # Call the function to install the extension
        if extension == "cmake tool":  # If the extension is "cmake tool", break the loop
            break

# Run the main function when the script is executed
if __name__ == "__main__":
    main()  # Call the main function
