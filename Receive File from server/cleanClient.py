import socket
import time
import pickle
import os
def show(folder_path):
    try:
        # Get a list of all items (files and subdirectories) in the folder
        items = os.listdir(folder_path)
        
        # Iterate through the items and print file paths
        for item in items:
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                print(item_path)
                

        
                
    except OSError as e:
        print(f"Error: {e}")


def replace_slashes(input_string):
    return input_string.replace('\\', '/')




def main():
    # Client configuration
    host = '127.0.0.1'  # Server's IP address
    port = 12345       # Server's port number
    folder_path_here = "C:/Users/Chirag/Desktop/DPPL Lab"
    show(folder_path_here)

    message=input("Enter the file path you want send :: ")
    # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # sends and decode the message from the server
    client_socket.send(message.encode())
    #message = client_socket.recv(1024).decode()

    file_name = client_socket.recv(1024).decode('utf-8')
    with open(file_name, 'wb') as file:
        while True:
          data = client_socket.recv(1024)
          if not data:
             break
          file.write(data)

    print("File received and saved as:", file_name)


    client_socket.close()

if __name__ == "__main__":
    main()