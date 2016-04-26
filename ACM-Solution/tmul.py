import sys
for _ in [0]*int(input()):
    a,b=map(int,input().split())
    if (a>b):
        c=b
        while(a>1):
            b+=c
            a-=1
        print(b)
    else:
        c=a
        while(b>1):
            a+=c
            b-=1
        print(a)
