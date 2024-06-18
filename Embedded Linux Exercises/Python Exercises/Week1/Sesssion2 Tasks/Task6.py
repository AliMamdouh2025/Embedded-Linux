import webbrowser

# Dictionary of websites with names and URLs
websites = {
    "Facebook": "https://www.facebook.com/",
    "YouTube": "https://www.youtube.com/",
    "ChatGPT": "https://chat.openai.com/"
}

# List of website names for easy indexing
urls = ["Facebook", "YouTube", "ChatGPT"]

def open_website(url_index):
    """
    Open a website in the specified web browser.

    Args:
        url_index (str): The index of the website to open, provided by the user.
    """
    browser_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(browser_path))
    
    try:
        # Convert the user's input to an integer and open the corresponding website
        index = int(url_index) - 1
        if index in range(len(urls)):
            webbrowser.get('edge').open(websites[urls[index]])
        else:
            print("Invalid number. Please choose a valid website number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    # Prompt the user to choose a website
    website = input("Choose website number:\n 1- Facebook\n 2- YouTube\n 3- ChatGPT\n")
    open_website(website)
