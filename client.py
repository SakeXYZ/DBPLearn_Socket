import socket
import threading

HOST = '0.0.0.0'
PORT = 12345


def received_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(message)
        except:
            break


def send_message(client_socket):
    while True:
        try:
            message = input("")
            if message.lower() == '/quit':
                client_socket.close()
                break
            client_socket.send(message.encode('utf-8'))
        except:
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

name = input("Enter your name: ")
client_socket.send(f"Name {name} has been joined the chat".encode('utf-8'))

received_thread = threading.Thread(target=received_message, args=(client_socket,))
send_thread = threading.Thread(target=send_message, args=(client_socket,))

received_thread.start()
send_thread.start()

received_thread.join()
send_thread.join()
