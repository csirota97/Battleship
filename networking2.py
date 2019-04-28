import socket

# Principles Of Programming Languages - CS314
# Final Project
# File: networking.py
# Names: Craig Sirota and Dov Kassai

#TCP VERSION

my_ip = socket.gethostbyname(socket.gethostname())
reciever_ip = ""

port = 15723

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))


#Sets target IP address for communications
def set_target (recv_addr):
    global reciever_ip, 
    reciever_ip = recv_addr

#Waits for incoming message of X length
def rec(bytes_in):
    data = sock.recv(bytes_in)
    return data.decode('utf-8')

#Waits for incoming message of X length and sets target IP address to sender
def rec_set_reciever(bytes_in):
    global reciever_ip, sock
    sock.bind((my_ip, port))
    sock.listen(1)
    sock, addr = sock.accept()
    sock.recv(bytes_in)
    reciever_ip = addr[0]
    return data.decode('utf-8')

#Sends message to target IP address
def send(data):
    print(reciever_ip+"")
    sock.send(data.encode('utf-8'))

#Sends message to local host 127.0.0.1
#def send_local(data):
#    sock.sendto(data.encode('utf-8'),('127.0.0.1',port))
