while True:
    a,b=input().strip().split()
    if(a[0]=="*"):break
    cnt=ans=0
    for c,x in enumerate(a):
        if(a[c]==b[c]):cnt=0
        else:
            if cnt==0:ans+=1
            cnt+=1
    print(ans)
