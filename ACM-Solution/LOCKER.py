import sys
def mPow(b,e):
    r=1
    while(e>0):
        e,c=divmod(e,2)
        if(c==1):
            r=(r*b)%1000000007
        b=(b*b)%1000000007
    return r
def main():
    for _ in[0]*int(input()):
        n=int(input());
        if n==1: print(1)
        elif(n%3==0):print("%d" %(mPow(3,n//3)%1000000007))
        elif(n%3==1):print ("%d" %(4*mPow(3,(n-4)//3)%1000000007))
        else:print("%d"%(2*mPow(3,(n-2)//3)%1000000007))
if __name__=="__main__":main()
