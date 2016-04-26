try:
 while 1:
  n=int(input())
  k=(n-10)//9
  m=n-10-9*k
  print(81*(k+1)+m*(m+2)+1)
except:pass
