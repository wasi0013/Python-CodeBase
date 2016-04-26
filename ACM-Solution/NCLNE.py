from sys import stdin,stdout
out=''
for _ in range(int(stdin.readline())):
 t=int(stdin.readline())
 c=1
 if t==1:
    print("Yes" if int(stdin.readline())==1 else "No")
 else:
    naruto=1       
    for x in map(int,stdin.readline().split()):
        if c==t:print("Yes" if naruto==x else "No")
        elif x==0:naruto*=2;c+=1
        else:
            if x>naruto:
                print("No")
                break
            naruto-=x
            naruto*=2
            c+=1
        
