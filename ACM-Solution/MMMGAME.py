import sys
for _ in[0]*int(input()):
    n=int(input())
    c=0
    a=[]
    for x in map(int,input().split()):
        a.append(x)
        if x==1: c+=1
    ans=a[0]
    if c==n:print("Brother" if n%2 else "John")
    else :
        for i in range(1,n):ans^=a[i]
        print("John"if ans else "Brother" )
            
        
        
