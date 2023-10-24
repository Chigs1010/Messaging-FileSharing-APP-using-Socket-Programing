import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'#127.0.0.1  192.168.137.1
port = 1234
client_socket.connect((host, port))
def replace_slashes(input_string):
    return input_string.replace('/', '\\')
# Send the file
file_path = 'C:/Users/Chirag/Desktop/tessss.txt'  
file_name = file_path.split('/')[-1]
#file_path = replace_slashes(file_path)
client_socket.send(file_name.encode('utf-8'))

with open(file_path, 'rb') as file:
    while True:
        data = file.read(1024)
        if not data:
            break
        client_socket.send(data)

print("File sent:", file_name)

# Close the connection
client_socket.close()


