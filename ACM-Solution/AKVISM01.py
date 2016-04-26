for _ in [0]*int(input()):
    a,b,n=map(int,input().split())
    d=b-a
    print(d,int(n/2*(2*a+(n-1)*d)))
    
