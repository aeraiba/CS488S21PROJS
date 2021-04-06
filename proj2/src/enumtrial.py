#!/usr/bin/env python 

testdata = ['a','b','c','d','e','f','g','h','i'] 
count = 0 
for data in testdata:  
	print(count) 
	if(data == 'e'): 
		count = count - 2
		print(count)
	count+=1
