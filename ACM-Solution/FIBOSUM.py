def fib(n):
    if n==0:return (0,1)
    else:
        x,y=fib(n//2)
        c=(x*(2*y-x))%1000000007
        d=(y*y+x*x)%1000000007
        if n&1: return (d,c+d)
        else: return (c,d)

print(fib(1000)[0])
from sys import stdin,stdout
def main():
    o=[]
    a,*b=map(bytes,stdin.buffer.readlines())
    for i in b:
      x,y=map(int,i.split())
      o.append("%d"%((fib(y+2)[0]-fib(x+1)[0]+1000000007)%1000000007))
    stdout.write("\n".join(o))
if __name__=="__main__":main()
