from networking import networking2 as net
import time

while net.reciever_ip == "":
    print("CONNECTING...")
    time.sleep(2)


print ("\n\nCONNECTION SUCCESSFUL\n\n")
msg = input("What would you like to say?\n")

while not msg.upper() == "QUIT":
    net.send(msg)
    net.send_local(msg)

    msg = input("What would you like to say?\n")