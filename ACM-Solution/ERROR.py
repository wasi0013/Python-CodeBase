from sys import stdin,stdout
from math import*
#a,*b=map(str,stdin.buffer.readlines())
#b=[]
x=[]    
for i in range(int(stdin.readline())):
    L,D,S,C=map(int,stdin.readline().split())
    T=(log(S)+(D-1)*log(C+1))
    x.append("ALIVE AND KICKING"if  T>=log(L) else"DEAD AND ROTTING")
print("\n".join(x))    
