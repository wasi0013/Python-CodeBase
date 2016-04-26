x=[]
y=[]
for _ in [0]*int(input()):
    l=input().split()
    x.append(l)
    y.extend(l)
k=[]
for w in x:
    k.append(set(w).difference(y))
print("k is ",k,"\n x is ",x,"And y is ",y)
