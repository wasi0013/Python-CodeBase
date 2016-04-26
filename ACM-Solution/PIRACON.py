t=0
for _ in[0]*int(input()):
     t+=1
     k=int(input())
     p=k*k
     print("pyramid E. Nro# %d: %.0f"%(t,(2*p*k+6*p-5*k)/3))
     print("tringus: %.0f"%(2*(p-k)))
