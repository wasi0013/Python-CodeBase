import sys
for _ in [0]*int(sys.stdin.readline().strip()):
    n= int(sys.stdin.readline().strip())
    print('Yes' if(n%252==0) else 'No' ,end=" ")
    print('Yes' if(n%525==0) else 'No')
