a=[i*i for i in range(1,32)]
m=[100]*1001
for i in range(1,1001):
    for j in a:
        if j==i:m[i]=1
        if(j<=i):
            m[i]=min(m[i],m[i-j]+1)
m[0]=0
for i in[0]*int(input()):
    print(m[int(input())])
