from sys import stdin,stdout
a,b,c=map(int,stdin.readline().split())
while a!=0 or b!=0 or c!=0:
    n=abs(c-a)
    k=b*3
    if(n%b!=0):print("No accounting tablet")
    else:print(n//k if n%k==0 else n//k+1)
    a,b,c=map(int,stdin.readline().split())
