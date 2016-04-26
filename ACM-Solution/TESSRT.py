from sys import stdin,stdout
def fib():
    a, b = 0, 1
    while True:
        yield a
        a,b=b,a+b
for i in range(int(input())):
    F=0
    t=int(input())
    for x in fib():
        if t==x:F=1;break
        elif x>t:break
    print("YES" if F else "NO") 
