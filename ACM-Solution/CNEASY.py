import sys,math
for _ in[0]*int(sys.stdin.readline().strip()):
    n=int(sys.stdin.readline().strip())
    i=0
    a=[]
    while i<n:
        s,x=sys.stdin.readline().strip().split(" ")
        a.insert(0,float(x))
        i+=1
    a.sort()
    low=a[n-1]-a[0]
    i=1
    while i<n:
        t=360.00-a[i]+a[i-1]
        low=min(t,low)
        i+=1
    print(int(math.ceil(low*12.0)))
    

