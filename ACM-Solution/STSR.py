c=x=1
for _ in[0]*int(input()):
 if(x):
  a=[]
  print("case",1,"Y")
  xt=int(input())
  for x in range(xt):
      a.append(input())
  b=set(a)
  b=''.join(b)
  print(b)
  for x in a:
       print(1+b.find(x))
 else: print('case',c,"N")
 x=0
 c+=1
  
  
