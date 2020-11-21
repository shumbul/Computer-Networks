import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))
print("Socket Created")

while True:
    data,addr=sock.recvfrom(4096)
    print(str(data))
    message=input("Enter your reply.")
    sock.sendto(message.encode('utf-8'),addr)
