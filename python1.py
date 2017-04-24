#!/usr/bin/python
import sys
print sys.argv[1]

def makeFile(fileName, message, mode): #(1)
	a=open(fileName, mode) #(2)
	a.write(message) #(3)
	a.close()

makeFile("/etc/squid/aulas-prohibidas.txt", "10.0.%s.0/24\n" % sys.argv[1], "a")




