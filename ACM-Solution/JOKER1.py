from sys import stdin,stdout
for _ in [0]*int(stdin.readline()):
    ans,cond=1,False
    n=int(stdin.readline())
    maxn=list(map(int,stdin.readline().strip().split()))
    maxn.sort()
    i=n-1
    while(i>=0):
        maxn[i]-=i
        if maxn[i]<1:
            cond=True
            break;
        ans=(ans*maxn[i])
        i-=1
    print(0) if cond else print(ans%1000000007)
    print('Kill Batman')
    
