from sys import stdin,stdout
t=int(input())
l=[942,192,442,692]
while t:
    t-=1
    a=int(input())
    i=a%4
    ans=((a-1)//4)*1000+l[i]
    print(ans)
