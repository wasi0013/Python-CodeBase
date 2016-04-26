import sys
for _ in [0]*int(sys.stdin.readline()):
    c,n=map(int,sys.stdin.readline().strip().split())
    n-=1
    d=[1,2,3,4,5,6,7,8,9,10]
    while n:
        n-=1
        i=1
        while i<10:
            d[i]+=d[i-1]
            i+=1
    print(c,d[9])
