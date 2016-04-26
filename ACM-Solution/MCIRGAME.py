from sys import stdin,stdout
from math import factorial as f
out=[]
while True:
   i=int(input())
   if(i==-1):break
   else: out.append("%d"%(f(2*i)/(f(i)*f(i+1))))
print("\n".join(out))        
