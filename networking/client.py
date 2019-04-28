import socket

# Principles Of Programming Languages - CS314
# Final Project
# File: networking.py
# Names: Craig Sirota and Dov Kassai

#TCP CLIENT VERSION

my_ip = socket.gethostbyname(socket.gethostname())
reciever_ip = ""

port = 15723
s = ''

def setup():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((my_ip, port))

def send(msg):
    s.send(MESSAGE)

def rec(bytes_in):
    return s.recv(BUFFER_SIZE)

def set_target(recv_addr):
    global reciever_ip, sock
    reciever_ip = recv_addr


def close():
    s.close()

#print "received data:", data
