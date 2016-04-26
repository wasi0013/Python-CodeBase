import sys
def m(A,B):
    a,b,c=A
    d,e,f=B
    return (a*d + b*e),(a*e + b*f),(b*e + c*f)
def p(A, n):
    if n == 1:return A
    if n & 1 == 0: return p(m(A, A), n//2)
    else:return m(A, p(m(A, A), (n-1)//2))
def fib(n):
    if n < 2: return n
    return p((1,1,0), n-1)[0]
