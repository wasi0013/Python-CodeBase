from sys import stdin,stdout
def main():

  def calc(a,b,c):
    s=(a+b+c)/2
    return pow((s*(s-a)*(s-b)*(s-c)),.5)

  out=[]
  for i in[0]*int(stdin.readline()):
    stdin.readline()
    ins=list(map(float,stdin.readline().split()))
    ans=[0]*16
    n=len(ins)
    ins.sort()
    for i in range(n-1,-1,-1):
        j,ans[i]=i+1,ans[i+1]
        k=j+1
        while k<n:
          if ins[k]<ins[i]+ins[j]:
            for m in range(j,k):
                ans[i]=max(ans[i],ans[k+1]+calc(ins[i],ins[m],ins[k]))
            k+=1
          else:j+=1
    out.append("%.6f"%ans[0])            
  print("\n".join(out))
if __name__=="__main__":main()
