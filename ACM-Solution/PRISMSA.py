import sys
for _ in [0]*int(sys.stdin.readline().strip()):
    v=4*float(sys.stdin.readline().strip())
    a=pow(v,0.3333333333333333)
    x=a*a*1.7320508075688772
    print("%.10f"%((x/2)+(3*a*(v/x))))
