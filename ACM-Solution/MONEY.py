from math import floor
t=1
pr,rt,per=map(float,input().split())
while pr or rt or per:
        ans=pr
        for time in range(0,int(per)):ans+=floor(ans*rt/per)/100
        print("Case %d. $%.2f at %.2f%% APR compounded %d times yields $%.2f"%(t,pr,rt,per,ans)) 
        pr,rt,per=map(float,input().split())
        t+=1
