#!/usr/bin/env python3

from networking import networking2 as net
import time

while 1:
    print ("CONNECTING...")
    time.sleep(2)
    f = open("networking/config.svg", "r")
    m = f.read()
    print(m)
    if not m == "":
        net.reciever_ip = m
        break

print ("\n\nCONNECTED\n\n")

msg = input (":>")

net.send(msg)

while not msg.upper() == "QUIT":
    msg = input (":>")
    
    net.send(msg)
