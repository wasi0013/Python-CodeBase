import sys

g,b=map(int,sys.stdin.readline().split())
while g>-1 and b>-1:
    if g>b:
        print((g+b)//(b+1))
    else:
        g^=b
        b^=g
        g^=b
        print((g+b)//(b+1))
    g,b=map(int,sys.stdin.readline().split())
