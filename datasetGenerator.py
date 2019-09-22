import json

d={}

while True:
    print("Enter keyword")
    s=input()
    if(s=="close"):
        with open('responses.json','w') as filehandle:
            json.dump(d,filehandle)
        break
    print("Enter Response")
    k=input()
    d[s]=k
