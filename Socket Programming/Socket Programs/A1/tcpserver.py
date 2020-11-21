# server program for TCP connection
import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('0.0.0.0',599))
print("Socket Created")
sock.listen(5)

while True:
    print("Server waiting for connection")
    cli,addr=sock.accept()
    print("Client connected from ",addr)
    try:
        cli.send(bytes('Hey Client','utf-8'))
    except:
        print("Exited by user")
    cli.close()
