for _ in[0]*int(input()):
 n=int(input());c=2;x=y=a=0
 while(n>=c):
  t=c*c
  p=n//t*t
  s=n//t*(c-1)*(c-1)
  if(s*p>a):x,y,a=s,p,s*p
  c+=1
 print(x,'*',y)
