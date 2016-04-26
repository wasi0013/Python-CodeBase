
def c(a,b):
    q=[]
    q.append(a)
    try:
        while 1:
            x,y,z=q.pop(0)
            if(x<0 or x>7 or y>7 or y<0):continue
            if x==b[0] and y==b[1]:return z
            q.append([x+1,y+2,z+1])
            q.append([x+2,y+1,z+1])
            q.append([x+2,y-1,z+1])
            q.append([x+1,y-2,z+1])
            q.append([x-1,y-2,z+1])
            q.append([x-2,y-1,z+1])
            q.append([x-2,y+1,z+1])
            q.append([x-1,y+2,z+1])
    except:0
    
for _ in[0]*int(input()):
    x,y=input().split() 
    print(c([ord(x[0])-97,int(x[1]),0],[ord(y[0])-97,int(y[1])]))
