import sys
for _ in "a"*int(input()):
    a=set(list(map(str,input()[::-1].split())))
    print(len(a))
