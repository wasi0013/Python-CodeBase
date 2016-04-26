import sys
while 1:
    n=int(input())
    if n<=0:break
    x=list(map(int,input().split()))
    a=1
    i=0
    for i in range(0,n):x[i]-=1
    for i in range(0,n):
        if(i!=x[x[i]]):a=0;break
    print("ambiguous" if a else "not ambiguous")
