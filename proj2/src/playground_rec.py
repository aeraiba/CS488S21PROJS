from socket import *
import select 

buf = 1024  
host = "10.0.0.1" 
port= 5599 


s = socket(AF_INET,SOCK_DGRAM) 
s.bind((host,port)) 



data, addr = s.recvfrom(buf) 
result = ""
ack="acknowledge"
try: 
	while(data): 
		result = data.decode()
		s.sendto(bytes(ack, 'utf-8'),addr)
		if not data: 
			break 
		data,addr = s.recvfrom(buf) 
except timeout: 
	s.close()
	
