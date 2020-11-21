from socket import socket, AF_INET, SOCK_DGRAM, timeout

soc = socket(AF_INET, SOCK_DGRAM)
print("Socket successfully created")

IP = "127.0.0.1"
port = 52

soc.bind((IP, port))
print("Socket is binded to %s" % port)

all_clients = set()

while True:
    data, address = soc.recvfrom(10000)

    if address not in all_clients:
        all_clients.add(address)
        print("Received connection from : ", address)
        continue

    try:
        for other_client in all_clients:
            if other_client != address:
                soc.sendto((str(address[1]) + ' says ' + data.decode("utf-8")).encode(), tuple(other_client))

    except timeout:
        continue

    except ConnectionResetError:
        all_clients.remove(address)