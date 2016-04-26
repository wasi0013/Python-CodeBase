from sys import stdin,stdout
out=[]
for i in[0]*int(stdin.readline()):
    a,b=map(int,stdin.readline().split())
    out.append("%.3f"%(2*(a*a-b*b)**.5))
print("\n".join(out))
