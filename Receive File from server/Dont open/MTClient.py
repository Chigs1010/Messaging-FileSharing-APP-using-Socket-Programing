import socket

def main():
    host = '127.0.0.1'  # Change this to the server's IP address
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    file_path = input("Enter the file path: ")
    client_socket.send(file_path.encode('utf-8'))

    file_name = client_socket.recv(1024).decode()
    with open(file_name, 'wb') as file:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            file.write(data)

    print("File received:", file_name)

    client_socket.close()

if __name__ == "__main__":
    main()
