import socket

# Principles Of Programming Languages - CS314
# Final Project
# File: networking.py
# Names: Craig Sirota and Dov Kassai

#TCP CLIENT VERSION

my_ip = socket.gethostbyname(socket.gethostname())
reciever_ip = ""

port = 15723


def setup():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', port))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((my_ip, port))

def send(msg):
    s.send(MESSAGE)

def rec(bytes_in):
    data = s.recv(BUFFER_SIZE)

def set_target(recv_addr):
    global reciever_ip, sock
    sock.connect((recv_addr, port))
    reciever_ip = recv_addr


def close():
    s.close()

#print "received data:", data
