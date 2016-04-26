import sys,math
from decimal import *
getcontext().prec=10000
for _ in[0]*int(input()):
    a,b,c=map(int,input().split())
    s=a*b*c
    st="%.100f"%(a/(a*b+b*c+c*a+Decimal(2)*Decimal(math.sqrt(s*(a+b+c))))*b*c)
    print(st)
