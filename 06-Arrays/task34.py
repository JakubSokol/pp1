array1=[1,3,5,7,9]
array2=[5,7,9]
array1=set(array1)
array2=set(array2)
if array2.issubset(array1) == True:
    print("array2 is a subset of array1")
else:
    print("array2 is not a subset of array1")
    