def divisors(n):
    count=2 # accounts for 'n' and '1'
    i=2
    while(i**2 <= n):
        if(n%i==0):
            count+=2
        i+=1
    return count  
print(divisors(100000000000000))
