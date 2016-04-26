ans=[]
for i in[1]*int(input()):
        input()
        y=list(map(int,input().split()))
        boolie =True
        temp=y[0]
        for i in y[1:]:
                if i<temp:
                        boolie =False
                        break
                else:   temp=i-temp
        ans.append("YES" if boolie and not temp else "NO")
print("\n".join(ans))          
