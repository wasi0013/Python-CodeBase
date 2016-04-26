import sys
cs=1
while 1:
    c,z=0,0
    s=sys.stdin.readline().strip()
    if s[0]=="-":break
    else:
        for x in s:
            c+=1 if x=='{' else -1
            if c<0:c+=2;z+=1
    print("%d. %d"%(cs,c//2+z))
    cs+=1
