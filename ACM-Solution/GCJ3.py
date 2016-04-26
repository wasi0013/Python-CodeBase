import sys,re
for _ in [0]*int(input()):    
    N =int(input())
    r=0
    s=1
    b=input()
    b=re.split("(\d+)",b)
    for x in b:
        if x.isnumeric():
            if(int(x)&1):
                r=r^s
            s+=1            
    print("Hanks Wins" if(r==0) else "Tom Wins")
    
