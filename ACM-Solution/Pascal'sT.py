exec('t=int(input())+1;R=[[1]];exec("R+=[list(map(sum,zip(R[-1]+[0],[0]+R[-1])))];"*t);print(" ".join("%d"%i for i in R[t-1]));'*int(input()))
