import sys
for _ in [0]*int(input()):
    a,b,c=map(int,input().split())
    a=abs(a)
    if b>0: z=a*a-2*abs(b)
    else: z=a*a+2*abs(b)
    print(abs(z))
