from sys import stdin,stdout
o=[]
for i in range(int(stdin.readline())):
    x=stdin.readline()
    y=stdin.readline().strip()
    fc={}
    for i in y:
        if i.isalpha():
            try:fc[i]+=1
            except:fc[i]=1
    a=sorted(fc.values(),reverse=True)
    for i in a:
        print(fc.keys())
