from sys import stdin,stdout
import math
for _ in [0]*int(input()):
    n=int(input())
    i=math.ceil(math.log(n,2))
    minimum=0
    k=0
    while(k<=i):
        temp=n>>k
        if(temp&1):
            minimum = k
            break
        k+=1
    print(pow(2,i),(i-minimum))
        
