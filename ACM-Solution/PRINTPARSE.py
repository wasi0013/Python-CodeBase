import sys
for _ in[0]*int(input()):
 c=input().replace("f","",1).replace('",','"%(',1).replace(';',');',1)
 print(c)
 exec(c)
