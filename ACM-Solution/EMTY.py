from sys import stdin,stdout
import re
out=[]
for i in[0]*int(stdin.readline()):
    s=stdin.readline().strip()
    while 1:
           
           s=re.sub(s,"100","")
           print(s)
    
print("\n".join(out))
