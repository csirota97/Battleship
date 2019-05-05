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

#Sends message to target IP address
def send(data):
    sock.sendto(data.encode('utf-8'), (reciever_ip, port-1))
    sock.sendto(data.encode('utf-8'),('127.0.0.1',port-1))

#Sends message to local host 127.0.0.1
def send_local(data):

