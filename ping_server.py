#!/usr/bin/env python3

# Server for UDP pinger

import socket
import random

def main():
	bufferSize = 2048
	serverPort = 12000
	serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	serverSocket.bind((socket.gethostbyname(""), serverPort))
	# server running
	print ("The server is ready to receive.")

	while True:
		message, clientAddress = serverSocket.recvfrom(bufferSize)
		message = message.upper()
		serverSocket.sendto(message,clientAddress)
	pass

if __name__ == '__main__':
	main()
	

