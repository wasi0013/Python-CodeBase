import sys
for i in [0]*int(input()):
    b=int(input())
    if b==1 or b==2: print(0)
    #elif b==4:print(1)
    else :print (((b-b//2)**2)%b) if b%2 else print (((b-b//2-1)**2)%b) 
