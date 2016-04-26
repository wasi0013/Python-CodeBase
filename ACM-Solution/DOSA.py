def LIS(X):
    n = len(X)
    X = [None] + X  
    M = [None]*(n+1)
    P = [None]*(n+1)
    L = 0
    for i in range(1,n+1):
        if L == 0 or X[M[1]] >= X[i]:j = 0
        else:
            lo = 1;hi = L+1
            while lo < hi - 1:
                mid = (lo + hi)//2
                if X[M[mid]] < X[i]:lo = mid
                else:  hi = mid
            j = lo
        P[i] = M[j]
        if j == L or X[i] < X[M[j+1]]:
            M[j+1] = i
            L = max(L,j+1)
    output = []
    pos = M[L]
    while L > 0:
        output.append(X[pos])
        pos = P[pos]
        L -= 1
    output.reverse()
    print(output)
    return len(output)
print(int(input())-LIS(list(set(map(int,input().split())))))          

