import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 55556                 # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
f = open('torecv.png','wb')
s.listen(5)                 # Now wait for client connection.
print ("Server Started")
while True:
    c, addr = s.accept()     # Establish connection with client.
    print ('Got connection from'), addr
    print ("Receiving...")
    l = c.recv(1024)
    while (l):
        print ("Receiving...")
        f.write(l)
        l = c.recv(1024)
    f.close()
    print ("Done Receiving")
    open('torecv.png')
    c.send(bytes('Thank you for connecting !!','utf8'))
    c.shutdown(1)                # Close the connection
    break