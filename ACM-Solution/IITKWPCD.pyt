import sys
n=1299710
s=range(0,n+1);s[1]=0;b=2
while b*b<=n:s[2*b:n:b]=[0]*((n-1)//b-1);b+=1
p=[x for x in s if x]
for i in sys.stdin:print p[int(i)-1]

