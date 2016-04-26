from sys import stdin,stdout
from math import ceil,floor
out=''
for testcases in[0]*int(stdin.readline()):
      x,y,z=map(int,stdin.readline().split())
      i=(7*x/2+5*y/2+z)
      tmp=x+y
      k=i*i
      l=12*z*tmp
      sq=(k-l)**.5
      n1=(i+sq)/tmp
      n2=(i-sq)/tmp
      if(floor(n1)==ceil(n1)):n=round(n1)
      elif(floor(n2)==ceil(n2)):n=round(n2)
      d=round((y-x)/(n-6))
      a=x-2*d
      out+="%d\n%d "%(n,a)
      cnt=0
      while(cnt<=n-3):
          a+=d
          out+="%d "%a
          cnt+=1
      a+=d
      out+="%d\n"%a
print(out)
