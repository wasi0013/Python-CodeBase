from sys import stdin,stdout
ans=[0,0,0]
striker=0
nonstriker=1
for char in stdin.readline().split():
    if char=='O':striker=2
    try:
        run=int(char)
        ans[striker]+=run
        if run%2:striker,nonstriker=nonstriker,striker
    except:pass    
for out in ans:print(out)
