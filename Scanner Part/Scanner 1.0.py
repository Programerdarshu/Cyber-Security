#simple Scanner program, This program can be implemented in kali linux
--------------------------------------------------------------------
#!/user/bin/python

import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = input("[+]Enter Host IP: ")
port = int(input("[+]Enter Port To Scan: "))

def portscanner(port):
      if sock.connect_ex((host,port)):
             print("[-]Port %d is closed" % (port))
      else:
             print("[+]Port %d is Open" % (port))

portscanner(port)             

