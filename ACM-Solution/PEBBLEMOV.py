#not AC
import sys
try:
 while 1:
  s=input().strip().split()
  try:s.pop(0)
  except ValueError:continue
  ans=[]
  for x in s:
    f=1
    for u,m in enumerate(ans):
        if m==x:
            ans.pop(u)
            f=0
    if f: ans.insert(0,x)
  try :
      ans.pop()
      print('first player')
  except ValueError:print('second player')
except EOFError:pass
