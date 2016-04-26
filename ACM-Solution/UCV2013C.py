from sys import stdin,stdout
out=''
a,b,c,d=map(int,stdin.readline().split())
while a or b or c or d:
    b=b*(b+1)//2+1
    ans=a-c*b
    if ans<d:
        ans=d-ans
        out+="The firm is trying to bankrupt Farmer Cream by %d Bsf\n"%ans
    else:
        out+="Farmer Cream will have %d Bsf to spend\n"%ans    
    a,b,c,d=map(int,stdin.readline().split())
print(out)
