from sys import stdin,stdout
out=[]
a,*b=map(int,stdin.buffer.readlines())
for i in b:
    x=int(stdin.readline().strip())
    s=2**(bin(x)[2::]).count("1")
    out.append("%d %d"%(x+1-s,s))
print("\n".join(out))
