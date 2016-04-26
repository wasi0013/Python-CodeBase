import sys
for _ in [0]*int(input()):    
    N =float(input())
    print("%.8lf"%(((N-1.0)-(1.0/N))/(N+1.0)+(1.0/N)))        
