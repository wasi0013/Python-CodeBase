import math
case=0
rad=math.pi/180
test=int(input())
D,L,HA,HB,ERR=map(float,input().split())
for _ in [0]*test:
    a,b,c,d=map(float,input().split())
    if a>0 and b>0 and c>0 and d>90 and a<90 and b<90 and c<90 and d<180:
        ga=c*rad
        de=(180-d)*rad
        h=math.tan(ga)*(D*math.tan(de)/(math.tan(de)+math.tan(ga)))
        h1=HA+h/math.sin(ga)*math.tan(a*rad)
        hr=HB+h/math.sin(de)*math.tan(b*rad)
        if abs(h1-hr)>ERR:print(case,"ERROR")
        else :print(case,int(.5+(h1+hr)/2))
    else :print(case,"DISQUALIFIED")
    case+=1
