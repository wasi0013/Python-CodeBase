from sys import stdin,stdout
t=int(stdin.readline())
l=[0]
c=0
x=1
while x<20002:
    l.insert(x,0)
    x+=1
line=stdin.readline()
for a in line:
    if a== " ":
        continue
    if(t<=0):
        break
    t-=1
    a=int(a)
    l[a]=1
    if int(l[a-1])==int(l[a+1]):
        if int(l[a-1])>0:
            c+=(-1)
        else:
            c+=1
    print(c)
print("Justice\n")
