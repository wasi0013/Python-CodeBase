import sys
try:
    while 1:
        x=input()
        t=x[0]
        ans=x[0]
        s=[]
        for i in x[1::]:
           if i==t:
               ans+=i
           else:
               l=len(ans)
               s.append(ans if l<=3 else "%d!%c"%(l,ans[0]))
               ans=t=i
        s.append(ans if len(ans)<=3 else "%d!%c"%(len(ans),ans[0]))
        

        print("".join(s))
except: pass
