from socket import socket, AF_INET, SOCK_DGRAM, timeout

soc = socket(AF_INET, SOCK_DGRAM)

IP = "127.0.0.1"
port = 52
address = (IP, port)

message = b'Hello, server!'
soc.sendto(message, address)
print("Welcome to the chat room!\n")
while True:
    message = input("Enter any message to be sent to server. (To exit, enter blank message)\n  ")

    if message != '':
        soc.sendto(message.encode(), address)

    try:
        rec, addr = soc.recvfrom(10000)
        rec = rec.decode("utf-8") + "\n"
        print("Received : ", rec)

    except timeout:
        break