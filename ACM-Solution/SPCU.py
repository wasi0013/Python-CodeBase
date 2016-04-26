from sys import stdin,stdout
out=[]
for i in[0]*int(stdin.readline()):
    
    flag = True
    stdin.readline()
    for b,i in enumerate(map(int,stdin.readline().split())):
        if i>b:
            flag = False
            break
        
    out.append("YES" if flag else "NO")
print("\n".join(out))
