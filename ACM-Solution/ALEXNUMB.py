from sys import stdin,stdout
o=[]
for i in range(int(stdin.readline())):
    n=int(stdin.readline())
    o.append("%d"%(n*(n-1)//2))
    stdin.readline()
print("\n".join(o))

