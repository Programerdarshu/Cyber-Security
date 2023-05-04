#This program is to compare banner(vulnerable) with text file 
#First create or download a text file that content vulnerables software names, By compareing this banners you can get an idea

#!/user/bin/python

import socket
import os
import sys #SYSTEM package or module

def retbanner():
        try:
            socket.setdefaulttimeout(5)
            s = socket.socket()
            s.connect((ip,port))
            banner = s.recv(1024)
            return banner
        except:
            return
          
def checkvulns(banner,filename):
          f = open(filename,"r")
          for line in f.readlines():
                  if line.strip("\n")in banner:
                            print("[+]Server is vulnerable: "+banner.strip("\n"))
        
#Lets code main function
def main():
      if len(sys.argv)==2:
              filename = sys.argv[1]
              if not os.path.isfile(filename):
                        print("[-]File Doesnot Exists!!!!!")
                        exit(0)
              if not os.access(filename,os.R_OK):
                        print("[-]Access denied!!!")
                        exit(0)
      else:
            print("[-]Usage: "+str(sys.argv[0])+"<vuln filename>")
            exit(0)
      portlist = [21,22,25,80,110,443,445] #this are all important ports 
      for x in range(1,255):
            ip = "192.268.1."+str(x)
            #192.168.1.1 To 192.168.1.255
            for port in portlist:
                  banner = retbanner(ip,port)
                  if banner:
                      print("ip"+"/"+str(port)+":"+banner)
                      checkvulns(banner,filename)
main()                      
