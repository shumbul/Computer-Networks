# client program for asking current date
import socket

cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(('127.0.0.1',599))
payload='Hey server, can you please tell me today\'s date?'
print("Client: "+payload)
try:
    cli.send(payload.encode('utf-8'))
    data = cli.recv(1024)
    print("Server: "+str(data))
except KeyboardInterrupt:
    print("Exited by user")
cli.close()