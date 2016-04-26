import random, sys
def main():
    c=1
    for _ in [0]*int(input()):    
        n =int(input())
        if n==3:print("%d:2"%c)
        else :print ("%d:"%c+(mr(n) and "1" or "NOTPRIME"))
        c+=1
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
    for _ in range(5):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not mrp(a, s, d, n):
            return False
    return True
if __name__ == "__main__":main()

