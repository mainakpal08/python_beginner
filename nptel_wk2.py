from math import *
def issqr(n):
    k=int(sqrt(n))
    return (k**2==n)
def sumofsquares(m) :
    if (m<=0):
        return (False)
    for i in range(1,(m//2)+1):
        if((issqr(i) and issqr(m-i))==True):
         return(True)
         break
    return(False)

def wellbracketed(s):
    c=0
    for i in range (0,len(s)):
        if(s[i]=='('):
            c=c+1
        if(s[i]==')'):
            c=c-1
    if(c==0):
        return(True)
    return(False)
        
    
