try:
    while 1:
        x=int(input())
        a=[]
        for t in list(map(int,input().split())):a.append(abs(t))
        a.sort()
        s=0
        for n in a:
           if n==1: s+=1
           elif n>0:
               if(s==1):s+=n
               elif s>0:s*=n
               else: s=n;
        print(-s if s>0 else s)
               
except:
    pass
