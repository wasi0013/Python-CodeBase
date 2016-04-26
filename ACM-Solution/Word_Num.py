
x=('zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen')
y=('twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety','hundred','thousand')
ins=["one","hundred","fourty","nine"]
d=t=h=T=1
ans=0
for i in ins[::-1]:
    if d: ans+=x.index(i);d=0
    print(i)
print(ans)
