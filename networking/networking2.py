#!/usr/bin/env python3

import socket

# Principles Of Programming Languages - CS314
# Final Project
# File: networking2.py
# Names: Craig Sirota and Dov Kassai

#UDP Version

my_ip = socket.gethostbyname(socket.gethostname())
reciever_ip = ""

port = 15722

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

#Sends message to target IP address
def send(data):
    sock.sendto(data.encode('utf-8'),('127.0.0.1',port+1))
    sock.sendto(data.encode('utf-8'), (reciever_ip, port+1))
