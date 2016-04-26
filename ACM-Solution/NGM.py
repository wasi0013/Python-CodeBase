import sys
try:
    while 1:
        n=int(input())
        print('1\n%d'%(n%10) if n%10 else 2)
except:pass
