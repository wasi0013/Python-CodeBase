from sys import stdin,stdout
b=[5,1,2,3,4,5]
#a,*b=map(int,stdin.buffer.readlines())
o=[]
for num in b:
    z=0
    counter=1
    factor=5
    while num >=factor:
        z+=num//factor
        factor*=5
    o.append("%d"%z)
stdout.write("\n".join(o))
