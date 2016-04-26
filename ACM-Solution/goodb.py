from sys import stdin
from math import factorial 
x,y,z,r= map(int,stdin.readline().strip().split())
s=(factorial(x))//(factorial(y)*(factorial(z))*(factorial(r)))
print(s%1000000007)
