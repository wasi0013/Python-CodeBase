import sys
try:
 while 1:
  n=int(sys.stdin.readline().strip())
  sys.stdout.write(str(int((2**n-(-1)**n)/(2*3)))+'\n')
except:pass
