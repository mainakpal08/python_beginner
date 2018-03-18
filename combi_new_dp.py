def combi(n,k):
    if (n==k) or (k==0) :
        return 1
    else:
        return((n/k)*combi(n-1,k-1))

print(combi(5,2))    