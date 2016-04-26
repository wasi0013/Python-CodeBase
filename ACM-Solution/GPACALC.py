for i in[0]*int(input()):
    s=0
    u=0
    t="00000EDCBAS"
    for o in [0]*int(input()):
        x,y=map(str,input().split())
        s+=int(x)*t.find(y)
        u+=int(x)
    print("%.2f"%round(s/u,2))
