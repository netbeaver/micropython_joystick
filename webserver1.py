#import move and lance
#from move import *
#from lance import *

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

print('reading webpage joy.html')
with open('joy.html', "r") as myfile:
    html=myfile.read()
myfile.close()

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    
    #change
    request = cl.recv(1024)
    print("Content = %s" % str(request))
    #request = str(request)
    
      
    #end change
    response = html
    cl.send(response)
    cl.close()
