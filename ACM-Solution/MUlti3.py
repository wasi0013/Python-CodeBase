from sys import stdin
for _ in [0]*int(stdin.readline().strip()):
    x=int(stdin.readline().strip())
    print(x,"is a multiple of 3" if (x%3==0) else "is not a multiple of 3" )

