import socket

host=socket.gethostname()
port=3000

print("host =",host)
s=socket.socket()

s.bind((host,port))

s.listen(1)
a,c=s.accept()
print("a =",a)
print("c =",c)

while True:
    msg=input("Enter message:-")
    
    a.send(msg.encode())
    if msg in ['bye','by']:
        break
    abc=a.recv(1024)
    if abc in ['bye','by']:
        break
    print(abc.decode())


