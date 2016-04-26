from sys import stdin,stdout
from math import sqrt
for _ in [0]*int(stdin.readline().strip()):
    a,b,c,d=map(float,stdin.readline().strip().split())
    sur=(a+b+c+d)/2
    print('%.2f'%sqrt((sur-a)*(sur-b)*(sur-c)*(sur-d)))
