def o(l):
    d=lambda l,a:[(d+1,m-a)if m>a/2 else(d,m) for d,m in(divmod(x,a)for x in l)]
    a,x=min((a+sum(abs(x)+abs(y)for x,y in d(l,a)),a,d(l,a))for a in range(1,max(l)+1))[1:]
    return [a]+list(zip(*x))
def bf(l):
    N,f,s=o(l)
    return ('%s[%s%s-]%s'%(N*'+',
                           ''.join('>' + x*'+' for x in f),
                           ''.join('<' for _ in f),
                           ''.join('>' + abs(x)*('+' if x>0 else '-')for x in s)))
print(bf([37,76,8,48]))
