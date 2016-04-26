import sys

for _ in [0]*int(sys.stdin.readline().strip()):
    s=0
    n=1
    x=int(sys.stdin.readline().strip())
    for _ in [0]*x:
        s+=x/n
        n+=1
    print('%.2f'%s)
