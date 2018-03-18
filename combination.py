#code:
def c(n,k):
    if(k==0 or k==n):
        return 1
    else:
        return(c(n-1,k-1)+c(n-1,k))


#example:
print(c(5,2))

#recursive implimentation
