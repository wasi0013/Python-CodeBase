import sys,math
a,b=map(float,input().split())
r=(a+4+math.sqrt((a+4)**2-16*(a+b)))/4
c=(a+b)/r
print('%.f %.f'%(r,c)) if (r>c) else print('%.f %.f'%(r,c))
