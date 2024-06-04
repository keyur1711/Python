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
print("d =",d)
print("e =",e)


def send():
    while True:
        msg = d.recv(1024)
        #msg = input()
        a.send(msg)
        

def recv():
    while True:
        msg = a.recv(1024)
        d.send(msg)

t1 = Thread(target=send)        
t2 = Thread(target=recv)        


t1.start()
t2.start()