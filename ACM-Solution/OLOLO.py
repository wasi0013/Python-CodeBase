import sys
ans=0
for _ in[0]*int(sys.stdin.readline().strip()):
    ans^=int(sys.stdin.readline().strip())
print(ans)
