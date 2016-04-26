#!C:\python32\
def  function1(bnum):
    dnum=0
    base=1
    r=0
    while(bnum>0):
        r= (bnum%10)
        bnum=  (bnum // 10)
        dnum+=r*base
        base*=2
    return dnum    
def main():
    bnum=input("Enter a binary number:\n-->")
    re=function1(int(bnum))
    print("The decimal form is {}".format(re))
    pause_exits =input("Press any key to quit")
if __name__=="__main__":main()
