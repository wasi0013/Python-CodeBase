import sys
for _ in[0]*int(input()):
    input()
    f=1
    a=list(map(int,input().split()))
    for x in a:
        if a.count(x)>2:f=0
    print("Yes" if f else "No")
