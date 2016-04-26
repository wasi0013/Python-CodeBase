import re
k=input
a=int(k())
c=0
b=k()
b=b[::-1]
b=re.split(" ",b)
for l in b:
    print((l+" ") *a,end ="")

