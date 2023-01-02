import sys  # for handling exceptions
import socket   # for checking the ports
from datetime import datetime   # to get the current date and time

target = input(str("Target IP: "))
print("-------------------------")
print("Scanning " + target)
print("Scanning started at: " + str(datetime.now()))
print("-------------------------")

try:
    for port in range(1,65535): # iterating through all ports
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #internet address of ipv4 address, socket type for tcp which sends messages
        socket.setdefaulttimeout(0.5)   # default time to skip a port and move to next

        result=s.connect_ex((target,port))  # returns 0 for successful operation
        if result==0:
            print("[+] Port " + str(port) + " is open \n")
        s.close()

except KeyboardInterrupt:   # to terminate the program like with ctrl C
    print("\n Exiting")
    sys.exit()

except socket.error:
    print("\n Host unresponsive")
    sys.exit()
