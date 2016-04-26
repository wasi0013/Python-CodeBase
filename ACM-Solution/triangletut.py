c=input
a=1
for _ in [0]*int(c()):
    x,y=map(int,c().split())
    s=1
    print("Case %d:"%a)
    a+=1
    while(s<=y):
        t=1
        while t<=s:
            print(x,end="")
            t+=1
        s+=1
        print()
