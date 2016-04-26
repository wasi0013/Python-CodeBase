def gcd(a,b): return a%b if b else a

for i in range(100):
    a,b=map(int,input().split())
    c=(a*a-b)//2
    print(c,"answer",gcd(b,a),gcd(a,2*c))
