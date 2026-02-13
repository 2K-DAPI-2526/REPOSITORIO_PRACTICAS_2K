#-----------------SERVIDOR BÄSICO CON SOCKETS-----------------

import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

def manejar_cliente(conn, addr):
    print(f"Conectado con {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        mensaje = data.decode()
        print(f"Mensaje recibido: {mensaje}")
        conn.send("Acción recibida".encode())
    conn.close()

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))
servidor.listen()

print("Servidor iniciado...")

while True:
    conn, addr = servidor.accept()
    thread = threading.Thread(target=manejar_cliente, args=(conn, addr))
    thread.start()