def main():
    a=int(input())
    toi=0
    while toi<a:
        toi+=1
        start={} 
        end={}   
        l=[]
        b=int(input())
        while b:
            b-=1
            [c,d]=map(int,input().split())
            l.append([c,d])
            if c not in start.keys():
                start[c]=[[c,d]]
            else:
                start[c].append([c,d])
            if d not in end.keys():
                end[d]=[[c,d]]
            else:
                end[d].append([c,d])
        s=0
        for i in end.keys():
            if i in start.keys():
                for j in end[i]:
                    for k in start[i]:
                        if [j[0],k[1]] not in l:
                            s+=1
        print ("Case #%r:"%toi,s)

if __name__=='__main__':main()

"""3
0 1
1 2
2 0"""
