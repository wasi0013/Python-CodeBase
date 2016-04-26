x=input;i=int
exec('''x();p=n=0
for r in map(i,x().split()):p+=r*(r>0)if n else(r<0)*r;n=~n
print('SEovmeer yM iGrirrolr sL iLeise!!'[p<0::2])
'''*i(x()))
