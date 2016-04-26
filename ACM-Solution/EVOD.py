import sys
a,b=map(int,input().split())
while a!=0 and b!=0:
    s=a*b+(b-a)*(b-a+1)//2
    print("Even" if s%2==0 else "Odd")
    a,b=map(int,input().split())
