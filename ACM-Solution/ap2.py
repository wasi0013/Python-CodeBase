from sys import stdin
for _ in [0]*int(stdin.readline().strip()):
    x,y,z=map(int,stdin.readline().strip().split())
    n=(2*z)//(x+y)
    print(n)
    d=(y-x)//(n-5)
    a=x-(2*d)
    s=0
    while(s<n):
        s+=1
        print(a,end = " ")
        a+=d
    
    print()

