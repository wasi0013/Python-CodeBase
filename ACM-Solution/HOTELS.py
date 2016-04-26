import sys
n,m=map(int,input().split())
b=list(map(int,input().split()))
a=s=j=0
for i in b:
    if a+i<m:a+=i
    elif a+i==m:
        a+=i
        s=a
        break
    else:
        temp=a
        while temp+i>m:
            a-=b[j]
            temp=a
            if a+i<m:a+=i
            elif temp+i==m:
                a+=i
                s=a
                break
            j+=1
    s=max(s,a)
print(s)
