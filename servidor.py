import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print('Servidor UDP rodando...')

while True:
    data, addr = server_socket.recvfrom(1024)
    
    print('Received from client:', data.decode())

    result = ""

    for a in data.decode():
        if a.islower():
            result += a.upper()
        else:
            result += a.lower()

    server_socket.sendto(result.encode(), addr)

server_socket.close()
