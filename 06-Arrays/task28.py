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

def median(array):
    if len(array)%2==0:
        print((array[((len(x)-1)//2)]+array[((len(x)-1)//2)+1])/2)
    if len(array)%2==1:
        print(array[((len(x)-1)//2)])


x=[1,0,9,4,6]
y=[6,8,3,1,0,5]
x=bubblesort(x)
y=bubblesort(y)
median(x)
median(y)

