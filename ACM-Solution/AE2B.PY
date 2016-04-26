def gcd(k,n):
  while n:
    k%=n
    n^=k
    k^=n
    n^=k
  return k
for _ in[0]*int(input()):
    from sys import stdin,stdout
    k,n,a,b,x,y=map(int,stdin.readline().split())
    c=abs(a-b)
    d=abs(x-y)
    g=gcd(k,n)
    if g>1:
     if (d%g)!=0 or (c%g)!=0:
        print('NIE')
        continue
     k//=g
     n//=g
     c//=g
     d//=g
    if (~(k&1) or ~(n&1)):print("TAK")
    elif ((c&1)+(d&1)==1) : print("NIE")
    else: print("TAK")
