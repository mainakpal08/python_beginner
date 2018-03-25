def fn(a,b):
    while (a%b==0):
        a=a/b
    return (a)
def isugly(n):
    n=fn(n,2)
    n=fn(n,3)
    n=fn(n,5)
    if(n==1):
        return 1
    else:
        return 0
def nugly(n):
    c=1
    i=1
    while(c<n):
        i+=1
        if isugly(i):
            c+=1
    return i        

print(nugly(150))        
