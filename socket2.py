import socket
from threading import Thread
host=socket.gethostname()
port=3000

print("host =",host)
s=socket.socket()

s.bind((host,port))

s.listen(1)
a,c=s.accept()
print("a =",a)
print("c =",c)


def send():
    while True:
        msg = input()
        a.send(msg.encode())
        

def recv():
    while True:
        msg = a.recv(1024)
        print(msg.decode())

t1 = Thread(target=send)        
t2 = Thread(target=recv)        


t1.start()
t2.start()