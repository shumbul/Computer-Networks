from socket import socket, AF_INET, SOCK_STREAM

soc = socket(AF_INET, SOCK_STREAM)
print("Socket successfully created")

port = 545

soc.bind(('127.0.0.1', port))
print("Socket is binded to %s" % port)

soc.listen(5)
print("Socket is listening")

clt, addr = soc.accept()
print('Got connection from', addr)

while True:
    print("Waiting for input from client")
    received_message = clt.recv(1024).decode("utf-8")
    if(received_message != "Bye"):
        sent_message = received_message.upper()
    else:
        sent_message = "Bye"
    print("Contents received : "+received_message+"\nContents sent : "+sent_message+"\n")
    clt.send(bytes(sent_message, encoding='utf8'))
    if(received_message == "Bye"):
        print('Socket is closed...')
        clt.close()
        exit()