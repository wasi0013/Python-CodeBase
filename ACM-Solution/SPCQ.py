from sys import stdin,stdout
def digit(n):
    s=0
    while n: n,r=divmod(n,10);s+=r
    return s
a,*b=map(int,stdin.buffer.readlines())
out=[]
for i in b:
    while(i%digit(i)!=0):i+=1
    out.append("%d"%i)
print("\n".join(out))
