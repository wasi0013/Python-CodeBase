c=0
for i in [0]*int(input()):
    a,b= input().split(" ")    
    b=list(b)
    b[int(a)-1]=""
    c+=1
    print(c,"".join(b))
""" GNY07A"""
