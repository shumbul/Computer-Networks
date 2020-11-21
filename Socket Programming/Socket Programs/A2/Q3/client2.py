import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
IP_address = "127.0.0.1"
Port = 12343
server.connect((IP_address, Port))

while True:

	# maintains a list of possible input streams
	sockets_list = [sys.stdin, server]
	read_sockets=sockets_list
	write_socket= []
	error_socket=[]

	for socks in read_sockets:
		if socks == server:
			message = socks.recv(2048)
			print (message )
		else:
			message = sys.stdin.readline()
			sys.stdout.write("<You> ")
			sys.stdout.write(message)
			server.send(message.encode())
			sys.stdout.flush()