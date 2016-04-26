from fractions import gcd
def count(s):
    moves=1
    a=s[0]
    b=0
    while(b!=s[2]and s[2]!=a):
        po=min(s[1]-b,a)
        b+=po
        a-=po
        moves+=1
        if(a==[s2] or b==s[2]):break
        if(b==s[1]):
            moves+=1
            b=0
        elif a==0:
            moves+=1
            a=s[0]
    return moves
for _ in[0]*int(input()):
    a,b,c=map(int,input().split())
    if(a<c and b<c):print(1)
    elif(c%gcd(a,b)):print(-1)
    else:print(min(count(b,a,c),count(a,b,c)))
