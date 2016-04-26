from sys import stdin,stdout
import re
#a,*b=map(str,stdin.buffer.readlines())
#b=[]
x=[]    
for i in range(int(stdin.readline())):
    L=stdin.readline() 
    x.append("Good"if L.rfind("010")>-1 or -1<L.rfind("101") else"Bad")
print("\n".join(x))    
