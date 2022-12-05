def minmax(array):
    x=[]
    array=sorted(array)
    x.append(array[0])
    x.append(array[(len(array))-1])
    return x

y=[4,2,8,4,7,9,5]
print(minmax(y))
