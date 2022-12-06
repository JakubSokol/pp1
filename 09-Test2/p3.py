def f(array2D):
    sum1=0
    sum2=0
    sum3=0
    sum4=0
    x=[]
    for i in range(0,len(array2D)):
        for j in range(0,len(array2D[i])):
            if j==0:
                sum1=sum1+array2D[i][j]
            if j==1:
                sum2=sum2+array2D[i][j]
            if j==2:
                sum3=sum3+array2D[i][j]
            if j==3:
                sum4=sum4+array2D[i][j]
    x.append(sum1)
    x.append(sum2)
    x.append(sum3)
    x.append(sum4)
    return x
x=[ [3,6,2,7], [9,5,4,0], [2,8,0,9] ]
print(f(x))