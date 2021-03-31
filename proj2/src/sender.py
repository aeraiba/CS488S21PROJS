# ----- sender.py ------

#!/usr/bin/env python
from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host = sys.argv[1]
port = int(sys.argv[2])
buf =1024
addr = (host,port)

#f=open("a.txt","rb")
#data = f.read(buf)
#print(type(data))
#while (data):
#    if(s.sendto(data,addr)):
#        print("sending ...")
#        data = f.read(buf)
#file_size = sys.getsizeof(sys.stdin)
#data = " "
#data_bytes = b''
#print(type(data_bytes))
#for bits in sys.stdin:
#	if((sys.getsizeof(data)-1) < buf):
#		data += bits
#	else:
#		print(data)
#		data_bytes = str.encode(data)
#		s.sendto(data_bytes,addr)
#		data = bits
#		data_bytes = b''

data = ""

while True:
	line = sys.stdin.readline()
	if not line:
		if(s.sendto(bytes(data, 'utf-8'),addr)):
			print("sending...")
		break
	if((sys.getsizeof(data)-1 + sys.getsizeof(line)) < buf):
		data += line
	else:
		if(s.sendto(bytes(data, 'utf-8'),addr)):
			print("sending...")
		data = line




#print("sent" + str(file_size))
s.close()
#f.close()