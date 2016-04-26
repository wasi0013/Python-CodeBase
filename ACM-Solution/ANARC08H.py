from sys import stdin,stdout
def jos(n,k):
   r=0
   for i in range(2,n+1):r=(r+k)%i
   return r+1
x=[]
a,b=map(int,input().split())
while a or b:
    x.append("%d %d %d"%(a,b,jos(a,b)))
    a,b=map(int,input().split())
print("\n".join(x))        
