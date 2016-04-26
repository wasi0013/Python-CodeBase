import random, sys
def main():
    for _ in [0]*int(sys.stdin.readline().strip()):    
        n =int(sys.stdin.readline().strip())
        if n>4294967291:
         print(4294967291)
        else:
         n=n-(n%2==0)-2
         while(not mr(n)):n-=2
         print(n)
def mrp(a, s, d, n):
    ap = pow(a, d, n)
    if ap == 1:
        return True
    for i in range(s-1):
        if ap == n - 1:
            return True
        ap = (ap * ap) % n
    return ap == n - 1
def mr(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for _ in[0]*2:
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not mrp(a, s, d, n):
            return False
    return True
if __name__ == "__main__":main()
