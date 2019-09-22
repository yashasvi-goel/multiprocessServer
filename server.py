import socket
import sys
import json
from multiprocessing import Manager,Process

def human(Input):
    print("Human")

def check(Input,dic):
    print("Checking")
    if(Input in dic.keys()):
        return dic[Input]
    else:
        print("NOPE")
        return human(Input)

def response(conn,dic):
    try:
        while True:
            data=conn.recv(4096)
            if((data==bytes("close","utf-8"))or(data==bytes("","utf-8"))):
                print("proc returning")
                conn.close()
                return
            data=data.decode()
            print(data)
            res=check(data,dic)
            print(res)
            conn.send(bytes(res,"utf-8"))
    except:
        pass
    finally:
        conn.close()

if __name__=="__main__":

    serv=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    port=6534
    serv.bind(('localhost',port))
    serv.listen(5)
    print(f"listening on port:{port}")
    dic=Manager().dict()
    with open('responses.json','r') as filehandle:
        dic=json.load(filehandle)
    print(type(dic))
    while True:
        conn,addr=serv.accept()
        proc=Process(target=response,args=(conn,dic))#creating process
        proc.daemon=True
        proc.start()
#        proc.join()
    for p in multiprocessing.active_children():
        p.terminate()
        p.join()
