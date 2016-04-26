import sys
def gcd(a,b):
    k=0
    while(b):
        a%=b
        k=a
        a=b
        b=k
    return a
def ncr(n,r):
    k= r if(r>n-r) else n-r
    m=n-k
    hr=lb=1
    i=k+1
    j=m
    while(i<=n and j>0):
        hr*=j
        lb*=i
        g=gcd(lb,hr)
        lb//=g
        hr//=g
        i+=1
        j-=1
    return lb
def main():
    for _ in [0]*int(input()):
        n,r=map(int,input().split())
        print(ncr(n-1,r-1))
    return 0
if __name__== "__main__":main()
