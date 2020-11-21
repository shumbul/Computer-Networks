import socket

cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(('127.0.0.1',599))
payload='Hey server'
print("Start the conversation! \n Send \"exit\" to leave chat")
try:
    while True:
        cli.send(payload.encode('utf-8'))
        data = d.recv(1024)
        print(str(data))
        payload=input()
        if payload=="exit":
            break
except KeyboardInterrupt:
    print("Exited by user")
cli.close()