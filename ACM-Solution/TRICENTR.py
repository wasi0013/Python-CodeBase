import sys
for x in[0]*int(sys.stdin.readline().strip()):
    d,a,b,c=map(float,sys.stdin.readline().split())
    ans1=d*a*1.5
    y=2/3*ans1/c
    x=2/3*ans1/b
    z=d*x*y/ans1/4
    ans2=4*z*z-(4/9)*(d*d+x*x+y*y)
    print("%.3f %.3f"%(ans1,ans2**.5 if ans2>0 else 0))
