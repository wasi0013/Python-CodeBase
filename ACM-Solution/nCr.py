from sys import stdin,stdout
for x in [0]*int(stdin.readline()):
     a=int(stdin.readline())     
     print((pow(2,a)*a//2)%1000000007)
