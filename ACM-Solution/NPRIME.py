import sys
n=1001
s=[0,0]+list(range(2,n+1));b=2
while b*b<n:s[2*b:n:b]=[0]*((n-1)//b-1);b+=1
p=list(filter(None,s))
print(p,len(p))#for i in [1230]:print (p[int(i)-1])

