import socket
import queue

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',7877))
s.listen(5)

while True:
    conn,addr=s.accept()
    from_client=''
    while True:
        data=conn.recv(4096)
        print(data.decode())
        k=input()
        conn.send(bytes(k,"utf-8"))
    conn.close()
