r=res1=res2=0.0
eps=0.00000000100000000000
pi=3.141592653589793
while True:
    w,h=map(float,input().split())
    if(w+h)<=0.0: break
    r=min(w/2.000000,h/(2.00000000*pi+2.0))
    res1=pi*r*r*w
    r=w/(2.0*pi)
    res2=pi*r*r*(h-2.0*r)
    print("%.3f"%((max(res1,res2)+eps)))
