import sys,math
v,h=map(float,input().split())
while h>=0 and v>=0:
    print('%6f'%(v*v/9.8/math.tan(math.asin(v/math.sqrt(2*9.8*h+2*v*v)))))
    v,h=map(float,input().split())
