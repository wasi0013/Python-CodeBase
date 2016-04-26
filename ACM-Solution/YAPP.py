import sys

for u in[0]*int(sys.stdin.readline().strip()):
 n=int(sys.stdin.readline().strip())-1
 x,ans=[2,1]
 while n:
     n,m=divmod(n,2)
     if m!=0:ans*=x
     x*=x
 print(ans)
