import socket
import threading

HOST = '0.0.0.0'
PORT = 12345


def handle_client(client_socket, clients):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break

            for client in clients:
                if client != client_socket:
                    client.send(message)
        except:
            break
    client_socket.close()
    clients.remove(client_socket)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

clients = set()

while True:
    clients_socket, addr = server_socket.accept()
    print('')
    clients.add(clients_socket)
    clients_thread = threading.Thread(target=handle_client, args=(clients_socket, clients))
    clients_thread.start()
