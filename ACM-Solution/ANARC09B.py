#from fractions import gcd
def gcd(a,b):return gcd(b,a%b) if b else a
x,y=map(int,input().split())
while x or y:
    div=gcd(x,y)
    ans=(x*y)//div
    ans//=div
    print(ans)
    x,y=map(int,input().split())
    
