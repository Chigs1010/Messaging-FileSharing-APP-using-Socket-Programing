import socket

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)

    print("Server is listening...")

    # Accept a connection
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Send a message to the client
    for i in range(3):

      message = f"Hello, client! This is a message from the server {i}."
      client_socket.send(message.encode())

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
