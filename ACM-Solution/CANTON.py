exec("n=int(input());s=int((8*n-7)**.5/2-.5);t=n-s*(s+1)/2;print('%d/%d'%[(s+2-t,t),(t,s+2-t)][int(t)%2]);"*int(input()))
