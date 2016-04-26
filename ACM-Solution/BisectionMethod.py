def f(x):    return x*x-5*x+6

x1,x2,tolerance_value=map(float,input().split())
if f(x1)*f(x2)<0:
    x3=(x1+x2)/2
    while f(x3)!=0 or( abs(x1-x2)>tolerance_value):
        if(f(x3)*f(x1)<0):x2=x3
        else : x1=x3
        x3=(x1+x2)/2
    print("the root is ",x3)
    
else:    print("There is no root")
