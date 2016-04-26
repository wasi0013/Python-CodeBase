try:
 while 1:x,y,z=map(int,input().split());t=max(y,max(x,z));u=min(min(x,y),z);v=sum([x,y,z])-t-u;n=(u**2+v**2)**.5;k=u+v;print(['acute','right','none','obtuse'][(n==t)*1+(k<=t)*2+(n>t)*3])
except:0
