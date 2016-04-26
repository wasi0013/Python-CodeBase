import sys
t=1
for u in[0]*int(sys.stdin.readline().strip()):
    N=int(sys.stdin.readline().strip())
    if N==0:
        print('Case %d:'%(t),0)
        input()
        t+=1
        continue
    if N==1:
        print('Case %d:'%(t),int(input()))
        t+=1
        continue
    s=list(map(int,sys.stdin.readline().strip().split()))
    dp=[s[0],s[1]]
    for c,x in enumerate(s):
        if(c<2):continue
        dp.insert(c,max(x+dp[c-2],dp[c-1]))
    print('Case %d:'%(t),dp[N-1])
    t+=1
