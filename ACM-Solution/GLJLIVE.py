a=0
for x in [0]*10:
   k=int(input())
   if a+k-100<=100-a or 100>=a+k: a+=k
   else:break
print(a)
