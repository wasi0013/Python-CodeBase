fibs = {0: 0, 1: 1}
def fib(n):
    if n in fibs: return fibs[n]
    if n % 2 == 0:
        fibs[n] = ((2 * fib((n / 2) - 1)) + fib(n / 2)) * fib(n / 2)
        return fibs[n]
    fibs[n] = (fib((n - 1) / 2) ** 2) + (fib((n+1) / 2) ** 2)
    return fibs[n]
# limit 100000
