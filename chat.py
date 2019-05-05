#!/usr/bin/env python3

from networking import networking2 as net
import time

while 1:
    print ("CONNECTING...")
    time.sleep(2)
    f = open("networking/config.py", "r")
    m = f.read()
    print(m)
    if f.read():
        net.reciever_ip = m
        break


from networking import config as c

print ("\n\nCONNECTED\n\n")

msg = input (":>")

net.send(msg)

while not msg.upper() == "QUIT":
    msg = input (":>")
    
    net.send(msg)
