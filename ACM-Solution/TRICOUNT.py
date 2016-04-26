from sys import stdin,stdout
buffer=500000000
a,*b=map(int,stdin.buffer.read())
o=[]
for t in b:
 o.append((t*(t+2)*(2*t+1))//8)
stdout.write("\n".join(o))
