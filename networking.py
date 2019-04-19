import socket

my_ip = socket.gethostbyname(socket.gethostname())
reciever_ip = ""

port = 15721

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

def set_target (recv_addr):
    global reciever_ip
    reciever_ip = recv_addr

def rec(bytes_in):
    data = sock.recv(bytes_in)
    return data.decode('utf-8')

def rec_set_reciever(bytes_in):
    data, addr = sock.recvfrom(bytes_in)
    reciever_ip = addr[0]
    return data.decode('utf-8')

def send(data):
    sock.sendto(data.encode('utf-8'),(reciever_ip,port))

def send_local(data):
    sock.sendto(data.encode('utf-8'),('127.0.0.1',port))
