#/usr/bin/env python3

# client for UDP pinger 

import socket
import datetime
import time

def main():

	# set server, port, and buffer size
	serverName = socket.gethostbyname("")
	serverPort = 12000
	bufferSize = 2048

	# UDP connection
	clientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	# send this to sever
	message = "ping"
	# list to store the round trip times for each packet
	rttList = []

	p = 0
	# send 10 packets
	while p < 10:
		# time when packet was sent
		sentTime = time.time()
		clientSocket.sendto(message.encode(),(serverName, serverPort))
		# timeout set to 1 second
		clientSocket.settimeout(1)

		# initialize values
		averageRTT = 0
		successfulPackets = 0

		try:
			modifiedMessage, serverAddress = clientSocket.recvfrom(bufferSize)
			# time when packet was received
			receivedTime = time.time()
			# get round trip time
			RTT = receivedTime - sentTime
			# add rtt's to list
			rttList.append(RTT)
			# calcualte the average rtt
			rttSum = sum(rttList)
			successfulPackets = len(rttList)
			averageRTT = rttSum / successfulPackets
			print ("Packet: ", p)
			print (modifiedMessage.decode())
			print ("The total round trip time (RTT) = ", RTT, "seconds\n")

		except socket.timeout:
			# timeout exception
			print ("Packet: ", p)
			print ("!! Request time out !!\n")

		p = p + 1

	print ("Done.\n")
	print ("Results: ")
	print ("The average round trip time (RTT) is: ", averageRTT, "seconds")
	print ("The total number of succesful packets is: ", successfulPackets)
	print ("the total number of lost packets is: ", p - successfulPackets) #calculate lost packets

	clientSocket.close()

if __name__ == '__main__':
	main()
