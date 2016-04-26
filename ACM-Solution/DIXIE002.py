import sys,math
i=c=0
try:
    a=input()
    print(a)
    a=a.lower()
    print(a)
    for x in a:
        if(x=="a"or x=='e'or x=='i' or x=='o' or x=='u'):
            i+=1
        c+=1
except:
    print("%d/%d"%(i,c))
