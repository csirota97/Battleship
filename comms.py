
#!/usr/bin/env python3

from networking import networking3 as net
import time

while 1:
    print ("CONNECTING...")
    time.sleep(2)
    from networking import config as c
    if c.reciever_ip:
        break


from networking import config as c

print ("\n\nCONNECTED\n\n")

msg, addr = net.rec(1024)

print (addr + ":\t" + msg)

while not msg.upper() == "QUIT":
    msg, addr = net.rec(1024)

    print (addr + ":\t" + msg)
