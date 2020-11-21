import socket
cli=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
cli.connect(('127.0.0.1',599))

try:
    while True:
        payload=input("Enter the strings ")
        cli.send(payload.encode('utf-8'))
        data = cli.recv(1024)
        # words=data.split()
        # lis=[]
        # for i in words:
        #     k=slice(2,-1,1)
        #     lis.append(i[k])
        # print(str(lis))
        print(str(data))
        more=input('Want to send more data to the server (y/n)?')
        if more.lower()=='n':
            break
except KeyboardInterrupt:
    print("Exited by user")
cli.close()