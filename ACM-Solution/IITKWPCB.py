def main():
    from sys import stdin,stdout
    from fractions import gcd
    for x in range(int(stdin.readline().strip())):
        t=i=int(input())
        i//=2
        while(gcd(i,t)!=1):i-=1
        print(i)
main()
