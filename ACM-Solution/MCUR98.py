a=[0]*1000100
s=[]
for i in range(1,1000000):
    if(a[i]==0):s.append("%d"%i)
    try:a[i+(i%10)+(i//10)%10+(i//100)%10+(i//1000)%10+(i//10000)%10+(i//100000)%10]=1
    except:print(i)
print(" ".join(s))
