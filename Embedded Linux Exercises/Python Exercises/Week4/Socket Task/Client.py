import socket  # Import the socket library for network communication.
import json  # Import the json library for JSON encoding and decoding.
import time  # Import the time library to add delays between messages.
import random  # Import the random library to generate random numbers.

def generate_message():
    """
    Generates a random JSON message.

    :return: A JSON string representing the message.
    """
    data = {
        "id": "XYZ",
        "Value": random.randint(0, 500),  # Generate a random value between 0 and 500.
        "type": "Temperture"
    }
    return json.dumps(data)  # Convert the dictionary to a JSON string.

def main():
    """
    Connects to the server and sends messages in a loop.
    """
    host = '127.0.0.1'  # The server's hostname or IP address.
    port = 12345  # The port used by the server.

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a IPV4(AF_INET,)/TCP(SOCK_STREAM) socket.
    client_socket.connect((host, port))  # Connect the socket to the server.

    while True:
        message = generate_message()  # Generate a new message.
        client_socket.send(message.encode('utf-8'))  # Send the message to the server.
        print(f"Sent: {message}")  # Print the sent message.
        time.sleep(1)  # Wait for 1 second before sending the next message.

    client_socket.close()  # Close the socket when done (this line is actually unreachable).

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly.
