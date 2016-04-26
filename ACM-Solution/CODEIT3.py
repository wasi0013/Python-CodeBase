import sys
for _ in [0]*int(input()):
    d=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    t=[0,3,2,5,0,3,5,1,4,6,2,4]
    ds,ms,ys=map(int,input().split())
    ys-= ms<3
    print(d[(ds+t[ms-1]+ys//400+ys//4+ys-ys//100)%7])
