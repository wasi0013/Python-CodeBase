v=1
for T in[0]*int(input()):
    def M(p,q,r,s):return max(max(p,r)+max(q,s),max(p,q)+max(r,s))
    a,b,c,d=map(int,input().split())
    ans=max(max(M(a,b,c,d),M(a,c,b,d)),M(a,d,b,c))
    print("Case",v,':',ans)
    v+=1
    
    
