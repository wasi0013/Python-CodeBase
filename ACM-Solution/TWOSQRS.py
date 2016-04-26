import sys
for _ in [0]*int(input()):
    n=int(input())
    i,c,flag=2,0,1
    while i*i<=n:
        while n%i==0:
            c+=1
            n//=i
        if i%4==3 and c%2==1:
            flag=0
            break
        i+=1
    if i%4==3: flag=0
    print('Yes' if flag else 'No')
