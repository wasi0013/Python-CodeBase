from fractions import gcd
for x in[0]*int(input()):x,y=map(int,input().split());print(y//gcd(x,y),x//gcd(x,y))
