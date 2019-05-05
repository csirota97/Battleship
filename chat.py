#!/usr/bin/env python3

from networking import networking2 as net
import time

while 1:
    print ("CONNECTING...")
    time.sleep(2)
    from networking import config as c
    print (c.reciever_ip)
    if c.reciever_ip:
        break


from networking import config as c

print ("\n\nCONNECTED\n\n")

msg = input (":>")

net.send(msg)

while not msg.upper() == "QUIT":
    msg = input (":>")
    
    net.send(msg)
