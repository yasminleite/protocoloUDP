import socket

SERVER_IP = 'localhost'
SERVER_PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Alunos: Ruan Carlos e Yasmin Leite\n")
print("Aplicação utilizando o protocolo UDP para inverter letras minúsculas para maiúsculas e letras maiúsculas para minúsculas.\n")

while True:
    message = input("Digite um texto: ")

    client_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

    response, addr = client_socket.recvfrom(1024)
    
    print("Resposta do server:", response.decode())

    c= input("Deseja continuar? (yes/no): ")

    if c.lower() != "yes":
        break

client_socket.close()
