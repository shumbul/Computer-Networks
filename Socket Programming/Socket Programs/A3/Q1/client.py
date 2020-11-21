from socket import socket, AF_INET, SOCK_STREAM

soc = socket(AF_INET, SOCK_STREAM)

port = 545

soc.connect(('127.0.0.1', port))

while True:
    sent_message = input("Input the message to be sent to server: ")
    soc.send(bytes(sent_message, encoding='utf8'))
    received_message = soc.recv(1024).decode("utf-8")
    print("Contents sent : "+sent_message+"\nServer's response : "+received_message+"\n")
    if(received_message == "Bye"):
        print("Socket is closed...")
        soc.close()
        exit()