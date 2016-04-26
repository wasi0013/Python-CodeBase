def N(n):
 if n==0:return"0"
 x=[];i=0
 for v in bin(n)[::-1]:
  if v=='1':x+=[["2("+N(i)+")","2"][i==1]]
  i+=1
 print(x)
 return'+'.join(x)
while 1: t=int(input());print("%d=%s"%(t,N(t)))
