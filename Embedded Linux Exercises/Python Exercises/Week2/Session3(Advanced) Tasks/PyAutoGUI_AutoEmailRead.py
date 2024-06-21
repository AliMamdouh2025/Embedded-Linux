import pyautogui  # Import pyautogui for GUI automation
import webbrowser  # Import webbrowser to open URLs in the default browser
import time  # Import time to add delays

def locate(image, x_shift=0, y_shift=0, is_clicked=False, max_attempts=5):
    """
    Locate an image on the screen and optionally click on it.

    Parameters:
    image (str): The filename of the image to locate on the screen.
    x_shift (int): Horizontal offset to move the cursor from the located image's position.
    y_shift (int): Vertical offset to move the cursor from the located image's position.
    is_clicked (bool): Whether to click on the located image's position.
    max_attempts (int): Maximum number of attempts to find the image before giving up.
    """
    # Attempt to locate the image up to max_attempts times
    for attempt in range(max_attempts):
        location = pyautogui.locateOnScreen(image)  # Locate the image on the screen
        if location is not None:
            # Move the cursor to the located image with the specified offsets
            pyautogui.moveTo(location[0] + x_shift, location[1] + y_shift, duration=0.5)
            if is_clicked:
                pyautogui.click()  # Click if is_clicked is True
            return True  # Return True if the image is found and (optionally) clicked
        time.sleep(1)  # Wait for a second before the next attempt
    # Print a message if the image is not found after max_attempts
    print(f"Image '{image}' not found on the screen after {max_attempts} attempts.")
    return False  # Return False if the image is not found

def main():
    # Open Gmail in a new browser tab
    webbrowser.open_new_tab("https://mail.google.com/mail/u/0/#inbox")
    # Wait for the browser and Gmail to load (adjust based on your computer and internet speed)
    time.sleep(7)

    # Locate and hover over the email to make the "Mark as read" button appear
    if not locate("Vector.png", x_shift=20, y_shift=20, is_clicked=False):
        return  # Exit if the image is not found

    # Wait for a few seconds to ensure the "Mark as read" button appears
    time.sleep(4)  # Adjust based on your computer and internet speed

    # Locate and click the "Mark as read" button
    if not locate("MarkAsRead.png", x_shift=20, y_shift=20, is_clicked=True):
        return  # Exit if the image is not found

    # Wait for the action to complete
    time.sleep(2)  # Adjust based on your computer and internet speed

    # Close the browser tab using the keyboard shortcut Ctrl+W
    pyautogui.hotkey('ctrl', 'w')

# Call the main function to execute the script
if __name__ == "__main__":
    main()
