import sys
a=[1]*3;exec("x=sum(a);a=[x-a[2],x,x-a[0]];"*(int(input())-1));print(sum(a))
