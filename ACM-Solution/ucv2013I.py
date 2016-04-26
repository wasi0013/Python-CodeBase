import math
t,n=map(float,input().split())
while int(n) and int(t):
 x=2*t/((2-2*math.cos(3.1415926535897932384626433832795/n)))**.5
 print("%.2f"%x)
 t,n=map(float,input().split())
