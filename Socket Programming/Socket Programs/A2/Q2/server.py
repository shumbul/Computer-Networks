import socket

socki=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socki.bind(('127.0.0.1',599))
print("Socket Created")
socki.listen(5)

while True:
    print("server waiting for connection")
    cli,addr=socki.accept()
    print("Client connected from ",addr)
    while True:
        data=cli.recv(1024)
        if not data or data.decode('utf-8')=='END':
            break
        print("Recieved from client: %s"% data.decode("utf-8"))
        more=input("Enter your reply.")
        try:
            cli.send(bytes(more,'utf-8'))
        except:
            print("Exited by user")
    cli.close()