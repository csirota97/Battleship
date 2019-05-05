#!/usr/bin/env python3

import socket

# Principles Of Programming Languages - CS314
# Final Project
# File: networking.py
# Names: Craig Sirota and Dov Kassai

#UDP Version

my_ip = socket.gethostbyname(socket.gethostname())
reciever_ip = ""

port = 15721

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))


#Sets target IP address for communications
def set_target (recv_addr):
    global reciever_ip
    reciever_ip = recv_addr

    f = open("networking/config.svg", "w")
    f.write(recv_addr)
    f.close()

#Waits for incoming message of X length
def rec(bytes_in):
    data = sock.recv(bytes_in)
    return data.decode('utf-8')

#Waits for incoming message of X length and sets target IP address to sender
def rec_set_reciever(bytes_in):
    global reciever_ip
    data, addr = sock.recvfrom(bytes_in)
    reciever_ip = addr[0]
    f = open("networking/config.svg", "w")
    f.write(addr[0])
    f.close()
    return data.decode('utf-8')

#Sends message to target IP address
def send(data):
    sock.sendto(data.encode('utf-8'), (reciever_ip, port))

#Sends message to local host 127.0.0.1
def send_local(data):
    sock.sendto(data.encode('utf-8'),('127.0.0.1',port))
