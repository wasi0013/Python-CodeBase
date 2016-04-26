from sys import stdin,stdout
out=[]
for i in[0]*int(stdin.readline()):
    V=int(stdin.readline())       
    out.append("%d"%((V*(V-1)*(V-2)*(V-3)//24)%1000000007))
print("\n".join(out))
