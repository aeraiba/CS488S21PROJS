# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys
import json 
import os 

s = socket(AF_INET,SOCK_DGRAM)
host = sys.argv[1]
port = int(sys.argv[2])
buf =1024
addr = (host,port)

command = "ping -qc3 " + host + " 2>&1 | awk -F\'/\' \'END{print(/^rtt/? \"\"$6\"\":\"1\")}\'"
temp = os.popen(cmd).read()

TimeOut_RTT = float(temp)

datagram  = {"sequence_number": 23134,"data":""}
datagram_buffer = []

while True:
	line = sys.stdin.readline()
	if not line:
		packet = json.dumps(datagram)
		if(s.sendto(bytes(datagram,'utf-8'),addr)):
			print("sending...")
			#print(datagram)
		break
	if((sys.getsizeof(datagram["data"])-1 + sys.getsizeof(line)) < buf):
#		data += line
		datagram["data"] += str(line)
	else:
		datagram = json.dumps(datagram)
		if(s.sendto(bytes(datagram,'utf-8'),addr)):
			print("sending...")
			#print(datagram)
#		data = line
		datagram = json.loads(datagram)
		datagram["data"] = str(line)

s.close()
