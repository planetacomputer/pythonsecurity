import socket, sys
target_host = "economia.elpais.com"
target_port = 80
# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect the client
client.connect((target_host,target_port))
# send some data
client.send("GET / HTTP/1.1\r\nHost: http://economia.elpais.com/economia/2017/03/31/actualidad/1490954088_670624.html/\r\n\r\n")
# receive some data
response = client.recv(9500)
if len(sys.argv)==2 and sys.argv[1] == "-h":
    c = response.lower().find("<html")
    print response[0:c]
else:
    print response