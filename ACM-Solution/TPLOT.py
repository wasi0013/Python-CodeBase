reg=list(map(int,input().split()))
bon=reg.pop()
for i in range(5):
    x=list(map(int,input().split()))
    ans=sum(map(reg.count,x))
    if ans<3:print("No Parking slot")
    elif ans==3:print("Fifth Parking slot")
    elif ans==4:print("Fourth Parking slot")
    elif ans==6:print("First Parking slot")
    elif ans==5:print("Second Parking slot" if bon in x else "Third Parking Slot")
            
