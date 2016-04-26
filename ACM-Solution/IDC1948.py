output=[]

for testcases in [0]*int(input()):
        x=int(input())
        d=int('9'*(len(str(x))))- x
        f=0
        i=3
        while i<d:
            if x%i==0 and d%i==0:
                f=1
                break
            i+=2
        output.append("%d"%(i if f else -1))
        
print('\n'.join(output))
