def main():
    a=int(input())
    s=0
    while (a!=0):
        a-=1
        v=int(input())
        if (v>0):
            s+=v
    print(s)
    return 0
if __name__=="__main__":main()
