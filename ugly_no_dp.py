# finding n th ugly no in dynamic programing method...
# series of a ugly no can be divided into 3 subsequences
# 2*1,2*2,2*3,2*4,2*5,2*6,2*8,2*9......
# 3*1,3*2,3*3,3*4,3*5,3*6,3*8,3*9......
# 5*1,5*2,5*3,5*4,5*5,5*6,5*8,5*9......
# we can easily notice that each subseq is a derivative of prev uglyno seq



def nugly(n):
    
    #initializing a uglyno seq
    uglyno=[0]*n
    
    #1st uglyno=1
    uglyno[0]=1
    
    #initializing 3 subseq with their initial values 2,3,5
    srs2=2
    srs3=3
    srs5=5

    #initializing 3 diff index no. for 3 diff subseq's
    i2=i3=i5=0
    
    for i in range(1,n):
        
        #i th ugly no alloting
        uglyno[i]=min(srs2,srs3,srs5)
        
        #change of index no of the three different subseq's
        if(uglyno[i]==srs2):
            i2+=1
            srs2=uglyno[i2]*2
        if(uglyno[i]==srs3):
            i3+=1
            srs3=uglyno[i3]*3
        if(uglyno[i]==srs5):
            i5+=1
            srs5=uglyno[i5]*5
    
    #returning the last member of the arrey
    return(uglyno[-1])                


print(nugly(150))