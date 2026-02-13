import socket

HOST = "127.0.0.1"
PORT = 5000

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))

while True:
    mensaje = input("Acción: ")
    cliente.send(mensaje.encode())
    respuesta = cliente.recv(1024).decode()
    print("Servidor:", respuesta)