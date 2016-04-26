def StarTrick_1():
    for a in range(6):
        print("*"*a)
def StarTrick_2():
    b=5
    for a in range(6):
        print("*"*b)
        b-=1
def StarTrick_3():
    b=6
    for a in range(6):
        print(" "*b,end='')
        b-=1
        print("*"*a)
def StarTrick_4():
    
    
    b=6
    for a in range(6):
        print(" "*b,end='')
        b-=1
        print("* "*a)
def StarTrick_5():
    b=4    
    for a in range(1,6):
        print(" "*a,end='')
        print(" *"*b)
        b-=1
    
def main():
    print("Star tricks 1")
    print("_____________")
    StarTrick_1()
    print("Star tricks 2")
    print("_____________")
    StarTrick_2()
    print("Star tricks 3")
    print("_____________")
    StarTrick_3()
    print("Star tricks 4")
    print("_____________")
    StarTrick_4()
    print("Star tricks 5")
    print("_____________")
    
    StarTrick_4()
    StarTrick_5()
    pause_exits =input("Press any key to quit")

if __name__=="__main__":main()
