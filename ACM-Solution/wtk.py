def main():
 from sys import stdin,stdout
 c=stdin.readlines
 c()
 for x in map(int,c().splitlines()):
     a=0
     k=2
     while k<=x:
         a=(x+1+a-k)%k
         k+=1
     print(a+1)
main()
