from sys import stdin,stdout
output=[]
a,*b=map(int,stdin.buffer.readlines())
for i in b:output.append('%d'%(((8*i-7)**.5-.5)//2))
print("\n".join(output))
