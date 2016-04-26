from calendar import month_name as o
a=[1,2,3,4]
for _ in[0]*int(input()):
 x=input().strip('').split()
 y=int(str(''.join(str(i) for i in x[2:13])),2)
 m=int(str(''.join(str(i) for i in x[13:17])),2)
 m=int(str(''.join(str(i) for i in x[17:])),2)
 """j=k=l=d=m=y=0
 while x:
  r=x%2
  if j<5:
   d+=r*2**j
   j+=1
  elif k<4:
   m+=r*2**k
   k+=1
  else:
   y+=r*2**l
   l+=1"""
print(d,o[m],y)
