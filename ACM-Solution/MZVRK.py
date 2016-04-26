def xrange(start, end):
    while start >= end:
        yield start
        start -= start>>1
a,b=map(int,input().split())
temp=0
l=(b-a)
ans=l//2+(a&1 or b&1)
for r in xrange(1125899906842624,2):
 o=a%r
 c=l//r-temp+(o>b%r or o==0)
 ans+=c*r
 temp+=c
print(ans)
