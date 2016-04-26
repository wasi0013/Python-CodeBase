import sys
c=1
for i in [0]*int(sys.stdin.readline().strip()):
    t=sys.stdin.readline().strip()
    n=a=0
    line=list(map(int,sys.stdin.readline().strip().split()))
    for x in line:
        n=n^x
    for x in line:
        t=n^x
        if(t<x):a+=1
    print("Case %d:"%c,a)
    c+=1
