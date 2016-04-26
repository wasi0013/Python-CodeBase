def lucky (n):
    ans =['2','3','5','7']
    if n<5:     return ans[n-1]
    elif n%4==0:return lucky(n//4-1) + ans[3]
    else:       return lucky(n//4)   + ans[n%4-1]

x=[]

for i in range(int(input())):     x.append(lucky(int(input())))

print("\n".join(x))        
