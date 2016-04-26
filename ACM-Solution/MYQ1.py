#time limit exceeded
from sys import stdin,stdout
out=''
for _ in[0]*int(stdin.readline()):
 a=int(stdin.readline())
 if a==1: out+="poor conductor\n"
 else:
     ans=(a+3)//5
     flag=a%10
     if flag==2 or flag==1:out+="%d W L\n"%ans
     elif flag==3 or flag==0:out+="%d A L\n"%ans
     elif flag==4 or flag==9:out+="%d A R\n"%ans
     elif flag==5 or flag==8:out+="%d M R\n"%ans
     elif flag==6 or flag==7:out+="%d W R\n"%ans
print(out)
