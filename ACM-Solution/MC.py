def modified_lcs(a,b,c,d):
    dp=[[0]*(d+1)]*(c+1)
    for i in range(1,c+1):
        for j in range(1,d+1):
            if b[j-1]==a[i-1]:dp[i][j]=dp[i-1][j-1]+1
            elif dp[i-1][j]>=dp[i][j-1]:dp[i][j]=dp[i-1][j]
            else:dp[i][j]=dp[i][j-1]
    precious_result=dp[c][d]
    return precious_result
from sys import stdin,stdout
t=[]
while True:
    x=stdin.readline().strip()
    if x=='#':break
    y=stdin.readline().strip()
    a=len(x)
    b=len(y)
    v=modified_lcs(x,y,a,b)
    t.append("%d"%(15*(a-v)+30*(b-v)))
print("\n".join(t))
