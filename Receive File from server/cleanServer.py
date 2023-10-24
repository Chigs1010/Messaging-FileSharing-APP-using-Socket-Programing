import socket
import time
import os
import pickle

def replace_slashes(input_string):
    return input_string.replace('\\', '/')


def main():
    # Server configuration
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 12345     # Use a port number of your choice
    folder_path_here = "C:/Users/Chirag/Desktop/DPPL Lab"
    #List=show(folder_path_here)


    
    
    # Create a socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one client connection

    print("Server is listening for incoming connections...")

    # Accept a client connection
    client_socket, client_addr = server_socket.accept()
    print(f"Connection established with {client_addr}")
    
    message = client_socket.recv(1024).decode()
    print(f"Received path from client: {message}")
    # Send a message to the client
    #message = "Hello, client! This is the server speaking."
    

    file_path = message  
    file_path = replace_slashes(file_path)
    file_name = file_path.split('/')[-1]
    
    print("File name is :::",file_name)
    client_socket.send(file_name.encode('utf-8'))
    with open(file_path, 'rb') as file:
        while True:
           data = file.read(1024)
           if not data:
               break
           client_socket.send(data)

    print("File sent:", file_name)

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
