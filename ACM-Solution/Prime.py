import sys
p=[2]
for i in range(3,100001,2):
    if all(i%x for x in p):p.append(i)
try:
    while 1:print (p[int(input())-1])
