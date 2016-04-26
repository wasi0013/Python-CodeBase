import sys
try:
  while True:
    u=l=f=0
    for c in sys.stdin.readline().strip():
        if c.isupper():
         if f:u+=1;f=0
         else:l+=1;f=1
        else:
            if f:l+=1;f=0
            else:u+=1;f=1
    print(u if u<l else l)
except:pass
