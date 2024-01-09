import socket               # Import socket module
from tkinter import filedialog
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 55556                 # Reserve a port for your service.


def openFile():
    filepath = filedialog.askopenfilename(initialdir="Bureau",
                                          title="Open file okay?",
                                          filetypes= (("Image","*.png"),
                                          ("all files","*.*")))
    return filepath

s.connect((host, port))
f = open(openFile(),'rb')
print ('Sending...')
l = f.read(1024)
while (l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print ("Done Sending")
s.shutdown(socket.SHUT_WR)
print (s.recv(1024).decode("utf8"))
s.close                     # Close the socket when done