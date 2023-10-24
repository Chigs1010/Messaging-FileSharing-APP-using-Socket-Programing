import socket
import threading
import os

def replace_slashes(input_string):
    return input_string.replace('\\', '/')

def handle_client(client_socket, client_addr):
    print(f"Connection established with {client_addr}")

    message = client_socket.recv(1024).decode()
    print(f"Received path from client: {message}")

    file_path = message
    file_path = replace_slashes(file_path)
    file_name = file_path.split('/')[-1]

    print("File name is:", file_name)
    client_socket.send(file_name.encode('utf-8'))

    with open(file_path, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client_socket.send(data)

    print("File sent:", file_name)

    client_socket.close()

def main():
    host = '0.0.0.0'
    port = 12345
    folder_path_here = "C:/Users/Chirag/Desktop/DPPL Lab"

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print("Server is listening for incoming connections...")

    while True:
        client_socket, client_addr = server_socket.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_addr))
        client_handler.start()

if __name__ == "__main__":
    main()
