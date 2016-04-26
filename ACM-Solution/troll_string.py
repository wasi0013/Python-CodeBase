out=""
i=input()
for i,j in enumerate([2,3,5,7,9,11,13,15,17,19]):out+="%d%d"%(i,int(repr(j),32))
print(out)

print(int('bbc',32))
