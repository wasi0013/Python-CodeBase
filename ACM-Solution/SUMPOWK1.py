import sys
for _ in [0]*int(input()):
    a,b=map(int,input().split())
    c=0
    d=0
    while(c<=a):
        d+=pow(c,b)
        c+=1
    print(d)
