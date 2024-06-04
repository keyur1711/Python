import socket

host=socket.gethostname()
port=3000

s=socket.socket()

s.connect((host,port))
while True:

    msg = s.recv(1024)

    print(msg.decode())
    
    if msg in ['bye','by']:
        break
    message=input("Enter Message:-")
    if message in ['bye','by']:
        break
        
    s.send(message.encode())
    
    