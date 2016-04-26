import sys
for _ in[0]*int(input()):
    def gcd(a,b):
        while b:
            a=a%b
            b=b^a
            a=a^b
            b=b^a
        return a
    s=sys.stdin.readline().strip()
    try:
        x,y=s.split('.')
        t=10**len(y)
        print(t//gcd(int(x+y),t))
    except:
        print(1)
