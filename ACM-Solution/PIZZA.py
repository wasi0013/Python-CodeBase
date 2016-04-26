x=y=z=s=0
for _ in[0]*int(input()):
 b,c=input().split('/')
 if b=='3':x+=1
 elif c=='2':y+=1
 elif c=='4':z+=1
n=y%2
t=z%4
z-=x
s+=x+(y-n)//2
if n:z-=2;s+=1
if z>0:s+=(z-t)//4
if t>0:s+=1
print(1+s)
