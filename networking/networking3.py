#!/usr/bin/env python3

import socket

# Principles Of Programming Languages - CS314
# Final Project
# File: networking.py
# Names: Craig Sirota and Dov Kassai

#UDP Version

my_ip = socket.gethostbyname(socket.gethostname())
reciever_ip = ""

port = 15723

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))


#Waits for incoming message of X length
def rec(bytes_in):
    data, addr = sock.recvfrom(bytes_in)
    return addr[0], data.decode('utf-8')

