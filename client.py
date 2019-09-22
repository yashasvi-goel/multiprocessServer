import socket

s=socket.socket()
s.connect(('localhost',6534))
while True:
    data=input()
    data=data.lower()
    if(data=="close"):
        break
    s.send(bytes(data,"utf-8"))
    d=s.recv(4096)
    d=d.decode()
    if(d==''):
        continue
    print(d)
