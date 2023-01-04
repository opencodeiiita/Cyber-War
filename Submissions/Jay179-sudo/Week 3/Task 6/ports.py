import pyfiglet
import sys
import socket
from datetime import datetime

if len(sys.argv) == 2:
	
	# we take the host address as a system argument
	target = socket.gethostbyname(sys.argv[1])
else:
	sys.exit()

print("-" * 25)
print("Target: " + target)
print("-" * 25)

try:
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# returns an error indicator
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()
