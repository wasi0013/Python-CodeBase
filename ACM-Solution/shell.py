import sys
ans= dict(left=0,center=0,right=0);ans[sys.stdin.readline().strip()]=1
x=int(sys.stdin.readline().strip())
if x==10:print()
else:
 for _ in [0]*int(x):
  a,b = sys.stdin.readline().strip().split()
  ans[b],ans[a]=ans[a],ans[b]
 for k,v in ans.items():
  if v==1:print(k)
