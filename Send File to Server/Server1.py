import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '' #localhost
port = 1234
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

print("Server listening on {}:{}".format(host, port))

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

# Receive and save the file
file_name = client_socket.recv(1024).decode('utf-8')
with open(file_name, 'wb') as file:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        file.write(data)

print("File received and saved as:", file_name)

# Close the connection
client_socket.close()
server_socket.close()