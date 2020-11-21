# client program for TCP connection
import socket

cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(('0.0.0.0',599))

try:
    data = cli.recv(1024)
    print(str(data))
except KeyboardInterrupt:
    print("Exited by user")
cli.close()
