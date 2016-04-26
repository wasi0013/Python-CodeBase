import re
import sys
for _ in [0]*int(input()):    
    input()
    string=input()
    string=string.replace(" ","")
    a=string.split("+")[0]
    b,c=string.split("+")[1].split("=")
    print(a,b,c)
    try:
        a=int(a)
        try : b=int(b);print(a,"+",b,"=",a+b)
        except: c=int(c);print(a,"+",c-a,"=",c)
    except: b=int(b);c=int(c);print(c-b,"+",b,"=",c)
        
            
        
        
