k=input
a=int(k())
b=''
try:
 while 1:
  for c in k()[::-1].split(" "):b+=(' '+c)*a
except:print(b)
