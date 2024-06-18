import requests

def get_public_ip():
    """
    Get the public IP address using the ipify API.
    
    Returns:
        str: The public IP address if successful, None otherwise.
    """
    SiteUrlIp = "https://api.ipify.org/?format=json"
    try:
        # Make a request to the ipify API to get the public IP address
        response = requests.get(SiteUrlIp)
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        # Parse the JSON response to extract the IP address
        data = response.json()
        #Accesses the value associated with the key "ip" in the data dictionary. In JSON format, "ip" is a key that stores the public IP address returned by the ipify API. So it returns IP as string
        return data["ip"]
    except requests.RequestException as e:
        # Handle exceptions (e.g., network problems, invalid response)
        print(f"Error getting public IP: {e}")
        return None

def get_geolocation(ip):
    """
    Get geolocation information for the given IP address using the ipinfo API.
    
    Args:
        ip (str): The IP address to get geolocation for.
    
    Returns:
        dict: The geolocation information if successful, None otherwise.
    """
    SiteUrlGeo = f"https://ipinfo.io/{ip}/geo"
    try:
        # Make a request to the ipinfo API to get geolocation information for the given IP
        response = requests.get(SiteUrlGeo)
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        # Parse the JSON response to extract geolocation data
        return response.json()
    except requests.RequestException as e:
        # Handle exceptions (e.g., network problems, invalid response)
        print(f"Error getting geolocation: {e}")
        return None

if __name__ == "__main__": #Check if the script is being run directly (not imported as a module).
    # Get the public IP address
    ip = get_public_ip()
    if ip:
        # Print the public IP address if successfully obtained
        print(f"Your public IP address: {ip}")
        # Get geolocation information for the obtained IP address
        geo_info = get_geolocation(ip)
        if geo_info:
            # Print the geolocation information if successfully obtained
            print("Geolocation information:")
            for key, value in geo_info.items():
                print(f"{key}: {value}")
