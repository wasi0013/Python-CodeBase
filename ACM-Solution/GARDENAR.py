output=[]
for testcase in range(int(input())):
    a,b,c= map(float,input().split())
    s=(a+b+c)/2
    output.append("%.2f"%(3**.5/8*(a*a+b*b+c*c)+(3*pow(s*(s-a)*(s-b)*(s-c),.5))/2)) 
print("\n".join(output))
