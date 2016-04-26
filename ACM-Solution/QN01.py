from sys import stdin,stdout
out=[]
n=int(input())
b=list(map(int,input().split()))
high,start,end=-1,1,1
for i,v in enumerate(b):
   tmp,val=i,v
   if high<val:high,start,end=val,tmp,i
   c=i+1
   while c<n:
      val^=b[c]
      if high<val:high,start,end=val,tmp,c
      c+=1
out.append("%d\n%d %d"%(high,start+1,end+1))
print("\n".join(out))        
