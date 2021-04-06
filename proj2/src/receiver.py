# ----- receiver.py -----

#!/usr/bin/env python

from socket import *
import sys
import select
import json 

host="0.0.0.0"
port = int(sys.argv[1])
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf = 1024

data,addr = s.recvfrom(buf)
result = ""
try:
	while(data):
		result = data.decode('utf-8')
		result = json.loads(result)
#		print(result.strip("\n"))
		print((result["data"]).strip("\n"))
		s.settimeout(2)
		data,addr = s.recvfrom(buf)
except timeout:
	s.close()
