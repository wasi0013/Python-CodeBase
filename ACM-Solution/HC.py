from sys import stdin,stdout
ans=["hhb", "1xh"]
for x in [0]*int(stdin.buffer.readline().strip()):
   t=int(stdin.buffer.readline().strip())
   a=(stdin.buffer.readline().strip()[0]=="1") 
   for s in [0]*(t-1):
       a^=(stdin.buffer.readline().strip()[0]=='1')
   print(ans[a])
