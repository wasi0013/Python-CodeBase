for i in range(int(input())):
 w=input().split()
 ans=1 
 n=len( w )
 i=0  
 x=l=len(w[0])
 
 while i < n :
    count = 0 
    while i < n   :
        x = len(w[i])
        if x == l :
            count+=1
            i+=1
        else  :
            break
                
    l=x
    ans = max(count,ans) 

 print(ans)
                        
