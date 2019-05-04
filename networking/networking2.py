#!/usr/bin/env python3

import socket
from networking import config as c

# Principles Of Programming Languages - CS314
# Final Project
# File: networking.py
# Names: Craig Sirota and Dov Kassai

#UDP Version

my_ip = socket.gethostbyname(socket.gethostname())

port = 15722

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
except OSError:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port+1))

#Waits for incoming message of X length
def rec(bytes_in):
    data, addr = sock.recvfrom(bytes_in)
    return data.decode('utf-8'), addr[0]

#Sends message to target IP address
def send(data):
    sock.sendto(data.encode('utf-8'), (c.reciever_ip, port))


#Sends message to local host 127.0.0.1
def send_local(data):
    sock.sendto(data.encode('utf-8'),('127.0.0.1',port))
