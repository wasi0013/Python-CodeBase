for _ in range(int(input())):
    input()
    x,y=map(float,input().split())
    a,b,r=map(float,input().split())
    tx=52-x
    ty=3.66-y
    zy=-3.66-y
    a2=tx*tx+ty*ty
    a1=tx*tx+zy*zy
    n=2*(tx*(x-a)+ty*(y-b))
    t=2*(tx*(x-a)+zy*(y-b))
    c=x*x+y*y+a*a+b*b-r*r-2*(a*x+b*y)
    d=n*n-4*a2*c
    e=t*t-4*a1*c
    if(d<0 and e<0):
        print('No Goal!')
    else :print('Goal!')
