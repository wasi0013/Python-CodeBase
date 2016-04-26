import sys
ans=[0,3,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for x in range(3,31):ans[x]=ans[x-2]+ans[x-1]*2    
for _ in[0]*int(input()):print(ans[int(input())])
