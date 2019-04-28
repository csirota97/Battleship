
# Principles Of Programming Languages - CS314
# Final Project
# File: server.py
# Names: Craig Sirota and Dov Kassai

# TCP SERVER

import socket


my_ip = socket.gethostbyname(socket.gethostname())
port = 15723

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((my_ip, TCP_PORT))
s.listen(1)
conn, addr = s.accept()

def rec(bytes_in):
    return conn.recv(bytes_in)

def send(msg):
    conn.send(msg)

def close():
    conn.close()

