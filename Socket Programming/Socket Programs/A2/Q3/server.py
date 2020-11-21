import socket
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

IP_address = "127.0.0.1"
Port = 12343
server.bind((IP_address, Port))
server.listen(100)
list_of_clients = []


def clientthread(conn, addr):
    msg="Welcome to this chatroom!"
    conn.send(msg.encode())

    while True:
        try:
            message = conn.recv(2048)
            if message:
                print("<" + addr[0] + "> " + str(message))
                # Calls broadcast function to send message to all
                message_to_send = "<" + addr[0] + " " + str(addr[1]) + "> " + str(message)
                broadcast(message_to_send, conn)
            else:
                remove(conn)
        except:
            continue


def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            try:
                clients.send(message.encode())
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)


while True:
    conn, addr = server.accept()
    list_of_clients.append(conn)
    print(addr[0]+ " " + str(addr[1]) + " connected")
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close() 

