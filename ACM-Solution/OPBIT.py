from sys import stdin,stdout

out=[]

for _ in range(int(stdin.readline())):

   a,b=map(int,stdin.readline().split())

   sa=int(a**.5)
   sb=int(b**.5)

   lr=rr=(sa+1)**2-sa*sa
   for i in range(sa+1,sb):

      lr&=(i+1)**2-i*i
      rr^=(i+1)**2-i*i

   out.append("%d"%(lr&rr))

print("\n".join(out))   
