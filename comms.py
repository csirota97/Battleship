
#!/usr/bin/env python3

from networking import networking3 as net
import time

while 1:
    print ("CONNECTING...")
    time.sleep(2)
    f = open("networking/config.py", "r")
    m = f.read()
    print(m)
    if not m == "":
        net.reciever_ip = m
        break


print ("\n\nCONNECTED\n\n")

msg, addr = net.rec(1024)

print (addr + ":\t" + msg)

while not msg.upper() == "QUIT":
    addr, msg= net.rec(1024)

    if addr == "127.0.0.1":
        addr = "You"
    else:
        addr = "Enemy"
    print (addr + ": " + msg)
