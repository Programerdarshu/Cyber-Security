#!/user/bin/python

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Enter The Host To Scan:  ")

def portscanner(port):
    if sock.connect_ex((host,port)):
            print("[-] Port %d is colsed" % (port))
    else:
            print("[-] Port %d is colsed" % (port))

for port in range(1,1000):
       portscanner(port)
    
    #you can edit number port to scan 
