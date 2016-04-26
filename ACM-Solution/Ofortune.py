t=int(input())
while(t>0):
    t-=1
    am=final=temp=0
    num = int(input())
    yrs = int(input())
    op = int(input())
    while(op>0):
        op-=1
        i,fr,g=input().split()
        if(0==int(i)):
            am=num
            count=0
            while(count<yrs):
                count+=1
                am = int(am*float(fr))-int(g)
            temp=am
        elif(1==int(i)):
            am=num
            count=cum=0
            while(count<yrs):
                count+=1
                cum+=int(am*float(fr))
                am-=int(g)
            temp=am+cum
        if(temp>final):
            final=int(temp)
    print(final)
