try:
 while 1:
   x=input()
   y=input()
   z=input()
   input()
   for i in range(0,len(x),3):
        print(i)
        if x[i+1]==" ":print(4 if y[i+1]=="_" else 1)
        else:
            if y[i]=="|":
                if y[1+i]=="_":
                    if y[2+i]=="|":print(8 if z[i]=="|" else 9)
                    else:print(6 if z[i]=="|" else 5)
                else:print(0)
            else:
                if y[1+i]=="_":print(2 if z[i]=="|" else 3)
                else:
                    print(7)
                    

        
           



except:pass
