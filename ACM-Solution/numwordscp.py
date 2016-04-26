def a(b):
 if b==0:return'zero'
 T=('one','two','three','four','five','six','seven','eight','nine');n='teen';x='ty';c=[];d=b//1000%1000
 if d:c+=[a(d),'thousand']
 d=b//100%10
 if d:c+=[a(d),'hundred']
 h=b//10%10;i=b%10
 if h==1:c+=[['ten','eleven','twelve','thir'+n,T[3]+n,'fif'+n,T[5]+n,T[6]+n,T[7]+'een',T[8]+n][i]]
 else:
  if h:c+=[['twenty','thirty','forty','fifty',T[5]+x,T[6]+x,T[7]+'y',T[8]+x][h-2]]
  if i:c+=[T[i-1]]
 return' '.join(c)
print(a(int(input())))
