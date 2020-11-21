# server program for UDP connection
import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))
print("Socket Created")

while True:
    print("server waiting for connection")
    data,addr=sock.recvfrom(4096)
    print("Client connected from ",addr)
    message="Hello I am UDP Server"
    sock.sendto(message.encode('utf-8'),addr)
