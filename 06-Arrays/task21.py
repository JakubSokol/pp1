def  compare(array1, array2):
    if len(array1)>len(array2):
        long=len(array1)
    else:
        long=len(array2) 
          
    result=True
    if len(array1)==len(array2):
        for i in range(0,long):
            if array1[i]==array2[i]:
                continue
            else:
                result=False
        i+=1
    else:
        return False
    return result
def display(array1,array2):
    x=compare(array1 , array2)
    if x==False:
        x="arrays are not the same"
    else:
        x="arrays are the same"
    print(f"array1: {array1[:len(array1)]}")
    print(f"array2: {array2[:len(array2)]}")
    print(x)
display([5,3,1]  , [5,3,1])