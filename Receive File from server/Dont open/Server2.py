import socket
import time
import os
import pickle
def show(folder_path):
    try:
        # Get a list of all items (files and subdirectories) in the folder
        items = os.listdir(folder_path)
        
        # Iterate through the items and print file paths
        for item in items:
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                print(item_path)
               # new_list.append(item_path)

       # return new_list
                
    except OSError as e:
        print(f"Error: {e}")
def main():
    # Server configuration
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 12345     # Use a port number of your choice
    folder_path_here = "C:/Users/Chirag/Desktop/DPPL Lab"
    show(folder_path_here)

    
    message=input("Enter the file path you want send :: ")
    # Create a socket for the server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for one client connection

    print("Server is listening for incoming connections...")

    # Accept a client connection
    client_socket, client_addr = server_socket.accept()
    print(f"Connection established with {client_addr}")

    # Send a message to the client
    #message = "Hello, client! This is the server speaking."

    client_socket.send(message.encode())
    
    file_name = client_socket.recv(1024).decode('utf-8')
    with open(file_name, 'wb') as file:
        while True:
          data = client_socket.recv(1024)
          if not data:
             break
        file.write(data)

    print("File received and saved as:", file_name)

    #time.sleep(5)
    # Close the socket
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
