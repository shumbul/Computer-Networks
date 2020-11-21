import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('0.0.0.0',599))
sock.listen(5)


def sortLexo(strings):
    words = strings.split()
    data=[]
    for i in words:
        data.append(i)
    data.sort()
    for i in data:
        print("Client: "+ str(i))
    return data


while True:
    conn,addr=sock.accept()
    while True:
        data=conn.recv(1024)
        if not data or data.decode('utf-8')=='END':
            break
        data=sortLexo(data)
        try:
            conn.send(bytes(str(data),'utf-8'))
        except:
            print("Exited by user")
    conn.close()
