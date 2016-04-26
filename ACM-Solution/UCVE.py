for i in[0]*int(input()):
    a,b=map(int,input().split())
    if a<=b: print(0)
    else:
        a//=b
        print(a-1)
