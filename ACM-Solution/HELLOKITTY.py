try:
 while 1:x,y=input().split();t=len(x);x*=int(y);exec("print(x[-t:]+x[:-t]);t-=1;"*t)
except:0
