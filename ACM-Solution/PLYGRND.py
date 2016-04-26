import sys
s=int(input())
while s:
    x=list(map(float,input().split()))
    x.sort()
    if s==1:
        print("NO")
    else:
     tot=f=0
     i=len(x)
     for c,v in enumerate(x):
        tot+=v
        if c==i-1:break
        if(tot>=x[c+1]):
            f=1
            break
     print("YES"if f else"NO")
    s=int(input())
