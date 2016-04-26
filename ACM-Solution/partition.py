import sys
def part(S):
    A=[]
    B=[]
    C=[]
    a,b,c=0,0,1
    for i in S:
        if a<b:
            A.insert(1,i)
            a+=i
            C.insert(1,c)
            c+=1
        else:
            B.insert(1,i)
            b+=i
            c+=1
    return C
def main():
    c=int(input())
    s=[]
    while c:
        c-=1
        x=int(input())
        s.insert(1,x)
    A= part(s)
    for _ in A:
        print(_)

if __name__=='__main__':main()
