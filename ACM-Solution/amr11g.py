import sys
for x in[0]*int(input()):
    s=input()
    c=1
    for l in s:
        if l=='D':
            print('You shall not pass!')
            c=0
            break
    if c:print("Possible")
        
        
