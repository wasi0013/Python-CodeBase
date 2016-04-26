def j(n,k):
   r=0
   i=2
   while i<=n:
     r+=((i+k+1)+k-1)%i+1;
     i+=1
   return r+1
for _ in[0]*int(input()):print(j(int(input()),1))
