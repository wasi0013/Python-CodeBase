import sys
def a(n): 
    if n==0 or n==1: return 1
    return 4*a(n-1) - a(n-2)

x=int(sys.stdin.readline().strip())
while x!=-1:
    print(0 if x%2 and x>=0 else [1,3, 11, 41,153,571,2131,7953,29681,110771,413403,1542841,5757961,21489003,80198051,299303201][x//2])
    print(0 if x%2 and x>=0 else a(x//2+1))
    x=int(sys.stdin.readline().strip())
