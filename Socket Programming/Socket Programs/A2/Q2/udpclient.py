import socket
cli=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="Hello UDP Server"
print("Start the conversation! \n Send \"exit\" to leave chat")
while True:
    cli.sendto(msg.encode('utf-8'),('127.0.0.1',12345))
    data,addr=cli.recvfrom(4096)
    print("Server says: "+ str(data))
    msg=input()
    if msg=="exit":
        break
cli.close()