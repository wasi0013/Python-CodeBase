for _ in[0]*int(input()):
    a,b=map(int,input().split())
    q,r=divmod(a,b-1)
    if r==0:q-=1
    print(a+q)
