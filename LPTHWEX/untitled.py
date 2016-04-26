def main():
    a= int (input())
    sums=1    
    while(a>0):


        b=int (input())
        while(b>0):
            sums*=b
            b-=1
        print(sums)
        a-=1
        sums=1
    


if __name__== "__main__" : main()
