from sys import stdin,stdout
out=[]
for i in[0]*int(stdin.readline()):
    div=[9,8,7,6,5,4,3,2]
    n=int(stdin.readline())
    ans=0
    if n<10:ans=n
    else:
        for i in div:
            while n%i==0:
                ans*=10
                ans+=i
                n//=i
    out.append("{}".format(10 if n==0 else (-1 if n>10 else str(ans)[::-1])))
print("\n".join(out))
