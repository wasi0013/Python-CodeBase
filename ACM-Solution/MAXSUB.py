from sys import stdin,stdout
out=[]
for i in[0]*int(stdin.readline()):
    digit=stdin.readline().strip()
    x=stdin.readline().strip()
    t=len(x)
    for c,i in enumerate(((digit+digit[::-1])*t)[:t+1:]):
        if c==t:break
        tmp=(ord(x[c])-int(i))
        print("%d"%tmp)
    
    
    
