from sys import stdin,stdout
import math
n=int(input())
while(n>0):
    i=0
    l=[]
    while(i<n):
        x=int(input())
        l.insert(1,x)
        i+=1
    i=1
    l.sort()
    while(i<n):
        if(l[i]-l[i-1]>200): break
        i+=1
    if(i<n or ((1422-l[i-1]*2)>200)):print('IMPOSSIBLE')
    else: print('POSSIBLE')
    n=int(input())
