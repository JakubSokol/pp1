def string(array):
    i=0
    y=[]
    result=""
    for i in range(0,len(array)):
        y.append(str(array[i]))
    i+=1
    j=0
    for j in range(0,len(y)):
        result=result+y[j]
        if j!=(len(y)-1):
            result=result+","
    j+=1
    return result

x=[5,4,3,2,6,5]
print(string(x))
