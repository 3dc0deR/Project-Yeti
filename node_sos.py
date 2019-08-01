#this script sends a sos signal to the nearest raspberry pi node
import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = "192.168.43.27"          # IP address of pi
port = 1337                     # Reserve a port for your service.

s.connect((host, port))
filename='test.txt'
f = open(filename,'rb')
l = f.read()
print(l)
while (l):
   s.send(l)
   print('Sent ',repr(l))
   l = f.read()
f.close()

print('Done sending')
s.close()