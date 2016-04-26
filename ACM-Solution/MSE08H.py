from sys import stdin ,stdout
x=[]

   stdin.readline()
   n=list(map(int,stdin.readline().split()))
   n.sort()
   q=n[::]
   i=1
   t=len(n)
   ans=1
   while i<t:
      if q[i]==n[i]:
         j=i
         while j<t:
            if n[j]%n[i]==0:
               q[j]//=n[i]
               q[j]*=n[i]-1
            j+=1
      ans=(ans*q[i])%1000000007
      i+=1
   x.append("%d"%ans)
except:print("\n".join(x))
