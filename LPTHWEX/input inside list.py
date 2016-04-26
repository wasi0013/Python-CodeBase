def main():
    mylist1= []
    mylist2= []
    b=0
    while (b<=10):
        x,y = input().split()
        mylist2.insert(b,y)
        mylist1.insert(b,x)
        b+=1
    print(mylist1)
    print(mylist2)
if __name__== "__main__" : main()
