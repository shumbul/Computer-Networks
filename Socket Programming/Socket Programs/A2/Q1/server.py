# server program
import socket
from datetime import date

socki=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socki.bind(('127.0.0.1',599))
print("Socket Created")
socki.listen(5)

while True:
    print("server waiting for connection")
    cli,addr=socki.accept()
    print("Client connected from ",addr)
    data=cli.recv(1024)
    if not data or data.decode('utf-8')=='END':
        break
    print("Recieved from client: %s"% data.decode("utf-8"))
    today = date.today()
    msg="Hey Client, today is "+str(today)
    try:
        cli.send(bytes(msg,'utf-8'))
    except:
        print("Exited by user")
    cli.close()