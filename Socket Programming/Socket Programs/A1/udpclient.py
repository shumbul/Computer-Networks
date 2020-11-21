# client program for UDP connection
import socket
cli=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="Hello UDP Server"
cli.sendto(msg.encode('utf-8'),('127.0.0.1',12345))
data,addr=cli.recvfrom(4096)
print("Server says: "+ str(data))
cli.close()
