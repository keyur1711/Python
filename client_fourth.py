import socket
import socket
from threading import Thread
host=socket.gethostname()
port=3000

s=socket.socket()

s.connect((host,port))

def send():
    while True:
        msg = input()
        s.send(msg.encode())
        

def recv():
    while True:
        msg = s.recv(1024)
        print(msg.decode())
        

t1 = Thread(target=send)        
t2 = Thread(target=recv)        


t1.start()
t2.start()