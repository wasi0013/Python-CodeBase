from sys import stdin
def gcd(a,b):
    c=a%b
    while c!=0:
        a=b
        b=c
        c=a%b
    return b
if __name__ == "__main__":
    for _ in [0]*int(stdin.readline().strip()):
        x,y=map(int,stdin.readline().strip().split())
        ans= x-y if x>y else y-x
        ans=ans//gcd(x,y)
        print(ans)

