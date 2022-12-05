def bubblesort(array):
    x=True
    p=None
    while x==True:
        x=False
        i=0
        for i in range(0,len(array)-1):
            if array[i]>array[i+1]:
                p=array[i]
                array[i]=array[i+1]
                array[i+1]=p
                x=True               
    return array
    


# mylist =[6,2,14,5,6]
# mylist=bubblesort(mylist)
# print(mylist)
