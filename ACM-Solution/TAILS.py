a=list(map(int,input().split()))
c=x=y=0
for i in a:
    if i^x:c,x,y=c+1,y^1,1        
    else:x,y=y,0
ans=1048576 if x else c 
if a[0]:
    a[0:2]=0,a[1]^1
    c=x=y=0
    for i in a:
        if i^x:c,x,y=c+1,y^1,1        
        else:x,y=y,0
    ans2=(1048576 if x else c)+1
    ans=min(ans,ans2)
print(ans)
