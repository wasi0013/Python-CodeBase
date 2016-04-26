import sys
l=0
for u in[0]*int(sys.stdin.readline().strip()):
    N,R=map(int,sys.stdin.readline().strip().split())
    s=c=set([])
    for t in[0]*R:
        x,y=map(int,sys.stdin.readline().strip().split())
        s.add(x)
        c.add(y)
    s=list(s).sort()
    c=list(c).sort()
    f=0
    for _ in range(N):
        
    print(('Scenario #%d:'%(l))+(' spied' if f else ' spying'))
    l+=1
