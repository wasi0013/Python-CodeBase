for _ in [0]*int(input()):
    x=input()
    y=list(map(int,input().split()))
    t=y[int(input())-1]
    y.sort()
    print(y.index(t)+1)
