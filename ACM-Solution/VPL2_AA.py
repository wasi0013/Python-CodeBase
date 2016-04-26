from math import log
ct=1
out=''
for _ in[0]*int(input()):
    a,b,c,d=map(int,input().split())
    out+="Scenario #%d: %.2f\n"%(ct,log(d/a,10)/(log(b/a,10)/c))
    ct+=1
print(out)
