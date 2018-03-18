def bsearch(l,v,lb,ub):
    if(ub-lb)==0:
        return(False)
    mid=(ub+lb)//2
    if(v==l[mid]):
        return(True)
    if(v<l[mid]):
        return(bsearch(l,v,lb,mid))
    else:
        return(bsearch(l,v,mid+1,ub))

(l,v,lb,ub)=input().split(' ')
bsearch(l,v,lb,ub)
