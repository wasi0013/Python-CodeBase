import sys
x=1
for i in [0]*int(input()):    
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    s=a/2
    strs=('%.4f' %s)[:-1]
    print('Case %d:'%x,strs)
    x+=1
