output=[]

for testcases in [0]*int(input()):

    for number in [0]*int(input()):

        num=''.join(sorted(input()))
        revnum=num[::-1]

        #print(num,revnum)

        flag=1000
        dif=int(revnum)-int(num)
        div6=dif%6
        div9=dif%9

        if dif>0:   flag=9

        elif dif==0:flag=dif


        if div6==0 and div9==0: ans="YONP" if flag==9 else "YZER"

        else:
            ans='NONP' if flag==9 else 'NZER'

            if div6!=0 and div9!=0:
                ans+='GTN'

            elif div6!=0 and div9==0:
                ans+='LTN'

            elif div6==0 and div9!=0:
                ans+='EQL            

        output.append(ans)
        
print('\n'.join(output))
