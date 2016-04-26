def solve(n):
    i=1
    while n!=1:
        i+=1
        n=(3*n+1)if n&1 else n//2
    return i
from sys import stdin,stdout
def main():
    o=[]
    b=map(int,stdin.buffer.readlines())
    #test case b=[1,2,321,1111111111111,111111111111111111111111111111111111111111111111111111111111]
    for i in b:
      o.append("%d"%solve(i))
    stdout.write("\n".join(o))
if __name__=="__main__":main()
