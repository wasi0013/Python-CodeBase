import sys

def fib(n):
    i=h=1
    k=j=0
    while n>0:
        if n%2==1:
            t=j*h
            j=i*h+j*k+t
            i=i*k+t
        t=h*h
        h=2*k*h+t
        k=k*k+t
        n=n//2
    return j
def main():
    i=0
    while i<50:
        print(fib(i))
        i+=1



if __name__=="__main__":main()
