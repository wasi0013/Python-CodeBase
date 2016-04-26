def psychon(n):
    a,b=0,0
    div=2
    while div*div<=n:
        trigger = False
        c=0
        while not n%div:
            n//=div
            c+=1
            trigger =True
        if trigger:
            if c%2:b+=1
            else:a+=1
        div+=1
    b+=n>1
    return "Ordinary Number" if a<b else "Psycho Number"
            
from sys import stdin,stdout    
#a,*box=map(int,stdin.buffer.readlines())
box=[3,4]
output=[]
for ins in range(int(stdin.readline())):   output.append(psychon(int(stdin.readline()))

print("\n".join(output))
