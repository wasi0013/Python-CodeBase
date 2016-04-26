import sys,math
for _ in [0]*int(input()):
   x,b=map(int,input().split())
   a=len(str(x))
   print(a)
   s=(a-10//9)*pow(10,a-1)-int('1'*(a))
   print(s)
