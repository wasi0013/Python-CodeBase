import sys
c=1
try:
    while 1:
        s=sys.stdin.readline().strip()
        res=0
        flag= False
        for x in s:
            if (x=='0' and flag)or(x=='1' and not flag):
                res+=1
                flag=not flag
        print('Game #%d:'%c,res)
        c+=1
except:pass
