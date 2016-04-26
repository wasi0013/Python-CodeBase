tc = int(input())
while tc > 0:
    a = input()
    b = []
    b = a.split()
    x = -1
    c = 0
    m = 0
    for i in b:
        if x == len(i):
            c = c + 1
        else:
            x = len(i)
            if c > m:
                m = c
                c = 1
    if c > m:
        m = c
    if len(b) != 0:
        print(m)
        tc = tc - 1
