import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('localhost', 12345)
    client_socket.connect(server_address)

    # Receive the message from the server
    for i in range(3):

        message = client_socket.recv(1024).decode()
        print(f"Received message from server: {message} \n")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    main()
