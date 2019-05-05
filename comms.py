
#!/usr/bin/env python3

from networking import networking3 as net
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

addr, msg  = net.rec(1024)

if addr == "127.0.0.1":
    addr = "You"
else:
    addr = "Opponent"

print (addr + ": " + msg)


while not msg.upper() == "QUIT":
    addr, msg= net.rec(1024)

    if addr == "127.0.0.1":
        addr = "You"
    else:
        addr = "Opponent"
    print (addr + ": " + msg)

print("QUIT")
