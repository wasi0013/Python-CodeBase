import re
a=int(input())
while(a):
    a-=1
    b=input()
    b=input()
    b=b.replace(" ","")
    b=re.split("(\d+)",b)
    b.remove("")
    s=int(b[0])
    t=len(b)
    c=1
    while(True):
        if(b[c]=="+"):
            s+=int(b[c+1])
            c+=2
        elif(b[c]=="-"):
            s-=int(b[c+1])
            c+=2
        elif(b[c]=="/"):
            s//=int(b[c+1])
            c+=2
        elif(b[c]=="*"):
            s*=int(b[c+1])
            c+=2
        elif(b[c]=="="):
            break
    print(int(s))
