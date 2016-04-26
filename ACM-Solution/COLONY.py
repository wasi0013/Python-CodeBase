from sys import stdin,stdout
y=int(stdin.readline())
x=int(stdin.readline())
c=sum(map(bin(x).count,"1"))
if y%2:
      print("red" if c%2 else "blue")
else:
      print("blue" if c%2 else "red")
