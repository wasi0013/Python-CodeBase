import sys
a,b=map(int,sys.stdin.readline().strip().split())
while a and b:
    s=list(map(int,sys.stdin.readline().strip().split()))
    t=list(map(int,sys.stdin.readline().strip().split()))
    for x in s:
      for c,k in enumerate(t):
        if x==k:
            t[c]=0
            break
    print(sum(s)+sum(t))
    a,b=map(int,sys.stdin.readline().strip().split())
    
