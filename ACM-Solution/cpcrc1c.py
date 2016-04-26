from sys import stdin,stdout
def dsum(n):
    if n//10==0:return n*(n+1)//2
    count,temp=0,n
    while not temp//10==0:count,temp=count+1,temp//10
    p=10**count
    mod=n%p
    return (dsum(mod)+temp*(mod+1)+p*temp*(temp-1)//2+(p*count*temp*45//10))

def main():
    out=""
    a,b=map(int,stdin.readline().split())
    while a!=-1 and b!=-1:
        out+="%d\n"%(dsum(b)-dsum(a-1))
        a,b=map(int,stdin.readline().split())
    print(out)
    
if __name__=="__main__":main()
