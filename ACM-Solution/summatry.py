try:
    import psyco
    psyco.full()
except ImportError:
    pass
from sys import stdin,stdout
def mod(a):
    MOD=1000000003
    if a> MOD : return (a%MOD)
    return a
def main():
    
    n=0
    p=[0,0,0,0,0]
    co=[0,4,30,50,30,6]
    inv = 441666668
    tst= int(stdin.readline())
    while(tst>0):
        tst-=1
        ai=int(stdin.readline())
        i=1
        p.insert(0,1)
        while(i<=5):
            p[i]=mod(ai*int(p[i-1]))
            i+=1
        j=1
        while(j<=5):
            p[j]=mod(int(co[j])*int(p[j]))
            j+=1
        k=1
        sums=0
        while(k<=5):
            sums=mod(sums+int(p[k]))
            k+=1
        sums=mod(sums*inv)
        print(sums)
    return 0
if __name__=="__main__": main()
