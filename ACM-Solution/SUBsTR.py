p=0
s=""
def go(x):
    global p
    global s
    while p>x:
        s+="<"
        p-=1
    while p<x:
        s+=">"
        p+=1
def clr(x):
    go(x)
    global s+="[-]"
def move(x,y):
    clr(y)
    go(x)
    global s+="[-"
    go(y)
    s+="+"
    go(x)
    s+="]"
#incomplete
    
