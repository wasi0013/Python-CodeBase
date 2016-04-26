def f(n):
 s=n**.5
 i=2;a=1
 while(i<=s):a+=[0,i+n//i][n%i==0];i+=1
 return (a-(n==s*s)*s)
while 1:
 n,x=map(int,input().split())
 if(n+x==0):break
 print(int(f(x)+x-f(n)-n))
    
