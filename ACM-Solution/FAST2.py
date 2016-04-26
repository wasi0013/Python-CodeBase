pre=[]
mod=1298074214633706835075030044377087
print(mod)
a,t=0,1
for x in [0]*501:
    a+=t
    pre.append(a)
    t*=2
for i in [0]*int(input()):
    n=int(input())
    print(pre[n]%mod)
