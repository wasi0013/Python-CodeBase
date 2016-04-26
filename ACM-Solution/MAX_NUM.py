for _ in [0]*int(input()):
    n,k=map(str,input().split())
    if int(k)==int(n): print()
    elif int(k)==0:print(n)
    else:
        d=dict()
        count=1
        for i in n:
            d[count]=i
            count+=1
        ls=sorted(d.values())
        c=0
        for n in ls:
            if c==int(k): break
            else :ls[c]='';c+=1
        ks=''
        for l,b in sorted(d.items()):
            ks=ks+b
        print(ks,ls)
        ans=''
        for c in ks: 
            if c in ls:
                ans+=c
        print(ans)
#not solvable till now!
