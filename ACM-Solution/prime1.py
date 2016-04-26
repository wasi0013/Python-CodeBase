import sys
def prime(n):
 s=[1]*n
 for i in range(3,int(pow(n,.5)),2):
  if s[i]:
     s[i*i::2*i]=[0]*((n-i*i-1)/(2*i)+ 1)
 return [2]+[i for i in range(3,n,2) if s[i]]
def seg_sieve(a,b):
size=b-a+1
m=[1 for x in range(0,size)]
for prime in primelist:
if(a%prime==0):i=0
else:
 i=prime-a%prime
while i<size:
 m[i]=0
 i+=prime
return sum(m)

