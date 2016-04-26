def arc(x,dig):
    p=tot=10**(11+dig)/x;n=3;sign=term=-1
    while term:
        p /= x*x
        term=p / n
        n+=2
        tot+=sign*term
        sign=-sign
    return tot/100
def pi(dig):
    pi=4*(4*arc(5, dig) - arc(239, dig))
    return pi/10
print '3.'+str(pi(97402))[1::]
