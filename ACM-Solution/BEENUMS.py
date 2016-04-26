import sys
import math
while True:
    a=int(input())
    if a<0 : break
    d= 9+ 12*(a-1)
    r= math.sqrt(d)
    if r*r ==d :
        r-=3
        if r%6==0:
            print("Y")
        else :
            print("N")
    else : print("N")
