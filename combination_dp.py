#dynamic programing of binomial coeff-->
#motive--> in recursive implimentation same value of function is called several times.

def bincoeffd(n,k):

    #initializing a n*k matrix named c
    c=[[0 for x in range(k+1)]for x in range (n+1)]

    #computing the values of c[i][j]
    ##we have to calculate values for c[i][j] where i>=j
    for i in range (n+1):
        for j in range (min(k,i)+1):

            #base case: terminal values where the recurssion ends
            if(j==0 or j==i):
                c[i][j]=1
            #recursion
            else:
                c[i][j]=c[i-1][j-1]+c[i-1][j]

    return c[n][k]


# Driver program to test above function
n = 5
k = 2
print("Value of C[" + str(n) + "][" + str(k) + "] is "
      + str(bincoeffd(n,k)))


    
    
