#This Scanner Program helps to receive banner from targat host
#!/user/bin/python

import socket

def retBanner(ip,port):
     try:
          socket.setdefaulttimeout(5)
          s = socket.socket() #s is object of socket
          s.connect((ip,port))  #connect function helps to connect to host
          banner = s.recv(1024)  #recv function hepls to receive banner
          retun banner
     except:
          retun
def main():
      ip = input("[+]Enter Target TP: ")
      for port in ranger(1,100):
                banner=retBanner(ip,port)
                if banner:
                        print("[+]"+ip+"/"+str(port)+":"+banner)
main()                
