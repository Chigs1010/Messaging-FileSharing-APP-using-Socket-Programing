import socket
import time
import pickle
def replace_slashes(input_string):
    return input_string.replace('\\', '/')
def main():
    # Client configuration
    host = '127.0.0.1'  # Server's IP address
    port = 12345       # Server's port number

    # Create a socket for the client
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Receive and decode the message from the server
    message = client_socket.recv(1024).decode()
    print(f"Received message from server: {message}")
    
    file_path = message  
    file_name = file_path.split('/')[-1]
    file_path = replace_slashes(file_path)
    print("File name is :::",file_name)
    client_socket.send(file_name.encode('utf-8'))
    with open(file_path, 'rb') as file:
        while True:
           data = file.read(1024)
           if not data:
               break
        client_socket.send(data)

    print("File sent:", file_name)
    #time.sleep(5)
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()