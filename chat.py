from networking import networking2 as net

print ("\n\nCHAT OPEN\n\n")

msg = ""

while not msg.upper() == "QUIT":
    msg, addr = net.rec(1024)
    print(addr[0] + ":\t" + msg)
    

