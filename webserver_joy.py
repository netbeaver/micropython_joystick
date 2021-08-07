#import move and lance
from move_pwm import *
#from lance import *

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

print('reading joy.html')
with open('test.html', "r") as myfile:
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
    #print("Content = %s" % str(request))
    request = str(request)
    print(request+'\n')
    
#    if request.find('/?CMD=forward') == 6:
#      forward()
#    elif request.find('/?CMD=back') == 6:
#      backward()
#    elif request.find('/?CMD=left') == 6:
#      left()
#    elif request.find('/?CMD=right') == 6:
#      right()
#    elif request.find('/?CMD=stop') == 6:
#      stop()
    # elif request.find('/?CMD=arm') == 6:
    #  arm()
    #elif request.find('/?CMD=disarm') == 6:
    #  disarm()
      
    #end change
    response = html
    cl.send(response)
    cl.close()
