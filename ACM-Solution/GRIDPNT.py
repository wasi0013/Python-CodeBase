for _ in[0]*int(input()):
    a,b,c=map(int,input().split())
    i=0
    while i<=a:
        r=(i*b)//c+1
        if r<=a:x=r;y=i
        i+=1
    print(x,y)
