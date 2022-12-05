x=int(input("Value: "))
array=[1,3,5,7,91,22,45,22]
array=sorted(array)
y=[] #good array
i=0
for i in range(i,len(array)):
    if array[i]<x:
        continue
    if array[i]>x:
        y.append(array[i])
    i+=1
y=sorted(y)
print(y)