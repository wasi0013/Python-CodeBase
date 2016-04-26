exec("""x=input();t=x[0];c=0;n=""
for l in x:
 if t==l:c+=1
 else:n+=c+''+t;t=l;c=1
n+=str(c)+str(t)
print(n)
"""*int(input()))
