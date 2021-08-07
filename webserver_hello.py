#import move and lance
#from move import *
#from lance import *

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

html = '<h1>Hello</h1>'

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    
    #change
    request = cl.recv(1024)
    #print("Content = %s" % str(request))
    
    #request = str(request)
    
      
    #end change
    response = html
    cl.send(response)
    cl.close()
