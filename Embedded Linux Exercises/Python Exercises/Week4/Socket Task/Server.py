import socket  # Import the socket library to facilitate network communication.
import threading  # Import threading to handle multiple clients simultaneously.

def handle_client(client_socket):
    """
    Handles communication with a connected client.

    :param client_socket: The socket object representing the client connection.
    """
    while True:
        data = client_socket.recv(1024)  # Receive data from the client (max 1024 bytes).
        if not data:
            break  # If no data is received, exit the loop.
        print("Received:", data.decode('utf-8').strip())  # Decode and print the received data.
    client_socket.close()  # Close the client socket when done.

def main():
    """
    Sets up and runs the server.
    """
    host = '127.0.0.1'  # The server will listen on the localhost.
    port = 12345  # Port number to listen on.

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a IPV4(AF_INET,)/TCP(SOCK_STREAM) socket.
    server_socket.bind((host, port))  # Bind the socket to the host and port.
    server_socket.listen(5)  # Listen for incoming connections (up to 5 in the backlog).

    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()  # Accept a new connection.
        print(f"Connection from {addr}")

        # Create and start a new thread to handle the client connection.
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()  # Run the main function if this script is executed directly.
