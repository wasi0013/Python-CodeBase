from sys import stdin,stdout
a=int(stdin.readline())
if a<2:print("TAK")
elif a%2==0 and a%3!=0:
    while a>1:
        if a%2==0: a//=2
        else:
            if a%3==0:
                print("NIE")
                break
            else:
                a=3*a+3
    if a<=2:
        print("TAK")
else:print("NIE")
