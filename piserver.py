#this script runs on a raspberry pi, waiting for an sos signal, as soon as it receives one, it saves it to a file and relays it to the next node
import socket                   # Import socket module

s = socket.socket()             # Create a socket object
addr = socket.getaddrinfo('0.0.0.0', 1337)[0][-1]
s.bind(addr)
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

while True:
    with open('received_file', 'wb') as f:
        print 'file opened'
        while True:
            print('receiving data...')
            data = s.recv()
            print('data=%s', (data))
            if not data:
                break
            # write data to a file
            f.write(data)

    f.close()
    print('Successfully get the file')