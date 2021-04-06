#!/usr/bin/env python 

import json 
import subprocess 
import os
from socket import * 
import time

s = socket(AF_INET, SOCK_DGRAM)
host = "10.0.0.1"
port= 5599 
buf = 1024 
addr = (host, port) 
ticks = 0
strACK = ''
testdata=["1000","2000","3000","4000","5000","6000","7000","8000","9000","10000"
	 ,"11000" ,"12000","13000","14000","15000","16000","17000","18000","19000"
	 ,"20000"]

ackdata = ['']*20
#print(ackdata)
for data in testdata:
	count = 0
	#print(data)
	if (ackdata[count] != ''):
		ticks = time.time()
		s.sendto(testdata[count].encode(),addr)
		print("sending .." + testdata[count]) 
		ACK, address = s.recvfrom(buf) 
		postticks = time.time()
		strACK = ACK.decode('utf-8')
		if(strACK != ''): 
			print(strACK)
			print("getting ack") 
			ackdata[count] = "ack" + str(count+1) +  "recv"
			count = count + 1
		elif(postticks - ticks > 10): 
			count = count - 1
			print("waiting")

print(ackdata)
print("done")
s.close()
