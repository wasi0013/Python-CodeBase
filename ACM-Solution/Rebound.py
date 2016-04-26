import sys,math
for cases in [0]*int(sys.stdin.readline().strip()):    
    x,y,z=map(int,sys.stdin.readline().strip().split())
    tmp=(x*x)+(y*y)+(y*z)<<1
    root=int(math.sqrt(tmp))
    if root*root == tmp:
        m=(z*(root+x))<<1
        n=((z<<1)+y)<<1
        print("Not this time." if(m%n) else "%d"%(m//n))
    else:
        print("Not this time.")
