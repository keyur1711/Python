import socket
from threading import Thread
host=socket.gethostname()
port=3000

print("host =",host)
s=socket.socket()

s.bind((host,port))

s.listen(2)
a,c=s.accept()
d,e=s.accept()
print("a =",a)
print("c =",c)


def send():
    while True:
        msg = input()
        a.send(msg.encode())
        d.send(msg.encode())
        
       
def recv():
    while True:
        
        msg = a.recv(1024)
        print(msg.decode())
        
        msg2 = d.recv(1024)
        print(msg2.decode())
        
        a.send(msg2)
        d.send(msg)
        
t1 = Thread(target=send)        
t2 = Thread(target=recv)        


t1.start()
t2.start()