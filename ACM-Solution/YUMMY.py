import sys
c=1
for _ in[0]*int(input()):
    yummy=[1, 1, 1, 4, 6, 19, 43, 120, 307, 866, 2336, 6588, 18373, 52119, 147700, 422016, 1207477]
    print("Case %d: %d"%(c,yummy[int(input())-1]))
    c+=1
