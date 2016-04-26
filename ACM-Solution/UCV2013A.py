from sys import stdin,stdout
out=''
while a or b:
    out+='%d\n'%(((a*(a**b-1))//(a-1))%1000000007)
    a,b=map(int,stdin.readline().split())
print(out)
