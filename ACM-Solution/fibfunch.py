def fib(n):
    if n==0:return (0,1)
    else:
        x,y=fib(n//2)
        c=(x*(2*y-x))%1000000007
        d=(y*y+x*x)%1000000007
        if n&1: return (d,c+d)
        else: return (c,d)
for i in range(int(input())):
    x,y=map(int,input().split())
    print((fib(y+2)[0]-fib(x+1)[0]+1000000007)%1000000007)
