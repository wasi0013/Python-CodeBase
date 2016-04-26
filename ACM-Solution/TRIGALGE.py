def main():
 from sys import stdin,stdout
 from math import sin
 for _ in[0]*int(input()):
    a,b,c=map(int,stdin.readline().split())
    p=0
    r=c
    while(r-p>0.000009):
        q=(p+r)/2
        if(a*q+b*sin(q)>c):r=q
        else :p=q
    print("%.6f"%q)
main()
